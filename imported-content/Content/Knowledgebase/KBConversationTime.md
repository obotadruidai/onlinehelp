---
layout:
  title:
    visible: false
---

<a id="KBManagementatConversationTime"></a>

# KB Management at Conversation Time

You can perform Knowledge Base operations directly within your conversational flows using KB-specific internal actions. These actions enable you to:

- Create, edit, and delete KB data sources directly within your conversational flows.
- Easily edit existing data sources to ensure accuracy and relevance.
- Extract content from documents or URLs to enrich the KB with valuable information.
- Efficiently train the KB to improve its performance and responsiveness.

<a id="Createdatasourcesfromfiles"></a>

## Create data sources from files

Create a data source from structured Excel and PDF files by using the internal action **KBCreateDataSource**.

**Syntax**

```
{
  "Name":"[[Entity]].Field",
  "Type":"FILE_REPOSITORY",
  "Language":"string",
  "SourceFile":"[[Entity]].FileProperty",
  "MinThreshold":"string",
  "TargetThreshold":"string"
}
```

| Parameter | Description |
| --- | --- |
| Name | The new name of the data source (hardcoded, stored in a variable or entity field). This parameter is mandatory. |
| Type | The data source type: FILE\_REPOSITORY. |
| Language | The language of the data you upload. It must be one of the AI Agent languages. |
| SourceFile | The entity field of type File that stores the data source file (Excel or PDF). |
| MinThreshold | The minimum acceptable score for content extraction. |
| TargetThreshold | The desired score threshold for content extraction. This threshold determines the level of confidence required for the extracted content to be considered relevant and accurate. |

> **NOTE:** After adding the data source, you must train the KB. To do so, use the internal action **KBTrain**.

<a id="CreatedatasourcesfromSharePointOnline"></a>

## Create data sources from SharePoint Online

Extract question and answer pairs from Excel, Word, and PDF documents within a SharePoint site library using the internal action **KBCreateDataSource**.

<a id="Prerequisites"></a>

### Prerequisites

- Reach out to your company's Microsoft Azure subscription administrator and ask for the following Microsoft Azure details: Tenant Id, Client Id and Client Secret.

![](../Resources/Images/KB/tenant%20ids.png)

![](../Resources/Images/KB/azure%20client%20secret.png)

- Your company's Microsoft Azure subscription administrator should check and ensure that the API permissions provided in the figure below are granted in Microsoft Azure.

![](../Resources/Images/KB/azure%20API%20permissions.png)

<a id="Syntax"></a>

### Syntax

**Syntax**

```
{
  "Name": "[[Entity]].Field",
  "Type": "SHAREPOINT",
  "Language": "",
  "SharepointTenantId": "",
  "SharepointClientId": "",
  "SharepointClientSecret": "",
  "Uri": "",
  "MinThreshold": "",
  "TargetThreshold": ""
}
```

| Parameter | Description |
| --- | --- |
| Name | The new name of the data source (hardcoded, stored in a variable or entity field). |
| Type | The data source type: **SHAREPOINT**. |
| Language | The language of the data. It must be one of the AI Agent languages. |
| SharepointTenantId | The Tenant Id you received from your MS Azure administrator. |
| SharepointClientId | The Client Id you received from your MS Azure administrator. |
| SharepointClientSecret | The Client Secret you received from your MS Azure administrator. |
| Uri | The SharePoint content location (SharePoint library) from which DRUID will extract data.  To find the SharePoint Content Location (Uri):   1. Right-click on the desired site library/folder/document in Microsoft SharePoint and select **Details**.  ![](../Resources/Images/KB/folder%20details.png) 2. In the right-side panel, click More details.  ![](../Resources/Images/KB/sharepoint%20more%20details.png) 3. Scroll down the right-side panel until you locate the **Path** field, and then click the copy icon next to it. This is the **Content Location (URL)**.  ![](../Resources/Images/KB/copy%20path.png) |
| MinThreshold | The minimum acceptable score for content extraction. |
| TargetThreshold | The desired score threshold for content extraction. This threshold determines the level of confidence required for the extracted content to be considered relevant and accurate. |
| DisableCertificate | Set to "False" to authenticate using a SharePoint client secret instead of a DRUID-generated certificate. |

> **NOTE:** After adding the data source, you must train the KB. To do so, use the internal action **KBTrain**.

<a id="CreatedatasourcesfromSharePoint2019"></a>

## Create data sources from SharePoint 2019

Extract paragraphs from documents stored in SharePoint 2019 libraries using the internal action **KBCreateDataSource**.

<a id="Syntax1"></a>

### Syntax

**Syntax**

```
{
  "Name":"[[Entity]].Field",
  "Type":"SHAREPOINT",
  "Language":"en-US",
  "Uri":"string”,
  "MinThreshold": "string",
  "TargetThreshold": "string",
  “UserName”:”string”,
  “Password”:”string”,
  “SourceType”:”Sharepoint 2019”
}
```

| Parameter | Mandatory for | Description |
| --- | --- | --- |
| Name | File repository, SharePoint online, Shared drive | The new name of the data source (hardcoded, stored in a variable or entity field). This parameter is mandatory. |
| Type | File repository, SharePoint online, Shared drive | The data source type: **SHAREPOINT**. |
| Language | File repository, SharePoint online, Shared drive | The language of the data you upload. It must be one of the AI Agent languages. |
| Uri | SharePoint online, Shared drive | The SharePoint content location (SharePoint library) from which DRUID will extract data. |
| MinThreshold | File repository, SharePoint online, Shared drive | The minimum acceptable score for content extraction. |
| TargetThreshold | File repository,SharePoint online, Shared drive | The desired score threshold for content extraction. This threshold determines the level of confidence required for the extracted content to be considered relevant and accurate. |
| UserName | Shared drive, SharePoint 2019 | The SharePoint username. |
| Password | Shared drive, SharePoint 2019 |  |
| SourceType | SharePoint | **Sharepoint 2019**. |

<a id="CreatedatasourcesfromNetworkSharedDrive"></a>

## Create data sources from Network Shared Drive

Extract paragraphs from documents stored in network shared drive using the internal action **KBCreateDataSource**.

<a id="Syntax2"></a>

### Syntax

**Syntax**

```
{
  "Name":"[[Entity]].Field",
  "Type":"SHARED_DRIVE",
  "Language":"en-US",
  "Uri":"string”,
  "MinThreshold": "string",
  "TargetThreshold": "string",
  “StoreType”:”string”,
  “Host”:”string”,
  “UserName”:”string”,
  “Password”:”string”,
  “Port”:”string”,
}
```

| Parameter | Mandatory for | Description |
| --- | --- | --- |
| Name | Shared drive | The new name of the data source (hardcoded, stored in a variable or entity field). This parameter is mandatory. |
| Type | Shared drive | The data source type: **SHARED\_DRIVEdrive**. |
| Language | Shared drive | The language of the data you upload. It must be one of the AI Agent languages. |
| Uri | Shared drive | Provide the Uri based on the data source type and storage type, as follows:   - **Shared drive (FTP/SFTP)** - the relative path to the folder (on the FTP/SFTP server) you want to crawl. - **Shared drive (Local file)** - path to the local folder you want to crawl. - **Shared drive (Local share)** - the shared drive file path the KB Agent can access. |
| MinThreshold | Shared drive | The minimum acceptable score for content extraction. |
| TargetThreshold | Shared drive | The desired score threshold for content extraction. This threshold determines the level of confidence required for the extracted content to be considered relevant and accurate. |
| StoreType | Shared drive | The storage type: **Local File**, **Local Share**, **FTP** or **SFTP**. |
| Host | Shared drive (FTP/SFTP) | The host name of the SFTP server. |
| UserName | Shared drive (FTP/SFTP) | The FTP/SFTP login ID for Shared drive data sources. |
| Password | Shared drive (FTP/SFTP) | The SFTP login password. |
| Port | Shared drive (FTP/SFTP) | The host name of the FTP/SFTP server. |

<a id="Deletedatasources"></a>

## Delete data sources

Delete a specific data source from the KB using the internal action **KBDeleteDataSource**.

**Syntax**

```
{
  "DataSourceId": "[[Entity]].Field"
}
```

| Parameter | Description |
| --- | --- |
| DataSourceId | The Id of the data source (hardcoded, stored in a variable or entity field). This field is mandatory. |

<a id="Updatedatasources"></a>

## Update data sources

Update a specific data source in the KB using the internal action **KBEditDataSource**.

**Syntax**

```
{
  "DataSourceId":"[[Entity]].Field",
  "SourceFile":"[[Entity]].FileProperty",
  "Name":"string",
  "Uri":"string",
  "SharepointTenantId":"string",
  "SharepointClientId":"string",
  "SharepointClientSecret":"string",
  "MinThreshold":"string",
  "TargetThreshold":"string",
  "StoreType":"string",
  "Host":"string",
  "UserName":"string",
  "Password":"string",
  "DisableCertificatValidation":"string",
  "Port""string"
}
```

Each data source type has unique settings you can adjust to keep your knowledge base (KB) data accurate and up-to-date. Here’s what you can edit for each data source type:

- For a data source of type File (Excel or PDF), you can:

- Edit the name
- Upload a new source file
- Update extraction thresholds

- For a data source of type SharePoint, you can:

- Edit SharePoint credentials (Tenant ID, Client ID, and Client Secret)
- Update extraction thresholds

- For a data source of type Shared Drive (FTP/SFTP), you can:

- Edit the host and port
- Update FTP/SFTP login credentials (ID and password)
- Update extraction thresholds

| Parameter | Data source type | Description |
| --- | --- | --- |
| DataSourceId | all | The Id of the data source (hardcoded, stored in a variable or entity field). This field is mandatory. |
| Name | all | The new name of the data source if want to update the name. |
| SourceFile | File Repository | The new data source file you want to upload, which is hardcoded or stored in a variable or entity field of type 'File'. |
| SharepointTenantId | SharePoint online | The new Tenant Id you received from your MS Azure administrator. |
| SharepointClientId | SharePoint online | The new Client Id you received from your MS Azure administrator. |
| SharepointClientSecret | SharePoint online | The new Client Secret you received from your MS Azure administrator. |
| Uri | SharePoint online, Shared drive | The Uri based on the data source type and storage type, as follows:   - **SharePoint** - The SharePoint content location (SharePoint library) from which DRUID will extract data. - **Shared drive (FTP/SFTP)** - the relative path to the folder (on the FTP/SFTP server) you want to crawl. - **Shared drive (Local file)** - path to the local folder you want to crawl. - **Shared drive (Local share)** - the shared drive file path the KB Agent can access. |
| MinThreshold | File repository, SharePoint online, Shared drive | The minimum acceptable score for content extraction. |
| TargetThreshold | File repository,SharePoint online, Shared drive | The desired score threshold for content extraction. This threshold determines the level of confidence required for the extracted content to be considered relevant and accurate. |
| StoreType | Shared drive | The storage type: **Local File**, **Local Share**, **FTP** or **SFTP**. |
| Host | Shared drive (FTP/SFTP) | The host name of the SFTP server. |
| UserName | Shared drive, SharePoint 2019 | The FTP/SFTP login ID for Shared drive data sources or the username for SharePoint on premises. |
| Password | Shared drive, SharePoint 2019 | The SFTP login password or the password for SharePoint on premises. |
| DisableCertificatValidation | SharePoint online | Set to "true" to authenticate using a SharePoint client secret instead of a DRUID-generated certificate. |
| Port | Shared drive (FTP/SFTP) | The host name of the FTP/SFTP server. |

> **NOTE:** After editing a data source, you must train the KB. To do so, use the internal action **KBTrain**.

<a id="TraintheKB"></a>

## Train the KB

Train the KB after adding / updating a specific data source using the **KBTrain** internal action.

**Syntax**

```
{
  "DataSourceId": "[[Entity]].Field"
}
```

| Parameter | Description |
| --- | --- |
| DataSourceId | The Id of the data source that was added/updated (hardcoded, stored in a variable or entity field). This field is mandatory. |
