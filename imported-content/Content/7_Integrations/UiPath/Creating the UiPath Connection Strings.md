---
title: "Creating the UiPath Connection Strings"
---

<a id="CreatingtheUiPathConnectionStrings"></a>


The UiPath connector allows integration with the UiPath Orchestrator, to serve the DRUID UiPath Connector Action with the credentials needed to perform the required tasks. Thus, the UiPath Connector App only stores access credentials to the Orchestrator.

Check out Lesson 7 of the Technical Intermediate Course on DRUID Academy for a detailed video tutorial on how to set up UiPath integration.

[Watch video](https://academy.druidai.com/mod/resource/view.php?id=56)

To define a UiPath connection string for the AI Agent within the selected solution, on the main menu click Apps. The Apps page appears listing the connection strings created for the selected solution.

At the top-right corner of the page, click CreateConnector and select **UiPath**.

![](../../Resources/Images/UiPath%20Connector/create%20app.png)

The Edit Connector page appears.

![](../../Resources/Images/UiPath%20Connector/new%20app.png)

In the **Code** field, enter a name for the UiPath connector.

Optionally, from the **Icon** field, select the icon that best describes the app. It helps you easily identify the app in the list of apps. If no icon is selected, DRUID default icon per selected app type will be shown in the apps list.

> **NOTE:** The **Icon** field is available in DRUID 1.71 and higher.

In the **Execution Timeout** field, enter the maximum number of seconds a request is allowed to execute. By default, the timeout for all connector integrations is 60 seconds. This setting will apply to all connector tasks which use this app.

> **NOTE:**  This field is available for DRUID version 1.60 or higher and requires Connector Host upgrade.

If you want to encrypt the data on the connector, from the **Encryption Type** drop-down, select **AESCGM**.

> **NOTE:**  This feature is available in DRUID version 1.61 or higher.

**Encryption Type** enables data encryption on the connector using the AES CGM encryption algorithm and allows authors to encrypt specific data before sending it to external UiPath Orchestrator or RPA unattended robots, by using the Encrypt Data integration task as first task in the desired connector action.

When you select AES CGM encryption algorithm (the only one currently available), two new options are available:

- **Encryption Key** – click the **Generate** button to generate the key, which will be used by the Encrypt Data task to encrypt the data and by the client / 3rd party application to decrypt the data and use it further.
- **Secure encryption with salt** – adds a random 64-bits salt to the data before encrypting it. If data encryption is used for integration with RPA unattended robots, the RPA robot (UiPath Studio) should contain the Decrypt Text activity from UiPath.Cryptography package, configured to use the AESCGM algorithm, DRUID decryption key and the text to be decrypted from a local variable. This option is set to true by default on the UiPAth connector app (because the UiPath.Cryptography package uses this algorithm).

For more information, see [Encrypt Data - UiPath Use Cases](Encrypt%20Data%20UiPath%20Use%20Cases.md).

The connector can integrate with both the Cloud and on premise versions of the Orchestrator. From the SecurityType drop-down, select the type of Orchestrator you want to integrate with.

![](../../Resources/Images/Integrations/Creating%20Druid%20Connectors_1.png)

Based on the selected **SecurityType**, set up the following parameters:

<a id="ForOnPremOrchestrator"></a>

## For OnPremOrchestrator

| Parameter | Description |
| --- | --- |
| Url | The physical address of the on-premise orchestrator |
| Tenant | Orchestrator tenant |
| User Name | (Technical) User name |
| Password | Password |

<a id="ForCloudOrchestratorAPIAccess"></a>

## For CloudOrchestrator (API Access)

> **NOTE:** It is available for backwards compatibility. This functionality will be deprecated in Orchestrator version 21.10. Please use the new OAuth feature to register 3rd party applications and in DRUID select **Cloud Orchestrator (External Applications)**.

| Parameter | Description |
| --- | --- |
| UserKey | To get the values for these parameters, go to the UiPath Cloud Services Portal (https://cloud.uipath.com/<tenancyName>/portal\_/serviceinstances), under Admin > Services, click the API Access option corresponding to the desired service. |
| Account Logical Name |  |
| Tenant Logical Name |  |
| ClientId |  |
| Folder Name or Id | Specify the ID of the Orchestrator folder which contains the resources to be accessed. |

<a id="ForCloudOrchestratorExternalApplications"></a>

## For CloudOrchestrator (External Applications)

<a id="Prerequisite"></a>

### Prerequisite

In order to use this security type, you need to new OAuth feature to register 3rd party applications. To do so, in Orchestrator follow these steps:

1. On the main menu, click **Admin** > **External Applications**.
2. Click the **Add application** button (![](../../Resources/Images/Integrations/external%20app%20button.png)). The Add Application page appears.
3. Enter the **Application Name** and leave selected **Confidential application**.

![](../../Resources/Images/Integrations/add%20exte%20app.png)

4. Click the **Add Scopes** button. The scopes editor appears on the right side.
5. From the **Resources** drop-down, select the **Orchestrator API Access**.
6. Click the **Application Scope(s)** tab and select the following scopes: **OR.Folders.Read**, **OR.Robots.Read**, **OR.Machines.Read**, **OR.Execution.Read**, **OR.Jobs** and **OR.Queues**.
> **IMPORTANT!** Make sure that you're on the **Application Scope(s)** tab and not the **User Scope(s**) tab. If when saving the settings you get an error message that the **Redirect URL** field is mandatory, than you did not click the **Application Scope(s)** tab.

![](../../Resources/Images/Integrations/edit%20resources.png)

7. Click the **Save** button. The application scopes appear on the external app configuration page.
8. Click the **Add** button. The application is successfully added and a pop-up appears providing you with the **App ID** and **App secret**. Store them in a safe location, you will need them in DRUID.

![](../../Resources/Images/Integrations/app%20details.png)

| Parameter | Description |
| --- | --- |
| App Id | The App ID and App Secret of the external application you created in Orchestrator. If you forgot the App Secret, you can generate a new one. ![](../../Resources/Images/Integrations/edit%20app.png) |
| App Secret |  |
| Tenant Logical Name | To get the values for these parameters, go to the UiPath Cloud Services Portal (https://cloud.uipath.com/<tenancyName>/portal\_/serviceinstances), under Admin > Tenants, click the desired tenant and click the dots displayed inline with the Orchestrator service and select the API Access. ![](../../Resources/Images/Integrations/tenant%20details.png)  ![](../../Resources/Images/Integrations/api%20access%20details.png) |
| Account Logical Name |  |
| External Application Scopes | To get the scopes, go to your Orchestrator external application and from the Resources table, click the **Copy** icon and paste them in DRUID. ![](../../Resources/Images/Integrations/copy%20scopes.png) |

Save the app.

<a id="TesttheOrchestratorconnection"></a>

## Test the Orchestrator connection

After saving the configurations, you can test the connectivity to the targeted UiPath Orchestrator service by clicking the Test button at the bottom of the editor.

![](../../Resources/Images/Integrations/Creating%20Druid%20Connectors_3.png)

> **Info:** It might take a while to test the connectivity to the targeted UiPath Orchestrator service. so please wait until the connection is tested.

## Related Topics

- [Defining Connection Strings (Apps)](../Defining%20Connection%20Strings.md)
