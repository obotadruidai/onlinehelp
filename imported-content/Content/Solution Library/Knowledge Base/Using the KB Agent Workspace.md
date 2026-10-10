---
title: "Using the KB Agent Workspace"
---

<a id="UsingtheKBAgentWorkspace"></a>


The [Understanding KB Agent V4 Routing Logic](Understanding%20AI%20Agent%20Routing%20Logic.md) topic explains how the KB Agent routes user requests to a conversation Flow, the Knowledge Base, or the OpenAI fallback. The **KB Agent Workspace** builds on that foundation by providing the operational insights needed to monitor those routing decisions in production, evaluate their effectiveness, and continuously optimize your Knowledge Base solution.

Use the KB Agent Workspace to:

- Monitor Knowledge Base accuracy.
- Measure user satisfaction and solution ROI.
- Analyze routing decisions.
- Identify incorrect Knowledge Base matches.
- Detect excessive OpenAI fallback usage.
- Continuously optimize your Knowledge Base and conversation flows.

<a id="AccesstheWorkspace"></a>

## Access the Workspace

To open the workspace, from the **Workspace** dropdown, select **KB Agent**.

The workspace contains three core areas described in subsequent sections.

<a id="Intent"></a>

### Intent

The Intent section helps you understand how each user request was processed.

Use this section to answer questions such as:

- How was the request routed?
- Was the request handled by a conversation Flow?
- Was it answered by the Knowledge Base?
- Did it trigger the OpenAI fallback?

The available reports (views and charts) let you review individual interactions, routing history, daily activity, and trends across conversation flows, the Knowledge Base, and the OpenAI fallback. Click the tabs to navigate intent-related insights.

![](../../Resources/Images/Knowledge%20Base%20with%20GPT/intent%20tab.png)

> **Info:** The **Intent** area (views and charts) is typically the first place to investigate when troubleshooting routing issues.

<a id="Feedback"></a>

### Feedback

The Feedback section helps you evaluate user satisfaction and measure the effectiveness of your AI Agent

Use this section to:

- Review positive and negative feedback.
- Analyze user comments.
- Identify frequently down-rated responses.
- Monitor satisfaction trends over time.
- Export feedback for additional analysis.

Click the tabs to navigate feedback-related insights.

![](../../Resources/Images/Knowledge%20Base%20with%20GPT/feedback%20tab.png)

> **Info:** Consistently positive feedback usually indicates that users are receiving accurate answers and that your KB Agent effectively covers the supported scenarios.

<a id="KBAgent"></a>

### KB Agent

The KB Agent area provides operational dashboards for monitoring the overall health of your AI Agent.

Use this section to:

- Get intent insights by flows
- Review the most frequently referenced Knowledge Base articles.
- Monitor citation activity.
- Analyze user feedback.
- Measure KB Agent accuracy / resolution rates.

![](../../Resources/Images/Knowledge%20Base%20with%20GPT/kb%20agent.png)

> **Info:** Navigate through KB Agent tabs to see the specific overall insights. Use **KB Agent** insights together with the **Intent** and **Feedback** areas to continuously improve your solution.

<a id="MonitortheAIAgentPerformance"></a>

## Monitor the AI Agent Performance

Review the workspace regularly after publishing new Knowledge Base content or updating conversation flows.

A healthy AI Agent typically shows:

- High positive feedback.
- High resolution rate.
- Accurate routing between Flows and the Knowledge Base.
- Low OpenAI fallback usage.
- Frequently reused Knowledge Base articles.

If any of these metrics begin to decline, investigate the affected conversations and update the appropriate Knowledge Base articles or conversation flows.

<a id="BestPractices"></a>

## Best Practices

To maintain a high-performing AI Agent:

- Review user feedback regularly.
- Investigate negatively rated conversations.
- Keep Flow Description LLMs concise and specific.
- Organize Knowledge Base articles into clearly defined topics.
- Monitor OpenAI fallback usage and minimize it by expanding Knowledge Base coverage or creating new conversation flows.
- Measure the impact of every Knowledge Base update by monitoring feedback, routing behavior, and resolution rates over time.
