---
title: "Druid 7.0"
---

<a id="Druid70"></a>


Deployment Dates

The table below lists the deployment date of DRUID v7.0 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| January 18, 2023 | February 15, 2024 | February 15, 2024 | February 15, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Knowledge Base Engine Upgrade**.
  The Knowledge Base engine has undergone a significant upgrade to the latest DRUID-based version, bringing you enhanced performance across all AI Agents. During this upgrade, your Knowledge Base content seamlessly migrated to the new infrastructure.
> **NOTE:**
> To have an operational Knowledge Base, it's essential to manually retrain all your AI Agents before making any predictions in the Knowledge Base.

- **Office 365 Email channel**. This release introduces the ability to configure your AI Agent for communication with users through Microsoft Office 365 email. By setting up your AI Agent to access an email account, it can receive notifications when new emails arrive. This functionality allows the AI Agent to utilize email as a channel for responding to user inquiries. Responses may include sending email replies in response to user messages.

![](../../Resources/Images/Email%20channel/email%20section.png)

For more information, see [Office 365 Email channel](../../Channels/Email/Email%20Integration.md).

- **New system entity fields**. With the introduction of the new Ofiice 365 channel the following system entity fields are now available: **[[ConversationInfo]].Email** and **[[Email]].DateTimeSent**. For the fields description, see [System Entities](../../5_Entities/System%20Entities.md).
- **Knowledge Base - SharePoint Data Sources (Beta Version)**. In this release, we are excited to introduce the beta version of SharePoint data sources for the Knowledge Base. Users now have the capability to add a SharePoint data source to the KB, enabling the extraction of question and answer pairs from a SharePoint site library. It's important to note that this functionality is limited to Excel, Word, and PDF documents within the SharePoint site library.

![](../../Resources/Images/druid%205.31/client%20silence.png)

For more information, see [Knowledge Base](../../Knowledgebase/Knowledgebase.md).
