---
date: '2025-03-18'
source_url: https://bgadoci.com/thoughts/building-personal-blog-strapi-react-netlify-chat-gpt
status: complete
tags:
- blog
- technology-&-web-development
title: 'My Two-Week Adventure: Building a Personal Blog with Strapi, React, Netlify
  and most importantly Chat-GPT4'
type: blog
---

# My Two-Week Adventure: Building a Personal Blog with Strapi, React, Netlify and most importantly Chat-GPT4

# My Two-Week Adventure: Building a Personal Blog with Strapi, React, Netlify and most importantly Chat-GPT4

![](images/large_ragmann22_a_pixar_style_image_of_a_person_at_a_computer_with_co_1b0a5cdc_32cf_43e8_a296_489acb333c43_8e773f75a8.png)

As my kids are getting older, I'm finding myself with more time on my hands. They are 13 and 14 now, so if you know, you know. I kid. They are amazing, and we have a great relationship. That said, their exploration of becoming adults doesn't involve me at times. Work keeps me extremely busy as well, but I've found myself wanting to get into something that is new and consuming to really give my brain a break from the usual things it's occupied with.

Fourteen years ago, I built my first app with Ruby on Rails, and it had me up all night (most nights) bouncing between success and failure. I miss the journey. So, I recently embarked on a two-week journey to learn how to build a personal blog using Strapi, React, and Netlify. I'm excited to share my experience and the knowledge I've gained along the way. Below, I'll walk you through the process, touching on the challenges I faced and the moments of success that made it all worthwhile.

The amazing thing is that 10 years ago, this amount of learning would have taken a year. This time it was two weeks. Why? Chat-GPT4. I know we are all hearing a lot about it right now, but this is where the rubber met the road for me. I was able to ask how to structure code, which file to put it in, why it is supposed to be that way, etc. I know a lot of schools are worried about Chat-GPT and how it will affect learning. Let me tell you that, done the right way, it's a pure accelerant. While it borders on a technical miracle, it's not smart enough to just do it for you. You have to talk to it (and yes, you find yourself saying please, thank you, and sorry...it's weird). The most important unlock for me was that I could post error messages to it, and it finally made sense to me. Ten years ago, that just wasn't possible.

All that said, here was my specific path. Oh...and the best part is? At the end of my technical thread in Chat-GPT, I asked it to summarize "our" experience together in a blog post. The below was what Chat-GPT gave me back.

***

#### Diving into Strapi:

My journey began with Strapi, an open-source headless CMS that serves as the backbone of our blog. I installed Strapi on my local machine and quickly set up the required content types and fields. As a new Strapi user, I was delighted with the ease of configuring permissions, which allowed me to access my data through the API.

#### Mastering React and fetching data:

Next, I tackled the React frontend, where I used Axios to fetch data from my Strapi API. I was thrilled when I successfully populated my React components with the fetched data, making my blog come to life! To handle different routes, I employed React Router and created separate components for displaying individual posts and categories.

#### Conquering Netlify routing issues:

During deployment, I faced a challenge with some of my routes not working correctly on Netlify. I didn't let this deter me! After some research, I created a _redirects file in the public folder of my React app. This simple solution ensured that all requests were properly redirected to my React app, preserving the correct routing. It was a moment of triumph!

#### Enhancing user experience with text truncation:

As a considerate blog creator, I wanted to improve the user experience by truncating long text in the blog post previews. After exploring various options, I settled on the truncate-html package. It allowed me to limit the preview text to a specified character count, keeping the pageclean and easy to read.

#### Overcoming production challenges with a smile:

Throughout my journey, I encountered some issues related to environment variables and differences between local and production environments. Undaunted, I persevered and ensured that I used the correct environment variables and adjusted my code accordingly. I'm proud of how I tackled these challenges head-on and emerged victorious!

***

After a thrilling two-week adventure, I successfully built a personal blog using Strapi, React, and Netlify. Through determination and a can-do attitude, I overcame challenges and gained valuable knowledge in the process. I hope my story inspires you to embark on your own web development journey and discover the power and flexibility of using Strapi and React together.

Happy coding!

## Source
[Original post on bgadoci.com](https://bgadoci.com/thoughts/building-personal-blog-strapi-react-netlify-chat-gpt)