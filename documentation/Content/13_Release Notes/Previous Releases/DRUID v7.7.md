<a id="DRUID77"></a>

# DRUID 7.7

Deployment Dates

The table below lists the deployment date of DRUID v7.7 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| April 26, 2024 | May 09, 2024 | May 09, 2024 | May 09, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

> **IMPORTANT!** DRUID AI Platform no longer supports connector hosts older than version 5.5. Beginning with DRUID 7.7, we will only maintain backward compatibility with hybrid connector hosts for a period of 1 year. To ensure seamless operation, we strongly advise you to upgrade connectors every 3 months.

<a id="WhatsNew"></a>

## What's New

- **Data Manipulation without DRUID entity structures**. With the new JArray and JObject field types, you can seamlessly store JSON arrays and objects from third-party systems via DRUID Data Service and REST connectors. You no longer need to align the AI Agent entity model with each JSON property, saving time from creating multiple entities and fields. Enjoy flexibility to manipulate the data within integrations using Custom Code or integrate it into flows (Set Variables or Code Extension) and forms using the Code Editor. For more information, see [Manipulate Data without DRUID Entity Structures](../../How%20to/Manipulate%20Data%20without%20Entity%20Structures.md).
- **KB - Network Shared Drive Data Sources**. Now, you have the ability to add a Network shared drive data source directly into the Knowledge Base (KB). This feature empowers you to extract question and answer pairs from Excel, Word, and PDF documents stored on your premises. The process is simple and can be accomplished through the following storage types:

- **FTP**: Enables the crawling and extraction of data from an FTP server.
- **LocalFile**: Facilitates the crawling and extraction of data from files located on the machine where the KB Agent is installed.
- **LocalShare**: Supports the crawling and extraction of data from files stored on the shared drive within your network, accessible to the KB Agent.

> **NOTE:** While all three storage options are available for DRUID hybrid (incl. KB Agent) and full on-premise deployments, FTP storage stands as the sole option available for KB in the cloud.

For more information, see [Knowledge Base](../../Knowledgebase/Knowledgebase.md).

- **Webhooks**. Users can now easily access DRUID endpoint specifications within the UI and generate bearer tokens for authentication. Click Webhooks in the Solution Contents menu to view endpoint details and manage token generation.

![](../../Resources/Images/druid%207.7/webhook%20endpoints.png)

![](../../Resources/Images/druid%207.7/webhooks.png)

For more information, see [Webhooks](../../Webhooks.md).

- **Start Flow endpoint - authentication**. You can now authenticate the StartFlow endpoint using the authentication endpoints. This provides you with the option to use a bearer token that expires every 30 minutes. For more information, see [Start DRUID conversations by API](../../How%20to/Start%20Druid%20conversations%20by%20API.md).
- **DRUID Data Service Connector- Upsert entity**. This integration task combines the functionality of updating existing records and inserting new ones into DRUID Data Service. It streamlines the process by automatically updating records if they exist or inserting new ones if they don't.  For more information, see [Upsert entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Upsert.md).

<a id="Improvements"></a>

## Improvements

- **Start Flow endpoint - authentication enhancement**. You can now utilize the authentication endpoint to obtain bearer tokens, offering enhanced security with tokens that expire every 30 minutes and flexible authorization for StartFlow API calls. For more information, see [Start DRUID conversations by API](../../How%20to/Start%20Druid%20conversations%20by%20API.md).
- **KB - File Repository improvements**

- **Download Original File**. In this release, for File Repository data sources, users now have the capability to download the original file version that was uploaded into the data source. This feature enables users to access the original version of files, providing them with the ability to compare it with any updated or modified extracted articles.

![](../../Resources/Images/druid%207.7/download%20original%20file.png)

- **Rename folders**. Users can now easily rename folders according to their preferences, providing greater flexibility in organizing project assets.

![](../../Resources/Images/druid%207.7/rename%20folders.png)

- **KB on premise installation - errors in the UI**. If errors occur during the training of all the AI Agents, they will be displayed in the UI, providing you with sufficient details to troubleshoot them.
- **Improved Solution References**. When linking an entity to a solution, the Parent Name column within Solution References now provides a comprehensive entity path. This includes details about any fields added on a view or form, offering complete visibility into the entity's structure and the specific web view or form where the field has been added.

![](../../Resources/Images/druid%207.7/full%20parent%20path.png)

- **Export Conversation History to Excel - time stamp adjustment**. When exporting the Conversation History to Excel (accessible through **History & Logs** > **Conversation History**, **then Export Excel** button), the Date UTC is now automatically converted to the tenant's timezone. This enhancement ensures consistency with the DRUID AI Portal.

![](../../Resources/Images/druid%207.7/export%20excel.png)

![](../../Resources/Images/druid%207.7/date%20utc.png)

- **Expanded Language Support for AI Agents**. Users can now utilize Kurdish language for AI Agents, enhancing accessibility and enabling broader communication capabilities.

<a id="BugFixes"></a>

## Bug Fixes

- Resolved issue with CNN REST where the local scope failed to map the response properly.
- Fixed search functionality in DRUID Data Service query to properly handle diacritics.
