---
title: Druid 9.7
---


Deployment Dates

The table below lists the deployment date of DRUID v9.7 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| October 09, 2025                                     | October 23, 2025                       | October 23, 2025                             | October 23, 2025                                    |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

* Netopia Payments Integration

## What's New

* **Netopia Payments Integration**. You can now integrate Netopia Payments directly into your DRUID conversational flows. This new integration enables your AI Agent to guide users through a complete, secure payment process — from capturing billing and shipping details to providing a Netopia payment link that users can use to finalize their transaction.

![](<../../../.gitbook/assets/payment url rn.png>)

The integration helps streamline sales and billing workflows by combining conversational engagement with fast, secure online payments — all within the chat interface.

For more information, see [Netopia Payments](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/netopia-payments).

* **Knowledge Base - ServiceNow data sources**. A new data source type, **ServiceNow**, is now available in the Knowledge Base. You can use it to connect to your ServiceNow instance and extract articles from the ServiceNow Knowledge Base.

![](<../../../.gitbook/assets/servicenow type.png>)

For more information, see [ServiceNow Data Sources](https://druidai.gitbook.io/druid-ai-docs/knowledge-base/data-sources/servicenow-data-sources).

* **Channels – Outlook Channel**. The new Outlook email channel connects directly with Microsoft using the Graph API, offering an alternative to the Office 365 email channel, which integrates through the Bot Framework.

![](<../../../.gitbook/assets/outlook (1).png>)

For more information, see [Outlook channel](https://druidai.gitbook.io/druid-ai-docs/channels/web-and-email/outlook).

* **New Internal Action: TranslateText**. The new **TranslateText** internal action performs machine translation using the eTranslation provider set up on the AI Agent. It can translate literal text or text from a specified DRUID entity field into another language, which can be different from the chat conversation language. The translated text is saved in a specified destination entity field, and both the input and output (including source and target languages) are logged in the Conversation History.

![](<../../../.gitbook/assets/translatetext action.png>)

For more information, see [Internal Actions](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/conversational-flows/internal-actions).

## Improvements

* **Set Variables – Enhanced error handling**. You can now configure the behavior of the conversational engine when encountering an error on variable assignment. When an error occurs, you can choose to raise it in the Conversation History and stop the conversation — similar to how connector errors are logged.

To configure this setting, go to AI Agent details > **Dialogue management**, and in the **Set variable error severity** field, select one of the following options:

* **Silent** – Skips the error and continues the conversation. (This was the default behavior in previous versions.)
* **Raise exception** – Interrupts the conversation and records the error in the conversation history.

![](<../../../.gitbook/assets/set var error.png>)

* **Webchat – Burmese Language Support**. The Webchat interface now supports the Burmese language. All interface elements, including messages in the typing area and labels displayed below user and AI Agent messages, are now shown in Burmese when this language is selected.
* **Workspaces – Add URLs**. You can now add URLs to workspaces. When business users click a URL in the workspace menu, the corresponding web page opens. This makes it easier for users to quickly access relevant resources, tools, or documentation directly from the workspace, improving workflow efficiency.

![](<../../../.gitbook/assets/workspace url.png>)

![](<../../../.gitbook/assets/save url.png>)

![](<../../../.gitbook/assets/url in menu.png>)

* **Web Views and Forms – Dropdown Automation list improvement**. A scroll bar has been added to the **Automations** dropdown, allowing you to view more than 12 items. This enhancement applies to both web views and forms, improving navigation and selection in long lists.

![](<../../../.gitbook/assets/view automations.png>)

![](<../../../.gitbook/assets/form automations (1).png>)

* **Webchat – Fallback for Voice Provider**. You can now configure a fallback Speech-to-Text (STT) provider in Webchat. This fallback is used when the STT provider selected in the portal does not support the chat user’s language.

![](../../../.gitbook/assets/deepgram.png)

This feature requires setting up the Voice Channel with Microsoft Cognitive Services and Deepgram. For more information on configuring these channels, see Voice Channel.

* **Knowledge Base improvements**. This release introduces various improvements:
* **Improved KB Search**. The Knowledge Base search has been enhanced to support **Title & Content** filters. You can now search specifically within article titles and content, rather than searching across all article elements or URLs.

![](<../../../.gitbook/assets/filters (1).png>)

* **KB Scheduler**: The option to select which data to extract (Extract All / Extract Unprocessed) has been removed. Starting with this release, the scheduler will extract by default only unprocessed nodes—new nodes and nodes from sources where content has been updated.

![](<../../../.gitbook/assets/kb scheduler previous.png>)

![](<../../../.gitbook/assets/extract (1).png>)

* **KB Advanced Settings - Generative Endpoints**. The default **Max Tokens per Session Limit** has been increased from 500,000 to **2,000,000**. This means large extractions—such as datasets with hundreds of pages—can now complete without interruptions. After resetting the Advanced Settings, the new limit will take effect. You can also manually increase the limit from 500,000 to 2,000,000.

![](<../../../.gitbook/assets/max limit.png>)

## Bug Fixes

* **Flow Engine – Adaptive Cards in Teams**. Fixed an issue where consecutive adaptive cards in MS Teams could cause the second card to be skipped if the user clicked the save button twice on the first card.
* **Telegram – New Lines**. Fixed a bug where new lines in messages were ignored when rendered in Telegram. Messages now preserve formatting correctly.
* **Entity Field – Currency Input Mapping**. Resolved an issue where currency inputs (e.g., 100, 100.00, one hundred) failed to map correctly in Druid Data Service. The payload now correctly maps currency values without casting errors.
* **VoiceChannel in LiveChat (with Microsoft Cognitive Services STT)** fixes:
* **TTS Issue**. Fixed a problem where Text-To-Speech didn’t play on the agent side (client-side was unaffected).
* **Microphone Activation**. Improved microphone behavior; previously, it only activated briefly after a client message. The microphone now responds more reliably, though it still requires the chat to be in focus.
* **Duplicate Flows for Polish**. Fixed an issue where importing a solution with Polish as the default language could trigger the same flow 2–3 times.
* **Evaluation Tool – Diacritics Handling**. Fixed inconsistent diacritic handling between Train and Test sets in NLU Evaluation tools. All utterances are now correctly evaluated, providing accurate performance metrics.
