---
title: "Set Up the Solution"
---

<a id="SetUptheSolution"></a>


For solution admins

This section will walk you through the steps to import and configure the solution to ensure a smooth setup and operation.

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have an AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../../../2_AI%20Agents/Creating%20AI%20Agents.md).
- Druid Vision key with **convert-pdf-to-jpeg** and **convert-pdf-page-to-jpeg** permissions
- LLM resource enabled on the tenant; not required if you use your own LLM for configuration instead of Druid Service Gateway.

<a id="Installationandsetupprocedure"></a>

## Installation and setup procedure

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

1. Go to the **Solutions Library**.
2. Search for **Appointment Management Agent**.
3. Import the solution.

Wait until the import status shows Success.

<a id="Step2Configureappconnections"></a>

### Step 2. Configure app connections

Navigate to **Solution Contents** > **Apps** and configure the apps as follows:

The default connections are preconfigured using tenant credentials.

| App | Connection Details | Mandatory |
| --- | --- | --- |
| gpt-agent | If provisioned via Druid Service Gateway, enter only the key the Variables tab. Take the key value from **Administration** > **Druid Services**.  If you're using your own LLM resources, configure the details. | Yes |
| Druid Vision | Enter the key inside the Variables tab. Ensure permissions for **convert-pdf-to-jpeg** and **convert-pdf-page-to-jpeg** are active in **Administration** > **Druid Services**. | Yes |
| SendGrid App REST | Enter the key inside the Variables tab. This App is used for all the emails that are sent in the environment. | No |
| Outbound AudioCodes | Enter the Auth value for your integration. This enables the AI Agent to make outbound calls. | Yes for voice AI Agents |

Click **Publish** to make the apps available.

<a id="Step3ConfigureAIAgentspecialflows"></a>

### Step 3. Configure AI Agent special flows

To configure the required special flows:

1. Go to the **AI Agent** details page and click **Dialogue Management.**
2. Set the special flows listed below:

| Special Flow Name | Select |
| --- | --- |
| Welcome flow | welcome-flow |
| Intent not found flow | agent-small-talk |

3. Save the configuration.

<a id="Step4ConfigureNLUIntentsClassificationwithLLM"></a>

### Step 4. Configure NLU Intents Classification with LLM

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **Classification Model Type**.
3. Select **Llm** as **Model Type**.
4. Set **Endpoint Type** to **Druid**. If you’re using your own LLM resource, select your resource instead. Then choose the **Model Name**.
5. Click **Set default** for both prompts to automatically fill in instructions.

![](../../../../Resources/Images/appointment%20management%20agent/ll%20classif.png)

6. Save and train the AI Agent.

<a id="Step5Importdefaultsettings"></a>

### Step 5. Import default settings

To provision all the required information for the AI Agent, follow these steps:

1. Select the **Appointment Admin** workspace.
2. Click **Settings** on the workspace menu.
3. Click the **Provision Data** button.

![](../../../../Resources/Images/Agentic%20Healthcare/provision%20data.png)

The default settings include a predefined set of values and records. You can extend the configuration at any time by manually adding new data records. For more information, see [Manage Data Records](Manage%20Data%20Records.md).

The default settings include provider timeslots for the next two weeks.

{% hint style="warning" %}
**IMPORTANT!** Timeslots represent the actual availability of a provider at a specific facility. These are the bookable units used during patient appointment scheduling. Because timeslots are generated for a limited period (two weeks), you must **generate new timeslots regularly**. If all existing timeslots are in the past, patients won’t be able to schedule future appointments. For information on how to generate new timeslots, see [Generate New Timeslots](Generate%20new%20timeslots.md).
{% endhint %}

<a id="Step6Customizethepatientexperience"></a>

### <a id="Step_6"></a>Step 6. Customize the patient experience

Solution admins can customize the patient experience. To offer tailored experience, go to the **Appointment Admin** workspace and click **Settings** on the workspace menu.
Click on **Default Healthcare Settings**. The Default Healthcare Settings form appears.

![](../../../../Resources/Images/Agentic%20Healthcare/default%20settings%20form.png)

Here you can:

- Guide patients through a logical selection process—Department, Specialty, Provider, and Service—to ensure they are booked with the correct professional.
  In the General section of the form, turn on the **Enable Medical Guidance** toggle.
- Enter the number of days before the appointment when the system should send the automated confirmation email to the patient (set the value in the **Days Before Confirmation Message Is Sent** field).
- In the **Default Email** field, enter the sender email address used to send notifications. Enter the email address that will appear as the sender when the system emails patients.
{% hint style="warning" %}
**IMPORTANT!** This mandatory field determines the display sender address when emailing patients. Notification emails will fail until a sender address is configured.
{% endhint %}

- Enable patients to auto-confirm their appointment.
  Enter the URL of the landing page where the Druid Webchat is hosted. The system uses this link in confirmation emails so patients can confirm their appointment. If you leave this field empty, the email is sent as a reminder only and does not include the confirmation option. For information on how to embed Druid web chat within your website, [Deploy the WebChat Snippet](../../../../Channels/WebChat/WebChat.md#Deploy).
- Decide which fields are mandatory when creating a new full patient account. In the Account Creation section on the form, click one by one the mandatory fields and turn on the **IsEnabled** toggle.

![](../../../../Resources/Images/Agentic%20Healthcare/mandatory%20field.png)

<a id="Step7Scheduleautomatedalerts"></a>

### Step 7. Schedule automated alerts

The Healthcare Agentic Solution relies on background triggers to manage time-sensitive tasks such as appointment reminders and flagging missed visits as "No Show". These triggers ensure that the solution intelligence remains accurate without manual intervention.

There are two pre-configured alerts available, which require scheduling to run on a defined cadence:

| Alert | Purpose |
| --- | --- |
| send-appointment-confirmation-alert | Sends automated email or push notifications to patients ahead of their appointment, based on the **Days Before Confirmation Message Is Sent** setting defined in Healthcare Settings ([Step 6](#Step_6)). |
| alert-mark-past-appointments-no-show | Scans for past appointments that were not marked as **Completed** and automatically updates their status to **No Show**. |

To see the two alerts, go to **Solution Content** > **Flows** and select **Alerts** category.

![](../../../../Resources/Images/Agentic%20Healthcare/alerts.png)

To define when and how often an alert runs, follow these steps:

1. Click on the alert flow.
2. Click the **Info** action to access the flow information.
3. Click on the **Scheduling** tab, then click **Schedule**.

![](../../../../Resources/Images/Agentic%20Healthcare/schedule%20alert.png)

4. Select **Is scheduler enabled**.
5. Set the alert schedule. We recommend scheduling the alerts as follows:

| Alert | Recommended schedule |
| --- | --- |
| send-appointment-confirmation-alert | Once **daily at 9:00 AM**, to reach patients at the start of the day. |
| alert-mark-past-appointments-no-show | Once **daily at 11:00 PM**, to process the previous day's records. |

6. Save the flow.

For more information on alerts, see [Alert Flows](../../../../4_Flows/Alert%20Flows.md).

<a id="Testalerts"></a>

## Test alerts

To ensure the alert logic and data model binding are functioning correctly, trigger each alert manually immediately after the initial data provisioning. To test the alerts without waiting for the schedule. Use the following commands in the chat:

| Command | Trigger |
| --- | --- |
| sudo\_email\_alert | Use this command to manually trigger the appointment confirmation alert and send automated emails or notifications to patients. |
| sudo\_status\_alert | Use this command to manually trigger the status maintenance logic, which scans for past appointments and updates them to "No Show." |

<a id="InteractwiththeAIAgent"></a>

## Interact with the AI Agent

To begin, initiate a conversation with the AI Agent using natural language. The AI Agent understands intent and will guide you through the necessary steps based on your request

| Patient intent | Example Utterance | Process |
| --- | --- | --- |
| New appointment | I want to make an appointment to cardiology | Appointment creation process |
| Schedule changes | Can I reschedule my visit for next Tuesday | Appointment modification |
| Account history review | I want to check my past appointments. | My Account |
