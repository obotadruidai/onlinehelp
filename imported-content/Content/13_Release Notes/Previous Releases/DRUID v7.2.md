---
title: "Druid 7.2"
---

<a id="Druid72"></a>


Deployment Dates

The table below lists the deployment date of DRUID v7.2 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| February 15, 2024 | March 14, 2024 | March 14, 2024 | March 14, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

> **IMPORTANT!**
> In DRUID 7.0, the Knowledge Base engine has undergone a significant upgrade to the DRUID-based version, bringing you enhanced performance across all AI Agents. The old KB engine is decommissioned in PROD environments on February, 15, 2024. To have an operational Knowledge Base after this date, it's essential to manually retrain all your AI Agents before making any predictions in the Knowledge Base.

<a id="WhatsNew"></a>

## What's New

- **KB management at conversation time**. This release introduces KB-specific internal actions that enable you to perform Knowledge Base operations directly within your conversational flows.

![](../../Resources/Images/RELEASE%207.2/INTERNAL%20ACTIONS.png)

These actions enable you to:

- Create, edit, and delete KB data sources directly within your conversational flows.
- Easily edit existing data sources to ensure accuracy and relevance.
- Extract content from documents or URLs to enrich the KB with valuable information.
- Efficiently train the KB to improve its performance and responsiveness.

For more information, see [KB Management at Conversation Time](../../Knowledgebase/KBConversationTime.md).

- **KB Content extraction from websites during conversations**. This release introduces the **KBExtractUrlContent** internal action, a powerful external tool designed for content extraction from websites during conversations, particularly valuable for conducting document analysis using Large Language Models (LLMs). For more information, see [KB Extraction Tools](../../Knowledgebase/KBExtractionTools.md).
- **KB API endpoints**. The Knowledge Base operation methods are conveniently available through the connector as API services.

<a id="Improvements"></a>

## Improvements

- **Query and Query related entity integration - custom query improvements**. We've enhanced the functionality of custom queries. Now, you can use the 'TOP' argument alongside various scalar functions that operate on string input values and return either string or numeric outputs. These functions include LEFT, LEN, LOWER, LTRIM, REPLACE, RIGHT, RTRIM, UPPER, and SUBSTRING. For more information, see [Query Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Query_Entity.md) or [Query Related Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Query_Related_Entity.md).
- **Identification of Integration Task Errors**. Within Connector Designer, integration tasks containing configuration errors that prevent publishing are now flagged with a red bar.

![](../../Resources/Images/RELEASE%207.2/CNN%20TASK%20ERROR.png)

- **Connector UI improvement for isResponseCollection**. When a Connector task or action has a response of type collection, the response entity will now be displayed with the suffix "List" (e.g., AccountList) in the user interface.

![](../../Resources/Images/RELEASE%207.2/iscollection.png)

- **Fields protected from deletion**. Fields that are included in web views and forms are now protected from deletion. Attempting to delete entity fields that are utilized in web views and forms will result in an error message.

![](../../Resources/Images/RELEASE%207.2/error%20field%20deletion.png)

<a id="BugFixes"></a>

## Bug Fixes

- **Druid Conductor Dashboard - KPI fix**. The ROI KPIs configured on child AI Agents are now available on the Druid Conductor dashboard.
- **DRUID Data Service - Update entity integration task fix**. If 'Batch execution entity list' was selected, the current mappings are no longer lost when clicking **Refresh Fields**.
- **Proper Handling of IsCollection Flag in Connector Mappings**.
  Connector mappings now accurately consider the 'IsCollection' flag when the request context is set to Global and the response context is set to Local.
- **Get Entity integration fix**. The Get Entity integration, when configured with the request context set to Global and the response context set to Local, no longer overrides the global response.
- **Query GUID fields in DRUID Data Service**. Using the WHERE clause, you can now extract GUID fields (e.g., WHERE ds.CollectionId = "@CollectionId").
- **Web views fix**. You can now delete multiple records without refreshing.
- **Saving web views**.The buttons 'Save&New' and 'Save&Close' are now working properly.
- **Import solution issue with automated views**. When importing a solution containing views with automation, the referenced flow IDs remained linked to the source IDs. Now, upon import, the referenced flow IDs are updated to the new IDs in the destination.
