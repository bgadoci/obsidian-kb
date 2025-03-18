---
date: '2025-03-18'
source_url: https://bgadoci.com/thoughts/building-the-dataworld-vectorizer-laying-the-infrastructure-for-ai-in-the-enterprise
status: complete
tags:
- blog
- ai-projects-&-case-studies
title: 'Building the data.world Vectorizer: Laying the Infrastructure for AI in the
  Enterprise'
type: blog
---

# Building the data.world Vectorizer: Laying the Infrastructure for AI in the Enterprise

# Building the data.world Vectorizer: Laying the Infrastructure for AI in the Enterprise

At data.world, we have been on a journey to build the necessary infrastructure to fully leverage AI in the enterprise (read about our AI Context Engine) but we’re not just developing tools for our customers we’re developing tools for ourselves. This post is about an internal tool we call the Vectorizer and is a significant step towards creating a culture of AI usage within our organization, enabling us to streamline processes, enhance productivity, and foster innovation.

### The Problem We Faced

Our journey began with the realization that our initial approach to integrating AI into our operations was not sustainable. Early in the year, we created a variety of productivity enhancement apps for our colleagues. These apps were designed to write landing pages, research customers and accounts, and provide information about data.world's resources. However, we quickly encountered a significant challenge: maintaining and updating the data these apps relied on was becoming cumbersome and inefficient.

Our initial solution involved creating a JSON file containing all the URLs from our websites and docs sites, along with relevant metadata. This file, which grew to 32 megabytes, had to be embedded in every single application. As we continued to build more internal apps, updating this file for new or stale content became increasingly impractical. It was clear that we needed a more scalable and dynamic solution.

### The Birth of the Vectorizer

Enter Jon Monette one of our Principal Engineers who developed the first version of the Vectorizer. This initial version automated the process of scraping our website and documentation site, creating a vector database accessible via an API endpoint. This allowed other apps to retrieve up-to-date resources relevant to their needs. Building on Jon’s foundational work, we developed Vectorizer V2, an internal app that significantly enhances our ability to manage and utilize content for AI operations.

### How the Vectorizer Works

The Vectorizer operates by either receiving a URL or a sitemap URL. For efficiency, sitemap URLs are preferred as they streamline the scraping process. Users provide the HTML tags or classes they wish to target, and the system either scrapes the site directly or processes the sitemap. The crucial part is selecting the type of embedding: summary or content embedding.

Our experience has shown that different types of content require different approaches. For general information, summarizing the content before generating embeddings works well. However, for detailed documentation, direct content embeddings are more effective. This flexibility allows us to tailor our AI tools to the specific needs of various departments within the company. In the later case we use some chunking strategies where needed and average embeddings for final storing.

![](images/Screenshot+2024-05-16+at+1.54.27+PM.png)

### Technical Details and Innovations

The technical backbone of the Vectorizer is built using a React app with a MongoDB database, supported by Node.js and Express. One of the innovative strategies we implemented involves generating an SHA-1 hash of the scraped content. This hash is stored in the database and checked before reprocessing any content, ensuring that only updated content goes through the embedding process. This approach minimizes unnecessary API calls to OpenAI, optimizing costs and efficiency.

![](images/Screenshot+2024-05-16+at+1.54.40+PM.png)

The Vectorizer runs nightly, processing each site and updating the vector database. It provides real-time feedback on the number of sitemaps and articles processed, skipped, or deleted, allowing for continuous monitoring and refinement. The endpoint created for the Vectorizer allows applications to send text blobs and receive the most relevant articles, complete with titles, summaries, and types.

![](images/Screenshot+2024-05-16+at+1.54.51+PM.png)

### Building a Culture of AI Usage

The development of the Vectorizer is not just about technical capabilities; it's about creating a culture of AI usage within data.world. By providing a robust and scalable infrastructure, we empower our employees to leverage AI in their daily tasks by being able to build more solutions faster, fostering innovation and enhancing productivity. This culture shift is crucial for maximizing the benefits of AI in the enterprise.

For example, our Customer Success Directors (CSDs) use an app supported by the Vectorizer to query information about products and services. This app retrieves relevant articles and generates responses that help CSDs provide accurate and timely information to clients. The app also tracks the most popular links and resources, creating a dynamic library that evolves with our needs.

![](images/Screenshot+2024-05-16+at+1.55.10+PM.png)

### The Impact of the Vectorizer

The impact of the Vectorizer extends beyond individual apps. It supports a wide range of AI-driven initiatives across the company, from sales and marketing to customer support and internal training. By centralizing and streamlining content management, the Vectorizer reduces redundancy, enhances data accuracy, and accelerates decision-making processes.

Moreover, the Vectorizer embodies the principles of innovation and continuous improvement. By iteratively building and refining our AI tools, we demonstrate the potential of AI to transform traditional workflows and create new opportunities. This iterative approach also helps demystify AI for our employees, encouraging them to explore and experiment with AI in their roles.

### Conclusion

Building the Vectorizer has been a pivotal step in laying the infrastructure necessary to leverage AI within data.world. It exemplifies our commitment to creating a culture of AI usage, where employees are empowered to harness the power of AI to enhance their work and drive innovation. As we continue to develop and refine our AI capabilities, the Vectorizer will play a central role in our journey towards becoming a truly AI-driven enterprise.

## Source
[Original post on bgadoci.com](https://bgadoci.com/thoughts/building-the-dataworld-vectorizer-laying-the-infrastructure-for-ai-in-the-enterprise)