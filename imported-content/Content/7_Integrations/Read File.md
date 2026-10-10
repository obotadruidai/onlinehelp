---
title: "Read Files with the Druid Connector Host"
---

<a id="ReadFileswiththeDruidConnectorHost"></a>


The Read File integration task enables the DRUID Connector Host to read files from a specific local disk or network location accessible by the host machine and then deliver these files within conversations.

{% hint style="info" %}
**NOTE:** This integration is available for DRUID Connector Host version 9.0 and higher and is exclusively for hybrid and on-premises installations.
{% endhint %}

<a id="Prerequisites"></a>

## Prerequisites

Before setting up the Read File integration:

- Upgrade the Connector Host to version 9.0 or higher.
- If you have Connector Host 9.3 or higher, in the installation parameters, select **Use local files**, then enter the full path where the connector can access the files. Use single backslashes in the path (e.g., C:\folder\subfolder), not double backslashes.

For previous versions, update the appsettings.json file on the machine where the Connector Host is installed:

- Locate and open the appsettings.json file.
- Add or update the following parameters:

```
"ENABLE_FILEMANAGER": "true",
"FILEMANAGER_ALLOWED_PATHS": [ "<enter the root path here>","<another root path>" ],
```

The `FILEMANAGER_ALLOWED_PATHS` array should include all root paths you want the Connector Host to access for reading or saving files. E.g., “C:\fd”.

```
"ENABLE_FILEMANAGER": "true",
"FILEMANAGER_ALLOWED_PATHS": [“C:\fd”],
```

- Ensure you have an active connector action created.
<a id="AddandconfiguretheReadfileintegration"></a>

## Add and configure the Read file integration

To set up the Read File integration, follow these steps:

1. Go to the desired connector action configuration page.
2. Click on the **Connector steps** tab.
3. Add a Custom Code integration to construct and store the full file path in the request entity. This step is crucial for dynamically specifying the file to be read.

**Example Custom Code**

```
let root = "C:\\fd"; // Replace with your desired root path, e.g., "C:\\YourFiles"

let requestEntity = Context.GetRequestEntity();

let fileName = requestEntity.Name; // Assuming the file name is passed in the 'Name' field of the request entity
let fullPath = root + "\\" + fileName;
requestEntity.Name = fullPath;

Context.SetRequestEntity(requestEntity);
```

This code snippet retrieves the file name (e.g., from a user input) and combines it with a predefined root path to form the complete file path. This fullPath is then stored back into the request entity Name field, making it accessible for the Read File task.

4. Save and close the Custom Code integration.
5. In the top-right corner, click **Create task** > **Files** > **Read File**.

![](../Resources/Images/Read%20File/rea%20file%20select.png)

6. Provide a short description for the task.
7. In the **File Path** field, enter [[request entity]].Name using the explorer selector.
   This will dynamically retrieve the full file path constructed in the previous Custom Code step.
{% hint style="info" %}
**Info:** You can manually enter a full file path as a string. Example: *"C:\\fd\\publish20250630170421.pdf"*.
{% endhint %}

8. In the **File Entity** field, select the file-type field where the read file should be stored.

![](../Resources/Images/Read%20File/read%20file%20integration.png)

9. Save and close the integration.
10. Publish the integration.
