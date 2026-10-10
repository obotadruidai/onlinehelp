---
title: "DRUID 7.5"
---

<a id="DRUID75"></a>


Deployment Dates

The table below lists the deployment date of DRUID v7.5 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| March 28, 2024 | April 11, 2024 | April 11, 2024 | April 11, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Required!** This release includes features that require upgrade of your DRUID Connector Host:

- Knowledge Base installation on premises.
- Data Service improvements and bug fixes

> **IMPORTANT!** We've moved the conversation transcript storage to [[ConversationInfo]].TranscriptTxt from [[ChatUser]].Transcript.Txt for technical reasons. When setting up CNN integration mappings, note that direct access to [[ConversationInfo]] isn't available like with [[ChatUser]]. To ensure smooth integration, it's best to perform a SetVariable action first, setting **[[ConversationInfo].TranscriptTxt** to your business request entity. This update requires configuration adjustments for transmitting conversation transcripts to external systems.  For more information, see [Sending the conversation transcript to external systems](../../How%20to/Sending%20the%20conversation%20transcript%20to%20external%20systems.md).

<a id="WhatsNew"></a>

## What's New

- **Knowledge Base installation on premises**. Enable authors and business users to manage a collection of text articles exclusively sourced from within your network, and securely store all KB-related data within your local network environment by installing the Knowledge Base in hybrid mode.
> **IMPORTANT!** To use the DRUID Knowledge Base in hybrid mode (on-premises), you must switch the tenant to hybrid deployment by installing the DRUID Connector Host version 7.5 or higher on-premises.

For detailed information on how to install the KB on premises, see [Knowledge Base Installation](../../Druid%20Deployment/KB%20Installation.md).

- **Start Flow endpoint**. You can now trigger conversations via API using the `/api/Druid/{botId}/StartFlow` endpoint.  For more information, see [Start DRUID conversations via API](../../How%20to/Start%20Druid%20conversations%20by%20API.md).
- **KB Advanced settings - reranker**. Refine search behavior in the Knowledge Base by customizing parameters to use both the keyword and semantic search algorithms. Furthermore, leverage the reranker to conduct additional analysis and notably enhance result quality. For more information, see [Knowledgebase](../../Knowledgebase/Knowledgebase.md).

<a id="Improvements"></a>

## Improvements

- **Data source metadata phase 1: Search by website URL**. We've implemented a new parameter, **UrlMetadataFilter**, in the GetIntentMatching internal action. This feature empowers you to predict against KB articles located under a parent URL containing specific words, filenames, or subfolders, enhancing the precision of LLM prediction. For more information, see [Internal Actions](../../4_Flows/Internal%20Actions.md).
- **Live Chat working hours available in the conversation context**. Now, within the conversation context, the internal action ConnectToHelpdeskAgent provides the status of the agent/queue relative to working hours, setting [[HelpdeskClient]].IsOutsideWorkingHours to "true". Additionally, it populates **[[HelpdeskClient]].WorkingHoursBeginAt** and **[[HelpdeskClient]].WorkingHoursEndAt** with datetime values, offering insight into the active working hours when agents are outside the schedule.
  For more information, see *internal action ConnectToHelpdeskAgent*  - [Internal Actions](../../4_Flows/Internal%20Actions.md).
- **Live Chat - Preventing manual connection to clients during Break or Logout**. In Live Chat, manual connection to clients is prohibited when a break or logout is requested. If a break or logout is requested, the **Connect** button is disabled or removed from the waiting clients list. The button is re-enabled if the request for break or logout is canceled.
> **NOTE:** This feature requires page upgrade.

- **Welcome Message sent in persisted channels**. In WhatsApp, Telegram, Twilio, Facebook Messenger, Google Chat, Line Channel, Slack, and Instagram, the Welcome flow now automatically triggers when a user initiates a conversation with the AI Agent. Regardless of the user's subscription status, they will promptly receive the welcome message, ensuring a seamless and engaging interaction experience.
- **[[QueryParams]] new field**. In web views and forms, when executing automations on a set of records, the IDs of the records are now stored in **[[QueryParams]].recordIds**, separated by commas. You can leverage these values to perform additional manipulations on the records within the automation flow.
- **Hero Card buttons opening URLs**. Now, when a user clicks a hero card button that opens a URL in a new browser window, the action is logged in the Conversation History. Additionally, the flow engine refrains from making predictions based on the button value.
> **NOTE:** This feature is exclusively available for web chat and Teams channels.

For information on how to configure hero card buttons to open URLs, see [Hero Steps Configuration](../../4_Flows/Hero%20Steps%20Configuration.md).

- **Agent Name Display in Live Chat Typing**. During Live Chat sessions, when an agent is typing, the standard dots can now be replaced with the agent's name. To activate this feature, go to AI Agent Details page, click on the section **Theme**, then click the **Customize webchat** button. Go to the Miscellaneous parameters and select **Show typing name**.

![](../../Resources/Images/druid%207.5/show%20typing%20name.png)

Upon conclusion of the Live Chat, the client disconnected event is triggered to stop displaying the agent's name.

- **Connector actions - Disable Connector audit logging**. With this release, we've introduced the "Disable Connector Audit Logging" option at the integration level. This feature allows you to optimize execution time and conserve database resources, especially when handling significant payloads during integration tasks.
- **Query Entity & Query Related Entity Tasks - LIKE Operator in Custom Queries**. In custom queries for Query Entity and Query Related Entity tasks, the LIKE operator is now available. This operator, used within a WHERE clause, enables searching for a specified pattern in a column. For more information, see, [Query Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Query_Entity.md) and [Query Related Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Query_Related_Entity.md).
- **Kanban Views - Collect Unclassified Records**. In Kanban views, you can now collect all records that cannot be classified in a column by adding a column at design time and leaving the **Equals** field empty.

![](../../Resources/Images/druid%207.5/kanban%20design%20time.png)

![](../../Resources/Images/druid%207.5/kanban%20runtime.png)

- **NER Improvements**. Natural Entity Recognition (NER) now disregards the "?" mark and prioritizes delivering the longest record when two records are found with a matching score of 100%.
- **Knowledge Base: Display Predict Errors**.
  When testing the KB or a data source, if errors occur during prediction (such as reaching the provided credit limit for embeddings), error details are now shown below the "User says" field instead of the generic "NoMatchesFound" message.
- **File Repository data sources improvement**. The **Details** tab is now accessible for data sources of type File Repository, providing users with additional information and options for managing these data sources.

![](../../Resources/Images/druid%207.5/file%20repo%20details%20tab.png)

- **Web Forms - Added Mandatory option on fields**. In the Form Designer, authors can now include a mandatory option for fields, streamlining the process of designing web forms and ensuring essential information is captured.

*Web form design time*

![](../../Resources/Images/druid%207.5/required%20fields.png)

*Web form runtime*

![](../../Resources/Images/druid%207.5/save%20empty%20required%20field.png)

![](../../Resources/Images/druid%207.5/error%20required%20field.png)

- **Conversation History - Message Details**. In the Integration Log tab of message details, the connector action is now presented alongside the integration task under the "Connector Task Name" column. This enhancement facilitates the rapid identification of integration tasks that failed within a specific connector action.
- **View Inside a Form**. During web form design, you can now open the view designer in a new browser page for improved efficiency.

![](../../Resources/Images/druid%207.5/open%20view%20designer.png)

![](../../Resources/Images/druid%207.5/view%20designer.png)

- **Dynamic Charts**. You now have the ability to include two axes to group information for two fields, streamlining the user experience. This enhancement enables effortless visualization, such as the number of cases opened each week and their respective status.
  For more information, see [Dynamic Charts](../../CBA/Dynamic%20Charts.md).

<a id="BugFixes"></a>

## Bug Fixes

- **Knowledge Base**: Deleting file in repository marks respective records as deleted in MongoDB without retrain.
- **Channels**: Voice messages and stickers are now correctly marked as unsupported files.
- **Code Editor**: False syntax checker errors have been resolved.
- **Data Service - Delete Entity**: Response entity now matches request entity.
- **Data Service**: Invalid character on custom query has been addressed.
- **Data Service - Get Entity**: The integration task now returns entity list fields as expected.
- **Adaptive Cards**: Saving the adaptive card triggers the flow step saving.
- **Natural Language Processing** : The NLP Engine now reads Cyrillic alphabet on indexed entities without failing.
