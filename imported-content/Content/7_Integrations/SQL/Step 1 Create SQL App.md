---
title: "Step 1. Create SQL App"
---

<a id="Step1CreateSQLApp"></a>


Creating an SQL app means defining your SQL connection string for the AI Agent within the selected solution.

The connection string is a list of key/value pairs that the Connection object will parse; it will use the information to find the Data Source and Initial Catalog, authenticate, and establish a connection.

To create an SQL app:

1. From the solution menu, click **Apps**. The Apps page appears listing the connection strings created for the selected solution.
2. Place the cursor at the top-right corner of the page on **CreateConnector**. A drop-down appears
3. Click **SQL**.

![](../../Resources/Images/SQL%20Connector/Step%201%20Create%20SQL%20App.png)

The Edit Connector page appears.

4. Provide the details listed in the table below.

| Field | Description |
| --- | --- |
| Code | Unique name to identify the App. You will reference in each Integration you call from this SQL App. |
| Icon | Select the icon that best describes the app. It helps you easily identify the app in the list of apps. If no icon is selected, DRUID default icon per selected app type will be shown in the apps list.  **NOTE:** This field is available in DRUID 1.71 and higher. |
| Execution Time | The maximum number of seconds a request is allowed to execute. By default, the timeout for all connector integrations is 60 seconds. This setting will apply to all connector tasks which use this app.  **NOTE:**  This field is available for Druid version 1.60 or higher and requires Connector Host upgrade.  **IMPORTANT!** To avoid long execution time for an integration with many tasks, in DRUID 5.4 and higher, the maximum sum of all timeouts configured on an integration is 250 seconds. Whenever this maximum is reached, the execution of the currently running integration task is interrupted and any subsequent integration tasks are no longer executed. |
| Encryption Type | **NOTE:**  This feature is available in Druid version 1.61 or higher and requires Connector Host upgrade.  Enables data encryption on the connector using the AES CGM encryption algorithm and allows authors to encrypt specific data before sending it to external SQL apps, by using the Encrypt Data integration task as first task in the desired connector action.  When you select AES CGM encryption algorithm (the only one currently available), two new options are available:   - **Encryption Key** – click the **Generate** button to generate the key, which will be used by the Encrypt Data task to encrypt the data and by the client / 3rd party application to decrypt the data and use it further. - **Secure encryption with salt** – adds a random 64-bits salt to the data before encrypting it. Please note that using this feature requires the client to develop code for data decryption.   For more information, see [Encrypt Data](../Encrypt%20Data/EncryptData.md). |
| ClientType | Select the type of SQL database you want to integrate. The following database types are available:  ![](../../Resources/Images/SQL%20Connector/Step%201%20Create%20SQL%20App_1.png)  **NOTE:** IBM Db2 is available in technology preview in DRUID 5.11.  **IMPORTANT!** DRUID SQL Connector only supports DB2 Connect server-based license. To establish direct client connection to the Db2® for z/OS® or Db2 for i servers, you can activate the Db2 Connect Unlimited Edition license certificate file on the corresponding Db2 for z/OS subsystem or Db2 for i server, following the procedure described in [IBM documentation](https://www.ibm.com/docs/en/db2/11.5?topic=li-activating-license-certificate-file-db2-connect-unlimited-edition). |
| Server Name | Enter the name/address of the SQL server (exactly how you use it in Microsoft SQL Management Studio).  If you integrate with an Oracle DB, enter the connection string based on the Oracle DB connection details that you have:   - for SID:   `(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=<the name of the server where your database is running>)(PORT=<the port number for your database (the default port number for Oracle databases is 1521>))(CONNECT_DATA=(SID=<the unique name of your DB instance>)))` - for Service Name: `(DESCRIPTION=(ADDRESS=(PROTOCOL=<the protocol of the listener. E.g., TCP>)(HOST=<the host name or IP address of the computer>)(PORT=<the listening port number>))(CONNECT_DATA=(SERVICE_NAME=<alias to a DB instance used when connecting>)))` |
| Database Name | Enter the name of the database used you want to connect to.  **NOTE:** For each database you wish to connect to, you need to define a dedicated DruidConnector App. |
| User and Password | The credentials (user name and password) of your SQL Server account. |
| Windows authentication | Tap on if you want to connect to the SQL server by using the Windows account credentials under which the DRUID Connector Host runs.  **NOTE:** The Windows account should have access rights to the SQL server. The Windows authentication is available in DRUID Connector Host 5.11 and higher. |
| Server | The host name of the server if you selected the **DB2** as **ClientType**. Retrieve the server from the Db2 web console. |
| Database | The name of the Db2 database if you selected the **DB2** as **ClientType**. Retrieve the database details from the Db2 web console. |
| UserId / Password | The Db2 database credentials if you selected the **DB2** as **ClientType**. Your service comes provisioned with a database user ID and password that can be used to connect applications and tools to your database. Retrieve the database credentials from the Db2 web console. |
| Additional Connection Parameters (Optional) | **NOTE:** Additional connection parameters are available for Druid SQL Connectors v1.46 or above. If you have a hybrid or on premise Druid deployment, install Druid Connector Host version 1.46 or above.    **Syntax**:  `<Connection Parameter>``=``<value>``;` `<Connection Parameter>``=``<value>``;` `<Connection Parameter>``=``<value>`  Example:  `Integrated Security=true; MultiSubnetFailover=Yes; Trusted_Connection=Yes`  For information on the available connection parameters, see [Additional Connection Parameters](Additional%20Connection%20Parameters.md). |

![](../../Resources/Images/SQL%20Connector/Step%201%20Create%20SQL%20App_2.png)

5. Click **Save and Close**.
