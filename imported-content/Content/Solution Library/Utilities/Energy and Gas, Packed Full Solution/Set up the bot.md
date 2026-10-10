---
title: "Setting Up the AI Agent"
---

<a id="SettingUptheAIAgent"></a>


In Druid Portal:

1. [Configure the AI Agent](#Step_1%3A_Configure_bot).
2. [Run Setup Flow](#Step_3%3A_Run_Setup_Flow).

<a id="Step1ConfiguretheAIAgent"></a>

## <a id="Step_1:_Configure_bot"></a>Step 1: Configure the AI Agent

> **NOTE:** Energy and Gas, Packed Full Solution default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Energy and Gas, Packed Full Solution, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.

To configure the AI Agent for Energy and Gas, Packed Full Solution, you need to set Special Flows and configure the connection strings.

<a id="Setspecialflows"></a>

### Set special flows

Click the Special Flows section header and select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome | Welcome Volt |
| IntentNotFound | Intent not Found |
| Authentication | check-auth-lvl-1-and-2 |
| LanguageChangedFlowId | change-language.  **NOTE:** This special flow is valid only if your AI Agent is using bot framework version 4. |

![](../../../Resources/Images/utilities%20full/bot%20setup.png)

In production, you can configure these flows based on your needs.

<a id="SettheConnectionStringsAppsDetails"></a>

### Set the Connection Strings (Apps) Details

Energy and Gas, Packed Full Solution provides you with a wide range of apps for integration with various systems to demo various processes. Set up only the apps used by your organization or the ones dedicated to the particular processes you want to demo / use.

| Druid App | App Type | Integrates Druid with | Integration Purpose | Mandatory app |
| --- | --- | --- | --- | --- |
| [SQL-Electricity](#SQL-Electricity) | SQL | Your Database. | Connects Druid to your DB. | Yes |
| [ID OCR](#ID_OCR__Configuration) | REST | Druid AI Services | Performs OCR and data extraction from Romanian Identity Cards and Australian driving licenses. | Yes |
| [Namirial](#Namirial_Configuration) | REST | eSign from Namirial | Allows the electronic signature of a digital document generated for the onboarding process. | No |
| [Send-Email](#Send-Email_Configuration) | SendGrid | Your SMTP Server | Sends emails | No. (only if you need to send emails) |

> **NOTE:** To run the Volt setup flow, you only need to set up the **SQL-Electricity** app.

For information on how to set the connection strings, click on the configuration section specific to the app you want to set:

<a id="SQL-Electricity"></a>

## SQL-Electricity Configuration

**Prerequisite**

- You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your DB, from Energy and Gas, Packed Full Solution Apps, click **Druid-apps**. The Edit Connector page appears.

Make the following settings:

| Setting | Description |
| --- | --- |
| ClientType | Select SqlServer. |
| DataSource | Enter the name of the SQL server. |
| InitialCatalog | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account. |

Click **Save and Close**.

<a id="ID_OCR__Configuration"></a>

## ID OCR Configuration

In Energy and Gas, Packed Full Solution, you can use Druid AI Services for OCR of Romanian identity cards and Australian driving licenses.

This section describes the connection strings required if you are using Druid AI Services.

**Prerequisites**:

- In order to use the Druid AI Services, you need the URL and access token of the instance on which the Druid OCR is running. To get the URL and access token, contact [Druid Tech Support](<mailto:support@druidai.com?subject=I need access to Druid AI Services>).

> **NOTE:** Druid Tech Support generates the access token per tenant and environment.

To configure the REST connector to Druid AI Services, which performs OCR of Romanian identity cards, from Energy and Gas, Packed Full Solution Apps, click **ID OCR** . The Edit Connector page appears.

In the **URL** field, enter the URL provided by Druid Tech Support.

In the Variables section, add the token provided by Druid Tech Support.

Click **Save and Close**.

<a id="Namirial_Configuration"></a>

## Namirial Configuration

**Prerequisites**:

- You need to have an [eSign](https://www.esignanywhere.net/) subscription with Namirial. If you don't have a Namirial subscription, you can send an email to Druid Tech Support at [support@Druidai.com](mailto:support@druidai.com) and they will provide you with an API key you can use ONLY for testing purposes.
- You need to know the Namirial organizationKey (your organization API key). To find out the Namirial organization, in Namirial Digital Transaction Management Platform, go to **Settings** > **Api Tokens and Apps**.

To configure the REST connector used forused for electronic signature of the contracts, from Energy and Gas, Packed Full Solution Apps, click **Namirial**. The Edit Connector page appears.

In the **Base URL** field, enter the URL of the Namirial Digital Transaction Management Platform, *https://saas.esignanywhere.net* and from the **SecurityType** drop-down, select **None**.

In the Variables section, add the integration context variables associated to your organization’s Namirial account, **userLoginName** (your Namirial login e-mail address) and **organizationKey**.

Click **Save and Close**.

<a id="Send-Email_Configuration"></a>

## Send-Email Configuration

**Prerequisites:**

- You need to have an email service and know the API Key. To find out the API Key, you might need to contact your system administrator. If you don't have an email service, you can send an email to Druid Tech Support at [support@Druidai.com](mailto:support@druidai.com) and they will provide you with an API key you can use only for testing purposes.

To configure the Send-Email connector, which sends emails, from Human Resources Apps, click **Send-Email**. The Edit Connector page appears.

In the **ApiKey** field, enter the API Key received from your email service provider.

Click **Save and Close**.

> **IMPORTANT!** In order for the AI Agent integration with the apps to be up and running, you need to publish the connector actions. To do so, from the main menu, click **Integrations** and click the **Publish** button.

<a id="Step2RunSetupFlow"></a>

## <a id="Step_3:_Run_Setup_Flow"></a>Step 2: Run Setup Flow

Open chat land AI Agent page and send the message "**setup AI Agent**" or "**setup Volt**". This command sets up all the DB tables needed in Energy and Gas, Packed Full Solution.

Click **Done**. If the SQL connection strings are properly set, Energy and Gas, Packed Full Solution setup completes successfully.

You can now train the AI Agent.

<a id="Step3TraintheAIAgent"></a>

## Step 3. Train the AI Agent

Click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

> **NOTE:**  It might take a few minutes for the NLP training to complete, so you might need to wait for Druid to finish training all AI Agent entities that have NLP enabled (NLP=true).

You can now see the AI Agent in action.
