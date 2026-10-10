<a id="SetUptheSolution"></a>

# Set Up the Solution

For solution admins

This section will walk you through the steps to import and configure the solution to ensure a smooth setup and operation.

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have an installed and configured the [Appointment Management Agent](../Appointment%20Management%20Agent/Set%20Up%20the%20Solution.md).
- Druid Vision key with **convert-pdf-to-jpeg** and **convert-pdf-page-to-jpeg** permissions.
- LLM resource enabled on the tenant; not required if you use your own LLM for configuration instead of Druid Service Gateway.

<a id="Installationandsetupprocedure"></a>

## Installation and setup procedure

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

1. Go to the **Solutions Library**.
2. Search for **Patient Billing Agent**.
3. Import the solution.

Wait until the import status shows Success.

<a id="Step2Configureappconnections"></a>

### Step 2. Configure app connections

Navigate to **Solution Contents** > **Apps** and configure the apps as follows:

| App | Connection Details | Mandatory |
| --- | --- | --- |
| gpt-agent | Default connection using tenant credentials. No additional configuration required.  If you're using your own LLM resources, configure the endpoint and key. | Yes |
| Druid Vision | Enter the key inside the Variables tab. Ensure permissions for **convert-pdf-to-jpeg** and **convert-pdf-page-to-jpeg** are active in **Administration** > **Druid Services**. | Yes |
| SendGrid App REST | Enter the key inside the Variables tab. This App is used for all the emails that are sent in the environment. | Yes |
| AzureStorage | Enables AzureStorage capabilities for saving invoice files | No |

Click **Publish** to make the apps available.

#### Configure the Druid Vision app

To configure this app connection, follow these steps:

1. Go to **Administration** > **Druid Services**.
2. Copy the **Resource URL** and the **Token** corresponding to the **DRUID.Vision.Api** resource you want to use — you’ll need them to configure the app connection.

![](../../../../Resources/Images/Patient%20Billing%20Agent/vision%20details.png)

> **NOTE:** If the DRUID.Vision.Api resource does not appear, contact your sales representative to activate DRUID Vision on your tenant. The DRUID.Vision.Api resource should have the following two claims: **convert-pdf-page-to-jpeg** and **convert-pdf-to-jpeg**. If any of these claims are missing, ask your sales representative to update the configuration.

3. Go to **Solution Contents** > **Apps** and click on **Druid Vision**.
4. In the **Base URL** field, paste the resource URL you copied at step 2. Remove everything after api/, including `engine/{templateName}`. For example, change: `https://druidvision.eu.druidplatform.com/api/engine/{templateName}` to: `https://druidvision.eu.druidplatform.com/api/`.
5. In the Variables table, enter the token you copied at step 2 as the key.

![](../../../../Resources/Images/Patient%20Billing%20Agent/vision%20app%20config.png)

6. Click **Save & Close** to complete the configuration and return to the Apps page.

#### Configure the SendGrid App REST app

Click on the **SendGrid App REST** and in the variable key value field, enter your SendGrid API key.

![](../../../../Resources/Images/Patient%20Billing%20Agent/SENDGRID%20APP.png)

Click **Save & Close** to apply the configuration and return to the Apps page.

> **NOTE:** When [customizing the patient experience](#Step_6), set the **Default Email** to the company automated notification email. This address applies to all system-generated emails in the environment.

#### Configure the AzureStorage app

Click on the **AzureStorage** app and fill in the info in the **Account Name** and **Account Key** field with your Azure account information. Also make sure to check the **Use HTTPS** toggle.

![](../../../../Resources/Images/Patient%20Billing%20Agent/azure%20app.png)

Click **Save & Close** to apply the configuration and return to the Apps page.

<a id="Step3ConfigureAIAgentspecialflows"></a>

### Step 3. Configure AI Agent special flows

To configure the required special flows:

1. Go to the AI Agent details page and click **Dialogue Management.**
2. Set the special flows listed below:

| Special Flow Name | Select |
| --- | --- |
| Welcome flow | welcome-flow |
| Intent not found flow | agent-small-talk |

![](../../../../Resources/Images/Patient%20Billing%20Agent/SPECIAL%20FLOWS.png)

3. Save the configuration.

<a id="Step4ConfigureNLUIntentsClassificationwithLLM"></a>

### Step 4. Configure NLU Intents Classification with LLM

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **Classification Model Type**.
3. Select **Llm** as **Model Type**.
4. Set **Endpoint Type** to **Druid**. If you’re using your own LLM resource, select your resource instead. Then choose the **Model Name**.
5. Click **Set default** for both prompts to automatically fill in instructions.

![](../../../../Resources/Images/Patient%20Billing%20Agent/nlyu%20conifg.png)

6. Save and train the AI Agent.

<a id="Step5Importdefaultsettings"></a>

### Step 5. Import default settings

To provision all the required information for the AI Agent, follow these steps:

1. Select the **Billing Admin** workspace.
2. Click **Settings** on the workspace menu.
3. Click the **Provision Data** button.

![](../../../../Resources/Images/Patient%20Billing%20Agent/admin%20settings.png)

The default settings include a predefined set of values and records. You can extend the configuration at any time by manually adding new data records. For more information, see [Manage Data Records](Manage%20Data%20Records.md).

<a id="Step6Customizethepatientexperience"></a>

### <a id="Step_6"></a>Step 6. Customize the patient experience

Solution admins can customize the patient experience. To offer tailored experience, go to the **Billing Admin** workspace and click **Settings** on the workspace menu.
Click on **Default Settings**. The Default Settings form appears.

![](../../../../Resources/Images/Patient%20Billing%20Agent/default%20settings%20form.png)

Here you can:

- Enable patients to auto-confirm their payment. Enter the URL of the landing page where the Druid Webchat is hosted. The system uses this link in confirmation emails so patients can confirm their payments. If you leave this field empty, the email is sent as a reminder only and does not include the confirmation option. For information on how to embed Druid web chat within your website, see [Deploy the WebChat Snippet](../../../../Channels/WebChat/WebChat.md#Deploy).
- Set the **Default Email** to the automated notification email of your company.
- Enable invoice file storage by turning on the **EnableAzureStorage** toggle. This allows generated invoices and billing documents to be automatically saved in Azure Storage.

<a id="Step7Scheduleautomatedalerts"></a>

### Step 7. Schedule automated alerts

The Patient Billing Agent relies on background triggers to manage time-sensitive tasks such as payment order reminders and flagging unpaid invoices as "Overdue". These triggers ensure that the solution intelligence remains accurate without manual intervention.

There are four pre-configured alerts available, which require scheduling to run on a defined cadence:

| Alert | Purpose |
| --- | --- |
| alert-paymentOrder-reminder | Sends automated email to patients a day ahead of their payment order due date. |
| alert-invoice-payment-reminder | Sends automated email to patients 3 days ahead of their invoice due date. |
| alert-invoice-status-overdue | Scans for past invoices that were not marked as **Paid** and automatically updates their status to **Overdue**. |
| alert-installment-generate-invoice | Scans for due installments that do not have an invoice, automatically generates their invoice and sends it to the patients email. |

To see the alerts, go to **Solution Content** > **Flows** and select **Alerts** category.

To define when and how often an alert runs, follow these steps:

1. Click on the alert flow.
2. Click the **Info** action to access the flow information.
3. Click on the **Scheduling** tab, then click **Schedule**.

![](../../../../Resources/Images/Patient%20Billing%20Agent/schedule.png)

4. Select **Is scheduler enabled**.
5. Set the alert schedule. We recommend scheduling the alerts as follows:

| Alert | Recommended schedule |
| --- | --- |
| alert-paymentOrder-reminder | Multiple times a day, to reach all patients. |
| alert-invoice-payment-reminder | Multiple times a day, to reach all patients. |
| alert-invoice-status-overdue | Multiple times a day, to address all overdue invoices. |
| alert-installment-generate-invoice | Multiple times a day, to generate all invoices. |

6. Save the flow.

For more information on alerts, see [Alert Flows](../../../../4_Flows/Alert%20Flows.md).
