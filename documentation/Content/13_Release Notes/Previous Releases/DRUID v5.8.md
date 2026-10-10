<a id="DRUID58"></a>

# DRUID 5.8

Deployment Dates

The table below lists the deployment date of DRUID v5.8 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| February 16, 2023 | March 16, 2023 | March 16, 2023 | March 16, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Required!** This release includes features that require upgrade of your DRUID Connector Host to the latest version:

- Druid Data Service extended filtering options for query integration tasks.

<a id="WhatsNew"></a>

## What's New

- **Knowledge Base**. The Knowledge Base is a powerful Internal DRUID tool that enables authors and business users to maintain a collection of text articles. Integrating the knowledge base with your AI Agent enables it to answer basic user questions by serving the relevant answer when the user intent is not found / matched in flows. The knowledge base provides options to:

- Upload text articles from structured Excel and PDF data sources.
- Test the performance of data sources.
- Test the performance of the knowledge base.
- Promote text articles (QnA pairs) to QnA flows.
- Transform text articles (QnA pairs) into child intents.

> **NOTE:** The Knowledge Base is a tenant feature available in DRUID version 5.8 and higher. If you want to activate it for your tenant, get in touch with [DRUID Support Team](mailto:support@druidai.com?subject=Activate%20KB%20for%20my%20tenant).

For more information on how to create the AI Agent knowledge base and how to use it, see [Knowledge Base](../../Knowledgebase/Knowledgebase.md).

- **Setting specific views for entity links in workspaces**. Workspace authors can personalize each workspace with a specific view for entity links based on different business needs. After you define views for an entity, configure your workspace entity links with the web view, which addresses the specific needs of the business users who will use that workspace.

![](../../Resources/Images/CBA/specific%20view.png)

For information on how to create workspaces and define their menus, see [Create Workspaces](../../CBA/Create%20workspaces.md).

- **Druid Data Service extended filtering options for query integration tasks**. Filtering functions are now available in DRUID Data service query integration tasks, which provide authors with extended options to filter the data of type string, Date, DateTime, InvariantDateTime and InvariantDate, as follows:

- **Case Insensitive** function - Filter data of type string to ensure that the query returns results that are case-insensitive.
- **Date filtering** functions - Filter data of type date (Date, DateTime, InvariantDateTime and InvariantDate) to ensure that the query returns results from a specific day (Today, Yesterday) or within a specific time range (Next X Days, Last X Days, This Week, This Month, Next X Months, Last X Months, This Year, Last Year).

Using the date filtering functions enables you to get the data that is relevant to you. For example, if you are monitoring the revenue of your business, you might want to filter by Last Year and / or This Year and see your business performance.

![](../../Resources/Images/Druid%20Data%20Service%20Connector/filter%20by%20date.png)

For information on how to filter DRUID Data Service queries, see [Query Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Query_Entity.md) or [Query Related Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Query_Related_Entity.md).

<a id="Improvements"></a>

## Improvements

- **Validation rules for capturing email addresses in channels**. DRUID applies validation rules for capturing email addresses. The rules are less restrictive than the standard email format validation rules as emails are from conversational input. Authors can do extra email format validation if needed. For more information, see [Capturing Email Addresses](../../How%20to/Capturing%20email%20addresses%20in%20channels.md).
- **Conversation Transcript**. To avoid providing helpdesk agents with irrelevant information, error messages and events that are useful for debugging purposes (e.g., [File transfer], [step was skipped because the information is known]) are excluded from the agent's conversation transcript and from the conversation transcript returned by internal action GetConversationTranscript.
- **NER - alternative probability calculation becomes default in NER**. With this release, the parameter **NLU.NER.EntityIndex.AlternativeCalculationForProbability** provides an alternative method for computing the probability of an entity that favors partial matches within the index instead of exact matches. By default, it is set to "false".

<a id="BugFixes"></a>

## Bug Fixes

- Adding additional properties in the BF4 snippet Localization JSON configuration file has been fixed.
- User says no longer remains frozen when testing phrases from flows with NER.
