<a id="SaveFileswiththeDruidConnectorHost"></a>

# Save Files with the Druid Connector Host

The Save File integration task enables the DRUID Connector Host to save files uploaded by users in the chat to a specified local disk or network location accessible by the host machine.

> **NOTE:** This integration is available for DRUID Connector Host version 9.0 and higher and is exclusively for hybrid and on-premises installations.

<a id="Prerequisites"></a>

## Prerequisites

Before setting up the Read File integration:

- Upgrade the Connector Host to version 9.0 or higher.
- If you have Connector Host 9.3 or higher, in the installation parameters, select **Use local files**, then enter the path where the connector can access the files.

![](../Resources/Images/KB%20installer/allo%20file%20man.png)

For previous versions, update the appsettings.json file on the machine where the Connector Host is installed:

- Locate and open the appsettings.json file.
- Add or update the following parameters:

```
"ENABLE_FILEMANAGER": "true",
"FILEMANAGER_ALLOWED_PATHS": ["<enter the root path here>","<another root path>"],
```

The `FILEMANAGER_ALLOWED_PATHS` array should include all root paths you want the Connector Host to access for reading or saving files. E.g., “C:\\fd”.

```
"ENABLE_FILEMANAGER": "true",
"FILEMANAGER_ALLOWED_PATHS": [“C:\\fd”],
```

- Ensure you have an active connector action created.
<a id="SaveasinglefilefromtheConversation"></a>

## Save a single file from the Conversation

To configure the Save File integration for saving a single file:

1. Go to the desired connector action configuration page.
2. Click on the **Connector steps** tab.
3. In the top-right corner, click **Create task** > **Files** > **Save File**.

![](../Resources/Images/Read%20File/save%20file%20select.png)

4. Provide a short description for the task.
5. In the **File Path** field, enter the destination path where you want to save the file (e.g., *C:\fd*). Do not use quotation marks.
> **Info:** If you specify a folder and/or subfolder that doesn't exist (e.g., *C:\fd\b\d* where *b* and *d* are new), they will be created automatically, and the file will be saved at the specified location.

6. From the **File Entity** field, select the entity file-field that stores the file you want to save.
7. **Optional**: The file is saved both to your specified path and to the connector's temporary file storage folder (configured during installation in the Document generator section, under the **File Storage Folder** parameter). To automatically remove the file from the connector's temporary storage after it's saved to your specified file path, tap on **Delete Initial File**. The connector file storage is regularly auto-cleared, but this option provides immediate removal.

![](../Resources/Images/Read%20File/save%20single%20file.png)

8. Save and close the integration.
9. Publish the integration.

<a id="Savefilesinbulkfromaconversation"></a>

## Save files in bulk from a conversation

To configure the Save File integration for saving multiple files:

1. Go to the desired connector action configuration page.
2. Click on the **Connector steps** tab.
3. In the top-right corner, click **Create task** > **Files** > **Save File**.

![](../Resources/Images/Read%20File/save%20file%20select.png)

4. Provide a short description for the task.
5. Tap on **Use File Batch Execution**.
6. From the **File Batch Location** field, select the entity list of type file that stores the list of files you want to save.
7. In the **File Path** field, enter the destination path where you want to save the files (e.g., *C:\fd*). Do not use quotation marks.
> **Info:** If you specify a folder and/or subfolder that doesn't exist (e.g., *C:\fd\b\d* where *b* and *d* are new), they will be created automatically, and the file will be saved at the specified location.

8. **Optional**: The file is saved both to your specified path and to the connector's temporary file storage folder (configured during installation in the Document generator section, under the **File Storage Folder** parameter). To automatically remove the file from the connector's temporary storage after it's saved to your specified file path, tap on **Delete Initial File**. The connector file storage is regularly auto-cleared, but this option provides immediate removal.

![](../Resources/Images/Read%20File/save%20bulk.png)

9. Save and close the integration.
10. Publish the integration.
