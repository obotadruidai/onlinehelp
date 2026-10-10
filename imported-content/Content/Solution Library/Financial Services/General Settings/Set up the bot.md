---
title: "Setting Up the AI Agent"
---

<a id="SettingUptheAIAgent"></a>


In Druid Portal:

<a id="Step1ConfiguretheAIAgent"></a>

## Step 1: Configure the AI Agent

> **NOTE:** Financial Services default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Financial Services, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.

To configure the AI Agent for Financial Services, you need to set Live Chat timeouts and Special Flows, enable the AI Agent for Live Chat integration and configure the connection strings.

<a id="SetLiveChattimeouts"></a>

### Set Live Chat timeouts

In the AI Agent Details page, click the General section header. The General settings area expands.

Set the parameters for the Route-to-Human functionality:

- **LiveChatQueueWaitingTimeoutMins** - The amount of time in minutes that a client could wait until an agent accepts the incoming live chat request. When the time limit is reached, the live-chat-waiting-message-in-the-queue flow is triggered.
- **LiveChatConversationIdleTimeoutMins** - The idle time limit for which a client can be idle (i.e. does not respond) in an ongoing conversation with an agent. Once the time limit is reached, the dialog times out and the client is automatically returned to AI Agent context.

![](../../../Resources/Images/solution%20templates/Victor/live%20chat%20timeouts.png)

Save the AI Agent. For more information on how it works and how to configure Live Chat, see [Live Chat](../../../Live%20Chat/Live%20Chat.md).

<a id="Setspecialflows"></a>

### Set special flows

Click the Special Flows section header and select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome | welcome |
| IntentNotFound | intent-not-recognized |
| LiveChatClientDisconnectedFlowId | live-chat-feedback-client |
| LiveChatAgentDisconnectedFlowId | live-chat-agent-disconnect |
| LiveChatClientConnectedFlowId | live-chat-client-connected |
| ExceptionFlowId | exception-handling |

![](../../../Resources/Images/solution%20templates/Victor/special%20flows.png)

In production, you can configure these flows based on your needs.

<a id="EnableBotApi"></a>

### Enable BotApi

For live chat integration you need to enable BotApi at your tenant level. To do so, on the main menu, click **Administration** > **Settings**. Click the **BotApi** tab and tick the **Is enabled** check box.

![](../../../Resources/Images/solution%20templates/Victor/set%20botapi.png)

<a id="SettheConnectionStringsAppsDetails"></a>

### Set the Connection Strings (Apps) Details

Financial Services provides you with a wide range of apps for integration with various systems to demo various processes. Set up only the apps used by your organization or the ones dedicated to the particular processes you want to demo / use.

| Druid App | App Type | Integrates Druid with | Integration Purpose | Mandatory app |
| --- | --- | --- | --- | --- |
| [Druid-apps](#druid-apps_Configuration) | SQL | Your Database. | Connects Druid to your DB. | Yes |
| [Druid-apps-db-setup](#druid-apps-db-setup_Configuration) | SQL | Your Database. | Sets up your DB with test data. Used for demo purposes, it helps you see Financial Services in action prior to using it in a production environment. | Yes |
| [UiPathDruidsoft1](#UiPathDruidsoft1_Configuration) | UiPath | UiPath robots | Allows the AI Agent and UiPath robots to work seamlessly together to fulfill customers service and employee requests. | Yes |
| [UiPathOrchApi](#UiPathOrchApi_Configuration) | REST | UiPath Orchestrator API | Druid integration with UiPath Orchestrator API. | Yes |
| [UiPathAutomationHub](#UiPath_Automation_Hub_Configuration) | REST | UiPath Automation Hub |  | Yes |
| [Namirial\_Victor\_REST](#Namirial_Victor_REST_Configuration) | REST | eSign from Namirial | Allows the electronic signature of a digital document generated for the onboarding process. | Yes |
| [Victor OCR CALL](#Namirial_Victor_REST_Configuration) | REST | Druid AI Services | Performs OCR and data extraction from Romanian Identity Cards and Australian driving licenses. | Yes |
| [SendGrid](#SendGrid_Configuration) | SendGrid | Your SMTP Server | Sends emails | No. (only if you need to send emails) |
| [PXL](#PXL_Configuration) | REST | REST Pixel Vision | Enables the AI Agent to capture and extract data from European identity documents with a special machine-readable zone (MRZ) and verify their authenticity. | Yes |
| PXL Download File | REST | REST Pixel Vision | Used by Druid to send the documents uploaded by the clients to PXL Vision. | Yes. No setup is needed. |
| [Doqument](#Doqument_Configuration) | REST | Doqument | Enables the AI Agent automatically convert unstructured data of Romanian balance sheets into accurate, structured and relevant information. | No |
| [Keysfin](#KeysFin_Configuration) | REST | KeysFin | Enables the AI Agent instantaneously check any Romanian company via Credit & KeysFin reports. | No |

> **NOTE:** To run the Financial Services setup flow, you only need to set up the two SQL apps.

For information on how to set the connection strings, click on the configuration section specific to the app you want to set:

<a id="druid-apps_Configuration"></a>

## Druid-apps Configuration

**Prerequisite**

- You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your DB, from Financial Services Apps, click **Druid-apps**. The Edit Connector page appears.

Make the following settings:

| Setting | Description |
| --- | --- |
| ClientType | Select SqlServer. |
| DataSource | Enter the name of the SQL server. |
| InitialCatalog | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account. |

![](../../../Resources/Images/solution%20templates/Victor/druid%20apps%20settings.png)

Click **Save and Close**.

<a id="druid-apps-db-setup_Configuration"></a>

## Druid-apps-db-setup Configuration

**Prerequisite**

- You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your demo data, from Financial Services Apps, click **Druid-apps-db-setup**. The Edit Connector page appears. Make the same settings as for Druid-apps SQL connector.

| Setting | Description |
| --- | --- |
| ClientType | Select **SqlServer**. |
| DataSource | Enter the name of the SQL server. |
| InitialCatalog | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account. |

Click **Save and Close**.

<a id="UiPathDruidsoft1_Configuration"></a>

## UiPathDruidsoft1 Configuration

**Prerequisites**:

- Go to the UiPath Cloud Services Portal (https://cloud.uipath.com/<tenancyName>/portal\_/serviceinstances), under **Admin** > **Services**, click the **API Access** option corresponding to the desired service and write down the following details: **UserKey**, **Account Logical Name**, **Tenant Logical Name** and **ClientId**.
- Set up the [Orchestrator Victor\_Unattended Next Best Deal process](Step%202%20Set%20up%20Orchestrator.md).

To configure the UiPath connector, from Financial Services Apps, click **UiPathDruidsoft1**. The Edit Connector page appears.

Enter the Cloud Orchestrator details (the ones noted in the prerequisites):

![](../../../Resources/Images/solution%20templates/Victor/Uipathdruidsoft1%20app%20settings.png)

> **IMPORTANT!** To have Druid read all the folders from your UiPath Orchestrator, after you provide the UiPath connection strings to the UiPath Cloud Orchestrator, click the **Get UiPath folders** button.

For more information on how to configure the UiPath connector, see [Triggering an Unattended Process](../../../7_Integrations/UiPath/Running%20Unattended%20Process%20using%20Orchestrator%20Queues.md) or [Creating the UiPath Connection Strings](../../../7_Integrations/UiPath/Creating%20the%20UiPath%20Connection%20Strings.md).

After you finish setting up the UiPath connector, click **Save and Close**.

<a id="UiPathOrchApi_Configuration"></a>

## UiPathOrchApi Configuration

**Prerequisites**:

- You need a UiPath Orchestrator admin account.
- You need to set up the [Orchestrator Victor\_Unattended Next Best Deal process](Step%202%20Set%20up%20Orchestrator.md).
- Make sure that you know the following UiPath Orchestrator integration variables: **client\_id**, **refresh\_token**, **UiPath\_Account** and **UiPath\_Tenant**. To find out these variables, access cloud.uipath.com, log in and click **Manage**.

![](../../../Resources/Images/solution%20templates/Victor/manage%20tenant%20orchestrator.png)

Click on the tenant you are working on.

![](../../../Resources/Images/solution%20templates/Victor/select%20orchestrator%20tenant.png)

Click on **API Access** and write down the **client\_id** (mapped as Client Id), **UiPath\_Account** (mapped as Account Logical Name), **UiPath\_Tenant** and **TenantName** (both mapped as Tenant Name), **refresh\_token** (mapped as User Key).

To get the **OrganizationUnitId**, access the process folder in your Orchestrator and write down the FID provided in the **URL** field.

To configure the REST connector, from Financial Services Apps, click **UiPathOrchApi**. The Edit Connector page appears.

Set up the following Custom security details:

![](../../../Resources/Images/solution%20templates/Victor/orchestrator%20custom%20security.png)

In the Variables section, add the integration context variables as follows:

| Variable | Description |
| --- | --- |
| UserEmail | The email address associated to a UiPath Orchestrator admin account. The user should have access to both Orchestrator and to the folders in which the UiPath unattended process is configured. |
| client\_id | The Client Id from Cloud UiPath Orchestrator. |
| UiPath\_Account | The Account Logical Name from Cloud UiPath Orchestrator. |
| UiPath\_Tenant | The Tenant Name from Cloud UiPath Orchestrator. |
| refresh\_token | The User Key from Cloud UiPath Orchestrator. |
| OrganizationUnitId | The FID in your Orchestrator process folder. |

![](../../../Resources/Images/solution%20templates/Victor/orchapi%20variables.png)

Click **Save and Close**.

<a id="UiPath_Automation_Hub_Configuration"></a>

## UiPath Automation Hub Configuration

**Prerequisites**:

- You need to have an organization account on the [UiPath Automation Hub](https://automation-hub.uipath.com/).
- Generate **AutomationHubAccessToken** and write down its value. To do so, log into the [UiPath Automation Hub](https://automation-hub.uipath.com/), go to **Admin Console** > **Platform Setup** > **Open Api** and click the **Generate Token** button.

![](../../../Resources/Images/solution%20templates/Victor/automation%20hub%20generate%20token.png)

The system generates a new access token to your environment, **AutomationHubAccessToken**. Write down the access token you will need it to set up the Druid Connector.

![](../../../Resources/Images/solution%20templates/Victor/automation%20hub%20token.png)

To configure the REST connector, from Financial Services Apps, click **UiPathAutomationHub**. The Edit Connector page appears.

In the **Base URL** field, enter *https://automation-hub.uipath.com/api/v1/openapi*.

From the **SecurityType** drop-down, select **Custom** and from the **AuthorizeRequestConnectorApp** drop-down, select **AutomationHub-Authorize**.

![](../../../Resources/Images/solution%20templates/Victor/automation%20hub%20app%20settings.png)

In the Variables section, add the integration context variable **AutomationHubAccessToken** and enter the value of the access token generated in UiPath Automation Hub (the one from the prerequisites).

![](../../../Resources/Images/solution%20templates/Victor/automation%20hub%20app%20variables.png)

Click **Save and Close**.

<a id="Namirial_Victor_REST_Configuration"></a>

## Namirial\_Victor\_REST Configuration

**Prerequisites**:

- You need to have an [eSign](https://www.esignanywhere.net/) subscription with Namirial.
- You need to know the Namirial organizationKey (your organization API key). To find out the Namirial organization, in Namirial Digital Transaction Management Platform, go to **Settings** > **Api Tokens and Apps**.

To configure the REST connector used for electronic signature of documents generated for the onboarding process, from Financial Services Apps, click **Namirial\_Victor\_REST**. The Edit Connector page appears.

In the **Base URL** field, enter the URL of the Namirial Digital Transaction Management Platform, *https://saas.esignanywhere.net* and from the **SecurityType** drop-down, select **None**.

In the Variables section, add the integration context variables associated to your organization’s Namirial account, **userLoginName** (your Namirial login e-mail address) and **organizationKey**.

![](../../../Resources/Images/solution%20templates/Victor/namirial%20app%20settings.png)

Click **Save and Close**.

## Victor OCR Call Configuration

In Financial Services, you can use two types of OCR solutions:

- Druid AI Services for OCR of Romanian identity cards and Australian driving licenses.
- UiPath AI Center for OCR of any ID document that complies with the MRZ standard.

This section describes the connection strings required if you are using Druid AI Services. If you are using UiPath AI Center, follow the instructions described in section [Setting Up AI Center](Setting_up_AI_Center.md).

**Prerequisites**:

- In order to use the Druid AI Services, you need the URL and access token of the instance on which the Druid OCR is running. To get the URL and access token, contact [Druid Tech Support](<mailto:support@druidai.com?subject=I need access to Druid AI Services>).

> **NOTE:** Druid Tech Support generates the access token per tenant and environment.

To configure the REST connector to Druid AI Services, which performs OCR of Romanian identity cards, from Financial Services Apps, click **Victor OCR CALL**. The Edit Connector page appears.

In the **Base URL** field, enter the URL provided by Druid Tech Support.

![](../../../Resources/Images/solution%20templates/Victor/victor%20ocr%20call%20app%20settings.png)

In the Variables section, add the token provided by Druid Tech Support.

![](../../../Resources/Images/solution%20templates/Cristina/ocr%20variables.png)

Click **Save and Close**.

<a id="SendGrid_Configuration"></a>

## SendGrid Configuration

**Prerequisites:**

- You need to have an email service and know the API Key. To find out the API Key, you might need to contact your system administrator.

To configure the SendGrid connector, which sends emails, from Financial Services Apps, click **SendGrid**. The Edit Connector page appears.

In the **ApiKey** field, enter the API Key received from your email service provider.

![](../../../Resources/Images/solution%20templates/Victor/send%20grid.png)

Click **Save and Close**.

<a id="PXL_Configuration"></a>

## PXL Configuration

**Prerequisite**:

- You need to have a [PXL Vision](https://pxl-vision.com/) subscription.

To configure the PXL REST connector used for OCR of European identity documents, from Financial Services Apps, click **PXL**. The Edit Connector page appears.

In the **Base URL** field, enter *https://srv.pxl-vision.com/api/v1/*.

In the Variables section, add the integration context variables associated with your PXL Vision service account, email and password. They are used in the calls to the PXL Vision authorization APIs.

![](../../../Resources/Images/solution%20templates/Victor/pxl%20app%20settings.png)

Click **Save and Close**.

<a id="Doqument_Configuration"></a>

## Doqument Configuration

**Prerequisite**:

- You need to register for a [Doqument](https://www.doqument.ro/) account.

To configure this REST connector, from Financial Services Apps, click **doqument**. The Edit Connector page appears.

In the **Base URL** field, enter https://portal.doqument.ro.

In the Variables section, add the integration context variables associated with your doqument account, **client\_id** and **client\_secret**. They are used in the calls to the Doqument authorization APIs.

![](../../../Resources/Images/solution%20templates/Victor/doqument%20app%20settings.png)

Click **Save and Close**.

<a id="KeysFin_Configuration"></a>

## KeysFin Configuration

To configure the REST connector for Druid integration with KeysFin, from Financial Services Apps, click **Keysfin**. The Edit Connector page appears.

In the **Base URL** field, enter *https://testarews.keysfin.com/service.asmx*.

![](../../../Resources/Images/solution%20templates/Victor/keysfin%20app%20settings.png)

Click **Save and Close**.

> **IMPORTANT!** In order for the AI Agent integration with the apps to be up and running, you need to publish the connector actions. To do so, from the main menu, click **Integrations** and click the **Publish** button.
>
> ![](../../../Resources/Images/solution%20templates/Victor/publish%20apps.png)

<a id="Step2RunSetupFlow"></a>

## Step 2: Run Setup Flow

Open chat land AI Agent page and send the message “**setup-victor**”. This command sets up all the DB tables needed in Financial Services.

![](../../../Resources/Images/solution%20templates/Victor/druid%20bot%20run%20setup.png)

Click **Done**. If the SQL connection strings are properly set, Financial Services setup completes successfully.

![](../../../Resources/Images/solution%20templates/Victor/drui%20bot%20setup%20successfully.png)

You can now [train the entities and the AI Agent](Train_entities_and_bot.md), set up the webchat in HTML page and add service account and add Druid users.
