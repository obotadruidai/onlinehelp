---
title: Druid 9.26
---


Deployment Dates

The table below lists the deployment date of Druid 9.26 across Druid Clouds. To view the Druid Releases Calendar, see [Druid Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| July 02, 2026                                        | July 30, 2026                          | July 30, 2026                                | July 30, 2026                                       |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

## Improvements

*   **Knowledge Base – Improved Extracted Paragraphs Navigation**. We've redesigned the Extracted paragraphs page to offer a cleaner and more flexible browsing experience.

    * The page now opens in a simplified single-panel tree view by default, making it easier to browse extracted articles.

    ![](<../../../.gitbook/assets/tree view (1).png>)

    * Open paragraph details in a modal dialog with a simple double-click, allowing you to review and edit **Content**, **Metadata**, and **Advanced Settings** without changing the page layout.

    ![](../../../.gitbook/assets/modal.png)

    * Switch to Split view clicking the **View: Split** button whenever you prefer to browse the article tree and edit paragraph details side by side.

    ![](<../../../.gitbook/assets/dialog button.png>)

    * Revert to the clean, single-panel view at any time by clicking the **View: Dialog** button or by clicking the Close (X) icon at the top-right corner of the details panel.

    ![](<../../../.gitbook/assets/split button.png>)

    > **Info:** Your preferred layout is preserved while navigating between Knowledge Base data sources during the current browser session.
* **Improved Allowed IP Configuration for Druid SIP**. Updated the Allowed IPs configuration to enforce a secure-by-default posture. The **Type** field now defaults to **Simple**, requiring explicit, individual IP addresses to prevent unauthorized platform traffic.

![](<../../../.gitbook/assets/sip ip.png>)

{% hint style="info" %}
**Info:** If your telephony provider requires whitelisting IP subnets (such as CIDR blocks or specific IP ranges), please contact Druid Support for advanced security provisioning.
{% endhint %}

* **Enhanced Visibility for File Upload Restrictions in Conversation Trace**. To simplify troubleshooting and provide clear visibility into runtime file validation, Druid now logs explicit system messages to the Conversation Trace whenever a file upload is rejected based on your [File Type Priority Logic](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/conversational-flows/flow-steps/file-upload-steps-configuration#File).

**Multi-file behavior**. The system logs a dedicated message for each unaccepted file. For example, if a user attempts to upload five files at once and three are rejected, three distinct validation messages will be logged in the Conversation Trace to help you pinpoint exactly which files failed and why.

* **Social Media Channels - Support for story reaction handling**. Introduced the Social media reactions flow , enabling AI Agents to capture and process user reactions to Instagram stories. When enabled, the reaction value (such as applause or heart) is stored in **\[\[Intent]].Text** for custom handling; when disabled, story reactions are automatically ignored. For more information, see [Social Media Reactions Flow](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/special-flows/social-media-reactions-flow).

{% hint style="info" %}
**NOTE:** Facebook story reactions are not supported as Facebook does not generate reaction events.
{% endhint %}

## Bug Fixes

* **SQL integrations fix**. Fixed an issue in SQL integrations. Now parameters are properly mapped when using Local scope.
