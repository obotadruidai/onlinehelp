---
title: Druid 8.19
---

# Druid 8.19

Deployment Dates

The table below lists the deployment date of DRUID v8.19 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| June 19, 2025                                        | July 3, 2025                           | July 3, 2025                                 | July 3, 2025                                        |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host and DRUID Data Service:

* Enhanced Data Retrieval with \[\[PageInfo]].SelectedFields
* bug fixes

### What's New

* **Agent Builder**. We are excited to introduce the Agent Builder, a powerful tool that streamlines the creation of agent flows. Instead of manually configuring every step, you can now simply describe your agent's goal, required tools, user inputs, and validation logic. Agent Builder automates the process, translating your instructions into a fully configured agent flow with an Agent AI step, a Run Agent step, and all necessary conversational and function call branches. This feature is ideal for quickly generating production-ready agent flows, saving you significant time and effort.

For more information, see Agent Builder.

* **Zendesk Live Chat for DRUID channels**. We are pleased to announce that Zendesk Live Chat is now available for DRUID Channels. This new integration allows you to seamlessly route users from your DRUID channels, such as the web snippet or direct line, to Zendesk live agents. This enhancement provides the flexibility to offer live support to your users without the need to deploy Zendesk widgets, streamlining your customer service operations. For more information, see [Zendesk Contact Center](<../../Live Chat/Zendesk Contact Center.md>).
* **Website Data Sources new features**. This release introduces new functionality to the website data sources:
* **Support for Crawling External Domains**. You can now view and manage external domains linked from a website data source. Previously, links to domains other than the one specified in the data source URL were not crawled. With this release, these external domains are listed in the data source details, and you can choose to include them in your crawled data by adding each as a separate website data source.

![](<../../../.gitbook/assets/ADD EXTERNAL DOMAIN DS.png>)

![](<../../../.gitbook/assets/external domain new ds.png>)

For more information, see [Website data sources](<../../Knowledgebase/Website data sources.md>).

* **Website Data Sources – Recrawl selected pages.** You can now recrawl a list of selected website pages or documents directly—without applying depth, throttle, sitemap, or follow links settings.

This is especially useful when multiple pages (often documents) that were not processed or have failed to crawl due to issues like antimalware blocks or other infrastructure-related errors. Instead of recrawling the entire site or adjusting global settings, you can now target and retry only the affected pages.

![](<../../../.gitbook/assets/crawl selected.png>)

* **Advanced Settings JSON - New feature flag to ignore specific external link patterns**. A new feature flag, LinkToIgnorePatterns, is now available in the advanced settings JSON. This flag lets you exclude specific link patterns — such as links to social media platforms or phone numbers — from the list of identified external links.

By default, common social media domains (e.g., Facebook, LinkedIn) and phone numbers are automatically excluded from the External Links section.

![](<../../../.gitbook/assets/linsk to ignore.png>)

* **Knowledge Base – Reset Advanced Settings**. We've introduced a new **Reset Advanced Settings** button on the Knowledge Base Settings page, **Advanced Settings** tab. This provides a convenient way to revert all advanced settings, whether configured at the node or data source level, back to their default values. Additionally, it will clear any credentials previously set within the generative endpoint configuration.

{% hint style="info" %}
**NOTE:** This action is irreversible and will impact all customized generative endpoints settings and credentials.
{% endhint %}

![](<../../../.gitbook/assets/kb delete adv settings.png>)

This new option offers a more targeted and safer way to manage your Knowledge Base configurations, providing an alternative to the **Delete All** button available on the Knowledge Base Settings > General Settings, which removes all data sources.

* **Enhanced Data Retrieval with \[\[PageInfo]].SelectedFields**. Previously, the \[\[PageInfo]].SelectedFields field captured only the columns visible in table views. Now, this field has been extended to include visible columns from all view types, including:
* Calendar views
* Lookup views
* Subgrid views
* Quick search views

This expansion is designed to further optimize performance and reduce payload size in DRUID Data Service query entity integrations, particularly when utilizing the "Map all fields" option. By capturing only the essential visible columns, data retrieval becomes more efficient.

For SQL integrations, this comprehensive list of visible columns remains accessible via the **\[\[]] .PageInfo.SelectedFields** array.

{% hint style="info" %}
**NOTE:** This feature requires DRUID Connector Host and DRUID Data Service version 8.15 for hybrid and on-premise deployments.
{% endhint %}

### Improvements

* **Flow – UI Enhancements**. The Create New Flow page has been updated with a cleaner, more flexible UI.
* The **Utterances** field is now optional.
* The **Description** field has been expanded to support up to three lines of text.
* A new **Commands** field allows you to define technical utterances as exact-match commands, reducing noise in NLP training and improving model accuracy. For more information about using commands on flow details, see [Commands](<../../4_Flows/Adding Technical Intents.md>).
* If the new flow is a special flow type supported by DRUID, you can select the appropriate type from the list.

![](<../../../.gitbook/assets/create flow (1).png>)

### Bug Fixes

* LDAP Settings: Fixed an issue where the Test button remained in a loading state after displaying a user error message.
* Integrations: Fixed a bug where saving the same integration description with different capitalization (e.g., "HR" vs "hr") incorrectly created separate categories.
