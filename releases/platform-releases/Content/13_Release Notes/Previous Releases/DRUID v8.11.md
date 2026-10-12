---
title: DRUID 8.11
---


Deployment Dates

The table below lists the deployment date of DRUID v8.11 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](<../Druid AI Releases.md>).

{% hint style="info" %}
**NOTE:** **We’re rolling out version 8.11 in PROD-US ahead of schedule!** Originally set for March 13, the deployment will now happen on March 3 (morning, EET). This is a one-time exception to get the latest features out sooner—everything in the release remains the same.
{% endhint %}

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

* Debug Messages in Flow Steps

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| February 27, 2025                                    | March 3, 2025                          | March 13, 2025                               | March 13, 2025                                      |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

## What's New

* **External Webhook Call Handling in DRUID**. This release introduces the `/GenericIntegration` webhook endpoint, allowing you to seamlessly handle external webhook calls in DRUID. The feature captures key request details—such as query parameters, headers, and the request body—and processes them through DRUID’s connector integrations. By leveraging this functionality, you can efficiently interact with external systems while ensuring structured data handling within the DRUID platform.

For more information, see [External Webhook Call Handling in DRUID](https://druidai.gitbook.io/druid-ai-docs/integrations/webhooks/exchanging-data-with-external-systems).

* **Debug Messages in Flow Steps**. You can now use Debug Messages to troubleshoot and optimize flow steps without affecting live conversations. This feature allows you to track the execution of specific steps, understand unexpected flow paths, and gain insights into conversation context using the Conversation Trace tool. Since debug messages are never visible to end users, you can safely use them in production to diagnose and resolve issues efficiently.

{% hint style="info" %}
**NOTE:** For hybrid DRUID deployments, this feature requires you to upgrade your DRUID Connector Host to version 8.11 or later.
{% endhint %}

![](<../../../.gitbook/assets/debug message.png>)

For more information, see [Debug Messages in Flow Steps](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/flows/troubleshooting-steps-with-debug-messages).

* **WebChat – Update the Conversation Context**. You can now update the conversation context with data from the web page hosting the AI Agent without interrupting the current flow execution. Use the `sendEvent("UpdateConversationContext")` function to achieve this. For more details, see [Trigger AI Agent Events from the Web Page Hosting the AI Agent](https://druidai.gitbook.io/druid-ai-docs/channels/web-and-email/webchat/trigger-events-from-the-web-page).
* **Multichat – Voice-to-Voice Live Conversations**. Live voice conversations with real-time translation are now available in Multichat when the Voice channel is enabled. This feature allows agents to communicate more efficiently by switching seamlessly between text and voice during live interactions.

![](<../../../.gitbook/assets/agent voice.png>)

For more information, see [Voice-to-Voice Live Conversations](https://druidai.gitbook.io/druid-ai-docs/live-chat/live-chat-multiple-queues/multichat-voice-live-conversations).

* **Portal Administration - Login Attempts Report**. With this release, Portal administrators gain deeper insights into user login activity with the Login Attempts Report. Track failed login attempts, identify suspicious behavior, and export data for security audits. Advanced filtering and user exclusion options ensure focused monitoring. These capabilities enhance threat detection, compliance auditing, and access control, helping organizations strengthen security across their Druid Portal environment.

![](<../../../.gitbook/assets/login attempts report.png>)

For more information, see [Druid Portal Users Login Attempts Report](https://druidai.gitbook.io/druid-ai-docs/ai-governance-and-security/data-security-and-privacy/authoring-user-management/druid-portal-users-login-attempts-report).

* **Knowledge Base - Content extraction from PPTX and PPSX files**. DRUID now supports the Standard extractor for content processing of PPTX and PPSX files, enabling efficient and accurate text extraction from presentations.

## Improvements

* **KB improvements**: This release includes the following enhancements to the Knowledge Base:
* **Improved KB extraction**: Successfully crawled pages will now be extracted even if some pages fail during the crawling process.
* **Documents extraction from Website data sources (technology preview)**. You can now extract non-password-protected documents from websites in addition to web pages. To enable this, select **Document Content Extraction** when defining the crawling policy.

![](<../../../.gitbook/assets/extract docs.png>)

![](<../../../.gitbook/assets/doc link.png>)

* **Highlighted advanced settings changes in data sources**. The **Modified Configuration** icon now indicates updates to advanced settings at both the data source level and tree elements. In the **Advanced Settings** tab, the icon also appears next to modified parameters, allowing authors to easily identify what has changed.

![](<../../../.gitbook/assets/modified configuration.png>)

* **Service Gateway for Full On-Prem Deployments**. Full on-premise KB installations can now leverage DRUID LLM and embedding services with token-based authentication. The Service Gateway ensures seamless integration, enabling on-prem deployments to securely access DRUID's AI capabilities while maintaining full control over your environment.
* **Views & Forms - Action buttons for faster workflows**. To streamline workspace usage, authors can now add action buttons / icons to the top of a view or form. This enables users to trigger recommended automations with a single click — no need to open the Automations menu and select the action. They can quickly execute key actions from the top-right corner of the page, reducing extra steps and boosting efficiency.

![](<../../../.gitbook/assets/action button.png>)

![](<../../../.gitbook/assets/user action.png>)

![](<../../../.gitbook/assets/icon on form.png>)

For more information, see [Recommend automations on views](https://druidai.gitbook.io/druid-ai-docs/conversational-ai-apps/views/recommend-automations-on-views) or [Recommend automations on forms](https://druidai.gitbook.io/druid-ai-docs/conversational-ai-apps/forms/recommend-automations-on-forms).

* **AI Agent Summary Dashboard – Enhanced bar chart reporting**. The AI Agent Summary dashboard now supports side-by-side bar charts for clearer data visualization. Instead of stacking values on the same bar, you can select **Display side by side** in the bar chart configuration to show values as separate bars, making comparisons easier and more intuitive. This update helps you quickly analyze data and gain deeper insights.

![](<../../../.gitbook/assets/display side by side.png>)

![](<../../../.gitbook/assets/bar charts.png>)

## Bug Fixes

* **Data Service – Locale awareness**: The sameDay and sameWeek functions now consider the user's locale instead of relying solely on UTC.
* **Dynamic Query – filtering fixes**: Resolved an issue where the Equals, Starts With, and Different From filtering options failed to display results.
* **Solution export-import**: The following ConnectorAction properties are also now included during solution export and import: DisableAuditLogging, DisableDatabaseLogging, RequestIsCollection and IsSaveExecutionIdNeeded.
