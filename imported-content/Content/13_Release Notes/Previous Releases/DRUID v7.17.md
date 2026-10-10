---
title: "DRUID 7.17"
---

<a id="DRUID717"></a>


Deployment Dates

The table below lists the deployment date of DRUID v7.17 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| September 12, 2024 | September 26, 2024 | September 26, 2024 | September 26, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Conversation Trace
- REST Connector improvements

<a id="WhatsNew"></a>

## What's New

- **Conversation Trace**. Conversation Trace offers a comprehensive, tree-structured view of every AI Agent action during conversations, including visible steps and behind-the-scenes processes like GPT prompts and integrations. This feature simplifies troubleshooting with centralized flow logs and detailed timestamps, helping you quickly identify and resolve issues, optimize performance, and enhance response times. For more information, see [Conversation Trace](../../Data%20Analytics%20%26%20Insights/History%20%26%20Logs/Conversation%20History%20V2/Conversation%20Trace.md).

![](../../Resources/Images/Conversation%20History%20v2/conv%20trace.png)

![](../../Resources/Images/Conversation%20History%20v2/flow%20trace.png)

![](../../Resources/Images/Conversation%20History%20v2/integration%20log.png)

![](../../Resources/Images/Conversation%20History%20v2/flow%20update.png)

- **Salesforce MIAW Live Chat**. A new Live Chat provider, Salesforce MIAW is now available in DRUID, which allows you to integrate Salesforce MIAW and AI Agents. Salesforce MIAW enhances pre-chat support by identifying customer needs and accessing records before agents connect in the Service Console. It also enables real-time communication within the console, with asynchronous, persistent conversations across sessions, tabs, and devices.
> **NOTE:** Salesforce Live Chat is in maintenance mode and will retire on February 14, 2026. We recommend switching to Salesforce Messaging for In-App and Web (MIAW) for a modern, flexible customer experience.

For information on how to integrate AI Agents with Salesforce MIAW Live Chat, see [Salesforce MIAW Live Chat](../../Live%20Chat/Salesforce%20MIAW%20Live%20Chat.md).

- **Genesys Live Chat Integration**. You can now integrate AI Agents with Genesys Live Chat for on-premises Genesys installations, enabling seamless hand-offs to live agents. Additionally, you can send conversation transcripts and custom client information to Genesys agents during live chat sessions. For more information, see [Genesys Live Chat](../../Live%20Chat/Genesys%20Live%20Chat.md).

<a id="Improvements"></a>

## Improvements

- **REST Connector - Alternate Response Entity**: The list of HTTP status codes now includes a broader range of custom HTTP codes, streamlining error management. You can map additional error codes to DRUID entities and customize how errors are handled, allowing you to manage errors more effectively and avoid displaying them in conversations.

![](../../Resources/Images/druid%207.17/alternate%20response%20error%20codes.png)

- **REST Connector Audit Log - Test integration tasks**. With this release, you can initiate integration task tests directly from the Connector Audit Log.

![](../../Resources/Images/druid%207.17/test%20button%20ccn%20log.png)

The system automatically fills in the request entity with details from the log, reducing the need to navigate between screens to gather request information.

![](../../Resources/Images/druid%207.17/request%20entity%20prefilled%20on%20test.png)

This streamlines the testing process and saves time.

- **REST Connector - Cookie-based Authentication**. For REST APIs that support cookie-based authentication, you can now authenticate API calls directly from the browser. The browser will automatically attach the cookie to the API request, removing the need for bearer tokens or basic authentication in the request header. This feature simplifies API calls by allowing you to set up the cookie directly in the request settings.

![](../../Resources/Images/rest/map%20cookie.png)

For more information, see [REST Request Settings](../../7_Integrations/REST/Request%20Settings.md).

- **New AI Agents - Default Security Roles**. When creating new AI Agents, the default user security roles (Admin and User) are now automatically selected. This streamlines the setup process by pre-configuring essential user roles for each new AI Agent.

![](../../Resources/Images/druid%207.17/new%20bot%20roles.png)

- **Workspaces - Show/Hide Webchat Widget**. You can now configure workspaces to show or hide the webchat widget using the **Show webchat icon setting**. This feature allows you to tailor the workspace user experience by controlling the visibility of the webchat widget on web views and forms.

![](../../Resources/Images/druid%207.17/show%20web%20chat%20widget.png)

- **Live Chat - Hide Past Conversations on the Agent Page**. A new parameter, **Show past conversations**, is now available in the AI Agent details under the Live Chat section. This setting allows you to control the visibility of past conversations on the Agent page, letting you choose whether to display or hide previous conversations. This helps streamline the agent’s interface.

![](../../Resources/Images/CBA/pst%20conversations.png)

- **Conversational Business Applications - Organizational Charts**. With this release, you can create organizational charts that display data in a hierarchical tree structure. These charts visually represent parent-child relationships from top to bottom, providing a clear view of an organization's hierarchy and improving overall data visualization.

![](../../Resources/Images/CBA/org%20charts.png)

For information on how to create these charts, see [Organizational Charts](../../CBA/Organizational%20Charts.md).

- **Knowledge Base Improvements**. This release introduces two improvements to the Knowledge Base:

- **Document Extraction - Page Number Indication**: A subtle page number indicator now appears in the content area, allowing you to easily identify the original document's page from which each article was extracted.

![](../../Resources/Images/druid%207.17/page%20number%20original%20doc.png)

- **New PDF Extractor - Omni**: The new Omni PDF extractor, available under **KB Advanced Settings** > **File Extractors** > **PDF**, improves article extraction from structured PDF files only when added to unstructured data sources.

![](../../Resources/Images/druid%207.17/omni.png)

<a id="BugFixes"></a>

## Bug Fixes

- **Conversation History fix**: The username now correctly appears in the conversation history after user authentication, instead of remaining anonymous.
