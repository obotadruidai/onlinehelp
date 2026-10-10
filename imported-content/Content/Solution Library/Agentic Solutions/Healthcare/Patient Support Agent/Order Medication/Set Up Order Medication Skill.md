---
layout:
  title:
    visible: false
---

<a id="SetUptheSolution"></a>

# Set Up the Solution

For solution admins

This section explains how to install and configure the Order Medication Skill.

<a id="Prerequisites"></a>

## Prerequisites

Before installing the solution, verify that the following requirements are met:

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- The [Appointment Management Agent](../../Appointment%20Management%20Agent/Appointment%20Management%20Agent.md) is installed and configured in your tenant.
- LLM resource enabled on the tenant; not required if you use your own LLM for configuration instead of Druid Service Gateway.

<a id="Installationandsetupprocedure"></a>

## Installation and setup procedure

Complete the following steps to install and configure the solution:

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

1. Go to the **Solutions Library**.
2. Search for **Patient Support Agent - Order Medication Agent**.
3. Import the solution.
4. Wait until the import status shows Success.

<a id="Step2Configureappconnections"></a>

### Step 2. Configure app connections

Navigate to **Solution Contents** > **Apps** and configure the apps as follows:

| App | Connection Details | Mandatory |
| --- | --- | --- |
| gpt-agent | Default connection using tenant credentials. No additional configuration required.  If you're using your own LLM resources, configure the endpoint and key. | Yes |
| SendGrid App REST | This App is used for sending emails.  Enter your SendGrid API key, then save the app configuration.  [!\[\](../../../../../Resources/Images/Order%20Medication%20Agent/Set%20Up%20the%20Solution.png)](../../../../../Resources/Images/Patient%20Billing%20Agent/SENDGRID%20APP.png) | No |

Click **Publish** to make the apps available.

<a id="Step3ConfigureAIAgentspecialflows"></a>

### Step 3. Configure AI Agent special flows

To configure the required special flows:

1. Go to the AI Agent details page and click **Dialogue Management**.
2. Set the special flows listed below:

| Special Flow Name | Select |
| --- | --- |
| Welcome flow | welcome-flow |
| Intent not found flow | agent-small-talk |

[!\[\](../../../../../Resources/Images/Order%20Medication%20Agent/Set%20Up%20the%20Solution_1.png)](../../../../../Resources/Images/Patient%20Billing%20Agent/SPECIAL%20FLOWS.png)

3. Save the configuration.

<a id="Step4Importthedata"></a>

### Step 4. Import the data

To provision all the required information for the AI Agent, follow these steps:

1. Select the **Order Medication Admin** workspace.
2. Click **Settings** on the workspace menu.
3. Click the **Provision Medicine Data** button.

![](../../../../../Resources/Images/Order%20Medication%20Agent/import%20data.png)

The default settings include a predefined set of values and records. You can extend the configuration at any time by manually adding new data records. For more information, see [Manage Data Records](Manage%20Data%20Records.md).

<a id="Step5ConfigureNLUIntentClassificationwithLLM"></a>

### Step 5. Configure NLU Intent Classification with LLM

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **Classification Model Type**.
3. Set **Endpoint Type** to **Druid**. If you’re using your own LLM resource, select your resource instead. Then choose the **Model Name**.
4. Click **Set default** for both prompts to automatically fill in instructions.
5. Save and train the AI Agent.

<a id="Step6Customizethepatientexperience"></a>

### Step 6. Customize the patient experience

Solution admins can customize the patient experience. To offer tailored experience, go to the **Order Medication Admin** workspace and click **Settings** on the workspace menu. Click on **Default Settings**. The Default Settings form appears.

![](../../../../../Resources/Images/Order%20Medication%20Agent/Set%20Up%20the%20Solution_4.png)

Here you can:

- Enable patient automatic routing to the Reorder Agent.
- In the **Default Email** field, enter the sender email address used to send notifications. Enter the email address that will appear as the sender when the system emails patients.
> **IMPORTANT!** This mandatory field determines the display sender address when emailing patients. Notification emails will fail until a sender address is configured.

- Specify the Druid Web Chat URL by entering the Website URL of the landing page where the Druid Web Chat is hosted. The system includes this link in payment confirmation emails, allowing patients to access the chat and confirm their payments. If you leave this field empty, the system sends the email as a reminder only, without the payment confirmation option. For information about embedding the Druid Web Chat into your website, see [Deploy the WebChat Snippet](../../../../../Channels/WebChat/WebChat.md#Deploy).
