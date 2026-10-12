---
title: Setting Up the AI Agent
---


In Druid Portal:

1. [Configure the AI Agent](<Set up the bot.md#Step_1:_Configure_bot>).
2. [Set Up Druid Users](<Set up the bot.md#Step_2:_Set_Up_Druid_Users>).
3. [Run Setup Flow](<Set up the bot.md#Step_3:_Run_Setup_Flow>).

## Step 1: Configure the AI Agent <a href="#step_1-_configure_bot" id="step_1-_configure_bot"></a>

{% hint style="info" %}
**NOTE:** Retail default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Retail, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.
{% endhint %}

To configure the AI Agent for Retail, you need to set Live Chat timeouts and Special Flows, enable the AI Agent for Live Chat integration and configure the connection strings.

### Set Live Chat timeouts

In the AI Agent Details page, click the General section header. The General settings area expands.

Set the parameters for the Route-to-Human functionality:

* **LiveChatQueueWaitingTimeoutMins** - The amount of time in minutes that a client could wait until an agent accepts the incoming live chat request. When the time limit is reached, the live-chat-waiting-message-in-the-queue flow is triggered.
* **LiveChatConversationIdleTimeoutMins** - The idle time limit for which a client can be idle (i.e. does not respond) in an ongoing conversation with an agent. Once the time limit is reached, the dialog times out and the client is automatically returned to AI Agent context.

![](<../../../../.gitbook/assets/live chat timeouts.png>)

Save the AI Agent. For more information on how it works and how to configure Live Chat, see [Live Chat](https://druidai.gitbook.io/druid-ai-docs/live-chat/live-chat).

### Set special flows

Click the Special Flows section header and select the following special flows:

| Special Flow                       | Select                      |
| ---------------------------------- | --------------------------- |
| Welcome                            | first-welcome-flow          |
| IntentNotFound                     | Intent-not-recognized       |
| Authentication                     | web-authentication-customer |
| LiveChatClientDisconnectedFlowId   | live-chat-feedback-client   |
| LiveChatAgentDisconnectedFlowId    | live-chat-agent-disconnect  |
| LiveChatClientWaitingInQueueFlowId | live-chat-connect-to-agent  |
| LiveChatClientConnectedFlowId      | live-chat-client-connected  |

[../../../Resources/Images/Retail/special%20flows.png](../../../Resources/Images/Retail/special%20flows.png)![](<../../../../.gitbook/assets/special flows (3).png>)

In production, you can configure these flows based on your needs.

### Set the Connection Strings (Apps) Details

Retail provides you with a wide range of apps for integration with various systems to demo various processes. Set up only the apps used by your organization or the ones dedicated to the particular processes you want to demo / use.

### Enable BotApi

For live chat integration you need to enable BotApi at your tenant level. To do so, on the main menu, click **Administration** > **Settings**. Click the **BotApi** tab and tick the **Is enabled** check box.

![](<../../../../.gitbook/assets/set botapi.png>)

### Set the Connection Strings (Apps) Details

Victor provides you with a wide range of apps for integration with various systems to demo various processes. Set up only the apps used by your organization or the ones dedicated to the particular processes you want to demo / use.

| Druid App                                                              | App Type | Integrates Druid with   | Integration Purpose                                                                                                   | Mandatory app |
| ---------------------------------------------------------------------- | -------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------- |
| [SQL-DB](<Set up the bot.md#SQL-DB_Configuration>)                     | SQL      | Your Database.          | Connects Druid to your DB.                                                                                            | Yes           |
| [UiPathDruidsoft1](<Set up the bot.md#UiPathDruidsoft1_Configuration>) | UiPath   | UiPath robots           | Allows the AI Agent and UiPath robots to work seamlessly together to fulfill customers service and employee requests. | Yes           |
| [UiPathOrchApi](<Set up the bot.md#UiPathOrchApi_Configuration>)       | REST     | UiPath Orchestrator API | Druid integration with UiPath Orchestrator API.                                                                       | Yes           |

{% hint style="info" %}
**NOTE:** To run the Retail setup flow, you only need to set up the SQL app.
{% endhint %}

For information on how to set the connection strings, click on the configuration section specific to the app you want to set:

## SQL-DB Configuration

**Prerequisite**

* You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your DB, from Retail Apps, click **SQL-DB**. The Edit Connector page appears.

Make the following settings:

| Setting             | Description                                                                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ClientType          | Select SqlServer.                                                                                                                            |
| DataSource          | Enter the name of the SQL server.                                                                                                            |
| InitialCatalog      | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account.                                                                         |

Click **Save and Close**.

## UiPathDruidsoft1 Configuration

**Prerequisites**:

* Go to the UiPath Cloud Services Portal (https://cloud.uipath.com//portal\_/serviceinstances), under **Admin** > **Services**, click the **API Access** option corresponding to the desired service and write down the following details: **UserKey**, **Account Logical Name**, **Tenant Logical Name** and **ClientId**.
* Set up the [retail-case-workflow](<Set up Orchestrator.md>) process.

To configure the UiPath connector, from Retail Apps, click **UiPathDruidsoft1**. The Edit Connector page appears.

Enter the Cloud Orchestrator details (the ones noted in the prerequisites):

{% hint style="warning" %}
**IMPORTANT!** To have Druid read all the folders from your UiPath Orchestrator, after you provide the UiPath connection strings to the UiPath Cloud Orchestrator, click the **Get UiPath folders** button.
{% endhint %}

For more information on how to configure the UiPath connector, see [Starting UiPath Unattended](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/starting-uipath-unattended) or [Creating the UiPath Connection Strings](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/creating-the-uipath-connection-strings).

After you finish setting up the UiPath connector, click **Save and Close**.

## UiPathOrchApi Configuration

**Prerequisites**:

* You need a UiPath Orchestrator admin account.
* You need to set up the [retail-case-workflow](<Set up Orchestrator.md>) process.
* Make sure that you know the following UiPath Orchestrator integration variables: **client\_id**, **refresh\_token**, **UiPath\_Account** and **UiPath\_Tenant**. To find out these variables, access cloud.uipath.com, log in and click **Manage**.

![](<../../../../.gitbook/assets/manage tenant orchestrator.png>)

Click on the tenant you are working on.

![](<../../../../.gitbook/assets/select orchestrator tenant.png>)

Click on **API Access** and write down the **client\_id** (mapped as Client Id), **UiPath\_Account** (mapped as Account Logical Name), **UiPath\_Tenant** and **TenantName** (both mapped as Tenant Name), **refresh\_token** (mapped as User Key).

To get the **OrganizationUnitId**, access the process folder in your Orchestrator and write down the FID provided in the **URL** field.

To configure the REST connector, from Retail Apps, click **UiPathOrchApi**. The Edit Connector page appears.

Set up the following Custom security details:

![](<../../../../.gitbook/assets/orchestrator custom security.png>)

In the Variables section, add the integration context variables as follows:

| Variable           | Description                                                                                                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UserEmail          | The email address associated to a UiPath Orchestrator admin account. The user should have access to both Orchestrator and to the folders in which the UiPath unattended process is configured. |
| client\_id         | The Client Id from Cloud UiPath Orchestrator.                                                                                                                                                  |
| UiPath\_Account    | The Account Logical Name from Cloud UiPath Orchestrator.                                                                                                                                       |
| UiPath\_Tenant     | The Tenant Name from Cloud UiPath Orchestrator.                                                                                                                                                |
| refresh\_token     | The User Key from Cloud UiPath Orchestrator.                                                                                                                                                   |
| OrganizationUnitId | The FID in your Orchestrator process folder.                                                                                                                                                   |

![](<../../../../.gitbook/assets/orchapi variables.png>)

Click **Save and Close**.

{% hint style="warning" %}
**IMPORTANT!** In order for the AI Agent integration with the apps to be up and running, you need to publish the connector actions. To do so, from the main menu, click **Integrations** and click the **Publish** button.
{% endhint %}

## Step 2: Set Up Druid Users <a href="#step_2-_set_up_druid_users" id="step_2-_set_up_druid_users"></a>

The user roles that can interact with the retail AI Agent are the following:

* Customer Retail
* Visitor
* Customer Support Agent
* Manager

For production environments, you need to make sure that in the Druid Portal you assign the specific security roles to users, as follows:

* For all managers, create Druid users and assign them the **Manager** role.
* For all agents in your customer support department, create Druid users and assign them the **Helpdesk Agent** role.

{% hint style="info" %}
**NOTE:** To view all Druid users, in the Druid Portal, from the main menu click **Administration** > **Users** and in the Users page, tick the **ShowChatUsers** check box.
{% endhint %}

For Druid demo and community environments, assign all roles to your user.

## Step 3: Run Setup Flow <a href="#step_3-_run_setup_flow" id="step_3-_run_setup_flow"></a>

Open chat land AI Agent page and send the message “setup-retail-bot”. This command sets up all the DB tables needed in Retail.

Click **Done**. If the SQL connection strings are properly set, the Retail setup completes successfully.

You can now [train the entities and the AI Agent](Train_entities_and_bot.md) and set up the webchat in HTML page.
