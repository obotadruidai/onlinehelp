---
title: Setting Up the AI Agent
---


## Step 1. Install the solution from the Solutions Library

For information on how to install the solution, see [Installing Solution Templates](<../../Installing Solution Templates.md>).

## Step 2. Configure the AI Agent

{% hint style="info" %}
**NOTE:** Travel, Travel Management default language is set to EN-US and additional language is set to RO. If you want to add additional languages on this solution, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.
{% endhint %}

To configure the AI Agent for Travel, Travel Management, you need to set Special Flows and configure the connection strings.

**Set special flows**

Click the Special Flows section header and select the following special flows:

| Special Flow   | Select                           |
| -------------- | -------------------------------- |
| Welcome        | first-welcome-flow-travel-bot    |
| IntentNotFound | intent-not-recognized-travel-bot |

![](<../../../../.gitbook/assets/Setting up the solution template_5.png>)

In production, you can configure these flows based on your needs.

**Choose the bot framework**

By default, AI Agents use bot framework version 3. For Druid version 1.59 or higher, two framework versions are available: v3 and v4.

Bot framework version 4 allows you to use adaptive cards in the conversational flows and do extensive customization to the web chat snippet enabling chat users to:

* Show chat snippet on the left/right side of the screen.
* End current conversation and initiate a new chat.
* Change the chat language in any of the AI Agent languages.

{% hint style="warning" %}
**IMPORTANT!** Bot framework v4 is a tenant feature, so in order to activate it, get in touch with [Druid Support](../../../Solution%20Library/Travel/Travel%20Management/mailto:support@druidai.com).
{% endhint %}

If you want your AI Agent to use framework v4, in the AI Agent details page, **General** tab, from the **Bot Framework Version** drop-down, select **v4**.

![](<../../../../.gitbook/assets/Setting up the solution template_6.png>)

**Set the Connection Strings (Apps) Details**

Travel, Travel Management provides you with a wide range of apps for integration with various systems to demo various processes. Set up only the apps used by your organization or the ones dedicated to the particular processes you want to demo / use.

| Druid App                                                                     | App Type | Integrates Druid with | Integration Purpose                                                                            | Mandatory app                         |
| ----------------------------------------------------------------------------- | -------- | --------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------- |
| [SQL-DB-TRAVEL](<Setting up the bot.md#SQL-DB-TRAVEL_Configuration>)          | SQL      | Your Database.        | Connects Druid to your DB.                                                                     | Yes                                   |
| [OCR Identity Card](<Setting up the bot.md#OCR_Identity_Card__Configuration>) | REST     | Druid AI Services     | Performs OCR and data extraction from Romanian Identity Cards and Australian driving licenses. | Yes                                   |
| [Namirial](<Setting up the bot.md#Namirial_Configuration>)                    | REST     | eSign from Namirial   | Allows the electronic signature of digital travel documents                                    | No                                    |
| [SendGrid](<Setting up the bot.md#SendGrid_Configuration>)                    | SendGrid | Your SMTP Server      | Sends emails                                                                                   | No. (only if you need to send emails) |

{% hint style="info" %}
**NOTE:** To run the Travel Management setup flow, you only need to set up the **SQL-DB-TRAVEL** app.
{% endhint %}

For information on how to set the connection strings, click on the configuration section specific to the app you want to set:

## SQL-DB-TRAVEL Configuration

**Prerequisite**

* You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your DB, from Travel Management apps, click **SQL-DB-TRAVEL**. The Edit Connector page appears.

Make the following settings:

| Setting             | Description                                                                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ClientType          | Select SqlServer.                                                                                                                            |
| DataSource          | Enter the name of the SQL server.                                                                                                            |
| InitialCatalog      | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account.                                                                         |

![](<../../../../.gitbook/assets/Customer 360.png>)

Click **Save and Close**.

## OCR Identity Card Configuration

In Travel, Travel Management, you can use Druid AI Services for OCR of Romanian identity cards and Australian driving licenses.

This section describes the connection strings required if you are using Druid AI Services.

**Prerequisites**:

* In order to use the Druid AI Services, you need the URL and access token of the instance on which the Druid OCR is running. To get the URL and access token, contact [Druid Tech Support](../../../Solution%20Library/Travel/Travel%20Management/mailto:support@druidai.com).

{% hint style="info" %}
**NOTE:** Druid Tech Support generates the access token per tenant and environment.
{% endhint %}

To configure the REST connector to Druid AI Services, which performs OCR of Romanian identity cards, from Travel Management Apps, click **OCR Identity Card**. The Edit Connector page appears.

In the **URL** field, enter the URL provided by Druid Tech Support.

In the Variables section, add the token provided by Druid Tech Support.

![](<../../../../.gitbook/assets/Setting up the solution template_3.png>)

Click **Save and Close**.

## Namirial Configuration

**Prerequisites**:

* You need to have an [eSign](https://www.esignanywhere.net/) subscription with Namirial. If you don't have a Namirial subscription, you can send an email to Druid Tech Support at [support@Druidai.com](mailto:support@druidai.com) and they will provide you with an API key you can use ONLY for testing purposes.
* You need to know the Namirial organizationKey (your organization API key). To find out the Namirial organization, in Namirial Digital Transaction Management Platform, go to **Settings** > **Api Tokens and Apps**.

To configure the REST connector used for electronic signature of the contracts, from Travel Management Apps, click **Namirial**. The Edit Connector page appears.

In the **Base URL** field, enter the URL of the Namirial Digital Transaction Management Platform, _https://saas.esignanywhere.net_ and from the **SecurityType** drop-down, select **None**.

In the Variables section, add the integration context variables associated to your organization’s Namirial account, **userLoginName** (your Namirial login e-mail address) and **organizationKey**.

![](<../../../../.gitbook/assets/Setting up the solution template_2.png>)

Click **Save and Close**.

## SendGrid Configuration

**Prerequisites:**

* You need to have an email service and know the API Key. To find out the API Key, you might need to contact your system administrator. If you don't have an email service, you can send an email to Druid Tech Support at [support@Druidai.com](mailto:support@druidai.com) and they will provide you with an API key you can use only for testing purposes.

To configure the Send-Email connector, which sends emails, from Travel Management Apps, click **SendGrid**. The Edit Connector page appears.

In the **ApiKey** field, enter the API Key received from your email service provider.

![](<../../../../.gitbook/assets/Setting up the solution template_1.png>)

Click **Save and Close**.

{% hint style="warning" %}
**IMPORTANT!** In order for the AI Agent integration with the apps to be up and running, you need to publish the connector actions. To do so, from the main menu, click **Integrations** and click the **Publish** button.
{% endhint %}

## Step 3: Run Setup Flow <a href="#step_3-_run_setup_flow" id="step_3-_run_setup_flow"></a>

Open chat land AI Agent page and send the message "**setup-travel-bot**". This command sets up all the DB tables needed in Travel Management.

Click **Done**. If the SQL connection strings are properly set, Travel setup completes successfully.

You can now train the AI Agent.

## Step 4. Train the AI Agent

In the AI Agent details page, click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

{% hint style="info" %}
**NOTE:** It might take a few minutes for the NLP training to complete, so you might need to wait for Druid to finish training all AI Agent entities that have NLP enabled (NLP=true).
{% endhint %}
