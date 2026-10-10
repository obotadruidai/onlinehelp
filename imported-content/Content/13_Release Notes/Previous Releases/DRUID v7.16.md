---
title: "DRUID 7.16"
---

<a id="DRUID716"></a>


Deployment Dates

The table below lists the deployment date of DRUID v7.16 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| August 29, 2024 | September 26, 2024 | September 26, 2024 | September 26, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- REST Connector - response body content type
- Connector Audit Log - Local scope entity.

<a id="WhatsNew"></a>

## What's New

- **Reviewing and Validating LLM Responses**. You can now ensure your LLM-powered AI Agents deliver accurate and reliable information by setting up a workflow that allows human agents to review and validate all LLM-generated responses before they reach users.

![](../../Resources/Images/Reviewing%20and%20Validating%20LLM%20Responses/Reviewing%20and%20Validating%20LLM_3.png)

For more information, see [Reviewing and Validating LLM Responses](../../Live%20Chat/LLM%20Response%20Validation.md).

> **NOTE:** This feature requires Multi-chat configuration.

<a id="Improvements"></a>

## Improvements

- **Knowledge Base improvements**. This release brings two enhancements to the Knowledge Base:

- **KB: reset advanced configurations**. Easily reset all advanced configurations at the data source and node/leaf levels to the KB Advanced settings by clicking the **Save to All** button. This simplifies managing settings by applying KB advanced settings across your entire configuration with a single click.

![](../../Resources/Images/druid%207.16/reset%20adv%20settings.png)

![](../../Resources/Images/DRUID%207.15/leaf%20settings.png)

- **KB Data Source Logs - Copy logged messages**: This release introduces the ability to copy messages logged within data source logs. This feature is particularly useful for debugging errors or when contacting DRUID Support, making it easier to share detailed log information.

![](../../Resources/Images/druid%207.16/copy%20error%20message.png)

- **Data Sources - Explorer in Content area**: For data sources such as File Repository, SharePoint, and Network Shared Drive, users can now explore files directly within the **Content** tab, eliminating the need to use the file explorer menu on the left. As you navigate through the nodes, a breadcrumb trail at the top displays your current location within the data source, allowing easy navigation by clicking on the breadcrumb paths. Additionally, you can perform specific actions directly in the Content area for individual nodes and leaves, streamlining your workflow.

![](../../Resources/Images/druid%207.16/DS%20explorer.png)

- **REST Connector - response body content type**: We've added support for specifying the response body content type in REST integrations. This improvement simplifies the authoring process by letting you select the response type and map fields more easily.
  For more information, see [Response Settings](../../7_Integrations/REST/Response%20Settings.md).
- **Connector Audit Log - Local scope entity**: In this release, the connector audit log now provides insights into whether request and response entities were used in a global or local scope. This allows you to see which entity was used at runtime, offering greater transparency and control over your integration processes.

![](../../Resources/Images/druid%207.16/global%20scope.png)

![](../../Resources/Images/druid%207.16/local%20scope.png)

<a id="BugFixes"></a>

## Bug Fixes

- **Adaptive cards** - The issue with Adaptive Card value assignments for entities with the data type "Time" and "Invariant Time" has been resolved. The timezone is now correctly aligned relative to the current day.
- **Solution import**: An additional save is no longer required after importing solutions that contain web views and forms.
