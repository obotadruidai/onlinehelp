---
title: Setting Up the AI Agent
---


In Druid Portal:

1. [Configure the AI Agent](<Set up the bot.md#Step_1:_Configure_bot>).
2. [Set Up Druid Users](<Set up the bot.md#Step_2:_Set_Up_Druid_Users>).
3. [Run Setup Flow](<Set up the bot.md#Step_3:_Run_Setup_Flow>).

## Step 1: Configure the AI Agent <a href="#step_1-_configure_bot" id="step_1-_configure_bot"></a>

{% hint style="info" %}
**NOTE:** Human Resources default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Human Resources, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.
{% endhint %}

To configure the AI Agent for Human Resources, you need to set Special Flows and configure the connection strings.

### Set special flows

Click the Special Flows section header and select the following special flows:

| Special Flow   | Select                   |
| -------------- | ------------------------ |
| Welcome        | hr-intro-check-role      |
| IntentNotFound | hr-intent-not-recognized |
| Authentication | authenticate-hr-user     |

![](<../../../../.gitbook/assets/special flows (1).png>)

In production, you can configure these flows based on your needs.

### Set the Connection Strings (Apps) Details

Human Resources provides you with a wide range of apps for integration with various systems to demo various processes. Set up only the apps used by your organization or the ones dedicated to the particular processes you want to demo / use.

| Druid App                                                                      | App Type | Integrates Druid with | Integration Purpose                                                                                           | Mandatory app                         |
| ------------------------------------------------------------------------------ | -------- | --------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| [Druid\_Apps\_Cristina](<Set up the bot.md#Druid_Apps_Cristina_Configuration>) | SQL      | Your Database.        | Connects Druid to your DB.                                                                                    | Yes                                   |
| [UiPath Cristina](<Set up the bot.md#UiPath_Cristina_Configuration>)           | UiPath   | UiPath robots         | Allows the AI Agent and UiPath robots to work seamlessly together to fulfill employees and managers requests. | Yes                                   |
| [Cristina OCR CALL](<Set up the bot.md#Cristina_OCR_Call_Configuration>)       | REST     | Druid AI Services     | Performs OCR and data extraction from Romanian Identity Cards and Australian driving licenses.                | Yes                                   |
| [SendGrid-Cristina](<Set up the bot.md#SendGrid-Cristina_Configuration>)       | SendGrid | Your SMTP Server      | Sends emails                                                                                                  | No. (only if you need to send emails) |

{% hint style="info" %}
**NOTE:** To run the Human Resources setup flow, you only need to set up the **Druid\_Apps\_Cristina** app.
{% endhint %}

For information on how to set the connection strings, click on the configuration section specific to the app you want to set:

## Druid\_Apps\_Cristina Configuration

**Prerequisite**

* You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your DB, from Human Resources Apps, click **Druid-apps**. The Edit Connector page appears.

Make the following settings:

| Setting             | Description                                                                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ClientType          | Select SqlServer.                                                                                                                            |
| DataSource          | Enter the name of the SQL server.                                                                                                            |
| InitialCatalog      | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account.                                                                         |

![](<../../../../.gitbook/assets/sql connector setup.png>)

Click **Save and Close**.

## UiPath Cristina Configuration

**Prerequisites**:

* UiPath Orchestrator
* If you are using the Cloud Orchestrator, go to you tenant and under **Admin** > **Services**, click the **API Access** option corresponding to the desired service and write down the following details: **UserKey**, **Account Logical Name**, **Tenant Logical Name** and **ClientId**.

To configure the UiPath connector, from Human Resources Apps, click **UiPath Cristina**. The Edit Connector page appears.

The connector can integrate with both the Cloud and on premise versions of the Orchestrator. From the **SecurityType** drop-down, select the type of Orchestrator.

If you use the on premise Orchestrator, fill in the following fields: **Url**, **Tenant**, **User name** and **Password**.

If you are using the Cloud Orchestrator, fill-in the following fields with the values you have wrote down in the prerequisites: **UserKey**, **Account Logical Name**, **Tenant Logical Name** and **ClientId**.

{% hint style="warning" %}
**IMPORTANT!** To have Druid read all the folders from your UiPath Orchestrator, after you provide the UiPath connection strings to the UiPath Cloud Orchestrator, click the **Get UiPath folders** button.
{% endhint %}

For more information on how to configure the UiPath connector, see [Triggering an Unattended Process](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/running-unattended-process-using-orchestrator-queues) or [Creating the UiPath Connection Strings](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/creating-the-uipath-connection-strings).

After you finish setting up the UiPath connector, click **Save and Close**.

## Cristina OCR Call Configuration

In Human Resources, you can use two types of OCR solutions:

* Druid AI Services for OCR of Romanian identity cards and Australian driving licenses.
* UiPath AI Center for OCR of any ID document that complies with the MRZ standard.

This section describes the connection strings required if you are using Druid AI Services. If you are using UiPath AI Center, follow the instructions described in section [Setting Up AI Center](Setting_up_AI_Center.md).

**Prerequisites**:

* In order to use the Druid AI Services, you need the URL and access token of the instance on which the Druid OCR is running. To get the URL and access token, contact [Druid Tech Support](../../../Solution%20Library/Human%20Resources/General%20Settings/mailto:support@druidai.com).

{% hint style="info" %}
**NOTE:** Druid Tech Support generates the access token per tenant and environment.
{% endhint %}

To configure the REST connector to Druid AI Services, which performs OCR of Romanian identity cards, from Human Resources Apps, click **Cristina OCR CALL**. The Edit Connector page appears.

In the **URL** field, enter the URL provided by Druid Tech Support.

![](<../../../../.gitbook/assets/croistina ocr settings.png>)

In the Variables section, add the token provided by Druid Tech Support.

![](<../../../../.gitbook/assets/ocr variables.png>)

Click **Save and Close**.

## SendGrid-Cristina Configuration

**Prerequisites:**

* You need to have an email service and know the API Key. To find out the API Key, you might need to contact your system administrator.

To configure the SendGrid connector, which sends emails, from Human Resources Apps, click **SendGrid-Cristina**. The Edit Connector page appears.

In the **ApiKey** field, enter the API Key received from your email service provider.

![](../../../../.gitbook/assets/sendgrid.png)

Click **Save and Close**.

{% hint style="warning" %}
**IMPORTANT!** In order for the AI Agent integration with the apps to be up and running, you need to publish the connector actions. To do so, from the main menu, click **Integrations** and click the **Publish** button.
{% endhint %}

## Step 2: Set Up Druid Users <a href="#step_2-_set_up_druid_users" id="step_2-_set_up_druid_users"></a>

For production environments, you need to make sure that in the Druid Portal you assign the specific security roles to users, as follows:

* For all managers, create Druid users and assign them the **Manager** role. They will address employees’ requests.
* For all employees, create Druid users and assign them the **Employee** role.
* For all employees involved in the HR recruitment process, create Druid users and assign them the **HR Admin** role.
* For website candidates looking to apply for a job, create Druid users and assign them the **Candidate** role.

{% hint style="info" %}
**NOTE:** To view all Druid users, in the Druid Portal, from the main menu click **Administration** > **Users** and in the Users page, tick the **ShowChatUsers** check box.
{% endhint %}

For Druid demo and community environments, assign all roles to your user.

## Step 3: Run Setup Flow <a href="#step_3-_run_setup_flow" id="step_3-_run_setup_flow"></a>

Open chat land AI Agent page and send the message “setup-cristina”. This command sets up all the DB tables needed in Human Resources.

Click **Done**. If the SQL connection strings are properly set, Human Resources setup completes successfully.

You can now [train the entities and the AI Agent](Train_entities_and_bot.md) and set up the webchat in HTML page.
