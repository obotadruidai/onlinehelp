---
title: Set Up the Solution
---


For solution admins

This section will walk you through the steps to import and configure the solution to ensure a smooth setup and operation.

## Prerequisites

* Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
* A published AI Agent configured on your tenant. For information on how to create an AI Agent, see [Creating AI Agents](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/creating-ai-agents).
* Druid LLM API resources activated for Druid Becus and Azure OpenAI/gpt-4.1-mini on your tenant. Contact your Druid sales representative to enable dedicated resources and generate tokens.

## Installation and setup procedure

### Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution "Knowledgebase with GPT V4" and import it following the instructions provided in section [Installing Solution Templates](<../Installing Solution Templates.md>).

Wait until the import status shows as “Success”.

### Step 2. Install the custom solution from the Solutions Library

Go to the Solutions Library, search for solution "Knowledgebase with GPT V4 Custom" and import it following the instructions provided in section [Installing Solution Templates](<../Installing Solution Templates.md>).

Wait until the import status shows as “Success”.

The **Knowledgebase with GPT V4 – Custom** solution allows you to tailor the Knowledge Base flows to meet your bot’s specific needs.

{% hint style="info" %}
**NOTE:** **Best practice**: Instead of modifying the solution flows directly, clone the existing flows and create custom versions based on them. This ensures that your changes are preserved and prevents conflicts during future solution upgrades.
{% endhint %}

### Step 3. Set up the bot and KB special flows

Go to the AI Agent settings, Details page and click on **Dialog management**. The section expands. Select the following special flows belonging to the custom solution you imported from the Solution Library, as follows:

| Special Flow                 | Select                                         |
| ---------------------------- | ---------------------------------------------- |
| Intent not found flow        | Intent-not-recognized V4 - custom              |
| Knowledge Base response flow | Knowledge-Base-response-flow-agent V4 - custom |
| Intent rephrase flow         | Intent rephrase flow V4 - custom               |

Tap on **Use Knowledge Base**.

![](<../../../.gitbook/assets/KB gpt4.png>)

Scroll down and click **Save & Close**.

### Step 4. Set up AI Agent NLU parameters and the KB settings

Start with the default thresholds for both the Knowledge Base and Flows.

_KB Settings_

![](<../../../.gitbook/assets/kb settings.png>)

_NLU Thresholds_

![](../../../.gitbook/assets/nlu.png)

**Update the NLU System Prompt**

The default system prompt of the NLU Configuration contains an instruction that prevents simultaneous prediction and return response from both KB articles and Flow information.

Go to **NLU** > **Configurations** and click **Classification Model Type**. In the **System prompt** field, replace the restrictive line.

![](<../../../.gitbook/assets/system prompt.png>)

Locate the Outdated Line:

```
Using **Knowledge Base Articles** determine **if** the user's query is to get informed/retrieve information (**NOT** to perform an action or trigger a flow). In this case answer only by scoring the system intent **-800: system.knowledge-base**.
```

Replace it With:

```
Using **Knowledge Base Articles** determine **if** the user's query is best matched with KB articles or with available intents. if **Knowledge Base Articles** matches best, answer only by scoring the system intent **-800: system.knowledge-base**.
```

**Optimization Best Practices**

To prevent false positives and enable the KB Agent V4 to clearly differentiate between an information request and an action request, follow these best practices:

* **Action-oriented Flow Descriptions**. Keep your flow names and LLM descriptions specific, action-oriented, and explicitly distinct from KB article titles. This ensures the agent recognizes when a user intends to perform a task rather than just read text.
* **KB Article Matching**. Optimize article titles, summaries, and keywords to clearly state the exact user questions they answer. Avoid overly broad articles that can create false matches on unrelated queries.
* **Combined Results Behavior Testing**. Test common user scenarios that require a mixed response. The expected behavior is that the AI Agent successfully returns the KB answer while simultaneously offering or triggering the matching flow.
* **Iterative Tuning**. Review unmatched queries and false positives within the **KB Agent** workspace. Adjust your NLU thresholds, flow descriptions, and KB metadata iteratively based on real logs before training the AI Agent for production.

### Step 5. Enable Feedback Reactions in Web Chat

Users can provide positive or negative feedback / rating using thumbs-up or thumbs-down emojis, helping you enhance AI Agent interactions and improve the user experience.

![](<../../../.gitbook/assets/kn response_478x825.png>)

While the solution contains the flow for feedback collection, you need to enable feedback reactions to collect user ratings.

To enable feedback reactions in the web chat, follow these steps:

1. Go to the AI Agent details page.
2. Click **Theme** and navigate to the Webchat snippet section.
3. Click **Customize webchat** and search for **Show Actions for Bot Messages (botActivitiesActionsEnabled)**.
4. Select the option to enable it.

![](<../../../.gitbook/assets/enable buttons.png>)

5. Click on **Custom Handlers** and in the **Webchat Event Handlers (webChatEventHandler)** field, enter the following code:

```
(action, currentDruidState) => {
                        if (action.type === 'DIRECT_LINE/INCOMING_ACTIVITY' && DruidWebchat_v2.isNewActivity(currentDruidState, action.payload.activity)) {
                        if(action.payload.activity.type == "event" && action.payload.activity.name == "_positive_feedback_") {
                        DruidWebchat_v2.sendMessage("&#x1F44D");//replace the code between "" with the thumbs up emoji
                        };
                        if(action.payload.activity.type == "event" && action.payload.activity.name == "_negative_feedback_") {
                        DruidWebchat_v2.sendMessage("&#x1F44E");//replace the code between "" with the thumbs down emoji
                        }        
                        }
                    }
```

![](<../../../.gitbook/assets/custom handler feedback.png>)

6. Click the **Save** button at the top right-corner of the pop-up.
7. Save the AI Agent.

{% hint style="info" %}
**Info:** The ratings are aggregated in the [KB Agent Workspace](<Using the KB Agent Workspace.md>), where you can monitor user satisfaction (**Feedback** and **KB Agent** > **Feedback**), evaluate AI Agent performance and accuracy and identify routing issues.
{% endhint %}

### Step 6. Customize AI Agent Responses Using Variables

The **Knowledgebase with GPT V4 – Custom** solution allows you to tailor the Knowledge Base flows to meet your AI Agent specific needs.

{% hint style="info" %}
**Info:** **Best practice**: Instead of modifying the solution flows directly, clone the existing flows and create custom versions based on them. This ensures that your changes are preserved and prevents conflicts during future solution upgrades.
{% endhint %}

{% hint style="info" %}
**NOTE:** We recommend only the customization of the **Identity** part of the prompt, which contains two parts: one for the **KB V4 Agent** and one for the askOpenAi Agent. To access the prompt, in the flow **Knowledge-Base-response-flow-agent V4 - custom**, in the **Identity** step, click to open the **GPT-Identity-custom** flow.

<img src="../../../.gitbook/assets/view identity flow.png" alt="" data-size="original">

On the **GPT Prompts** step, click on the Code Extension icon and the edit icon in Editor.

<img src="../../../.gitbook/assets/code extension_prompts.png" alt="" data-size="original">

Locate the two parts of the Identity prompt and customize them as suits your needs.

<img src="../../../.gitbook/assets/GPT PROMPTS.png" alt="" data-size="original">
{% endhint %}

To customize how the AI Agent responds, navigate to the **Instructions** step in the flow **Knowledge-Base-response-flow-agent V4 - custom** and adjust the variables described in the table below.

![](<../../../.gitbook/assets/set variables.png>)

| Variable                                   | Default value | Description                                                                                                                    |
| ------------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| \[\[KBResponse]].IncludeCitations          | true          | When set to true, each response will show the source of the information received.                                              |
| \[\[KBResponse]].IncludeFeedback           | true          | When set to true, each response will have thumbs up and thumbs down for feedback.                                              |
| \[\[KBResponse]].IncludeFollowUpQuestion   | true          | When set to true, each response will have a follow-up question, related to the topic discussed.                                |
| \[\[KBResponse]].IncludeRecomendedInsights | false         | When set to true, the AI Agent offers advice to the end user, based on the information found in the knowledge base.            |
| @UseGraph                                  | false         | When set to true, the AI Agent can connect to the entity graph, if available at AI Agent level.                                |
| @DataRetrievalPrompt                       | —             | Builds instructions telling an AI how to generate and run a SQL Server Graph query, and takes action if **@UseGraph == True**. |
| @KeywordDictionary                         | —             | The user can define a specific dictionary with abbreviations for the AI Agent to use in conversations.                         |

The flow **OpenAI-response V4 - custom** exposes a similar set of variables in its **Instructions** step.

![](<../../../.gitbook/assets/openAI set var.png>)

Configure them the same way as above to control response behavior for the OpenAI flow, noting the channel-specific restrictions.

| Variable                                   | Default value | Description                                                                                                                                                                                                                           |
| ------------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[\[KBResponse]].IncludeCitations          | true          | When set to true, each response will show the source of the information received.                                                                                                                                                     |
| \[\[KBResponse]].IncludeFeedback           | true          | When set to true, each response will have thumbs up and thumbs down for feedback. Applies only to the Directline channel.                                                                                                             |
| \[\[KBResponse]].IncludeFollowUpQuestion   | true          | When set to true, each response will have a follow-up question, related to the topic discussed.                                                                                                                                       |
| \[\[KBResponse]].IncludeRecomendedInsights | false         | When set to true, the AI Agent offers advice to the end user, based on the information found in the knowledge base. Applies only to the Directline channel.                                                                           |
| \[\[KBResponse]].UseLLMStream              | false         | When set to true, the conversation will be routed to the agents that are set up to support streaming.                                                                                                                                 |
| \[\[KBResponse]].KBCheckPermissions        | false         | When set to true, the system enforces SharePoint permission checks for authenticated users. This only applies to data sources that natively support SharePoint access control lists (ACLs).                                           |
| \[\[KBResponse]].PermissionsIds            |               | Specifies the list of unique data source identifiers for which SharePoint permission validation is explicitly enabled. This parameter acts as a filter when **KBCheckPermissions** is active. Format: `["id 1", "id 2", ..., "id n"]` |
