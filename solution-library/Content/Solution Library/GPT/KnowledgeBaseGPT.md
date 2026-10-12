---
title: Knowledge Base with ChatGPT
---


The solution combines the DRUID Knowledge Base and ChatGPT features to provide an amazing human like, knowledgeable conversation.

Single-turn tasks are particularly useful for Knowledge Base summarization. Instead of asking the user to discover the answer by clicking all answers provided by the Knowledge Base, DRUID onboards GPT technology to summarize the answer. DRUID provides the context with the content and the question and GPT replies back with a compiled answer.

## Solution benefits

* Converse naturally, using GPT technology.
* Answer questions about your business, using information you control.
* Reduce hallucinations and inaccurate responses to acceptable levels.
* Require minimal configuration and setup.

## How it works?

DRUID orchestrates the entire conversation and asks expertise from GPT in the context of your data and business domain.

1. DRUID matches the user questions with all relevant articles from the Knowledge Base.
2. DRUD calls further the GPT3 completion model, to get a compiled, consolidated response to the user question, passing the Knowledge Base articles as context to GPT.
3. DRUID provides the consolidated response and links to the related articles.

![](<../../../.gitbook/assets/Knowledge Base with GPT.png>)

## Setting up the solution

The solution requires basic initial setup time.

### Prerequisites

* The solution requires you to have the “DRUID Starter” solution already imported in your AI Agent, as you will need the “Intent not recognized” flow
* You should have the Knowledge Base feature active on your tenant. If you want to activate it for your tenant, get in touch with [DRUID Support Team](mailto:support@druidai.com?subject=Activate%20KB%20for%20my%20tenant).

### Step 1. Import the solution

Go to the Solutions Library, search for solution **Knowledge Base with GPT** and import it.

### Step 2. Set up your Openai API Key

{% hint style="info" %}
**NOTE:** Charges apply to your Openai account according to the [Openai pricing policy](https://openai.com/pricing).
{% endhint %}

1. Go to [Openai](https://platform.openai.com/account/api-keys), log in and on the **User** menu, click **API Keys**.
2. In the API keys page, click the **Create new secret key** button.

![](<../../../.gitbook/assets/Knowledge Base with GPT_1.png>)

A secret key is generated.

3. Copy the secret key as you will need it in DRUID.
4. In Druid Portal, on your AI Agent, select solution **Knowledge Base with GPT** and on the main menu, click **Apps**.
5. Click on the **GPT** app.

![](<../../../.gitbook/assets/Knowledge Base with GPT_2.png>)

The app configuration page opens.

6. Scroll down to the Variables table and as value for the **key** variable, set up the secret key you copied from Openai.

![](<../../../.gitbook/assets/Knowledge Base with GPT_3.png>)

7. Publish the changes.

![](<../../../.gitbook/assets/Knowledge Base with GPT_4.png>)

### Step 3. Link the Knowledge Base special flow

Go to the AI Agent settings, Details page and click the **Dialog management** section header. The section expands.

![Graphical user interface, text, application, email Description automatically generated](<../../../.gitbook/assets/Knowledge Base with GPT_5.png>)

Scroll down and tap on **Use Knowledge Base**, then select the **Knowledge-base-response-flow** that comes with the solution.

![A picture containing application Description automatically generated](<../../../.gitbook/assets/Knowledge Base with GPT_6.png>)

### Step 4. Import your Knowledge Base data sources

Import your articles by following the procedure described in Knowledge Base, section [Adding data sources](https://druidai.gitbook.io/druid-ai-docs/knowledge-base/knowledgebase).

![Graphical user interface, text, application, Teams Description automatically generated](<../../../.gitbook/assets/Knowledge Base with GPT_7.png>)

### Step 5. Fine tune the GPT integration

Ask the AI Agent a question or multi-sentence questions, multiple topics. DRUID matches all relevant articles and GPT provides one compiled answer.

The solution uses the "text-davinci-003" model and you can further fine-tune the integration.

![](<../../../.gitbook/assets/Knowledge Base with GPT_8.png>)

## Related Topics

* [Knowledge Base](https://druidai.gitbook.io/druid-ai-docs/knowledge-base/knowledgebase)
