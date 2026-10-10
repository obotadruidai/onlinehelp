---
layout:
  title:
    visible: false
---

<a id="SettingUptheAIAgent"></a>

# Setting Up the AI Agent

In Druid Portal:

1. [Configure the AI Agent](#Step_1%3A_Configure_bot).
2. [Set Up Druid Users](#Step_2%3A_Set_Up_Druid_Users).
3. [Run Setup Flow](#Step_3%3A_Run_Setup_Flow).

<a id="Step1ConfiguretheAIAgent"></a>

## <a id="Step_1:_Configure_bot"></a>Step 1: Configure the AI Agent

> **NOTE:** Retail default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Retail, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.

To configure the AI Agent for Retail, you need to set Live Chat timeouts and Special Flows, enable the AI Agent for Live Chat integration and configure the connection strings.

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
| Welcome | first-welcome-flow |
| IntentNotFound | Intent-not-recognized |
| Authentication | web-authentication-customer |
| LiveChatClientDisconnectedFlowId | live-chat-feedback-client |
| LiveChatAgentDisconnectedFlowId | live-chat-agent-disconnect |
| LiveChatClientWaitingInQueueFlowId | live-chat-connect-to-agent |
| LiveChatClientConnectedFlowId | live-chat-client-connected |

[../../../Resources/Images/Retail/special%20flows.png](../../../Resources/Images/Retail/special%20flows.png)![](../../../Resources/Images/Retail/special%20flows.png)

In production, you can configure these flows based on your needs.

<a id="SettheConnectionStringsAppsDetails"></a>

### Set the Connection Strings (Apps) Details

Retail provides you with a wide range of apps for integration with various systems to demo various processes. Set up only the apps used by your organization or the ones dedicated to the particular processes you want to demo / use.

<a id="EnableBotApi"></a>

### Enable BotApi

For live chat integration you need to enable BotApi at your tenant level. To do so, on the main menu, click **Administration** > **Settings**. Click the **BotApi** tab and tick the **Is enabled** check box.

![](../../../Resources/Images/solution%20templates/Victor/set%20botapi.png)

<a id="SettheConnectionStringsAppsDetails1"></a>

### Set the Connection Strings (Apps) Details

Victor provides you with a wide range of apps for integration with various systems to demo various processes. Set up only the apps used by your organization or the ones dedicated to the particular processes you want to demo / use.

| Druid App | App Type | Integrates Druid with | Integration Purpose | Mandatory app |
| --- | --- | --- | --- | --- |
| [SQL-DB](#SQL-DB_Configuration) | SQL | Your Database. | Connects Druid to your DB. | Yes |
| [UiPathDruidsoft1](#UiPathDruidsoft1_Configuration) | UiPath | UiPath robots | Allows the AI Agent and UiPath robots to work seamlessly together to fulfill customers service and employee requests. | Yes |
| [UiPathOrchApi](#UiPathOrchApi_Configuration) | REST | UiPath Orchestrator API | Druid integration with UiPath Orchestrator API. | Yes |

> **NOTE:** To run the Retail setup flow, you only need to set up the SQL app.

For information on how to set the connection strings, click on the configuration section specific to the app you want to set:

<a id="SQL-DB_Configuration"></a>

## SQL-DB Configuration

**Prerequisite**

- You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your DB, from Retail Apps, click **SQL-DB**. The Edit Connector page appears.

Make the following settings:

| Setting | Description |
| --- | --- |
| ClientType | Select SqlServer. |
| DataSource | Enter the name of the SQL server. |
| InitialCatalog | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account. |

Click **Save and Close**.

<a id="UiPathDruidsoft1_Configuration"></a>

## UiPathDruidsoft1 Configuration

**Prerequisites**:

- Go to the UiPath Cloud Services Portal (https://cloud.uipath.com/<tenancyName>/portal\_/serviceinstances), under **Admin** > **Services**, click the **API Access** option corresponding to the desired service and write down the following details: **UserKey**, **Account Logical Name**, **Tenant Logical Name** and **ClientId**.
- Set up the [retail-case-workflow](Set%20up%20Orchestrator.md) process.

To configure the UiPath connector, from Retail Apps, click **UiPathDruidsoft1**. The Edit Connector page appears.

Enter the Cloud Orchestrator details (the ones noted in the prerequisites):

> **IMPORTANT!** To have Druid read all the folders from your UiPath Orchestrator, after you provide the UiPath connection strings to the UiPath Cloud Orchestrator, click the **Get UiPath folders** button.

For more information on how to configure the UiPath connector, see [Starting UiPath Unattended](../../../7_Integrations/UiPath/Starting%20UiPath%20Unattended.md) or [Creating the UiPath Connection Strings](../../../7_Integrations/UiPath/Creating%20the%20UiPath%20Connection%20Strings.md).

After you finish setting up the UiPath connector, click **Save and Close**.

<a id="UiPathOrchApi_Configuration"></a>

## UiPathOrchApi Configuration

**Prerequisites**:

- You need a UiPath Orchestrator admin account.
- You need to set up the [retail-case-workflow](Set%20up%20Orchestrator.md) process.
- Make sure that you know the following UiPath Orchestrator integration variables: **client\_id**, **refresh\_token**, **UiPath\_Account** and **UiPath\_Tenant**. To find out these variables, access cloud.uipath.com, log in and click **Manage**.

![](../../../Resources/Images/solution%20templates/Victor/manage%20tenant%20orchestrator.png)

Click on the tenant you are working on.

![](../../../Resources/Images/solution%20templates/Victor/select%20orchestrator%20tenant.png)

Click on **API Access** and write down the **client\_id** (mapped as Client Id), **UiPath\_Account** (mapped as Account Logical Name), **UiPath\_Tenant** and **TenantName** (both mapped as Tenant Name), **refresh\_token** (mapped as User Key).

To get the **OrganizationUnitId**, access the process folder in your Orchestrator and write down the FID provided in the **URL** field.

To configure the REST connector, from Retail Apps, click **UiPathOrchApi**. The Edit Connector page appears.

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

> **IMPORTANT!** In order for the AI Agent integration with the apps to be up and running, you need to publish the connector actions. To do so, from the main menu, click **Integrations** and click the **Publish** button.

<a id="Step2SetUpDruidUsers"></a>

## <a id="Step_2:_Set_Up_Druid_Users"></a>Step 2: Set Up Druid Users

The user roles that can interact with the retail AI Agent are the following:

- Customer Retail
- Visitor
- Customer Support Agent
- Manager

For production environments, you need to make sure that in the Druid Portal you assign the specific security roles to users, as follows:

- For all managers, create Druid users and assign them the **Manager** role.
- For all agents in your customer support department, create Druid users and assign them the **Helpdesk Agent** role.

> **NOTE:** To view all Druid users, in the Druid Portal, from the main menu click **Administration** > **Users** and in the Users page, tick the **ShowChatUsers** check box.

For Druid demo and community environments, assign all roles to your user.

<a id="Step3RunSetupFlow"></a>

## <a id="Step_3:_Run_Setup_Flow"></a>Step 3: Run Setup Flow

Open chat land AI Agent page and send the message “setup-retail-bot”. This command sets up all the DB tables needed in Retail.

Click **Done**. If the SQL connection strings are properly set, the Retail setup completes successfully.

You can now [train the entities and the AI Agent](Train_entities_and_bot.md) and set up the webchat in HTML page.
