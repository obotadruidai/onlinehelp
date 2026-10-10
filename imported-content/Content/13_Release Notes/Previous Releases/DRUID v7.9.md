---
layout:
  title:
    visible: false
---

<a id="DRUID79"></a>

# DRUID 7.9

Deployment Dates

The table below lists the deployment date of DRUID v7.9 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| May 23, 2024 | June 06, 2024 | June 06, 2024 | June 06, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Custom Code new features**. This release introduces new features to the Custom Code task:

- **JWT generator**: The EncryptionUtils now includes a JWT generator, enabling you to create a JWT using the provided header, data, and secret key.
- **JWT template**: Utilize the JWT custom code template to streamline the process of generating a JWT with specific claims/data from a client token and exchanging it for an access token at a designated endpoint, covering scenarios where a double JWT exchange is required.
- **CryptoJS library**: The Custom Code task now includes the CryptoJS library, empowering you to use JavaScript implementations of standard and secure cryptographic algorithms.

For information on how to use the JWT template, see [Custom Code](../../7_Integrations/Custom%20Code.md).

<a id="Improvements"></a>

## Improvements

- **Enhanced Knowledge Base (KB) Filtering with Metadata**. Streamline your AI Agent conversations by setting complex filters on KB metadata within the conversation context. Use the [[Intent]].KBQueryObject variable in flow steps (Set Variables) and use the Code extension to craft tailored conditions based on specific metadata fields.

![](../../Resources/Images/KnowledgeBase_0.2/kb%20query%20object.png)

For more information, see [KB Metadata](../../Knowledgebase/KB%20Metadata.md).

- **KB data sources improvements**. This release introduces several enhancements to KB data sources:

- **Network Shared Drive Data Source**: The KB Engine no longer performs automatic crawling when creating a network shared drive data source.
- **Crawling Depth Settings**: You can now set the crawling depth for SharePoint and network shared drive data sources. When you click **Start Crawling**, a pop-up appears, allowing you to set the crawling parameters.

![](../../Resources/Images/KnowledgeBase_0.2/shared%20drive%20crawling%20params.png)

- **Node-by-Node Crawling**: For storages that have a deep structure, you can now crawl each node individually instead of the entire root. Set the depth to '0' to achieve this and for the desired nodes select to **Crawl Path**.

![](../../Resources/Images/KnowledgeBase_0.2/crawl%20path.png)

- **Network Shared Drive - copy node path**: You can now copy the path of a specific node to access the folder on your PC using any file explorer. Ensure you have the necessary permissions to access the folder.

![](../../Resources/Images/KnowledgeBase_0.2/copy%20node%20path.png)

For more information, see [SharePoint data sources](../../Knowledgebase/SharePoint%20data%20sources.md) and [Network shared drive data sources](../../Knowledgebase/Network%20shared%20drive%20data%20sources.md).

- **KBCreateDataSource internal action improvement**. The internal action now returns the following data source information, which you can use to match articles within that specific data source:

- [[KBOperation]].CreatedDataSource.Id
- [[KBOperation]].CreatedDataSource.Name
- [[KBOperation]].CreatedDataSource.CreatedOn

- **StartFlow API Improvements**. In this release, we have made the following improvements to the StartFlow API:

- Removed the BotId from the request body.
- Property names in 'contextData' no longer need to match exactly the referred entity name behind the field of type entity/entity list.

For more information, see [Start DRUID conversations by API](../../How%20to/Start%20Druid%20conversations%20by%20API.md).

- **SQL Connector - Added ByteArray Support**. You can now use the SQL connector to insert files into Oracle databases. For details on how to insert files using the SQL statement and map fields, see [SQL request settings](../../7_Integrations/SQL/Request%20Settings.md).
- **Data Service - Query entity response improvement**. For Query Entity tasks with custom query filtering requests, you can now save the response in the Local scope using an entity different from the request entity. This enhancement allows for greater flexibility and organization in handling query results, enabling more efficient data management and processing.

![](../../Resources/Images/Druid%20Data%20Service%20Connector/differ%20response%20entity.png)

- **Conversational Business Applications - Quick search improvement**. You can now define the Query Entity task on a Quick Search view to normalize accents. During a search, accented characters and their non-accented counterparts will be treated as the same, enhancing search accuracy and user experience.

![](../../Resources/Images/CBA/normalized%20accents.png)

- **Knowledge Base main page improvement**. The Extract icon next to the data sources has been removed from the Knowledge Base page to align with improvements made to various data sources.

<a id="BugFixes"></a>

## Bug Fixes

- **Data Service CNN - Upsert fix**: Performing an upsert with duplicated target records now triggers an error.
- **Data Service CNN - Query entity fix**: When field mapping is missing, an error is now displayed indicating that field mapping is missing.
- **Fixed the Flow Diagram** so that the reference subflow retains the saved name in the right-side editor.
