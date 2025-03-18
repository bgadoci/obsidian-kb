---
date: '2025-03-18'
source_url: https://bgadoci.com/thoughts/a-brief-history-of-ai-operations-at-dataworld-scaling-for-the-future-with-chat-gpt-teams
status: complete
tags:
- blog
- ai-projects-&-case-studies
title: 'A Brief History of AI Operations at data.world: Scaling for the Future with
  Chat-GPT Teams'
type: blog
---

# A Brief History of AI Operations at data.world: Scaling for the Future with Chat-GPT Teams

# A Brief History of AI Operations at data.world: Scaling for the Future with Chat-GPT Teams

The world of AI has seen rapid evolution, and at data.world, we've been at the forefront of this revolution. As we continue to grow and adapt to the ever-changing landscape, it's essential to look back at where we started, understand the challenges we faced, and appreciate the solutions we've implemented to meet those challenges. This post will take you through the journey of AI Operations (AI Ops) at data.world, the need for scaling, and the pivotal role that Chat-GPT Teams has played as a front-end for our operations.

#### The Birth of AI Ops at data.world

AI Ops at data.world officially began on August 23, 2023—a date that marked the beginning of a transformative journey. The initiative was born out of the need to enhance productivity and create bespoke tools that could make our employees the most productive in the marketplace. The idea was simple: leverage AI to do more, better, and faster.

But the true origin story of AI Ops, and specifically the development of one of our most important tools, began earlier during a leadership onsite. I found myself in a conversation with our co-founder and CTO, Bryon Jacob. I was lamenting an idea I had to make it easier for those interested in data.world to research us. The idea was that instead of asking potential customers and partners to hunt and peck around the website, we could offer them a chat experience that directed them to relevant resources while letting them control the interaction. This conversation laid the groundwork for what would eventually become "Conversations with Archie," a precursor to the tools we now rely on. Here's Bryon, less than 24 hours after I mentioned my idea to him, letting me know that he created a working version of it. As you can see, I'm excited!

![](images/image.png)

"Conversations with Archie" was more than just a chatbot; it was an early attempt to democratize access to information about data.world. It allowed users to interact in a way that was natural, intuitive, and, most importantly, efficient. This concept of creating a more user-focused, AI-driven interface would later inspire many of the tools that now power our AI Ops.

Our early efforts centered around Archie, and this phase was characterized by experimentation and a desire to democratize AI across the company. We wanted to talk to everyone, understand their needs, and develop tools that could address those needs effectively.

The results were immediate and encouraging; even before the full implementation of the vectorizer, we saw a 25% increase in productivity across teams. This early success underscored the potential of AI Ops and justified further investment in building a robust, scalable system. We recognized that harnessing the creativity and pent-up innovation within our employees was crucial, and having a dedicated internal leader—someone like myself—to channel this energy was essential.

#### Scaling the Need: The Challenges We Faced

As AI Ops began to take shape, it quickly became apparent that scaling would be a significant challenge. The initial success of our tools—such as the Prospect Researcher, Account Researcher, Landing Page Maker, and RFI Writer—was promising. However, as more departments and teams began to adopt these tools, the demand for customization and new tool creation skyrocketed.

This rapid adoption highlighted several critical challenges:

1. Volume of Requests: With every department seeking AI-driven solutions, the volume of requests quickly became overwhelming. Each team had unique needs, requiring tailored solutions that couldn't be met with a one-size-fits-all approach.

2. Quality Control: As we scaled, maintaining the quality of AI-driven outputs became increasingly challenging. Ensuring that each tool was delivering accurate, relevant, and high-quality results was a top priority.

3. Integration and Accessibility: We needed a way to integrate these tools seamlessly into the workflows of various teams. Moreover, these tools had to be accessible and easy to use for all employees, regardless of their technical expertise.

Volume of Requests: With every department seeking AI-driven solutions, the volume of requests quickly became overwhelming. Each team had unique needs, requiring tailored solutions that couldn't be met with a one-size-fits-all approach.

Quality Control: As we scaled, maintaining the quality of AI-driven outputs became increasingly challenging. Ensuring that each tool was delivering accurate, relevant, and high-quality results was a top priority.

Integration and Accessibility: We needed a way to integrate these tools seamlessly into the workflows of various teams. Moreover, these tools had to be accessible and easy to use for all employees, regardless of their technical expertise.

#### The Evolution of the Vectorizer: Centralization and Advanced Knowledge Retrieval

One of the most significant breakthroughs in scaling AI Ops at data.world was the development of the vectorizer. Initially, our early tools each relied on separate JSON files that contained the necessary resources. This setup was functional but far from optimal. Managing these individual files across various tools became increasingly cumbersome as the number of tools grew. It also limited our ability to update resources efficiently, as each JSON file needed to be maintained separately.

The vectorizer revolutionized this process by centralizing all the resources into a single, unified system. Built on a Node.js Express backend, with a React front-end, and MongoDB Atlas serving as the database with vector search indexes, the vectorizer acts as the "enterprise brain" of our operations. This centralization allowed us to replace the separate JSON files with one central source that could be updated nightly, drastically improving efficiency and consistency across all tools. Instead of managing individual files, we now offered content via an API, making it accessible to all tools seamlessly.

![](images/Screenshot+2024-08-15+at+12.48.14%E2%80%AFAM.png)

But the vectorizer did more than just centralize resources. It expanded our capabilities from merely offering resources to providing deep knowledge. This advanced implementation of Retrieval-Augmented Generation (RAG) allows our tools to give not only accurate answers but also highly relevant resource recommendations. The vectorizer draws from a broad range of sources, including less obvious places like specific and detailed PDFs, which are integrated into the enterprise brain.

![](images/Screenshot+2024-08-15+at+12.48.25%E2%80%AFAM.png)

To achieve this, we employ several different chunking techniques and embedding approaches. These methods ensure that each source is optimally available for whatever tool is built on top of the vectorizer. For example, our Article Search API returns resources that the vectorizer scrapes from various sources across the enterprise, pulling in relevant articles, documents, and other materials. In contrast, our Knowledge API digs deeper, returning detailed knowledge based on the same scraped data plus specific PDFs and documents that we’ve intentionally added to the enterprise brain. This API is integral in delivering more in-depth and tailored responses.

Additionally, the vectorizer's API allows for filtering and limiting to ensure the most accurate retrieval of information. This capability is crucial for maintaining the precision and relevance of the tools built on the vectorizer, ensuring that users get the best possible results with each query.

#### Enter Chat-GPT Teams: The Front-End Solution and Custom GPTs

To address the challenges of scale and accessibility, we introduced Chat-GPT Teams as the front-end solution for our AI Ops. This decision was a game-changer, as it allowed us to provide a user-friendly interface for the mass consumption of AI-driven tools. But the true breakthrough came when we enabled custom GPTs within Chat-GPT Teams that could access the vectorizer directly.

These custom GPTs transformed how our employees interacted with AI tools. By integrating the vectorizer with Chat-GPT Teams, we created a system where custom GPTs could tap into the vast knowledge base stored within the vectorizer. This integration, combined with the built-in tools for Chat-GPT like file uploads, internet search, and the code interpreter, enabled incredibly robust interactions that benefited every department at data.world.

For example, a marketing team member could use a custom GPT to access the vectorizer and pull up the latest articles and PDFs related to a specific topic. At the same time, a sales team member could use a different custom GPT to generate detailed knowledge reports tailored to a potential client’s needs. The possibilities are endless, and the flexibility offered by custom GPTs has been instrumental in driving AI adoption across the organization.

The introduction of Chat-GPT Teams had several key benefits:

1. Scalability: With a centralized platform, we could scale the deployment of AI tools across the company. Employees could request new tools or modifications to existing ones through a simple interface, reducing the bottleneck that previously existed.

2. Ease of Use: Chat-GPT Teams was designed with the end-user in mind. The interface was intuitive, allowing even non-technical users to interact with AI tools effectively. This democratization of AI was crucial in driving adoption across the organization.

3. Speed of Deployment: Thanks to the integration with our vectorizer, we could create and deploy new tools faster than ever before. This agility was essential in keeping up with the growing demand for AI-driven solutions.

4. Robust Interactions: The custom GPTs, combined with tools like file uploads, internet search, and code interpreter, created an ecosystem where users could engage in deep, meaningful interactions with AI. This capability has empowered every department at data.world to leverage AI in ways that were previously unimaginable.

Scalability: With a centralized platform, we could scale the deployment of AI tools across the company. Employees could request new tools or modifications to existing ones through a simple interface, reducing the bottleneck that previously existed.

Ease of Use: Chat-GPT Teams was designed with the end-user in mind. The interface was intuitive, allowing even non-technical users to interact with AI tools effectively. This democratization of AI was crucial in driving adoption across the organization.

Speed of Deployment: Thanks to the integration with our vectorizer, we could create and deploy new tools faster than ever before. This agility was essential in keeping up with the growing demand for AI-driven solutions.

Robust Interactions: The custom GPTs, combined with tools like file uploads, internet search, and code interpreter, created an ecosystem where users could engage in deep, meaningful interactions with AI. This capability has empowered every department at data.world to leverage AI in ways that were previously unimaginable.

![](images/Screenshot+2024-08-15+at+12.48.48%E2%80%AFAM.png)

#### The Three Legs of the AI Ops Stool

At the core of AI Ops at data.world are three essential components: the vectorizer, the front-end interface (Chat-GPT Teams), and metrics and tracking. These three elements form the foundation upon which our AI operations are built.

1. The Vectorizer: The Enterprise Brain

As described earlier, the vectorizer is the engine that powers our AI tools. By centralizing all resources and implementing advanced knowledge retrieval techniques, the vectorizer ensures that every tool built on top of it is accurate, efficient, and up-to-date. The vectorizer's API allows for precise filtering and retrieval, making it the cornerstone of our AI Ops.

2. Chat-GPT Teams: Front-End for Mass Consumption

Chat-GPT Teams serves as the front-end interface for our AI tools. It is the bridge between the complex AI models powered by the vectorizer and the end-users who rely on these tools daily. The ability to create custom GPTs that directly access the vectorizer has been a major breakthrough, enabling robust and tailored interactions across all departments.

3. Metrics and Tracking: Measuring Success

The final leg of the AI Ops stool is metrics and tracking. To ensure that our AI tools are delivering value, we implemented robust tracking mechanisms using Mixpanel to measure their performance. These metrics allow us to assess the impact of our tools, identify areas for improvement, and make data-driven decisions about future development.

Metrics and tracking also play a crucial role in maintaining the quality of our AI outputs. By continuously monitoring performance, we can quickly identify and address any issues, ensuring that our tools remain reliable and effective.

![](images/Screenshot+2024-08-15+at+12.51.09%E2%80%AFAM.png)

#### The Road Ahead: Continuous Improvement and Innovation

As we look to the future, the journey of AI Ops at data.world is far from over. We are committed to continuous improvement and innovation, always seeking new ways to leverage AI to drive productivity and efficiency across the organization.

The introduction of Chat-GPT Teams and the development of our vectorizer have been significant milestones, but they are just the beginning. As we continue to refine our processes and expand our capabilities, we are confident that AI Ops will play an increasingly vital role in shaping the future of data.world.

In conclusion, the story of AI Ops at data.world is one of growth, adaptation, and innovation. From humble beginnings to the implementation of cutting-edge solutions, we have come a long way in a short time. And as we continue to scale and evolve, one thing is certain: the best is yet to come.

## Source
[Original post on bgadoci.com](https://bgadoci.com/thoughts/a-brief-history-of-ai-operations-at-dataworld-scaling-for-the-future-with-chat-gpt-teams)