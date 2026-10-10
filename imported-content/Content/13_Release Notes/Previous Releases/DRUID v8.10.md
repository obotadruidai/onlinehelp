---
title: "DRUID 8.10"
---

<a id="DRUID810"></a>


Deployment Dates

The table below lists the deployment date of DRUID v8.10 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

{% hint style="info" %}
**NOTE:** **We’re rolling out version 8.11 in PROD-US ahead of schedule!** Originally set for March 13, the deployment will now happen on **March 3** (morning, EET).
Since we only deploy even-numbered versions in PROD environments, this release also includes all features and fixes from version 8.10. This is a one-time exception to get the latest updates out sooner—everything in the release remains the same.
{% endhint %}

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| February 13, 2025 | March 3, 2025 | March 13, 2025 | March 13, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- DRUID Data Service Connector – improved GROUP BY in custom queries

<a id="WhatsNew"></a>

## What's New

- **DRUID NLU with LLM – Technology Preview**. This release introduces NLU intents classification with LLM. By setting the **NLU.NER.Classification.ModelType** parameter to **LLM**, you can leverage a large language model for intent classification.

Built into the Flow Predict Engine, this model automatically learns from flow intents and training phrases, improving intent recognition without requiring extensive manual classification. It streamlines the authoring experience, reducing the effort needed to define and refine intents within flows.

![](../../Resources/Images/druid%208.10/nlu%20with%20llm.png)

For information on how to configure it, see section [NLU Intents Classification with LLM](../../Conversational%20AI/NLU%20Intents%20Classification.md).

{% hint style="info" %}
**NOTE:** This model currently does not support Named Entity Recognition (NER).
{% endhint %}

<a id="Improvements"></a>

## Improvements

- **WhatsApp channels - receiving voice messages**. Your AI Agent can now process voice messages on WhatsApp without the need to activate the native Voice (MS Cognitive Service) channel. Simply configure the WhatsApp channel to support voice messages directly.

![](../../Resources/Images/druid%208.10/receive%20voice%20whatsapp.png)

For more information, see [WhatsApp Meta Channel](../../Channels/WhatsApp%20Integration/WhatsAppMeta%20Integration.md) or [WhatsApp Vonage Channel](../../Channels/WhatsApp%20Integration/WhatsApp%20Integration.md).

- **DRUID Data Service Connector – improved `GROUP BY` in custom queries**. In this release, the `GROUP BY` functionality in custom queries has been enhanced. You can now group data not only by aliases but also by column names, following standard SQL grouping conventions. This improvement provides greater flexibility and alignment with SQL query practices.  For more information, see [Filter using DRUID custom query](../../7_Integrations/Druid%20Data%20Service%20Connector/Filter%20using%20DRUID%20custom%20query.md).
- **Feedback Options in Web Chat**.
  You can now enable feedback options in web chat to collect user reactions (thumbs up or thumbs down) on AI Agent responses. This feature helps improve AI Agent interactions by capturing and storing feedback for analysis.  For more information, see  [Feedback Reactions in Web Chat](../../Channels/WebChat/Configure%20Feedback%20Options%20in%20Web%20Chat.md).

![](../../Resources/Images/druid%208.10/show%20actions%20feedback.png)

- **Resizable web chat snippet**. With this release, the web chat snippet is resizable both vertically and horizontally, allowing users to adjust the chat window for better readability and usability.

![](../../Resources/Images/druid%208.10/resize%20webchat.png)

- **Knowledge Base – filter search results**. With this release, you can filter search results within the Knowledge Base, allowing for more precise and efficient searches. The filtering options include data source type, document type, and the ability to exclude results from specific data sources or elements, providing greater control over search refinement.

![](../../Resources/Images/druid%208.10/filter%20search%20results.png)

- **AI Agent Summary – Export dashboard as PDF**. You can now export the AI Agent Summary dashboard as a PDF, with the option to export either the current page or all pages for easier reporting and sharing.

![](../../Resources/Images/druid%208.10/export%20dashboard.png)

<a id="BugFixesDRUIDDataServiceDeleteAllrecordsFixedanissuewheretheDeleteAlloperationwaslimitedtoremovingonly1000recordsinsteadofallrecordsinthedataset"></a>

## <a id="BugFixes"></a>Bug Fixes - **DRUID Data Service - Delete All records**. Fixed an issue where the Delete All operation was limited to removing only 1000 records, instead of all records in the data set.
