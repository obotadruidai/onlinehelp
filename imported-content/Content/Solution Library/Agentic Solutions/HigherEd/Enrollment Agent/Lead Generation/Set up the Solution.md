---
title: Set up the Solution
---

# Set up the Solution

This section will walk you through the steps to import and configure the solution to ensure a smooth setup and operation.

### Mandatory Prerequisites

* Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
* You should have a published AI Agent. For information on how to create an AI Agent, see   [Creating AI Agents](<../../../../../2_AI Agents/Creating AI Agents.md>).
* The Audiocodes channel configured for your AI Agent. For setup instructions, see [Voice AudioCodes Channel](<../../../../../Channels/Voice Audio Codes/Voice Audio Codes Channel.md>).

### Optional Prerequisites

* The Twilio SMS channel configured for your AI Agent. For setup instructions, see [Twilio SMS](../../../../../Channels/Twillio/TwilioSMS_Channel.md).
* The Vonage WhatsApp channel configured for your AI Agent. For setup instructions, see [WhatsApp Integration](<../../../../../Channels/WhatsApp Integration/WhatsApp Integration.md>).
* A dedicated web page that hosts the WebChat snippet for the Direct Line channel.

### Installation and setup procedure

To configure the solution, follow these steps:

#### Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution **Enrollment Agent - Lead Generation Skill** and import it following the instructions provided in section [Installing Solution Templates](<../../../../Installing Solution Templates.md>).

Wait until the import status shows as “Success”.

#### Step 2. Set up the AI Agent special flows

Go to the AI Agent settings, Details page and click on **Dialog management**. The section expands. Select the following special flows:

| Special Flow              | Select                          |
| ------------------------- | ------------------------------- |
| Welcome flow              | welcome-with-outbound-campaigns |
| Voice call terminate flow | early-voice-termination         |

Scroll down and click **Save & Close**.

#### Step 3. Configure the app connection

Go to solution **Apps** and configure the following connections with your credentials:

| App              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Setup required                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Audiocodes       | Used for outbound voice calls. Enter your Audiocodes token as key value and botId in the Variables table. ![](<../../../../../../.gitbook/assets/Set up the Solution.png>) You must also configure the request body for the REST integration used for AudioCodes integration: 1. Go to **Integrations**. 2. Search for **campaign-send-activities-outbound**, then click it. 3. Select the **outbound-call** Connector step, and then click the **Request** tab. 4. In the **Body template** field, provide values for the following properties: - **caller** – The phone number from AudioCodes associated with your AI Agent. - **callerDisplayName** – The friendly display name shown to the call recipient. ![](<../../../../../../.gitbook/assets/Set up the Solution_1.png>) For information on how to configure the Audiocodes channel , see [Voice AudioCodes Channel](<../../../../../Channels/Voice Audio Codes/Voice Audio Codes Channel.md>).                                                                                                                                                                                                                                                                                                                                                                                                | Mandatory                                        |
| DRUID.LLM.GPT4.1 | Configure this app using one of the following options: - **Druid-dedicated LLM resources**. Retrieve the required details from **Administration** > **Druid Services**. **NOTE:**  If the DRUID.LLM resource does not appear, contact your sales representative to activate Druid-dedicated resources for one of the following providers on your tenant: Azure OpenAI, Mistral, or Google. - **Custom LLM**. Connect the app to your own LLM deployment provided by Microsoft Azure, OpenAI, or another provider that supports tools or function calling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Mandatory                                        |
| Druid\_Sendgrid  | Used to send emails to users. Enter the **SendGrid API key**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Mandatory for the Web and Email campaigns        |
| Twilio           | Used to send SMSes. In the variables table, enter Twilio values for: **AccountId**, **SID**, **key** and **BotPhoneNumber**. [\<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/twilio variables.png>](../../../../../Solution%20Library/Agentic%20Solutions/HigherEd/Enrollment%20Agent/Lead%20Generation/https:/docs.druidai.com/1385954/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/twilio%20variables.png)![](<../../../../../../.gitbook/assets/Set up the Solution_2.png>) For information on how to get these details, see[Step 2. Retrieve Twilio Account Details](../../../../../Channels/Twillio/TwilioSMS_Channel.md#Step). **NOTE:** You should also hardcode the SID in the SMS sending integration **campaign-send-activities-sms**. [\<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/hardcode sid.png>](../../../../../Solution%20Library/Agentic%20Solutions/HigherEd/Enrollment%20Agent/Lead%20Generation/https:/docs.druidai.com/1385954/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/hardcode%20sid.png)![](<../../../../../../.gitbook/assets/Set up the Solution_3.png>) For information on how to configure the Twilio SMS channel , see [Twilio SMS](../../../../../Channels/Twillio/TwilioSMS_Channel.md). | Mandatory for creating custom SMS campaigns      |
| Vonage           | Used to send messages. In the variables table, enter your WhatsApp Vonage token. [\<https://docs.druidai.com/1385954/Content/Resources/Images/Agentic Campaign Management v2/vonage token.png>](../../../../../Solution%20Library/Agentic%20Solutions/HigherEd/Enrollment%20Agent/Lead%20Generation/https:/docs.druidai.com/1385954/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/vonage%20token.png)![](<../../../../../../.gitbook/assets/Set up the Solution_4.png>) For information on how to configure the Vonage WhatsApp channel , see [WhatsApp Integration](<../../../../../Channels/WhatsApp Integration/WhatsApp Integration.md>).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Mandatory for creating custom WhatsApp campaigns |

After you configure the connections, click Publish.

#### Step 4. Import default settings

1. Select the **Lead Generation Admin** workspace.
2. Click **Campaign Settings** on the workspace menu.
3. Click the **Import Settings** button.

![](<../../../../../../.gitbook/assets/Set up the Solution_5.png>)

This automation provisions the default app settings along with four demo campaigns.

#### Step 5. Configure NLU Intent Classification with LLM

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Select **Llm** from the **Model Type** dropdown.
3. Set **Endpoint Type** to **Druid**. If you’re using your own LLM resource, select your resource instead. Then choose the Model Name.
4. Click **Set default** for both prompts to automatically fill in instructions.

![](<../../../../../../.gitbook/assets/Set up the Solution_6.png>)

5. Save and train the AI Agent.

#### Step 6. Import leads (optional)

Perform this step only if you want to load your own lead students records from Excel.

1. Select the **Campaigns & Contacts** workspace.
2. Click **Contacts** on the workspace menu. The Lead Students view displays where you can import the prospect students.
3. Click the **Import Leads** button available on the form.

![](<../../../../../../.gitbook/assets/Set up the Solution_7.png>)

4. In the chat window that opens, choose whether to download an Excel template to fill in, or to upload the Excel file you have already prepared.

![](<../../../../../../.gitbook/assets/Set up the Solution_8.png>)

5. Wait until the success message is displayed.
6. Refresh the view to display the imported students.
