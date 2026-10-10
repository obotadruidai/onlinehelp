---
title: "Druid 9.5"
---

<a id="Druid95"></a>


Deployment Dates

The table below lists the deployment date of DRUID v9.5 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| September 11, 2025 | September 25, 2025 | September 25, 2025 | September 25, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Knowledge Base – Google Drive data sources**. You can now extract data directly from Google Drive by creating a Shared Drive data source with storage type 'Google Drive,' enabling seamless integration, centralized folder access, and reduced manual file handling.

![](../../Resources/Images/GoogleDrive/new%20data%20source.png)

For more information, see [Network Shared Drive Data Sources](../../Knowledgebase/Network%20shared%20drive%20data%20sources.md).

- **Knowledge Base – AWS Bedrock LLM support**. DRUID now supports AWS Bedrock LLM in both Knowledge Base advanced settings and NLU intents with LLM. The following models are available:

- anthropic.claude-3-haiku-20240307-v1:0
- anthropic.claude-3-5-sonnet-20240620-v1:0
- meta.llama3-8b-instruct-v1:0
- meta.llama3-70b-instruct-v1:0

{% hint style="info" %}
**NOTE:** To use AWS Bedrock LLM, please contact your DRUID representative to activate the LLM resource on your tenant.
{% endhint %}

- **Knowledge Base – Enhanced scraping for dynamic websites**. You can now provide Playwright-compatible scripts for website data sources with dynamically rendered content. This ensures that dynamically rendered content (including elements that require user interaction to be displayed) is captured during the scraping process, improving Knowledge Base completeness and reliability. While this option is also available at the KB level, we recommend configuring the script individually for each website data source to ensure complete content retrieval.

![](../../Resources/Images/druid%209.5/render%20script.png)

For more information, see [Website Data Sources](../../Knowledgebase/Website%20data%20sources.md).

<a id="Improvements"></a>

## Improvements

- **Multichat - Take agents offline**. This release introduces a simplified setup that allows helpdesk managers to take helpdesk agents offline directly from the Live Dashboard.

![](../../Resources/Images/Multichat/live%20dashboard.png)

For more information, see [Enabling Managers to Disconnect Helpdesk Agents](../../Live%20Chat/Disconnecting%20Helpdesk%20Agents.md).

- **Zendesk Sunshine**. Druid now supports receiving customer survey ratings from Zendesk Sunshine Conversations. For more information, see [Zendesk Sunshine](../../Channels/Sunshine/Sunshine_Channel.md).
- **Amazon Live Chat – Support for additional events**. To enhance the user experience, Druid webchat now supports two additional events from Amazon Connect:

- **Typing** – The user can see when the agent is typing a response.
- **Read** – The user can see when the agent has read their message.

- **Portal User Management – Enhanced security**. Portal user management has been updated to improve security and compliance. Instead of permanently deleting users, you can inactivate them. This preserves a full audit trail of user activity and safeguards data linked to user accounts, while still preventing inactive users from accessing the system.

![](../../Resources/Images/druid%209.5/delete%20user.png)

For more information, see [Disable Portal Users](../../Governance%20%26%20Security/User%20Management/DisablePortalUsers.md).

- **Knowledge Base - URL Bulk Exclusion for Website data sources**. To streamline your knowledge base authoring, you can now exclude a list of links from scraping in a website data source.

![](../../Resources/Images/druid%209.5/url%20bulk%20exclusion.png)

This new bulk exclusion option saves you from having to exclude links one by one.

![](../../Resources/Images/druid%209.5/manually%20exclude.png)

For more information, see [Website Data Sources](../../Knowledgebase/Website%20data%20sources.md).

- **Alert Flows – Support for automated workflows**. A new **RunAsJob** option is available in the Subscribers section. It enables alerts to be sent through a dedicated static Portal user and conversation, making it easier to integrate alerts into automated workflows and other jobs.

To use this feature, adjust your automation to reference the generated Portal user and conversation ID.

![](../../Resources/Images/druid%209.5/runjobalert.png)

For more information, see [Alert Flows](../../4_Flows/Alert%20Flows.md).

<a id="BugFixes"></a>

## Bug Fixes

- **Custom Dashboards – Table view data**. Fixed an issue where table views did not display data in dashboards when handling large record volumes (for example, 50,000 records).
- **Conversation History – Number of turns**. Fixed an issue where the Conversation insights tab displayed a higher number of turns than shown in Group by Conversation. The turn count is now consistent, and the correct number is the one displayed in Group by Conversation.
