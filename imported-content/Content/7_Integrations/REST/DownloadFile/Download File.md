---
title: Download File
---

# Download File

The Download File task downloads files from REST API endpoints. This REST connector task enables authors to map a file on the response.

**Prerequisites**

* You created a REST connector app.
* You have a connector action.

To add a Download File task, on the desired connector action, click on the **ConnectorSteps** tab, click the **Create Task** button, click **Files** and select **Download File**.

![](<../../../../.gitbook/assets/Download File.png>)

The Edit Connector Action page appears by default on the **General** tab.

To configure the Download File integration task:

1. Set the task general parameters. For more information, see [General Settings](<Download File.md#_General_Settings>).
2. Configure the request to the API. For more information, see [Request Settings](<Request Settings.md>).
3. Map the response into the conversation context. For more information, see [Response Settings](<Response Settings.md>).
4. Test the integration call.

### General Settings <a href="#general_settings" id="general_settings"></a>

Set the task general parameters:

| Setting         | Description                                                                              |
| --------------- | ---------------------------------------------------------------------------------------- |
| Description     | Provide a brief relevant description of the task to be performed.                        |
| Connection Code | Select the REST connection string. If you do not have one, go to **Apps** and create it. |
