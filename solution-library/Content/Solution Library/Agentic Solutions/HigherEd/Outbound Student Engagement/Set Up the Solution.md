---
title: Set Up the Solution
---


For solution admins

## Prerequisites

### Mandatory

* Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
* You should have an AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/creating-ai-agents).
* You should have installed and configured the [Academic Advisor Agent](<../Academic Advisor Agent.md>).
* The Audiocodes channel configured for your AI Agent. For setup instructions, see [Voice AudioCodes Channel](https://druidai.gitbook.io/druid-ai-docs/channels/voice-and-telephony/voice-audio-codes-channel).

### Optional

* The Twilio SMS channel configured for your AI Agent. For setup instructions, see [Twilio SMS](https://druidai.gitbook.io/druid-ai-docs/channels/voice-and-telephony/twiliosms_channel).
* The Vonage WhatsApp channel configured for your AI Agent. For setup instructions, see [WhatsApp Integration](https://druidai.gitbook.io/druid-ai-docs/channels/social-media-and-chat/whatsapp-integration).
* A dedicated web page that hosts the WebChat snippet for the Direct Line channel.

## Installation and setup procedure

To configure the skill template, follow these steps:

### Step 1. Install the solution from the Solutions Library

1. Go to the **Solutions Library**.
2. Search for **Outbound Student Engagement Agent**.
3. Import the solution following the instructions provided in section [Installing Solution Templates](<../../../Installing Solution Templates.md>).

Wait until the import status shows **Success**.

### Step 2. Set up the AI Agent special flows

Go to the AI Agent settings, Details page and click the Dialog management section header. The section expands. Select the following special flows:

| Special flow              | Select                          |
| ------------------------- | ------------------------------- |
| Welcome flow              | welcome-with-outbound-campaigns |
| Voice call terminate flow | early-voice-termination         |

Scroll down and click **Save & Close**.

### Step 3. Configure the app connections

Go to solution Apps and configure the following connections with your credentials:

| App               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Setup required                                                  |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Audiocodes        | Used for outbound voice calls. Enter your Audiocodes token as key value and botId in the Variables table. ![](<../../../../../.gitbook/assets/Set Up the Solution_16.png>) You must also configure the request body for the REST integration used for AudioCodes integration: 1. Go to **Integrations**. 2. Search for **outbound-call** and **campaign-send-activities-outbound**, then click it. 3. Select the Connector step, and then open the **Request** tab. 4. In the **Body template** field, provide values for the following properties: - `caller` – The phone number from AudioCodes associated with your AI Agent. - `callerDisplayName` – The friendly display name shown to the call recipient. ![](<../../../../../.gitbook/assets/Set up the Solution_1.png>) For information on how to configure the Audiocodes channel, see [Voice AudioCodes Channel](https://druidai.gitbook.io/druid-ai-docs/channels/voice-and-telephony/voice-audio-codes-channel).                                                                                                                                                                                                                                                                                                                                                                | Mandatory                                                       |
| DRUID.LLM.GPT4.1  | Configure this app using one of the following options: - **Druid-dedicated LLM resources**. Retrieve the required details from **Administration** > **Druid Services**. **NOTE:** If the DRUID.LLM resource does not appear, contact your sales representative to activate Druid-dedicated resources for one of the following providers on your tenant: Azure OpenAI, Mistral, or Google. - **Custom LLM**. Connect the app to your own LLM deployment provided by Microsoft Azure, OpenAI, or another provider that supports tools or function calling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Mandatory                                                       |
| DRUID-LLM-4o-mini | Configure this app using one of the following options: - **Druid-dedicated LLM resources**. Retrieve the required details from **Administration** > **Druid Services**. **NOTE:** If the DRUID.LLM resource does not appear, contact your sales representative to activate Druid-dedicated resources for one of the following providers on your tenant: Azure OpenAI, Mistral, or Google. - **Custom LLM**. Connect the app to your own LLM deployment provided by Microsoft Azure, OpenAI, or another provider that supports tools or function calling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Mandatory only for creating custom campaigns                    |
| Druid\_Sendgrid   | Used to send emails to users. Enter the **SendGrid API** key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Mandatory for creating campaigns for the Web and Email channels |
| Twilio            | Used to send SMSes. In the variables table, enter Twilio values for: **AccountId**, **SID**, **key** and **BotPhoneNumber**. [\<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/twilio variables.png>](../../../../Solution%20Library/Agentic%20Solutions/HigherEd/Outbound%20Student%20Engagement/https:/docs.druidai.com/1385954/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/twilio%20variables.png)![](<../../../../../.gitbook/assets/Set up the Solution_2.png>) For information on how to get these details, see [Step 2. Get Twillio SMS account info](https://druidai.gitbook.io/druid-ai-docs/channels/voice-and-telephony/twiliosms_channel#Step). You should also hardcode the SID in the SMS sending integration: **campaign-send-activities-sms**. [\<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/hardcode sid.png>](../../../../Solution%20Library/Agentic%20Solutions/HigherEd/Outbound%20Student%20Engagement/https:/docs.druidai.com/1385954/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/hardcode%20sid.png)![](<../../../../../.gitbook/assets/Set up the Solution_3.png>) For information on how to configure the Twilio SMS channel, see [Twilio SMS](https://druidai.gitbook.io/druid-ai-docs/channels/voice-and-telephony/twiliosms_channel). | Mandatory only for creating custom SMS campaigns                |
| Vonage            | Used to send messages. In the variables table, enter your WhatsApp Vonage token. [\<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/vonage token.png>](../../../../Solution%20Library/Agentic%20Solutions/HigherEd/Outbound%20Student%20Engagement/https:/docs.druidai.com/1385954/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/vonage%20token.png)![](<../../../../../.gitbook/assets/Set up the Solution_4.png>) For information on how to configure the Vonage WhatsApp channel , see [WhatsApp Integration](https://druidai.gitbook.io/druid-ai-docs/channels/social-media-and-chat/whatsapp-integration).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Mandatory only for creating custom WhatsApp campaigns           |

After you configure the connections, click **Publish**.

### Step 4. Import default settings

To provision all the required information for the AI Agent, follow these steps:

1. Select the **Outbound Admin** workspace.
2. Click **Campaign Settings** on the workspace menu.
3. Click the **Import Settings** button.

![](<../../../../../.gitbook/assets/Set Up the Solution_21.png>)

This automation provisions the default app settings along with four demo campaigns.

### Step 5. Configure NLU Intent Classification with LLM

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **Classification Model Type**.
3. Set **Endpoint Type** to **Druid**. If you’re using your own LLM resource, select your resource instead, then choose the **Model Name**.
4. Click **Set default** for both prompts to automatically fill in instructions.

![](<../../../../../.gitbook/assets/Set Up the Solution_22.png>)

5. Save and train the AI Agent.

### Step 6. Configure Campaigns

The Outbound Student Engagement Agent uses background triggers to automatically build audiences and execute campaigns, keeping the solution's intelligence up to date without any manual effort. Four pre-configured alerts are available and can be scheduled to run at a defined cadence.

| Alert                      | Purpose                                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------------------- |
| alert-no-declared-major    | Flags students who have not yet declared a major and engages them accordingly.                                  |
| alert-freshman-orientation | Identifies freshmen who need orientation guidance and initiates outreach.                                       |
| alert-student-counselling  | Initiates outreach for students who may need counselling support because of the low grades during the semester. |
| alert-counselling-followup | Triggers outreach for students who need a follow-up after a counselling session.                                |

To see the alerts, go to **Solution Contents** > **Flows** and select **Alerts** category.

To define when and how often an alert runs, follow these steps:

1. Click on the alert flow.
2. Click the **Info** action to access the flow information.
3. Click on the **Scheduling** tab, then click **Schedule**.
4. Select **Is scheduler enabled**.

![](<../../../../../.gitbook/assets/Set Up the Solution_23.png>)

5. Set the alert schedule. We recommend scheduling the alerts as follows:

| Alert                      | Recommended Schedule                                                                               |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| alert-no-declared-major    | Once a day during academic terms, targeting all students without a declared major.                 |
| alert-freshman-orientation | Once a day during the first couple of weeks of the academic year, targeting all incoming freshmen. |
| alert-counselling-followup | Once a day, targeting all students who require a follow-up session.                                |
| alert-student-counselling  | Once a day, targeting all students who require student counselling support.                        |

6. Save the flow.

For more information on alerts, see [Alert Flows](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/alert-flows).

{% hint style="info" %}
**Info:** If you want to build custom campaigns, follow the instructions provided in section [Campaign Management Agentic Solution](<../../Marketing/Campaign Management Agentic Solution.md#Building>) of the Campaign Management Agentic solution topic.
{% endhint %}
