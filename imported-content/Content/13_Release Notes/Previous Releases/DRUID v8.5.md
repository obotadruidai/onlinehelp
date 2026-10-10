---
title: DRUID 8.5
---

# DRUID 8.5

Deployment Dates

The table below lists the deployment date of DRUID v8.5 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| December 05, 2024                                    | December 19, 2024                      | December 19, 2024                            | December 19, 2024                                   |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

### What's New

* **Vonage SMS channel**. DRUID now integrates with Vonage SMS, enabling businesses to send and receive text messages globally through intelligent, automated workflows. This new channel enhances customer communication with reliable, two-way messaging directly from the DRUID platform.

![](<../../../.gitbook/assets/channel blank.png>)

For more information, see [Vonage SMS](../../Channels/Vonage_SMS.md).

* **Custom Code - read and write XML Files**. DRUID now supports reading content from XML files and generating new XML files. These enhancements enable seamless handling of XML data, including dynamic mapping, manipulation, file generation, and sending XML files directly within the chat. For more information, see [Custom Code](<../../7_Integrations/Custom Code.md>).
* **File Upload - support for XML files**. DRUID now allows users to upload XML files directly within the chat, enabling efficient reading and processing of XML data.

### Improvements

* **Validating LLM responses - improved timestamps in conversation context**. Timestamps in the conversation context, previously available only for specific agent actions during LLM response reviews, are now also included when the **MaxWaitTimeForAgentResponse** timeout is reached.
* **Improved Input mapping for Hero Card buttons**. Input mapping now properly stores the value of hero card buttons. If a chat user clicks a button from an older hero card during a prompt step, the button's value is stored instead of its label, ensuring more accurate and reliable data capture.
* **Custom Code - New JWT decrypt algorithm**. DRUID now supports the RS256 decryption algorithm in the decryptJWT function, enhancing security and flexibility for handling JWTs.
* **Move chat bubble in web views and forms**. You can now adjust the chat bubble position, ensuring that all fields in webviews and forms remain accessible while keeping the chat interface visible and easily reachable.
* **Flows - Deprecated List View**. Viewing flow steps in list view has been deprecated. You can now fully leverage the Flow Diagram for a more visual and comprehensive conversation management experience.

### Bug Fixes

* **Dashboards - Custom**: Fixed an issue where a linked custom dashboard continued to appear in the workspace menu after deletion.
* **Charts - Bar Chart**: Resolved a bug where the 'Sort by' filter did not update the displayed data correctly.
* **Workspaces - Links**: Addressed an issue where multiple links were incorrectly selected for the same entity.
