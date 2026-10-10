---
title: "Set Up the Solution"
---

<a id="SetUptheSolution"></a>


This section will walk you through the steps to import and configure the solution to ensure a smooth setup and operation.

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have an installed and configured the [Appointment Management Agent](../../Appointment%20Management%20Agent/Set%20Up%20the%20Solution.md).
- LLM resource enabled on the tenant; not required if you use your own LLM for configuration instead of Druid Service Gateway.

<a id="Installationandsetupprocedure"></a>

## Installation and setup procedure

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

1. Go to the **Solutions Library**.
2. Search for **Patient Support Agent – Lab Results Skill**.
3. Import the solution.

Wait until the import status shows Success.

<a id="Step2Configureappconnections"></a>

### Step 2. Configure app connections

Navigate to **Solution Contents** > **Apps** and configure the apps as follows:

| App | Connection Details | Mandatory |
| --- | --- | --- |
| gpt-agent | Default connection using tenant credentials. No additional configuration required.  If you're using your own LLM resources, configure the endpoint and key. | Yes |
| SendGrid App REST | Enter the key inside the Variables tab. This App is used for all the emails that are sent in the environment. | No |

Click **Publish** to make the apps available.

#### Configure the SendGrid App REST app

Click on the **SendGrid App REST** and in the variable key value field, enter your SendGrid API key.

[../../../../../Resources/Images/Patient%20Billing%20Agent/SENDGRID%20APP.png](../../../../../Resources/Images/Patient%20Billing%20Agent/SENDGRID%20APP.png)![](../../../../../Resources/Images/Lab%20Results%20Skill/Set%20Up%20the%20Solution.png)

Click **Save & Close** to apply the configuration and return to the Apps page.

<a id="Step3ConfigureAIAgentspecialflows"></a>

### Step 3. Configure AI Agent special flows

To configure the required special flows:

1. Go to the AI Agent details page and click Dialogue Management.
2. Set the special flows listed below:

| Special Flow Name | Select |
| --- | --- |
| Welcome flow | welcome-flow |
| Intent not found flow | agent-small-talk |

[../../../../../Resources/Images/Patient%20Billing%20Agent/SPECIAL%20FLOWS.png](../../../../../Resources/Images/Patient%20Billing%20Agent/SPECIAL%20FLOWS.png)![](../../../../../Resources/Images/Lab%20Results%20Skill/Set%20Up%20the%20Solution_1.png)

3. Save the configuration.

<a id="Step4Importdefaultsettings"></a>

### Step 4. Import default settings

To provision all the required information for the AI Agent, follow these steps:

1. Select the **Lab Results Admin** workspace.
2. Click **Settings** on the workspace menu.
3. Click the Provision Data button.

[../../../../../Resources/Images/Patient%20Billing%20Agent/admin%20settings.png](../../../../../Resources/Images/Patient%20Billing%20Agent/admin%20settings.png)![](../../../../../Resources/Images/Lab%20Results%20Skill/Set%20Up%20the%20Solution_2.png)

The default settings include a predefined set of values and records. You can extend the configuration at any time by manually adding new data records. For more information, see [Manage Data Records](Manage%20Data%20Records.md).

<a id="Step5ConfigureNLUIntentClassificationwithLLM"></a>

### Step 5. Configure NLU Intent Classification with LLM

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **Classification Model Type**.
3. Set **Endpoint Type** to **Druid**. If you’re using your own LLM resource, select your resource instead. Then choose the **Model Name**.
4. Click **Set default** for both prompts to automatically fill in instructions.

![](../../../../../Resources/Images/Lab%20Results%20Skill/Set%20Up%20the%20Solution_3.png)

5. Save and train the AI Agent.

<a id="Step6Customizethepatientexperience"></a>

### Step 6. Customize the patient experience

Solution admins can customize the patient experience. To offer tailored experience, go to the **Lab Results Admin** workspace and click **Settings** on the workspace menu. Click on **Default Settings**. The Default Settings form appears.

![](../../../../../Resources/Images/Lab%20Results%20Skill/Set%20Up%20the%20Solution_4.png)

Here you can:

- Enable patients to get automatically routed to the appointment agent. Enter the URL of the landing page where the Druid Webchat is hosted. The system uses this link in confirmation emails so patients can easily request an appointment for a test result consultation. If you leave this field empty, the email is sent as a reminder only and does not include the appointment request option. For information on how to embed Druid web chat within your website, see [../../../../../Channels/WebChat/WebChat.md#Deploy](../../../../../Channels/WebChat/WebChat.md#Deploy)[Deploy the WebChat Snippet](../../../../../Channels/WebChat/WebChat.md#Deploy).
- Set the **Default Email**. Configure the sender email address used for result notifications. Enter the email address patients will see as the sender upon receiving detailed results.
{% hint style="warning" %}
**IMPORTANT!** This mandatory field must be configured before the system can send result notification emails.
{% endhint %}
