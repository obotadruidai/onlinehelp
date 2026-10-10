---
layout:
  title:
    visible: false
---

<a id="OnlineAppointment"></a>

# Online Appointment

Using AI Agents in healthcare you can have a 35% increase in patient satisfaction, thanks to quick response time and personalized engagement.

The healthcare digital assistant enables patients and website visitors to schedule an online appointment.

authors can deploy this solution in the following channels: [web chat](../../Channels/WebChat/WebChat.md), [WhatsApp](../../Channels/WhatsApp%20Integration/WhatsApp%20Integration.md) and [Facebook](../../Channels/Facebook%20Integration/Facebook%20Integration.md).

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../2_AI%20Agents/Creating%20AI%20Agents.md).
- SQL server connection.

<a id="Configurethetemplate"></a>

## Configure the template

After you import this solution, configure it following these steps:

<a id="Step1SetUptheAIAgent"></a>

### Step 1. Set Up the AI Agent

In Druid Portal:

1. [Configure the AI Agent](#Step_1%3A_Configure_bot).
2. [Step 2. Set the Connection Strings (Apps) Details](#Step).
3. [Run Setup Flow](#Step_3%3A_Run_Setup_Flow).

#### <a id="Step_1:_Configure_bot"></a>Step 1: Configure the AI Agent

> **NOTE:** Healthcare default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Healthcare, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.

To configure the AI Agent for Healthcare, you need to set special flows and configure the connection strings.

#### Set special flows

Click the Special Flows section header and select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome | welcome-check-role |
| IntentNotFound | Intent-not-recognized |

In production, you can configure these flows based on your needs.

#### <a id="Step"></a>Step 2. Set the Connection Strings (Apps) Details

Victor provides you with a wide range of apps for integration with various systems to demo various processes. Set up only the apps used by your organization or the ones dedicated to the particular processes you want to demo / use.

| Druid App | App Type | Integrates Druid with | Integration Purpose | Mandatory app |
| --- | --- | --- | --- | --- |
| [Apps\_Healthcare](#SQL-DB_Configuration) | SQL | Your Database. | Connects Druid to your DB. | Yes |
| [send\_email](#UiPathDruidsoft1_Configuration) | Email | Your SMTP / SendGrid server | After appointment validation, an email with all the information is sent to the user | No |

> **NOTE:** To run the Retail setup flow, you only need to set up the SQL app.

For information on how to set the connection strings, click on the configuration section specific to the app you want to set:

<a id="SQL-DB_Configuration"></a>

## Apps\_Healthcare Configuration

**Prerequisite**

- You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your DB, from Healthcare Apps, click **SQL-DB**. The Edit Connector page appears.

Make the following settings:

| Setting | Description |
| --- | --- |
| ClientType | Select SqlServer. |
| DataSource | Enter the name of the SQL server. |
| InitialCatalog | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account. |

Click **Save and Close**.

<a id="send_email"></a><a id="UiPathDruidsoft1_Configuration"></a>

## send\_email

For detailed procedure on how to configure the Email connector, see [Email Connectors](../../7_Integrations/Email%20Connectors/Email%20Connectors.md).

#### <a id="Step_3:_Run_Setup_Flow"></a>Step 3: Run Setup Flow

Open chat land AI Agent page and send the message “setup-healthcare”. This command sets up all the DB tables needed in Retail.

Click **Done**. If the SQL connection strings are properly set, the Healthcare setup completes successfully.

You can now [train the entities and the AI Agent](../Retail/General%20Settings/Train_entities_and_bot.md) and set up the webchat in HTML page.

<a id="Step2TraintheEntitiesandtheAIAgent"></a>

### Step 2. Train the Entities and the AI Agent

We created Druid for enterprises and unlike other AI Agent platforms; its entities are business objects with attributes and references, similar to the UiPath Data Service entities.

#### Train the Entities

In the AI Agent configuration page, click the **Entities** tab. Train the entities "Specialty", "Doctor", "Service", "District" and "Location" by clicking the **Edit Schedule** icon displayed in line with each entity.

![](../../Resources/Images/Healthcare/train%20entities.png)

In the pop-up that appears, click the **Train** button.

After a few seconds, the Status **Trained** should appear in the pop-up:

> **NOTE:**  If the train status message does not appear, you might want to check you have properly configured the corresponding Druid app.

After you successfully train the entities, click **Save** button.

Now you can train the AI Agent.

#### Train the AI Agent

Click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

![](../../Resources/Images/solution%20templates/Cristina/train%20bot.png)

> **NOTE:**  It might take a few minutes for the NLP training to complete, so you might need to wait for Druid to finish training all AI Agent entities that have NLP enabled (NLP=true).
