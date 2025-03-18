---
date: '2025-03-18'
source_url: https://bgadoci.com/thoughts/harnessing-ai-for-better-customer-support-building-the-ai-docs-bot-at-dataworld
status: complete
tags:
- blog
- ai-projects-&-case-studies
title: 'Harnessing AI for Better Customer Support: Building the AI Docs Bot at data.world'
type: blog
---

# Harnessing AI for Better Customer Support: Building the AI Docs Bot at data.world

# Harnessing AI for Better Customer Support: Building the AI Docs Bot at data.world

![](images/Screenshot+2024-11-12+at+1.26.53%E2%80%AFPM.png)

At data.world, we are constantly innovating to make data work for our team and our customers. One of our recent projects, the AI Docs Bot, has transformed how employees and customers find crucial information within our extensive documentation. Powered by a middleware RAG (Retrieval-Augmented Generation) application called the Vectorizer, this bot bridges our massive documentation library and users, answering questions and surfacing resources in a fraction of the time traditional searches require. Here’s how we built it, why it matters, and the impact it’s making.

### The Challenge: Documentation at Scale

With 1,052 documentation pages hosted on our docs.data.world site, our content is both a rich resource and a daunting landscape. For teams in Customer Support, Customer Success, and Customer Solutions, accessing relevant information quickly is essential. Our customers expect accurate answers, fast onboarding, and smooth support experiences—all of which rely on this documentation. But finding the right page or troubleshooting step within a thousand-plus pages can be time-consuming and frustrating.

### The Solution: AI-Driven Document Retrieval, Built for Chat

Our solution, the AI Docs Bot, is powered by the Vectorizer. The Vectorizer takes our documentation and makes it accessible for retrieval through vector search and RAG. Hosted at aidocsbot.data.world, the bot leverages vectorized data to provide intelligent responses to user queries, matching questions with the most relevant information from our documentation.

But the AI Docs Bot isn’t just a standalone tool; it’s also integrated as a chatbox directly on our documentation site, offering users a seamless way to interact with our content without having to leave the page. This chat feature allows users to ask questions and receive contextual responses in real time, directly within their workflow. It’s an adaptation that enhances the bot’s usability, making it accessible exactly where our users need it most.

With approximately 1,365 user sessions each month, the bot has proven its worth both internally and externally. By delivering precise answers from our content, the AI Docs Bot is significantly cutting down the time spent searching for answers.

### The Build: Streamlit, Python, and Prompt Engineering

The AI Docs Bot build took about four weeks, with most of the effort focused on crafting a sophisticated prompt to ensure the bot’s responses were highly relevant. Developed as a Streamlit app in Python, the bot makes targeted calls to the Vectorizer, where vector search capabilities allow it to interpret complex queries and match them to relevant resources.

Prompt engineering was central to our approach. By refining the prompt to prioritize certain language and context, we trained the bot to provide responses that are not only accurate but tailored to our users’ needs. The RAG approach also allows it to pull together information from across multiple resources when necessary, giving users comprehensive, contextual answers.

### Impact: Saving Time and Improving Customer Experiences

In customer-facing roles, time is often of the essence, and the AI Docs Bot has proven invaluable. It’s estimated that our support and success teams save hours each week by using the bot, which has streamlined workflows and eliminated the need to dig through documentation manually. Moreover, it’s creating a better experience for our customers, who now receive faster, more accurate answers during support interactions.

For internal use, the bot has become an essential tool. It’s utilized for onboarding, technical support, and knowledge sharing, helping new employees get up to speed faster and enabling experienced employees to find answers quickly, even for complex queries.

### A Foundation for Future Innovation

The AI Docs Bot is more than just a tool; it’s an example of what AI Operations can achieve when it’s aligned with skilled human expertise and a clear operational goal. By combining the power of vectorized search, RAG, and prompt engineering—and embedding it directly within our documentation site—we’ve created an app that not only meets immediate needs but also provides a foundation for future AI-driven applications at data.world.

As we look forward, the success of the AI Docs Bot fuels our ambition to develop even more intelligent, user-focused applications that bridge information and insight at the speed of data.

## Source
[Original post on bgadoci.com](https://bgadoci.com/thoughts/harnessing-ai-for-better-customer-support-building-the-ai-docs-bot-at-dataworld)