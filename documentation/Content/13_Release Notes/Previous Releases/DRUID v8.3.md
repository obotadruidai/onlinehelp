<a id="DRUID83"></a>

# DRUID 8.3

Deployment Dates

The table below lists the deployment date of DRUID v8.3 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| November 07, 2024 | November 21, 2024 | November 21, 2024 | November 21, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Data Service Connector - Custom query enhancement

<a id="WhatsNew"></a>

## What's New

- **LDAP Portal User Authentication**: This release enables you to provision users from Active Directory into the Druid Portal by mapping AD groups to DRUID security roles. You can also test the AD integration via LDAP in the Test area under **Administration** > **Settings** > **External Login Settings** > **LDAP Settings**.

![](../../Resources/Images/User%20Auth/LDAP%20AD%20Test.png)

For more information, see [Provisioning Portal Users with Active Directory via LDAP](../../Governance%20%26%20Security/User%20Management/Provisioning%20Portal%20Users%20with%20LDAP.md).

- **Flow Diagram - Layered Digraph view**. The Layered Digraph view is now available in the Flow Diagram, providing a clear, structured layout that organizes nodes in layers, enhancing readability and flow visualization.

![](../../Resources/Images/druid%208.3/layered%20view.png)

<a id="Improvements"></a>

## Improvements

- Knowledge Base improvements: This release introduces two new improvements to the Knowledge Base:

- **KB - Crawling Sites and Subsites in SharePoint 2019 Data Sources**: For on-premises SharePoint data sources, the system now crawls sites and subsites. A new optional field, **Document Library Path**, is available during data source creation. If left blank, the system will crawl all sites and subsites under the specified **Content Location (URL)**. If a specific document library path is entered, the system will crawl only the sites and subsites within that library.  For more information, see [SharePoint data sources](../../Knowledgebase/SharePoint%20data%20sources.md).
- **Extracting Images from Documents**: The system now extracts images from documents for specific file extractors: the Standard extractor for DOC and DOCX files, and Elpis for PDF files. Extracted images are stored in DRUID storage and linked with a 30-minute authentication token. The image link is included in the extracted article paragraph, providing the chat user temporary access to the image within the chat.

To enable this feature, navigate to **Knowledge Base** > **Advanced Settings**, click **Advanced Settings JSON**, under `featureFlags` in the JSON configuration and set the `LinkAndPersistFileResourcesOnExtract` value to **true**.

```
  "featureFlagTypes": [
    {
      "key": "LinkAndPersistFileResourcesOnExtract",
      "name": "LinkAndPersistFileResourcesOnExtract",
      "value": "true"
    },
    {
      "key": "ContentChunkerLlmInstructions",
      "name": "ContentChunkerLlmInstructions"
    }
      ]
```

- **Embeddings Model**. The embedding models have been renamed for enhanced clarity.

![](../../Resources/Images/druid%208.3/model.png)

For more information about the embedding models, see [Knowledge Base](../../Knowledgebase/Knowledgebase.md), section *Knowledge Base Settings*.
- **Conversation History - Outside Working Hours Event**: With this release, messages sent outside of working hours are now flagged in the conversation history. A new activity event, **Outside working hours**, is available to help you track these messages.

![](../../Resources/Images/Conversation%20History%20v2/track%20outside.png)

- **Review and Validate LLM Responses Improvement**: When reviewing LLM responses, the **Pickup** feature is now disabled if the chat user is blocked for Live Chat. This prevents helpdesk agents from initiating a live chat session with users who are blocked.
- **Live Chat - Live chat conversation idle timeout mins Reset**: The idle timeout warning message timer is now reset by messages sent by the live chat agent, in addition to messages from clients. Previously, the timer reset only for client messages.
- **WhatsApp Vonage and Meta channels - AI Agent support for multiple phone numbers**. With this release, you can associate multiple phone numbers to the same AI Agent. In addition, a new field is available, **[[ChatUser]].ChannelBotIdentifier** that stores the AI Agent number through which a user message arrived. You can use it to route that conversation to dedicated branches in the conversational flows.
> **NOTE:** If the same chat user sends messages to multiple phone numbers associated to the same AI Agent, different conversation IDs will be generated for each phone number. This ensures that each ChannelBotIdentifier corresponds to a unique ConversationId.

- **Data Service Connector - Custom Query enhancement**. The `OFFSET` statement is now available in DRUID custom queries to filter request data more precisely. The OFFSET statement skips a specified number of records before returning results. When used with FETCH NEXT, it limits the number of records returned after the offset, enabling more efficient data retrieval. For more information, see [Filter Data using DRUID Custom Query](../../7_Integrations/Druid%20Data%20Service%20Connector/Filter%20using%20DRUID%20custom%20query.md).
- **Conversational Artificial Intelligence - Embeddings Model**. You can now select an embeddings model in the **NLU Configurations** > **Thresholds and parameters** area with the new parameter **NLU.NER.Classification.ModelEmbeddings**. This enhancement allows greater flexibility in tailoring the model to optimize semantic understanding and search efficiency.

![](../../Resources/Images/druid%208.3/nlp%20param.png)

For more information, [NLP Special Parameters](../../Conversational%20AI/NLP%20Special%20Parameters.md).

- **Druid Portal - Publish Notification**: A new icon now appears in the toolbar to indicate when changes made in the Druid Portal require publishing. Once the publish process is completed successfully, the icon will disappear.

![](../../Resources/Images/druid%208.3/publish%20icon.png)

![](../../Resources/Images/druid%208.3/publish%20popup.png)

<a id="BugFixes"></a>

## Bug Fixes

- **Live Chat Dashboard Auto-Update**. The issue where the Live Chat dashboard did not automatically update without a page refresh has been resolved. The dashboard now updates in real-time without needing a manual refresh.
