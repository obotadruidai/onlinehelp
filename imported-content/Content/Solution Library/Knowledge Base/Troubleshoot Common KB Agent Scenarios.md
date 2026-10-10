---
title: Troubleshoot Common AI Agent Scenarios
---

# Troubleshoot Common AI Agent Scenarios

The KB Agent Workspace helps you identify routing issues, improve AI Agent accuracy, and optimize the overall user experience. Use the following table to quickly identify where to investigate common issues, then refer to the corresponding troubleshooting scenario for detailed guidance.

| Scenario                                                                                           | Where to investigate             |
| -------------------------------------------------------------------------------------------------- | -------------------------------- |
| [False Flow Match](<Troubleshoot Common KB Agent Scenarios.md#False_Flow_Match>)                   | Intent                           |
| [False KB Match](<Troubleshoot Common KB Agent Scenarios.md#False_KB_Match>)                       | KB Agent > KB Search             |
| [Excessive OpenAI Fallback](<Troubleshoot Common KB Agent Scenarios.md#Excessive_OpenAI_Fallback>) | Intent > Daily OpenAI Agent      |
| [Negative Feedback](<Troubleshoot Common KB Agent Scenarios.md#Negative_Feedback>)                 | Feedback and KB Agent > Accuracy |

### False Flow Match <a href="#false_flow_match" id="false_flow_match"></a>

A conversation flow is triggered even though the requested information exists in the Knowledge Base.

#### Where to investigate

From the **KB Agent** workspace menu, click **Intent**. By default The **Intent** report displays.

![](<../../../.gitbook/assets/intent report.png>)

Review:

* the original question
* the rephrased question
* the Response Flow
* the associated user feedback

#### Possible cause

The Description LLM of one or more conversation flows is too broad and overlaps with topics covered by the Knowledge Base. As a result, the routing model predicts the conversation flow instead of the Knowledge Base.

#### Recommended action

Review the Description LLM of the triggered flow and make it more specific.

For example:

* narrow its business scope
* remove ambiguous wording
* clearly distinguish it from Knowledge Base topics

Monitor subsequent interactions to verify that the correct routing behavior has improved.

### False KB Match <a href="#false_kb_match" id="false_kb_match"></a>

The Knowledge Base answers the user's question, but references an incorrect or only partially relevant article.

#### Where to investigate

From the **KB Agent** workspace menu, click **Intent**. By default The **Intent** report displays.

![](<../../../.gitbook/assets/intent report.png>)

Click on the intent you want to investigate.

On the workspace menu, click **KB Agent** , then click the **KB Search** tab.

Review:

* the retrieved article
* frequently referenced articles
* citation activity
* user feedback

#### Possible cause

The retrieved documents contain overlapping information, ambiguous headings, or insufficient contextual separation between topics.

#### Recommended action

Review the source documentation.

Consider:

* reorganizing the document
* using descriptive headings
* separating unrelated topics
* rewriting ambiguous paragraphs
* republishing the updated Knowledge Base

Continue monitoring the KB Search dashboard to verify that the expected articles are being retrieved.

### Excessive OpenAI Fallback <a href="#excessive_openai_fallback" id="excessive_openai_fallback"></a>

Many requests bypass both the Knowledge Base and conversation flows and are answered by the OpenAI fallback.

#### Where to investigate

On the workspace menu, click **Intent**, then click the **Daily OpenAI Agent**.

![](<../../../.gitbook/assets/daily openai agent.png>)

#### Possible cause

The requested information is not available in the Knowledge Base, or no conversation Flow recognizes the user's intent.

#### Recommended action

Use the collected user questions to improve your solution.

Depending on the scenario:

* create new Knowledge Base articles
* expand existing Knowledge Base content
* create dedicated conversation flows
* refine Flow Description LLMs

Aim to reserve the OpenAI fallback for questions that are intentionally outside the supported scope of your solution.

### Negative Feedback <a href="#negative_feedback" id="negative_feedback"></a>

Negative feedback increases or the overall satisfaction score declines over time.

#### Where to investigate

Review:

* **Feedback** > **Overall Rating** or **Feedback** > **Feedback**

![](<../../../.gitbook/assets/feedback list.png>)

* **KB Agent** > **Accuracy**

From the workspace menu, click **Intent**. Filter by negative rating (filter by thumbs down icon)

![](<../../../.gitbook/assets/filter negative feedback.png>)

Then locate the affected conversations in the Intent area and click each record to understand how they were routed.

![](<../../../.gitbook/assets/view intent feedback.png>)

#### Possible cause

Declining user satisfaction may indicate:

* incorrect routing decisions
* incomplete Knowledge Base content
* outdated documentation
* missing conversation flows
* conversation flows that no longer match user requests

#### Recommended action

Determine whether the issue originates from:

* the routing logic
* the Knowledge Base
* or the conversation Flow.

Update the appropriate component and continue monitoring the workspace to confirm that user satisfaction and Knowledge Base accuracy improve.
