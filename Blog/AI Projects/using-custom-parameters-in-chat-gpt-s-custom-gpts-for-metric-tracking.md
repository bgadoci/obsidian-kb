---
date: '2025-03-18'
source_url: https://bgadoci.com/thoughts/using-custom-parameters-in-chat-gpts-custom-gpts-for-metric-tracking
status: complete
tags:
- blog
- ai-projects-&-case-studies
title: "Using Custom Parameters in Chat-GPT\u2019s Custom-GPTs for Metric Tracking"
type: blog
---

# Using Custom Parameters in Chat-GPT’s Custom-GPTs for Metric Tracking

# Using Custom Parameters in Chat-GPT’s Custom-GPTs for Metric Tracking

![](images/0c52fc4a-7c88-4dc4-b170-2e993be645c6+1.png)

I'm sharing this short article in case others are trying to solve a similar problem. Here is the setup: we’ve created several early and MVP versions of some generative AI tools for data.world. These tools were either quick Streamlit or React/Node apps that interacted with OpenAI through a detailed system message and a Retrieval-Augmented Generation (RAG) architecture.

The reason we built these apps instead of using Custom-GPTs was twofold. First, I didn’t quite understand how Custom-GPT actions worked and couldn’t find much information online at that time. Second, until recently, you couldn’t opt out of having OpenAI train on your data. Their recent updates to Teams have resolved this, so I started experimenting with how they might work.

It turns out the Actions feature is much more robust than I thought. Simply give it your API spec and specify some parameters in the “instructions,” and it does the rest of the work for you. I was busy trying to figure out where to put filters and parameters in the Actions UI when all you had to do was tell the bot about it in the instructions, and it forms the calls for you. Magical.

![](images/Screenshot+2024-07-30+at+3.28.23%E2%80%AFPM.png)

All that worked great. However, when I checked Mixpanel, all the calls to the Vectorizer (middleware where the tracking happened) had a domain of unknown. My code checked the Origin and Referrer to pull the domain out, but nothing was being set for calls coming from Chat-GPT. I tried for a while to get Origin and Referrer into the calls but didn’t get anywhere. Eventually, I figured it out. You can specify in your schema document a property that will show up in the params section. In this case, I called it customGPTId and told my middleware code to look for this if there is no value for Origin or Referrer. It worked like a charm. The end result is I now have metrics around how many times each Custom-GPT I’ve created is hitting my middleware and which APIs it’s using.

![](images/carbon+%283%29.png)

Learning how to use Actions and track their usage is a very powerful tool for companies looking at implementing AI operations. It will save you a lot of custom builds.

## Source
[Original post on bgadoci.com](https://bgadoci.com/thoughts/using-custom-parameters-in-chat-gpts-custom-gpts-for-metric-tracking)