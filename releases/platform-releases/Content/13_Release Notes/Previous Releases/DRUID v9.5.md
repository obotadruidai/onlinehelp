---
title: Druid 9.5
---


Deployment Dates

The table below lists the deployment date of DRUID v9.5 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| September 11, 2025                                   | September 25, 2025                     | September 25, 2025                           | September 25, 2025                                  |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

## What's New

* **Knowledge Base – Google Drive data sources**. You can now extract data directly from Google Drive by creating a Shared Drive data source with storage type 'Google Drive,' enabling seamless integration, centralized folder access, and reduced manual file handling.

![](<../../../.gitbook/assets/new data source.png>)

For more information, see [Network Shared Drive Data Sources](https://druidai.gitbook.io/druid-ai-docs/knowledge-base/knowledgebase/data-sources/network-shared-drive-data-sources).

* **Knowledge Base – AWS Bedrock LLM support**. DRUID now supports AWS Bedrock LLM in both Knowledge Base advanced settings and NLU intents with LLM. The following models are available:
* anthropic.claude-3-haiku-20240307-v1:0
* anthropic.claude-3-5-sonnet-20240620-v1:0
* meta.llama3-8b-instruct-v1:0
* meta.llama3-70b-instruct-v1:0

{% hint style="info" %}
**NOTE:** To use AWS Bedrock LLM, please contact your DRUID representative to activate the LLM resource on your tenant.
{% endhint %}

* **Knowledge Base – Enhanced scraping for dynamic websites**. You can now provide Playwright-compatible scripts for website data sources with dynamically rendered content. This ensures that dynamically rendered content (including elements that require user interaction to be displayed) is captured during the scraping process, improving Knowledge Base completeness and reliability. While this option is also available at the KB level, we recommend configuring the script individually for each website data source to ensure complete content retrieval.

![](<../../../.gitbook/assets/render script (1).png>)

For more information, see [Website Data Sources](https://druidai.gitbook.io/druid-ai-docs/knowledge-base/knowledgebase/data-sources/website-data-sources).

## Improvements

* **Multichat - Take agents offline**. This release introduces a simplified setup that allows helpdesk managers to take helpdesk agents offline directly from the Live Dashboard.

![](<../../../.gitbook/assets/live dashboard.png>)

For more information, see [Enabling Managers to Disconnect Helpdesk Agents](https://druidai.gitbook.io/druid-ai-docs/live-chat/live-chat-multiple-queues/disconnecting-helpdesk-agents).

* **Zendesk Sunshine**. Druid now supports receiving customer survey ratings from Zendesk Sunshine Conversations. For more information, see [Zendesk Sunshine](https://druidai.gitbook.io/druid-ai-docs/channels/engagement-and-support/sunshine_channel).
* **Amazon Live Chat – Support for additional events**. To enhance the user experience, Druid webchat now supports two additional events from Amazon Connect:
* **Typing** – The user can see when the agent is typing a response.
* **Read** – The user can see when the agent has read their message.
* **Portal User Management – Enhanced security**. Portal user management has been updated to improve security and compliance. Instead of permanently deleting users, you can inactivate them. This preserves a full audit trail of user activity and safeguards data linked to user accounts, while still preventing inactive users from accessing the system.

![](<../../../.gitbook/assets/delete user.png>)

For more information, see [Disable Portal Users](https://druidai.gitbook.io/druid-ai-docs/ai-platform/ai-governance-and-security/data-security-and-privacy/authoring-user-management/disableportalusers).

* **Knowledge Base - URL Bulk Exclusion for Website data sources**. To streamline your knowledge base authoring, you can now exclude a list of links from scraping in a website data source.

![](<../../../.gitbook/assets/url bulk exclusion (1).png>)

This new bulk exclusion option saves you from having to exclude links one by one.

![](<../../../.gitbook/assets/manually exclude.png>)

For more information, see [Website Data Sources](https://druidai.gitbook.io/druid-ai-docs/knowledge-base/knowledgebase/data-sources/website-data-sources).

* **Alert Flows – Support for automated workflows**. A new **RunAsJob** option is available in the Subscribers section. It enables alerts to be sent through a dedicated static Portal user and conversation, making it easier to integrate alerts into automated workflows and other jobs.

To use this feature, adjust your automation to reference the generated Portal user and conversation ID.

![](../../../.gitbook/assets/runjobalert.png)

For more information, see [Alert Flows](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/alert-flows).

## Bug Fixes

* **Custom Dashboards – Table view data**. Fixed an issue where table views did not display data in dashboards when handling large record volumes (for example, 50,000 records).
* **Conversation History – Number of turns**. Fixed an issue where the Conversation insights tab displayed a higher number of turns than shown in Group by Conversation. The turn count is now consistent, and the correct number is the one displayed in Group by Conversation.
