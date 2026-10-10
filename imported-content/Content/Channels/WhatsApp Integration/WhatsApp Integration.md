---
title: "WhatsApp Vonage"
---

<a id="WhatsAppVonage"></a>


To make it easy for your consumers to make purchases and get answers to questions using WhatsApp, the messaging channel they already use every day, Druid authors can integrate AI Agents with WhatsApp. This way, customers will be able to start a conversation with your AI Agent in WhatsApp.

The Druid AI Platform provides the WhatsApp channel via the integration partner Vonage.

{% hint style="info" %}
**NOTE:** The Welcome flow will be triggered at the user's first conversation with the AI Agent; the predict with the initial "user says" is dropped.
{% endhint %}

This section describes how to connect your AI Agent with your Vonage account.

<a id="Prerequisites"></a>

## Prerequisites

- You built and published an AI Agent.
- For Druid on premise deployments, make sure that you provide access to/from the necessary messaging endpoints as follows:

|  |  |
| --- | --- |
| Outbound | api.nexmo.com |
| Inbound | DRUID.BotApp  DRUID.BotApi |

<a id="Integrationprocedure"></a>

## Integration procedure

To integrate an AI Agent with your Vonage account, follow these steps:

<a id="Step1Getauthenticationdetails"></a>

### Step 1. Get authentication details

{% hint style="info" %}
**NOTE:** If a JSON Web Token (JWT) was provided to you upon Vonage account creation, you will use it to authenticate your requests; skip this step.
{% endhint %}

#### Step 1.1. Log into your Vonage Dashboard

In your browser go to [https://ui.idp.vonage.com](https://ui.idp.vonage.com/ui/auth/login?context=eyJoeWRyYUZsb3ciOiJhZDNjZTA0NjBhYzY0YWQ5YTk4Y2FlMWRhMDgzYjg0YSIsInN1YmplY3QiOiIiLCJmb3JjZUlkUCI6IiIsIm9pZGNDb250ZXh0Ijp7ImFjcl92YWx1ZXMiOm51bGwsInVpX2xvY2FsZXMiOm51bGx9LCJjbGllbnRJRCI6ImRhc2hib2FyZC1tYWluIiwicmVnaXN0cmF0aW9uRmxvdyI6IiIsImxvZ2luRmxvdyI6Ik1tV3Fwam9kN1h4V2VnRUJ2QzFqRVhmYlR4eStVWnhUdVZKcWdkbCsrNUNldlYwT2V2L3l3Nm40dU5oZDE0K09RU2JJbW1LM3VUWXo2eWxyK2U2MzZrR09ybWp6bjBwWGZDbU9NekxwT1FUT2E1UkJQcjBjUTBvVDc0T1c5NEZqIiwiYWRkcmVzc1ZlcmlmeSI6bnVsbCwiZm9yY2VMb2dnZWRPdXQiOmZhbHNlLCJmbG93VHJhY2VJZCI6IjQ3NzI5MDQ2LTZlZGEtNDE4Yy1hN2VhLWQ2YTJkMDkxYzJiZCIsInBob25lVmVyaWZpZWQiOmZhbHNlfQ==). The Login page appears.

![](../../Resources/Images/WhatsApp%20Integration/nexmo_1.png)

Enter your Vonage Dashboard credentials (email and password) and click **Log in**.

#### <a id="Step_1.2."></a>Step 1.2. Get API key and secret

When you create a Vonage account, an API key and secret will be created for you. To get these two values, in the Vonage Dashboard, from the **BUILD & MANAGE** menu, click **API Settings**.

![](../../Resources/Images/WhatsApp%20Integration/nexmo_3.png)

Write down or copy/paste in a document the API key and API secret, you will need them to activate the WhatsApp channel in Druid.

#### <a id="Step_1.3."></a>Step 1.3. Generate JWT token for WhatsApp PROD environment using WhatsApp Messages API version v1

{% hint style="warning" %}
**IMPORTANT!** If you operate in a WhatsApp PROD environment using WhatsApp Messages API version v1, you must generate a JWT token for your Vonage application because authenticating using the API Key and secret is not working.
{% endhint %}

To generate a JWT token, follow these steps:

1. Access [https://developer.vonage.com/en/jwt](https://developer.vonage.com/en/jwt).
2. Provide the following parameters:

- Your application's private key (copy it from the downloaded file during application creation).
- The application\_id.
- **Valid For** field: Enter or select the duration for which the JWT token will be valid.

![](../../Resources/Images/druid%205.29/jwt%20token.png)

<a id="Step2ActivatetheWhatsAppchannelinDruidPortal"></a>

### <a id="Step_2.whatsapp"></a>Step 2. Activate the WhatsApp channel in Druid Portal

1. In the Druid Portal go to your AI Agent settings.
2. Click the **Channels** tab, then search for **WhatsApp** and click on the **WhatsApp by Vonage** card.

![](../../Resources/Images/WhatsApp%20Integration/vonage%20channel.png)

3. In the **WhatsappNumber** field, enter the phone number associated with your Vonage account, without the “+”. To get the number, in the Vonage Dashboard, from the **TROUBLESHOOT & LEARN** > **Developer Tools** menu, click **Messages Sandbox**. Click the WhatsApp channel and copy the phone number.

![](../../Resources/Images/WhatsApp%20Integration/nexmo_4.png)

4. In the **URL** field, enter the URL from your Vonage Dashboard:

- For Vonage production environments use https://api.nexmo.com/v1/messages
- For Vonage sandbox environments use https://messages-sandbox.nexmo.com/v1/messages

![](../../Resources/Images/WhatsApp%20Integration/nexmo_5.png)

5. Based on your Vonage account authentication method, select the **Authentication Type** and enter the required information as follows:

- If you have a JWT from Vonage, select **JWT Token** and in the **JWT Token** field, enter the JWT provided to you by Vonage.

![](../../Resources/Images/WhatsApp%20Integration/jwt.png)

- If you operate in a WhatsApp PROD environment using WhatsApp Messages API version v1, select **JWT Token**, and enter the generated token ([Step 1.3](#Step_1.3.).) into the **VonageWhatsappJwtToken** field.
- If you have an API key and secret, select **API Key & API Secret** and in the two fields which appear enter the API key and secret you got at [Step 1.2](#Step_1.2.).

![](../../Resources/Images/WhatsApp%20Integration/basic%20auth.png)

6. Optionally, customize channel display settings as follows:

- **Alias**: Enter a clear, business-friendly display name (e.g., Interactive Messaging). This value is stored in**[[ChatUser]].ChannelDisplayName**, which appears in reporting tools like AI Agent Summary dashboard - Engagement KPIs and can also be referenced in flow business logic.
- **Description**: Enter a brief description. This is particularly helpful when using an alias, as it helps identify the channel's specific purpose within the Druid Portal.
- **Channel Icon**: Upload a custom icon to display on the channel card within the Druid Portal.

7. Click **Publish** to activate the channel. The channel activation might take up to 1 minute.
8. When the channel activation completes, <a id="the_Inbound_URL_and_Status_URL"></a>the **Inbound URL** and **Status URL** fields are automatically filled in. Copy the two values, you will need them at Step 3.

![](../../Resources/Images/WhatsApp%20Integration/inbound%20urls.png)

9. Click **Save & Close** to save the WhatsApp channel configuration.

After the channel activates, the following fields are available in Druid:

- **[[ChatUser]].ChannelId** = "nexmo-whatsapp"
- **[[ChatUser]].UserId** - Stores the user's phone number.
- **[[ChatUser]].ChannelDisplayName** - Stores the Alias which is used in AI Agent Summary Dashboard > Engagement KPIs > Channel chart.
- **[[ChatUser]].ChannelBotIdentifier** - Stores the AI Agent number through which a user message arrived.
- **[[HelpdeskClient]].PhoneNumber** - Stores the user's phone number if the user engages with a helpdesk agent in a live chat. It will enable the agents to send WhatsApp Message Templates.

<a id="Step3SetupyourVonageaccount"></a>

### Step 3. Set up your Vonage account

In the Vonage Dashboard, from the **TROUBLESHOOT & LEARN** menu, click **Messages Sandbox**.

From the **Message API version** drop-down, select the desired version.

{% hint style="info" %}
**NOTE:** Use the WhatsApp Messages API version v1 to render interactive messages. This way you provide a better end-user experience and streamline the interactions with your clients / users, which can lead to better engagement and response rates. Interactive messages provide users with a simplified way to make a selection from multiple options or from a menu.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** If you're changing the Message API Version for a AI Agent that has the WhatsApp Channel activated, you should provide the new **URL** in Druid channel configuration (see [Step 2](#Step_2.whatsapp)); otherwise, the AI Agent will NOT respond to users chatting in the WhatsApp channel.
{% endhint %}

![](../../Resources/Images/WhatsApp%20Integration/select%20message%20version.png)

In the Webhooks section, enter the Druid endpoints copied at [Step 2](#the_Inbound_URL_and_Status_URL) and click the **Save webhooks** button.

![](../../Resources/Images/WhatsApp%20Integration/nexmo_2.png)

You can now test the WhatsApp channel.

<a id="Step4AssociatemultiplephonenumberstothesameAIAgentoptional"></a>

### Step 4. Associate multiple phone numbers to the same AI Agent (optional)

{% hint style="info" %}
**NOTE:** AI Agent support for multiple phone numbers is available in DRUID 8.3 and higher.
{% endhint %}

Prerequisite: You need to have multiple accounts, each with an unique WhatsApp number. For more information on managing WhatsApp numbers, see [Vonage documentation](https://developer.vonage.com/en/messages/concepts/whatsapp?source=messages), section “WhatsApp Number Hosting”.

To associate multiple WhatsApp phone numbers to the same Vonage application, in Vonage developer portal, on the **BUILD & MANAGE** menu, click **Applications** and select the application you connected to the AI Agent. Click on the **Link external accounts** tab and link the desired accounts.

<a id="Step5Testtheintegration"></a>

### Step 5. Test the integration

You have two options to test the integration:

#### From Druid

To open the AI Agent in WhatsApp, in the Druid Portal, go to the AI Agent settings, click the **Channels** tab search for **WhatsApp by Vonage** and click on the card. In the modal clcik the channel icon on the left top. You can start talking to the AI Agent.

<a id="FromVonage"></a>

### From Vonage

Return to Vonage Dashboard and click the WhatsApp link.

![](../../Resources/Images/WhatsApp%20Integration/whatsapp%20link.png)

Follow the Web WhatsApp and send the passphrase message filled in automatically for you in the input area.

![](../../Resources/Images/WhatsApp%20Integration/whatsapp%20test_480x452.png)

You are now connected with your AI Agent in the WhatsApp channel.

{% hint style="info" %}
**NOTE:** When a user initiates a conversation with the AI Agent, the Welcome flow will be automatically triggered. Regardless of the user's subscription status to the AI Agent channel, the welcome message will be promptly sent to the user, ensuring a seamless and engaging interaction experience.
{% endhint %}

{% hint style="info" %}
**NOTE:** If the same chat user sends messages to multiple phone numbers associated to the same AI Agent, different conversation IDs will be generated for each phone number. This ensures that each ChannelBotIdentifier corresponds to a unique ConversationId.
{% endhint %}

<a id="Receivingandprocessingvoicemessages"></a>

## Receiving and processing voice messages

Druid supports audio messages only through Microsoft Cognitive Services and ElevenLabs. For Microsoft Cognitive Services, it supports all languages available in the Azure Speech Service. For a complete list of supported languages, refer to [Language and Voice Support for the Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#supported-languages).

Here's how it works:

1. Receive audio messages. When a user sends an audio message via WhatsApp, the AI Agent will:

- Process the audio recording using Azure Speech/ElevenLabs resources configured in the channel settings.
- Recognize the language for Speech-To-Text (STT) based on the user's language ([[ChatUser]].Language).
- Log in the Conversation History the user message type as 'Audio Recording'.

2. Process audio. The AI Agent:

- Converts the audio message to text using Microsoft Cognitive Services/ElevenLabs.
- Uses the converted text to predict the next conversational step.

3. Respond. By default, the AI Agent will respond to voice messages with text. You can choose the AI Agent to reply with voice.

To enable voice messages support, follow these steps:

1. In the channel configuration page, tap on **Support voice messages**.
2. Select the Speech provider (either **Azure** or **ElevenLabs**), then enter the required details:

- For **Azure**, enter your MS Azure Speech API key and select the region.
- For **ElevanLabs**, enter your API key.

3. By default, the AI Agent replies with text. To have the AI Agent respond with voice, toggle on **Reply with voice messages**.
4. In the table, click the plus icon. A row is added to the table.
5. From the **Language** drop-down, select the AI Agent language (default or additional) and from the **Voice** drop-down, select the human-like neural or standard voice the AI Agent will use to respond to the user.
6. Click the **Save** icon displayed inline. You can add more languages and different voices per language as best suits your needs.
7. Save the channel configuration.

<a id="Limitations"></a>

## Limitations

- When using a repeater with a hero button card, only the first five buttons are rendered. Any additional buttons beyond this limit are not displayed.

## Related Topics

- [Handling Authentication](../../How%20to/Handling%20Authentication.md)
