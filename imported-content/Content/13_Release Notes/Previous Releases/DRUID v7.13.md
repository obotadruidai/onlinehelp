---
title: "DRUID 7.13"
---

<a id="DRUID713"></a>


Deployment Dates

The table below lists the deployment date of DRUID v7.13 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| July 18, 2024 | August 01, 2024 | August 01, 2024 | August 01, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Custom Code - Decrypt JWT.

<a id="WhatsNew"></a>

## What's New

- **Knowledge Base: SharePoint On-Premises Data Sources**. This release expands your data extraction capabilities. You can now directly extract text from Word, Excel, and PDF documents stored within your on-premises SharePoint site libraries.

![](../../Resources/Images/druid%207.13/sharepoint%20onprem.png)

<a id="Improvements"></a>

## Improvements

- **Cuedesk Channel - Ticket assignment on specific queue**. With this release, you can assign tickets directly to designated Cuedesk queues. Use the internal action **ConnectToHelpdeskAgent** and simply provide the name of the desired Cuedesk queue as a string value within the **QueueCode** parameter.

For more information about the internal action ConnectToHelpdeskAgent, see [Internal Actions](../../4_Flows/Internal%20Actions.md).

- **Enhanced Conversation History Export**. We have enhanced the Conversation History export to Excel by adding a new column: User Email. This column displays the email addresses of authenticated users, offering valuable insights into communication participants.

![](../../Resources/Images/druid%207.13/CH%20export%20excel.png)

- **Custom Code - Decrypt JWT**. This release introduces the Decrypt JWT method that allows you to:

- **Verify JWT Authenticity**: Ensure the legitimacy of incoming JSON Web Tokens (JWTs) for secure communication. This helps prevent unauthorized access and data breaches.
- **Extract Conversation Context**: Decode JWTs to reveal valuable conversation-level details. Gain insights into user identities, access permissions, and other relevant information, enhancing your understanding of interactions.

For more information on how to use this method, see [Custom Code](../../7_Integrations/Custom%20Code.md).

- **GetMegaBotIntentMatching internal action - Accurate intent retrieval and prediction**. The new internal action, **GetMegaBotIntentMatching**, retrieves the intent specified by [[Intent]].Text considering the Druid Conductor feature. It captures the exact intent communicated to the user in the chat and manually executes a prediction against the NLU/KB models of megabots and child AI Agents. Predictions follow a specific order based on where the internal action is used, ensuring accurate intent matching across all AI Agent levels.  For more information, see [Internal Actions](../../4_Flows/Internal%20Actions.md).
- **New NLP experimental parameters**. We’ve introduced three new experimental NLP parameters to enhance your flow matching capabilities using the Reranker: **NLU.NER.Classification.UseReranker**, **NLU.NER.Classification.Reranker.MinThreshold** and **NLU.NER.Classification.Reranker.JoinUtterances**.  For more information, see [NLP Special Parameters](../../Conversational%20AI/NLP%20Special%20Parameters.md), section Experimental Parameters.
> **NOTE:** Using the Reranker can significantly increase training time, depending on the size of the test set. The Reranker is available in DRUID 7.13 onwards.

- **Special flow - Inactivity End Conversation Flow**: This special flow allows you to manage idle conversations by triggering a specified flow after a set timeout period, enabling actions such as expiring client-facing conversations, requesting user feedback, or initiating other flows.
  For more information, see [Inactivity End Conversation Flow](../../4_Flows/Inactivity%20End%20Conversation%20Flow.md).

<a id="KnownIssueTeamsChannelIntegration"></a>

## Known Issue: Teams Channel Integration

The latest Teams mobile app update causes hero cards to not render properly.

**Workaround**

To view hero cards correctly, rotate your mobile device to a horizontal orientation.

**Status**

We will update you once Microsoft releases a new version of the Teams mobile app that resolves this issue.
