---
title: "Troubleshoot Common AI Agent Scenarios"
---

<a id="TroubleshootCommonAIAgentScenarios"></a>


The KB Agent Workspace helps you identify routing issues, improve AI Agent accuracy, and optimize the overall user experience. Use the following table to quickly identify where to investigate common issues, then refer to the corresponding troubleshooting scenario for detailed guidance.

| Scenario | Where to investigate |
| --- | --- |
| [False Flow Match](#False_Flow_Match) | Intent |
| [False KB Match](#False_KB_Match) | KB Agent > KB Search |
| [Excessive OpenAI Fallback](#Excessive_OpenAI_Fallback) | Intent > Daily OpenAI Agent |
| [Negative Feedback](#Negative_Feedback) | Feedback and KB Agent > Accuracy |

<a id="FalseFlowMatch"></a>

## <a id="False_Flow_Match"></a>False Flow Match

A conversation flow is triggered even though the requested information exists in the Knowledge Base.

<a id="Wheretoinvestigate"></a>

### Where to investigate

From the **KB Agent** workspace menu, click **Intent**. By default The **Intent** report displays.

![](../../Resources/Images/Knowledge%20Base%20with%20GPT/intent%20report.png)

Review:

- the original question
- the rephrased question
- the Response Flow
- the associated user feedback

<a id="Possiblecause"></a>

### Possible cause

The Description LLM of one or more conversation flows is too broad and overlaps with topics covered by the Knowledge Base. As a result, the routing model predicts the conversation flow instead of the Knowledge Base.

<a id="Recommendedaction"></a>

### Recommended action

Review the Description LLM of the triggered flow and make it more specific.

For example:

- narrow its business scope
- remove ambiguous wording
- clearly distinguish it from Knowledge Base topics

Monitor subsequent interactions to verify that the correct routing behavior has improved.

<a id="FalseKBMatch"></a>

## <a id="False_KB_Match"></a>False KB Match

The Knowledge Base answers the user's question, but references an incorrect or only partially relevant article.

<a id="Wheretoinvestigate1"></a>

### Where to investigate

From the **KB Agent** workspace menu, click **Intent**. By default The **Intent** report displays.

![](../../Resources/Images/Knowledge%20Base%20with%20GPT/intent%20report.png)

Click on the intent you want to investigate.

On the workspace menu, click **KB Agent** , then click the **KB Search** tab.

Review:

- the retrieved article
- frequently referenced articles
- citation activity
- user feedback

<a id="Possiblecause1"></a>

### Possible cause

The retrieved documents contain overlapping information, ambiguous headings, or insufficient contextual separation between topics.

<a id="Recommendedaction1"></a>

### Recommended action

Review the source documentation.

Consider:

- reorganizing the document
- using descriptive headings
- separating unrelated topics
- rewriting ambiguous paragraphs
- republishing the updated Knowledge Base

Continue monitoring the KB Search dashboard to verify that the expected articles are being retrieved.

<a id="ExcessiveOpenAIFallback"></a>

## <a id="Excessive_OpenAI_Fallback"></a>Excessive OpenAI Fallback

Many requests bypass both the Knowledge Base and conversation flows and are answered by the OpenAI fallback.

<a id="Wheretoinvestigate2"></a>

### Where to investigate

On the workspace menu, click **Intent**, then click the **Daily OpenAI Agent**.

![](../../Resources/Images/Knowledge%20Base%20with%20GPT/daily%20openai%20agent.png)

<a id="Possiblecause2"></a>

### Possible cause

The requested information is not available in the Knowledge Base, or no conversation Flow recognizes the user's intent.

<a id="Recommendedaction2"></a>

### Recommended action

Use the collected user questions to improve your solution.

Depending on the scenario:

- create new Knowledge Base articles
- expand existing Knowledge Base content
- create dedicated conversation flows
- refine Flow Description LLMs

Aim to reserve the OpenAI fallback for questions that are intentionally outside the supported scope of your solution.

<a id="NegativeFeedback"></a>

## <a id="Negative_Feedback"></a>Negative Feedback

Negative feedback increases or the overall satisfaction score declines over time.

<a id="Wheretoinvestigate3"></a>

### Where to investigate

Review:

- **Feedback** > **Overall Rating** or **Feedback** > **Feedback**

![](../../Resources/Images/Knowledge%20Base%20with%20GPT/feedback%20list.png)

- **KB Agent** > **Accuracy**

From the workspace menu, click **Intent**. Filter by negative rating (filter by thumbs down icon)

![](../../Resources/Images/Knowledge%20Base%20with%20GPT/filter%20negative%20feedback.png)

Then locate the affected conversations in the Intent area and click each record to understand how they were routed.

![](../../Resources/Images/Knowledge%20Base%20with%20GPT/view%20intent%20feedback.png)

<a id="Possiblecause3"></a>

### Possible cause

Declining user satisfaction may indicate:

- incorrect routing decisions
- incomplete Knowledge Base content
- outdated documentation
- missing conversation flows
- conversation flows that no longer match user requests

<a id="Recommendedaction3"></a>

### Recommended action

Determine whether the issue originates from:

- the routing logic
- the Knowledge Base
- or the conversation Flow.

Update the appropriate component and continue monitoring the workspace to confirm that user satisfaction and Knowledge Base accuracy improve.
