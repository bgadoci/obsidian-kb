#!/usr/bin/env python3
"""
Blog Post Fetcher for bgadoci.com

This script fetches blog posts from bgadoci.com and saves them as Markdown files
in the Obsidian vault with proper formatting and organization.
"""

import os
import re
import sys
import json
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin, urlparse
import yaml

# Configuration
BLOG_OUTLINE_PATH = "/Users/brandongadoci/Documents/obsidian-kb/Blog/bgadoci-blog-outline.md"
BLOG_BASE_DIR = "/Users/brandongadoci/Documents/obsidian-kb/Blog"
IMAGE_DIR = os.path.join(BLOG_BASE_DIR, "images")
CATEGORIES = {
    "AI Operations & Enterprise AI": "AI Operations",
    "FrenchFryAI & Small Business AI": "FrenchFryAI",
    "AI Projects & Case Studies": "AI Projects",
    "AI in Education & Learning": "AI Education",
    "Career & Professional Development": "Career Development",
    "Personal Development & Reflection": "Personal",
    "Technology & Web Development": "Technology",
    "Business & Marketing": "Business",
    "Fitpholio": "Fitpholio"
}

# Ensure directories exist
for category_dir in CATEGORIES.values():
    os.makedirs(os.path.join(BLOG_BASE_DIR, category_dir), exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

def sanitize_filename(filename):
    """Convert a string to a valid filename."""
    # Replace spaces with hyphens and remove invalid characters
    sanitized = re.sub(r'[^\w\-\.]', '-', filename.lower().replace(' ', '-'))
    # Remove multiple consecutive hyphens
    sanitized = re.sub(r'-+', '-', sanitized)
    # Remove leading/trailing hyphens
    return sanitized.strip('-')

def download_image(image_url, post_title):
    """Download an image and save it to the images directory."""
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            # Extract filename from URL or create one based on post title if needed
            parsed_url = urlparse(image_url)
            filename = os.path.basename(parsed_url.path)
            if not filename or '.' not in filename:
                # Create a filename if none exists
                filename = f"{sanitize_filename(post_title)}-{int(time.time())}.jpg"
            
            # Save the image
            image_path = os.path.join(IMAGE_DIR, filename)
            with open(image_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Return the relative path for embedding in markdown
            return os.path.join("images", filename)
        else:
            print(f"Failed to download image: {image_url} (Status code: {response.status_code})")
            return None
    except Exception as e:
        print(f"Error downloading image {image_url}: {str(e)}")
        return None

def fetch_blog_post(url, category):
    """Fetch a blog post and convert it to Markdown."""
    try:
        print(f"Fetching: {url}")
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch {url}: {response.status_code}")
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title_elem = soup.find('h1')
        if not title_elem:
            title_elem = soup.find('title')
        title = title_elem.text.strip() if title_elem else "Untitled Post"
        
        # Extract date
        date_elem = soup.find('time')
        if date_elem:
            date_str = date_elem.get('datetime', '') or date_elem.text.strip()
            try:
                # Try to parse the date
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                date = date_obj.strftime('%Y-%m-%d')
            except ValueError:
                # If parsing fails, use today's date
                date = datetime.now().strftime('%Y-%m-%d')
        else:
            date = datetime.now().strftime('%Y-%m-%d')
        
        # Extract content
        content_elem = soup.find('article') or soup.find('main') or soup.find('div', class_='content')
        if not content_elem:
            print(f"Could not find content for {url}")
            return None
        
        # Process content
        markdown_content = []
        images = []
        
        # Process paragraphs, headings, lists, etc.
        for element in content_elem.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'blockquote', 'pre', 'code', 'img']):
            if element.name == 'img':
                img_src = element.get('src', '')
                if img_src:
                    img_src = urljoin(url, img_src)  # Make sure we have absolute URL
                    local_path = download_image(img_src, title)
                    if local_path:
                        markdown_content.append(f"![]({local_path})")
                        images.append(local_path)
            elif element.name.startswith('h'):
                level = int(element.name[1])
                markdown_content.append(f"{'#' * level} {element.text.strip()}")
            elif element.name == 'p':
                markdown_content.append(element.text.strip())
            elif element.name == 'blockquote':
                markdown_content.append(f"> {element.text.strip()}")
            elif element.name == 'pre' or element.name == 'code':
                markdown_content.append(f"```\n{element.text.strip()}\n```")
            elif element.name == 'ul':
                for li in element.find_all('li', recursive=False):
                    markdown_content.append(f"- {li.text.strip()}")
            elif element.name == 'ol':
                for i, li in enumerate(element.find_all('li', recursive=False), 1):
                    markdown_content.append(f"{i}. {li.text.strip()}")
        
        # Create YAML frontmatter
        frontmatter = {
            'title': title,
            'date': date,
            'type': 'blog',
            'status': 'complete',
            'tags': ['blog', category.lower().replace(' ', '-')],
            'source_url': url
        }
        
        # Format the final markdown content
        yaml_content = yaml.dump(frontmatter, default_flow_style=False)
        final_content = f"---\n{yaml_content}---\n\n# {title}\n\n"
        final_content += "\n\n".join(markdown_content)
        
        # Add source link at the bottom
        final_content += f"\n\n## Source\n[Original post on bgadoci.com]({url})"
        
        return {
            'title': title,
            'content': final_content,
            'date': date,
            'images': images,
            'category': category
        }
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return None

def update_outline_status(url, status='🔄'):
    """Update the status of a blog post in the outline file."""
    try:
        with open(BLOG_OUTLINE_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the line with this URL and update its status
        pattern = r'(⬜|\🔄|\✅) \[(.*?)\]\(' + re.escape(url) + r'\)'
        replacement = f'{status} [\\2]({url})'
        updated_content = re.sub(pattern, replacement, content)
        
        with open(BLOG_OUTLINE_PATH, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
    except Exception as e:
        print(f"Error updating outline for {url}: {str(e)}")
        return False

def save_blog_post(post_data):
    """Save the blog post as a Markdown file in the appropriate directory."""
    if not post_data:
        return False
    
    category_dir = CATEGORIES.get(post_data['category'], 'Uncategorized')
    filename = sanitize_filename(post_data['title']) + '.md'
    file_path = os.path.join(BLOG_BASE_DIR, category_dir, filename)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(post_data['content'])
        print(f"Saved: {file_path}")
        return True
    except Exception as e:
        print(f"Error saving {file_path}: {str(e)}")
        return False

def extract_blog_posts_from_outline():
    """Extract blog post URLs and categories from the outline file."""
    try:
        with open(BLOG_OUTLINE_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        
        blog_posts = []
        current_category = None
        
        for line in content.split('\n'):
            # Check if line defines a category
            category_match = re.match(r'^## (.+)$', line)
            if category_match:
                current_category = category_match.group(1)
                continue
            
            # Check if line contains a blog post link
            post_match = re.match(r'^\d+\. (⬜|\🔄|\✅) \[(.*?)\]\((https?://.*?)\)', line)
            if post_match and current_category:
                status, title, url = post_match.groups()
                blog_posts.append({
                    'title': title,
                    'url': url,
                    'category': current_category,
                    'status': status
                })
        
        return blog_posts
    except Exception as e:
        print(f"Error extracting blog posts: {str(e)}")
        return []

def main():
    """Main function to fetch blog posts."""
    blog_posts = extract_blog_posts_from_outline()
    
    if not blog_posts:
        print("No blog posts found in the outline file.")
        return
    
    print(f"Found {len(blog_posts)} blog posts in the outline.")
    
    # Ask which posts to process
    print("\nOptions:")
    print("1. Process a single post (by number)")
    print("2. Process all posts with 'Not started' status")
    print("3. Process posts from a specific category")
    
    choice = input("Enter your choice (1-3): ")
    
    posts_to_process = []
    
    if choice == '1':
        # Display posts with numbers
        for i, post in enumerate(blog_posts, 1):
            print(f"{i}. {post['title']} ({post['category']}) - {post['status']}")
        
        post_num = int(input("Enter post number to process: "))
        if 1 <= post_num <= len(blog_posts):
            posts_to_process = [blog_posts[post_num - 1]]
    
    elif choice == '2':
        # Process all not started posts
        posts_to_process = [post for post in blog_posts if post['status'] == '⬜']
        print(f"Found {len(posts_to_process)} posts with 'Not started' status.")
    
    elif choice == '3':
        # List categories
        categories = set(post['category'] for post in blog_posts)
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        cat_choice = input("Enter category number: ")
        try:
            selected_category = list(categories)[int(cat_choice) - 1]
            posts_to_process = [post for post in blog_posts if post['category'] == selected_category]
            print(f"Found {len(posts_to_process)} posts in category '{selected_category}'.")
        except (ValueError, IndexError):
            print("Invalid category selection.")
            return
    
    else:
        print("Invalid choice.")
        return
    
    # Process selected posts
    for post in posts_to_process:
        print(f"\nProcessing: {post['title']}")
        
        # Update status to "in progress"
        update_outline_status(post['url'], '🔄')
        
        # Fetch and save the post
        post_data = fetch_blog_post(post['url'], post['category'])
        if post_data and save_blog_post(post_data):
            # Update status to "completed"
            update_outline_status(post['url'], '✅')
            print(f"Successfully processed: {post['title']}")
        else:
            # Revert status to "not started" if failed
            update_outline_status(post['url'], '⬜')
            print(f"Failed to process: {post['title']}")
        
        # Add a small delay to avoid overwhelming the server
        time.sleep(1)
    
    print("\nAll selected posts have been processed.")

if __name__ == "__main__":
    main()
