---
date: '2025-03-18'
source_url: https://bgadoci.com/thoughts/cc-chat-ai-operations-bringing-catalog-cocktails-tolife
status: complete
tags:
- blog
- ai-projects-&-case-studies
title: "C&C Chat: AI Operations Bringing Catalog & Cocktails to\_Life"
type: blog
---

# C&C Chat: AI Operations Bringing Catalog & Cocktails to Life

# C&C Chat: AI Operations Bringing Catalog & Cocktails to Life

Juan and Tim’s engaging conversations on enterprise data just got even more interactive – with our new app. Ask questions, explore episodes, and dive into discussions with your favorite guests, all powered by data.world's cutting-edge AI Operations. Ready to chat? Jump in now!

![](images/8479fcf804dec8e8f76996700c2546b8+1.png)

We’re excited to launch a project that is more than it appears: Catalog & Cocktails Chat. For years, Juan and Tim have been discussing enterprise data with some of the smartest people around on their podcast, Catalog & Cocktails. Today, we’re giving fans of the show a new way to learn and have a little fun along the way. This app actually highlights a lot of the progress we’ve made on the AI Operations side at data.world and utilizes an internal infrastructure that had this bespoke app spun up in about a week. Let’s take a look at the app and then dive into some of the things that make it special.

### C&C Chat

You can find the app at here, where you can chat to learn what the show and its guests have said about just about any topic. Want to learn more about governance? Lineage? Data Discovery? Gen AI? Just type in your question, and the app will return specific episodes, conversations, and speakers. Want to go deeper? Just keep chatting. You can also select a speaker and find out what they had to say during their time on the show. What did Katariina Kari, Lead Ontologist at Ikea, say when she was on? Or Vip Parmer, Global Head of Data Management from WPP? The show has had hundreds of guests, each with a wealth of knowledge to share, and now you can access that instantly. The app lets you explore complex topics in a fun way and leverages what Juan and Tim have done so well with the show: having real, non-salesy, no-BS conversations about enterprise data. There are also a few Easter eggs in there for fun (ask it what its favorite cocktail is!).

### Why is this app worth talking about?

While C&C Chat appears to be a simple chat app, it’s doing a whole lot more and highlights the way we are using AI inside data.world in a serious way—not just to power our product but to make us a better company. We introduced AI Operations at data.world around 8 months ago because we believe that using AI isn’t just a technological enhancement but a way to create a smarter, more responsive business model. It’s about transcending traditional roles and redefining how artificial intelligence can fundamentally improve every aspect of an organization. Our implementation of AI Ops starts with a true operations perspective, and over my time leading this role, I’ve spent many hours interviewing and understanding how different areas of our business work. This process has led to internal tools that help salespeople research accounts and write RFPs, help BDRs write better emails, and help generate copy for landing pages. Additionally, we have external tools that help our customers find documentation faster and prospective customers get to know data.world in a more natural and comfortable way. It’s a truly rewarding experience to help our employees and customers become more efficient, productive, and happy about their work.

Throughout this process, as you can imagine, we have lots of fun ideas pop up. C&C Chat was one of those ideas. While it seems simple, there is actually some pretty complex stuff going on. To get the app to respond correctly, we had to give it access to all the podcast transcripts and their locations on the website. It also has to have an understanding of who all the speakers are and where they fit into the show. Moreover, it has to be able to not only recommend episodes but also answer questions and do so in a way that brings together opinions, resources, and enterprise data concepts. Creating a “simple” app like this is still a big undertaking. But, because of our investment in AI Ops as a discipline inside our company, we’ve built infrastructure that makes this much more doable. That infrastructure is called Vectorizer.

The Vectorizer is an internal app that works really hard for us. Every night, it visits all our public-facing resources (e.g., our website, docs site, tutorials, what’s new site, etc.) and checks to see if there is any new, deleted, or updated content. When Vectorizer ingests that content, it generates embeddings (in one of two ways: content or summary embeddings) and stores them in a database. With a vector search index sitting on top of that, we expose an API that allows other apps to send in text and get related resources. That API call can specify which resources it wants results from and how many. Essentially, the Vectorizer acts as a RAG middleware resource that is self-updating. This is really great for building apps that want to recommend resources. But, when it comes to something like podcast transcripts that are long and span multiple topics, it can be hard to get all the information a bot might need to answer a question directly, especially if you are averaging embeddings from chunked transcripts. You lose some nuance. This is where the Vectorizer Knowledge API comes in.

The Vectorizer Knowledge API allows us to turn the scraped website content into multiple smaller chunks with embeddings of their own. More it allows us to upload PDFs that might contain valuable information that don’t have a home on the web but may be valuable in answering certain questions.  When a call is made to the Knowledge API endpoint, it goes and finds the specific chunks that are most relevant and then summarizes them into a response that can help the bot with more complex questions and answers. Now, by making two calls from a chat app—one for resources and one for knowledge—the bot has a much better foundation for generating an answer.

Another thing that was important was making sure the right speakers were returned at the right time but also to surface other speakers who might have talked about similar topics. To do this the app creates a collection of speakers in the DB which contains each speaker and their episodes (and episode summaries). The app then generates embeddings for each speaker and based on the users input will insert them into the system message so the AI knows these people are related to the topic.

Lastly, this little chat app has one more surprise. As conversations happen, it’s monitoring the dialogue for any sign of genuine interest in data.world as a solution. If it detects there is a non-intrusive, non-salesy opportunity to offer to set up a conversation with an expert at data.world, it will do just that. It will ask the user if they would like to, and if they say yes, it will ask them for an email or phone number and a preferable time to meet. That information is immediately forwarded to the data.world team.

### AI Operations is worth it

As you can see, this fun and useful app is deploying a lot of pretty powerful technology and previous investment in infrastructure. At data.world, this commitment to AI for not just our product but also our customers and everyone at our company has us moving really fast and having a lot of fun creating powerful, useful solutions. Give C&C Chat a spin and let us know what you think.

## Source
[Original post on bgadoci.com](https://bgadoci.com/thoughts/cc-chat-ai-operations-bringing-catalog-cocktails-tolife)