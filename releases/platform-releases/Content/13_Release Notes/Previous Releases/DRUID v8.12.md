---
title: DRUID 8.12
---


Deployment Dates

The table below lists the deployment date of DRUID v8.12 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| March 13, 2025                                       | April 10, 2025                         | April 10, 2025                               | April 10, 2025                                      |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

## Improvements

* **Website Data Sources – File size limit for document content extraction**. In this release, a 20MB file size limit has been introduced for document content extraction from websites. Files larger than 20MB will not be processed.
* **Cuedesk and RingCentral Channels – Voice message support**. Your AI Agent can now process voice messages on Cuedesk and RingCentral channels. To enable this feature, configure voice message support in the channel settings by providing your MS Azure Speech API key and selecting the preferred language and voice options. This allows seamless audio message processing and AI Agent responses in a natural, human-like voice. For more information, see [Cuedesk Channel](https://druidai.gitbook.io/druid-ai-docs/channels/engagement-and-support/cuedesk-integration) and [RingCentral Channel](https://druidai.gitbook.io/druid-ai-docs/channels/voice-and-telephony/ringcentral_channel).
* **Evaluation Tool – Enhanced train details display for Train Set selection**. The Evaluation page now accurately updates the displayed train details based on the selected train set. When choosing **Current Train Set**, **Previous Train Set**, or **Earlier Train Set** from the **Train Set History** drop-down, the corresponding details (Train Started On, Trained On, and Duration) are shown, ensuring a more reliable evaluation process.

{% hint style="info" %}
**NOTE:** This data is not backwards compatible and will only be displayed as you train the AI Agent.
{% endhint %}

![](<../../../.gitbook/assets/set history.png>)

![](<../../../.gitbook/assets/previous set.png>)

* **Workspaces - Enhanced charts reporting**. Charts now support side-by-side bar charts for clearer data visualization. Instead of stacking values on the same bar, you can select **Display side by side** in the bar chart configuration to show values as separate bars, making comparisons easier and more intuitive. This update helps you quickly analyze data and gain deeper insights.

![](<../../../.gitbook/assets/charts side by side.png>)

* **Conversation History – Enhanced message timestamp visibility**. In the Conversation Transcript, hovering over the clock icon below a message now displays a tooltip with the exact date and time of the message. This improvement makes it easier to track messages across multiple days.

![](<../../../.gitbook/assets/timeand date.png>)

* **KnowledgeBase – Optimized Data Extraction from Excel Files**. To improve performance and prevent extraction failures in large Excel files, empty cells are now cleaned up during the extraction process, reducing memory usage and enhancing efficiency.

## Bug Fixes

* **Knowledge Base – Fixed counter refresh issue in website crawling**. Counters now update correctly after refreshing the page while crawling a website, ensuring accurate progress tracking.
