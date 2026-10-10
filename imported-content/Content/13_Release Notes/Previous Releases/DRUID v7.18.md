---
layout:
  title:
    visible: false
---

<a id="DRUID718"></a>

# DRUID 7.18

Deployment Dates

The table below lists the deployment date of DRUID v7.18 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| September 26, 2024 | October 24, 2024 | October 24, 2024 | October 24, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Connector Actions - Disable full database logging

<a id="WhatsNew"></a>

## What's New

- **Mobile App Channel**. You can now deploy AI Agents in mobile apps with support for push notifications, ensuring users receive messages even when the app is closed. The setup is managed through the DRUID Connector Host, providing secure communication between the AI Agent and the app's backend services.  For more information, see [Mobile App Channel](../../Channels/Mobile%20App%20Channel.md).
- **AI Agent Audit Trail**. The AI Agent Audit Trail feature provides a complete history of all changes made to flows and integrations within a AI Agent. Users can track updates, view detailed change logs, and compare different versions to easily identify modifications. This feature enhances transparency and simplifies troubleshooting.

![](../../Resources/Images/Bot%20Audit%20Trail/historical%20changes.png)

For more information, see [AI Agent Audit Trail](../../Data%20Analytics%20%26%20Insights/History%20%26%20Logs/AI%20Agent%20Audit%20Trail.md).

<a id="Improvements"></a>

## Improvements

- **Connector Actions - Disable full database logging**: Added the option to **Disable Connector Audit Full Database Logging**. With this feature, all successful integrations will be deleted from the Connector Audit logs, while only failed integrations will be recorded. This option is particularly useful when handling large entity payloads or processing a high volume of requests that don’t require detailed tracking. It helps reduce tracking overhead while ensuring errors are still logged for monitoring and debugging purposes.

![](../../Resources/Images/druid%207.18/logging.png)

- **Knowledge Base - Data source Type update**: The **Structured Documents** data source type now includes both structured Excel and PDF files, streamlining data source classification.

![](../../Resources/Images/Bot%20Audit%20Trail/structured%20docs.png)

- **NLU Classification Parameters - improvement**: A new NLP parameter is now available, **NLU.NER.Classification.ChildModelType** parameter, offering three model types: Non Semantic, Semantic, and Semantic Torch.

![](../../Resources/Images/druid%207.18/nlp%20param.png)

The **NLU.NER.Classification.UseSemantic** is now located in Experimental Parameters section if it was set to "true" in DRUID versions prior to 7.18. You can either remove this parameter or replace it by setting **NLU.NER.Classification.ChildModelType** to Semantic or Semantic Torch.

For more information, see [NLP Special Parameters](../../Conversational%20AI/NLP%20Special%20Parameters.md).

<a id="BugFixes"></a>

## Bug Fixes

- **Internal action**: The TakeHelpdeskClientOffTheQueue internal action now has effect in external contact centers (Amazon, Cisco, Freshchat, Oracle).
- **WhatsApp channel**: Added support for "reply to message" functionality.
- **Workspaces**: LiveChatAgents linked in Workspaces are now correctly filtered by botId at runtime.
- **Conversation trace**: The Conversation trace is now displayed after initiating a live chat session.
