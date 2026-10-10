---
title: "Set Up the Solution"
---

<a id="SetUptheSolution"></a>


For solution admins

<a id="Prerequisites"></a>

## Prerequisites

<a id="Mandatory"></a>

### Mandatory

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../../../2_AI%20Agents/Creating%20AI%20Agents.md).
- You should have installed and configured the [Appointment Management Agent](../Appointment%20Management%20Agent/Appointment%20Management%20Agent.md) and [Patient Billing Agent.](../Patient%20Billing%20Agent/Patient%20Billing%20Agent.md)
- A dedicated web page that hosts the WebChat snippet for the Direct Line channel.
- The Audiocodes channel configured for your AI Agent. For setup instructions, see [Voice AudioCodes Channel](../../../../Channels/Voice%20Audio%20Codes/Voice%20Audio%20Codes%20Channel.md).

<a id="Optional"></a>

### Optional

- The Twilio SMS channel configured for your AI Agent. For setup instructions, see [Twilio SMS](../../../../Channels/Twillio/TwilioSMS_Channel.md).
- The Vonage WhatsApp channel configured for your AI Agent. For setup instructions, see [WhatsApp Integration](../../../../Channels/WhatsApp%20Integration/WhatsApp%20Integration.md).

<a id="Installationandsetupprocedure"></a>

## Installation and setup procedure

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

1. Go to the **Solutions Library**.

2. Search for **Outbound Patient Engagement Agent**.

3. Import the solution following the instructions provided in section [Installing Solution Templates](../../../../Working%20with%20Solutions/Importing%20Solutions.md).

Wait until the import status shows **Success**.

<a id="Step2SetuptheAIAgentspecialflows"></a>

### Step 2. Set up the AI Agent special flows

Go to the AI Agent settings, Details page and click the **Dialog management** section header. The section expands. Select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome flow | welcome-flow-with-campaigns |
| Voice call terminate flow | early-voice-termination |

Scroll down and click **Save & Close**.

<a id="Step3Configuretheappconnections"></a>

### Step 3. Configure the app connections

Navigate to **Solution Contents** > **Apps** and configure the apps as follows:

| App | Description | Setup required |
| --- | --- | --- |
| Audiocodes | Used for outbound voice calls.  Enter your Audiocodes token as key value in the Variables table.  [<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/key audiocodes.png>](<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/key audiocodes.png>)![](../../../../Resources/Images/Outbound%20Patient%20Engagement/Set%20Up%20the%20Solution_7.png)  You must also configure the request body for the REST integration used for AudioCodes integration:   1. Go to **Integrations**. 2. Search for **outbound-call** and **campaign-send-activities-outbound**, then click it. 3. Select the Connector step, and then open the **Request** tab. 4. In the **Body template** field, provide values for the following properties:  - `caller` – The phone number from AudioCodes associated with your AI Agent. - `callerDisplayName` – The friendly display name shown to the call recipient.   ![](../../../../Resources/Images/Outbound%20Patient%20Engagement/Set%20Up%20the%20Solution_8.png)   For information on how to configure the Audiocodes channel, see [Voice AudioCodes Channel](../../../../Channels/Voice%20Audio%20Codes/Voice%20Audio%20Codes%20Channel.md). | Mandatory |
| gpt-agent | Default connection using tenant credentials. No additional configuration required.  If you're using your own LLM resources, configure the endpoint and key. | Mandatory |
| DRUID-LLM-4o-mini | Configure this app using one of the following options:   - **Druid-dedicated LLM resources**. Retrieve the required details from **Administration** > **Druid Services**.  **NOTE:** If the DRUID.LLM resource does not appear, contact your sales representative to activate Druid-dedicated resources for one of the following providers on your tenant: Azure OpenAI, Mistral, or Google. - **Custom LLM**. Connect the app to your own LLM deployment provided by Microsoft Azure, OpenAI, or another provider that supports tools or function calling. | Mandatory only for creating custom campaigns |
| Druid\_Sendgrid | Used to send emails to users. Enter the **SendGrid API** key. | Mandatory only for the Web and Email channels |
| Twilio | Used to send SMSes. In the variables table, enter Twilio values for: **AccountId**, **SID**, **key** and **BotPhoneNumber**.  [<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/twilio variables.png>](<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/twilio variables.png>)![](../../../../Resources/Images/Outbound%20Patient%20Engagement/Set%20Up%20the%20Solution_9.png)  For information on how to get these details, see [Step 2. Get Twillio SMS account info](../../../../Channels/Twillio/TwilioSMS_Channel.md#Step).  You should also hardcode the SID in the SMS sending integration: **campaign-send-activities-sms**.  [<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/hardcode sid.png>](<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/hardcode sid.png>)![](../../../../Resources/Images/Outbound%20Patient%20Engagement/Set%20Up%20the%20Solution_10.png)  For information on how to configure the Twilio SMS channel, see [Twilio SMS](../../../../Channels/Twillio/TwilioSMS_Channel.md). | Mandatory only for creating custom SMS campaigns |
| Vonage | Used to send messages. In the variables table, enter your WhatsApp Vonage token.  [<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/vonage token.png>](<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/vonage token.png>)![](../../../../Resources/Images/Outbound%20Patient%20Engagement/Set%20Up%20the%20Solution_11.png)  For information on how to configure the Vonage WhatsApp channel , see [WhatsApp Integration](../../../../Channels/WhatsApp%20Integration/WhatsApp%20Integration.md). | Mandatory only for creating custom WhatsApp campaigns |

After you configure the connections, click **Publish**.

<a id="Step4Importdefaultsettings"></a>

### Step 4. Import default settings

To provision all the required information for the AI Agent, follow these steps:

1. Select the **Outbound Admin** workspace.
2. Click **Campaign Settings** on the workspace menu.
3. Click the **Import Settings** button.

![](../../../../Resources/Images/Outbound%20Patient%20Engagement/Set%20Up%20the%20Solution_12.png)

This automation provisions the default app settings along with three demo campaigns.

<a id="Step5ConfigureDemoCampaigns"></a>

### Step 5. Configure Demo Campaigns

The Outbound Patient Engagement Agent relies on background triggers to create audiences and run the campaigns automatically. These triggers ensure that the solution intelligence remains accurate without manual intervention.

There are three pre-configured alerts available, which require scheduling to run on a defined cadence:

| Alert | Purpose |
| --- | --- |
| alert\_campaign\_no\_show | Sends an outbound call to patients the day after they don’t show up to their appointment. |
| alert\_campaign\_balance\_outreach | Send an outbound call to patients with overdue invoices to inform them about their open balance. |
| alert\_campaign\_demographic\_verification | Sends an outbound call to patients one year after their last verification in order to check for any personal data changes |

To see the alerts, go to **Solution Contents** > **Flows** and select **Alerts** category.

To define when and how often an alert runs, follow these steps:

1. Click on the alert flow.
2. Click the **Info** action to access the flow information.
3. Click on the **Scheduling** tab, then click **Schedule**.

![](../../../../Resources/Images/Outbound%20Patient%20Engagement/Set%20Up%20the%20Solution_13.png)

4. Select **Is scheduler enabled**.
5. Set the alert schedule. We recommend scheduling the alerts as follows:

| Alert | Recommended schedule |
| --- | --- |
| alert\_campaign\_no\_show | Once in the morning, following the Appointment Manager no-show alert. |
| alert\_campaign\_balance\_outreach | Around 1:00 PM (adjusted for local time zone) to catch people during typical free time. |
| alert\_campaign\_demographic\_verification | Around 1:00 PM (adjusted for local time zone) to catch people during typical free time. |

6. Save the flow.

For more information on alerts, see [Alert Flows](../../../../4_Flows/Alert%20Flows.md).

> **Info:** If you want to build custom campaigns, follow the instructions provided in section [Campaign Management Agentic Solution](../../Marketing/Campaign%20Management%20Agentic%20Solution.md#Building) of the Campaign Management Agentic solution topic.
