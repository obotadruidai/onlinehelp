---
layout:
  title:
    visible: false
---

<a id="DownloadFile"></a>

# Download File

The Download File task downloads files from REST API endpoints. This REST connector task enables authors to map a file on the response.

**Prerequisites**

- You created a REST connector app.
- You have a connector action.

To add a Download File task, on the desired connector action, click on the **ConnectorSteps** tab, click the **Create Task** button, click **Files** and select **Download File**.

![](../../../Resources/Images/Download%20File/Download%20File.png)

The Edit Connector Action page appears by default on the **General** tab.

To configure the Download File integration task:

1. Set the task general parameters. For more information, see [General Settings](#_General_Settings).
2. Configure the request to the API. For more information, see [Request Settings](Request%20Settings.md).
3. Map the response into the conversation context. For more information, see [Response Settings](Response%20Settings.md).
4. Test the integration call.

<a id="GeneralSettings"></a>

## <a id="_General_Settings"></a>General Settings

Set the task general parameters:

| Setting | Description |
| --- | --- |
| Description | Provide a brief relevant description of the task to be performed. |
| Connection Code | Select the REST connection string. If you do not have one, go to **Apps** and create it. |
