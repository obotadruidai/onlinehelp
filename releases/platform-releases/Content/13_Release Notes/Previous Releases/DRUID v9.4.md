---
title: Druid 9.4
---


Deployment Dates

The table below lists the deployment date of DRUID v9.4 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| August 28, 2025                                      | September 25, 2025                     | September 25, 2025                           | September 25, 2025                                  |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

* DRUID Data Service Connector new feature, improvement and bug fix

## What's New

* **DRUID Data Service Connector – Support for `IN`/`NOT IN` Operators in Custom Queries**. With this release, DRUID supports `IN` and `NOT IN` operators in custom queries, making multi-value filtering simpler. Use them in `WHERE` clauses to easily include or exclude multiple values.

For more information, see [Filter Data using DRUID Custom Query](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/data-and-storage/druid_data_-service_connector/filter-using-druid-custom-query).

## Improvements

* **Knowledge Base improvements**. This release introduces several enhancements to make finding and updating content easier:
* **Filter search results**: Narrow results by **Data Source** or **Document Type** for faster, more precise searches.

![](<../../../.gitbook/assets/KB SERACH FILTER.png>)

* **Preview and update articles**: Quickly preview search results and update articles directly if needed, saving time and effort.

![](<../../../.gitbook/assets/PREVIEW BUTTON.png>)

![](<../../../.gitbook/assets/EDIT PRTEVIEW.png>)

* **DRUID Data Service Connector – improved** `LIKE` **operator**. The `LIKE` operator now provides flexibility for users to choose between familiar SQL wildcards and regex-style expressions to suit their querying needs. The **^** and **$** symbols provide an alternative to specifying start or end-of-string patterns without the need for additional **%** wildcards.

For more information, see [Filter Data using DRUID Custom Query](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/data-and-storage/druid_data_-service_connector/filter-using-druid-custom-query).

* **Charts - do not show in workspaces**. You can now choose to hide specific charts from workspaces, helping you keep them clean and focused on what matters.

![](<../../../.gitbook/assets/chart in workspace.png>)

![](<../../../.gitbook/assets/select chart no workspace.png>)

![](<../../../.gitbook/assets/noc hart.png>)

* **Web forms - Resize and Zoom in/out the images**. Web forms – You can now resize images while filling out the form and zoom in or out when viewing them in full screen.

![](<../../../.gitbook/assets/resize image.png>)

![](<../../../.gitbook/assets/zoom image.png>)

## Bug Fixes

* **Zendesk Live Chat – Added a webhook trigger for closed sessions**. When an agent disconnects from a live chat session, the AI Agent is notified and the session is ended automatically, ensuring a smoother user experience.
* **Instagram Channel**: Buttons in Hero cards and Thumbnails are now rendering correctly.
* **Data Service Connector**: Updating an Entity with EntityLists / JArray is now working properly.
* **AI Agent Summary - Engagement Page**: The Number of Interactions drill-down is now working.
* **Knowledge Base – Extract JSON File mimetype**: The page number is now extracted correctly from JSON files with the application/json mimetype.
