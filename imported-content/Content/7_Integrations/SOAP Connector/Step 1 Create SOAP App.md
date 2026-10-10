---
layout:
  title:
    visible: false
---

<a id="Step1CreateSOAPApp"></a>

# Step 1.  Create SOAP App

Creating a SOAP app means defining your SOAP connection string for the AI Agent within the selected solution.

The connection string is a list of key/value pairs that the Connection object will parse; it will use the information to find the Data Source and Initial Catalog, authenticate, and establish a connection.

To create a SOAP app:

1. From the solution menu, click **Apps**. The Apps page appears listing the connection strings created for the selected solution.
2. Place the cursor at the top-right corner of the page on **CreateConnector** and click SOAP.

![](../../Resources/Images/SOAP%20Connector/Step%201%20Create%20SOAP%20App.png)

The Edit Connector page appears.

3. Provide the details listed in the table below.

| Setting | Description |
| --- | --- |
| Code | Unique name to identify the app. You will reference in each method you call from this SOAP App. This field is mandatory. |
| Type | The app type, automatically set to **SOAP**. |
| Icon | Select the icon that best describes the app. It helps you easily identify the app in the list of apps. If no icon is selected, DRUID default icon per selected app type will be shown in the apps list.  **NOTE:** This field is available in DRUID 1.71 and higher. |
| AI Agent | Automatically set to the current AI Agent. |
| Execution Time | The maximum number of seconds a request is allowed to execute. By default, the timeout for all connector integrations is 60 seconds. This setting will apply to all connector tasks which use this app.  **NOTE:**  This field is available for Druid version 1.60 or higher and requires Connector Host upgrade.  **IMPORTANT!** To avoid long execution time for an integration with many tasks, in DRUID 5.4 and higher, the maximum sum of all timeouts configured on an integration is 250 seconds. Whenever this maximum is reached, the execution of the currently running integration task is interrupted and any subsequent integration tasks are no longer executed. |
| Encryption Type | **NOTE:**  This feature is available in Druid version 1.61 or higher and requires Connector Host upgrade.  Enables data encryption on the connector using the AES CGM encryption algorithm and allows authors to encrypt specific data before sending it to external SOAP apps, by using the Encrypt Data integration task as first task in the desired connector action.  When you select AES CGM encryption algorithm (the only one currently available), two new options are available:   - **Encryption Key** – click the **Generate** button to generate the key, which will be used by the Encrypt Data task to encrypt the data and by the client / 3rd party application to decrypt the data and use it further. - **Secure encryption with salt** – adds a random 64-bits salt to the data before encrypting it. Please note that using this feature requires the client to develop code for data decryption.   For more information, see [Encrypt Data](../Encrypt%20Data/EncryptData.md). |
| URL | Base URL for all further method calls. The field is optional, you can use the entire API endpoint URL in the integration task’s request. |
| NTLM Security | By default, no authentication is required. The Druid Portal will not attempt to send authentication details with a request unless you specify otherwise.  When the Druid Connector Host is installed on premise and the client computer and Web server are in the same domain, you can use Windows Challenge/Response (NTLM) authentication. It is the authorization flow for the Windows operating system and for standalone systems.  Tap on **NTLM Security**. Enter your **User name** and **Password** for NTLM access or use default credentials. |
| Basic Security | By default, no authentication is required. The Druid Portal will not attempt to send authentication details with a request unless you specify otherwise.  When making API calls to external SOAP services you can use basic authentication and authorization to ensure that client requests access data securely using their credentials (username and password) |

![](../../Resources/Images/SOAP%20Connector/Step%201%20Create%20SOAP%20App_1.png)

4. Click **Save and Close**.
