---
date: '2025-03-18'
source_url: https://bgadoci.com/thoughts/combining-internet-research-vectorization-prompting-to-create-the-ultimate-quick-account-research-tool
status: complete
tags:
- blog
- ai-projects-&-case-studies
title: Combining Internet Research, Vectorization, & Prompting to Create the Ultimate
  Quick Account Research Tool
type: blog
---

# Combining Internet Research, Vectorization, & Prompting to Create the Ultimate Quick Account Research Tool

# Combining Internet Research, Vectorization, & Prompting to Create the Ultimate Quick Account Research Tool

![](images/owl-screen.png)

The ability to quickly and effectively research accounts is vital for sales and marketing teams. At data.world, we've taken a significant step in enhancing this process with the creation of a new application: Account Researcher. This tool leverages the power of RAG (Retrieval-Augmented Generation) technology, combining multiple data sources to create evolving, intelligent prompts that aid in account-based marketing and sales strategies. Let's dive into how Account Researcher is saving reps hours of time.

#### The Genesis of Account Researcher

The idea for Account Researcher stemmed from the need to streamline the research process for our account executives and sales teams. Traditionally, researching a potential client or account involved manually sifting through various sources of information, which was time-consuming and often inefficient. One of our reps, Samson, consistently requested a tool that could take a broader approach to research than our Prospect Researcher tool was providing. He wanted a way to quickly understand recent news and events about a company he was targeting while also creating a case for why data.world would be a good fit. Samson can then use this information to tailor his outreach.

#### The Core Components of Account Researcher

Account Researcher is a sophisticated bot that interacts with a vectorized database containing all of data.world's website and documentation site content. Additionally, it utilizes various search APIs, including Google and a tool introduced to me by Rachel Woods called "Metaphor." The integration of these diverse resources and their placement in the prompt for each API request to OpenAI is what makes Account Researcher truly impactful.

#### How it Works

The process begins with the bot asking the user for the name of the target account or company. Once this information is inputted, the app does the following:

1. The transcript of the conversation is sent to OpenAI, where we ask it to return the company name and industry.

2. The transcript is also sent to OpenAI again to return a list of competitors of that company.

3. The company name and competitors are then sent to various search APIs to return a list of resources with title, URL, and summary.

4. These results are then placed into the prompt at the appropriate place before sending it all off to OpenAI once again.

The transcript of the conversation is sent to OpenAI, where we ask it to return the company name and industry.

The transcript is also sent to OpenAI again to return a list of competitors of that company.

The company name and competitors are then sent to various search APIs to return a list of resources with title, URL, and summary.

These results are then placed into the prompt at the appropriate place before sending it all off to OpenAI once again.

For step three, we are using two sources:

- Google Custom Search API

- Metaphor

Google Custom Search API

Metaphor

Google is great, but it’s a keyword-based search and, while it offers some control of the output, the results weren’t exactly what we were looking for on their own. Metaphor solved this problem. In their words Metaphor “retrieves the best content on the Internet using embeddings-based search…” and offers some cool options for this process like auto-prompting and neural versus keyword-based search.

The combination of these results and the updating of the prompt on every user input creates some pretty magical results.

#### Constructing a Compelling Narrative

The app is then instructed to think critically about the information in the prompt. It analyzes the articles and resources, identifying how they demonstrate possible challenges faced by the target company, and then crafts a narrative that not only highlights these challenges but also outlines how data.world can provide solutions.

After some tweaking, the app successfully tells a story with resources about the target company, the possible challenges they are facing with respect to enterprise data management, and how data.world can help. All with linked resources.

![](images/Screenshot+2024-01-22+at+9.36.31+PM.png)

#### An Example of Account Researcher in Action

Let’s look at the output from Account Researcher for a few well-known companies. These results were generated in about 60 seconds.

![](images/Screenshot+2024-01-22+at+9.41.33+PM.png)

![](images/Screenshot+2024-01-22+at+9.41.29+PM.png)

![](images/Screenshot+2024-01-22+at+9.41.50+PM.png)

#### The Impact of Account Researcher

The hope is that Account Researcher will significantly streamline the research process for our sales and marketing teams. By automating the retrieval and analysis of relevant information, the tool has saved countless hours that would have otherwise been spent on manual research. Moreover, the narratives generated by the bot are not only coherent and informative but also tailored to the specific needs and challenges of the target accounts.

The Account Researcher is more than just a tool; it's a testament to the power of combining AI technologies to create innovative solutions. By harnessing the capabilities of RAG technology, neural search, and vectorized databases, we've created a tool that not only simplifies the research process but also enhances the accuracy and relevance of the information gathered. As we continue to explore the possibilities of AI in business, tools like Account Researcher will undoubtedly play a pivotal role in shaping the future of account research and analysis.

## Source
[Original post on bgadoci.com](https://bgadoci.com/thoughts/combining-internet-research-vectorization-prompting-to-create-the-ultimate-quick-account-research-tool)