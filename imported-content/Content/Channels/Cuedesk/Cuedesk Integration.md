<a id="Cuedesk"></a>

# Cuedesk

Cuedesk is a customer service platform that supports AI Agents, live chat, and broadcasts. By integrating a Druid AI Agent with Cuedesk, you can manage user conversations within Cuedesk-supported channels, such as WhatsApp and Facebook Messenger.

> **NOTE:** You can use the Cuedesk web channel for integration. WhatsApp or Facebook Messenger is only required if your specific use case demands it.

<a id="Prerequisites"></a>

## Prerequisites

Before you begin the integration process, ensure you have the following:

- **Cuedesk Account**: A Cuedesk user account in your company's workspace with the Workspace Owner and Flow Manager roles. If you plan to manage tickets, you also need the Agent role. For more information, see the [Cue documentation](https://help.cuedesk.com/how-to-add-users-to-your-cue-workspace/).
- **Channel Setup**: The required channel (WhatsApp, Facebook Messenger, or Cuedesk web channel) must be configured in your Cuedesk workspace.

<a id="IntegratingyourAIAgentwithCuedesk"></a>

## Integrating your AI Agent with Cuedesk

To integrate the AI Agent with Cuedesk, follow these steps:

<a id="Step1CreateCuedeskAPIKeyandWebhooks"></a>

### Step 1. Create Cuedesk API Key and Webhooks

You need to create an API key (Bearer token) and two webhooks (Inbound and Outbound) in your Cuedesk workspace.

#### Create an API Key

1. Sign in to [app.cuedesk.com](http://app.cuedesk.com/).
2. On the main menu, select **Settings** > **API Keys**.
3. On the API Keys page, click **Create API key**.
4. In the pop-up, enter a descriptive name for the key and click **Create**.

![](../../Resources/Images/Cuedesk/create%20key.png)

Cuedesk generates the key (Bearer token). Copy this key; you will need it later in the Druid Portal.

![](../../Resources/Images/Cuedesk/token.png)

#### Create Inbound Webhook

This webhook sends new incoming messages from the user to the DRUID AI Agent.

1. On the **Settings** menu, click **Webhooks**.
2. Click **Create Webhook** and configure the Inbound webhook:

- **Webhook Name**: Enter a name (e.g., DRUID\_Inbound\_Messages).
- **Trigger** (dropdown): Select **New inbound message**.
- **Channel** (dropdown): Select the activated WhatsApp/Facebook Messenger channel.
- **URL**: Enter the CallBack URL for Inbound messages. To get the URL, follow these steps:

1. Log in to the Druid Portal and select your AI Agent.
2. Click the **Channels** tab.
3. Search for 'cuedesk' and click the **Cuedesk** card.

![](../../Resources/Images/Cuedesk/channels%20card.png)

4. In the channel configuration modal, under the **Inbound messages** section, copy the **CallBack URL**.

![](../../Resources/Images/Cuedesk/callbacl%20url%20inbound.png)

3. Click **Create**.
4. Click the newly created Inbound webhook and copy the secret. You will need this secret in the **Druid Portal**.

![](../../Resources/Images/Cuedesk/copy%20inbound%20secret.png)

#### Create Outbound Webhook

This webhook ensures the Druid AI Agent can send messages back to the user through Cuedesk.

1. Click **Create Webhook** again and configure the Outbound webhook:

- **Webhook Name**: Enter a name (e.g., DRUID\_Outbound\_Messages).
- **Trigger** (dropdown): Select New outbound message.
- **Channel** (dropdown): Select the activated WhatsApp/Facebook Messenger channel.
- **URL**: Enter the CallBack URL for Outbound messages. To get the URL, follow these steps:

1. Log in to the Druid Portal and select your AI Agent.
2. Click the **Channels** tab.
3. Search for 'cuedesk' and click the **Cuedesk** card.

![](../../Resources/Images/Cuedesk/channels%20card.png)

4. In the channel configuration modal, under the **Outbound messages** section, copy the **CallBack URL**.

![](../../Resources/Images/Cuedesk/outbound%20url.png)

2. Click **Create**.
3. Click the newly created Onbound webhook and copy the secret. You will need this secret in the Druid Portal.

![](../../Resources/Images/Cuedesk/copy%20inbound%20secret.png)

<a id="Step2ConfiguretheCuedeskchannelintheDruidPortal"></a>

### Step 2. Configure the Cuedesk channel in the Druid Portal

1. Log in to the Druid Portal and select your AI Agent.
2. Click the **Channels** tab.
3. Search for 'cuedesk' and click the **Cuedesk** card.

![](../../Resources/Images/Cuedesk/channels%20card.png)

4. Enter the required connection details:

- **Cuedesk API URL**: Enter **https://api.cuedesk.com/v1/messages**.
- **Bearer token**: Paste the API key you copied from the Cuedesk workspace.

![](../../Resources/Images/Cuedesk/token.png)

- **Inbound messages** > **Secret Key**: Paste the secret for the Inbound webhook

![](../../Resources/Images/Cuedesk/copy%20inbound%20secret.png)

- **Outbound messages** > **Secret Key**: Paste the secret for the Outbound webhook.

![](../../Resources/Images/Cuedesk/copy%20inbound%20secret.png)

5. Click the **Publish** button to activate the channel.

<a id="Step3CreateCuedeskFlowsforAIAgentIntegration"></a>

### Step 3. Create Cuedesk Flows for AI Agent Integration

After activating the channel, you must create two flows in your Cuedesk workspace to manage the conversation lifecycle.

#### Create New Conversation Flow

The New Conversation flow directs all new user messages to the DRUID AI Agent for handling. To create this flow:

1. Download the [New-Conversation-Sample-Flow](https://druiddocs.file.core.windows.net/docs-shares/Cuedesk/New-Conversation-Sample-Flow.txt?sv=2023-01-03&st=2024-06-24T13%3A38%3A18Z&se=2030-06-25T13%3A38%3A00Z&sr=f&sp=r&sig=%2Fnu4VdyQ8rxwyxSzGoPZCfLdy3ctu6iHUbRlilzJN18%3D). This sample flow is designed for the WhatsApp channel but you can update it for Facebook Messenger.
> **Info:** All messages received from users in the WhatsApp channel via Cue will be handled by the DRUID AI Agent. If it can't answer a question, it will use the internal action **ConnectToHelpdeskAgent** to transfer the user to Cue Live Chat, and a ticket will be created in the Cue Inbox. Once an agent closes a ticket, the user-AI Agent conversation will continue.

2. In the Cue workspace, click the **Flows** icon on the main menu.
3. On the Flows page, click **Create a flow**.
4. Provide a flow name and description, select the channel and from the **Trigger** dropdown list, select **New conversation**.

![](../../Resources/Images/Cuedesk/New%20conv.png)

5. Click **Next** to open the flow diagram.
6. Click the three dots at the top-right corner and select **Import Flow**.

![](../../Resources/Images/Cuedesk/import%20flow.png)

7. Select the 'New-Conversation-Sample-Flow' you downloaded.
8. Click on the **POST** step and in the **URL** enter the **Conversation status CallBack URL**. Get this URL from the Cuedesk channel settings, under the section Conversation status.

![](../../Resources/Images/Cuedesk/status%20url.png)

9. In the **POST** step, click the **Body** section and replace the value of the "to" property with the Channel ID of the channel you are using. To find the channel ID, on the Cuedesk workspace menu, click **Channels** and copy the channel ID for the desired channel you're using in the flow.

![](../../Resources/Images/Cuedesk/json%20to%20property.png)

> **Info:** The structure of the Request Body in the POST step matches the Body Template structure that DRUID expects, as shown in the Conversation Status section of the channel configuration.

10. Save the step.

> **NOTE:** After the user sends the first message in the WhatsApp channel, a new conversation begins. This conversation remains active for 24 hours or until the user types "end" in WhatsApp.

#### Create Live Chat Ticket Closed Flow

This flow ensures the conversation returns to the DRUID AI Agent after a live agent closes a ticket.

1. In the Cuedesk workspace, click **Create a flow**.
2. Provide a name, description, and select the channel.
3. From the **Trigger** dropdown list, select **Live chat ticket closed**.
4. Design the flow logic to notify DRUID that the agent session has ended (typically by sending a message back to the DRUID endpoint).
5. Save the flow.

<a id="AssigningticketstospecificCuedeskqueues"></a>

## Assigning tickets to specific Cuedesk queues

The AI Agent uses the internal action **ConnectToHelpdeskAgent** to transfer the user to Cue Live Chat. A ticket is created in the Cue Inbox. To assign tickets directly to a designated Cuedesk queue, use the internal action **ConnectToHelpdeskAgent** and provide the name of the desired Cuedesk queue as a string value within the **QueueCode** parameter.

<a id="ReceivingandProcessingVoiceMessages"></a>

## Receiving and Processing Voice Messages

Druid supports audio messages only through Microsoft Cognitive Services and ElevenLabs. For Microsoft Cognitive Services, it supports all languages available in the Azure Speech Service. For a complete list of supported languages, refer to [Language and Voice Support for the Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#supported-languages).

Here's how it works:

1. Receive audio messages. When a user sends an audio message via Cuedesk, the AI Agent will:

- Process the audio recording using Azure Speech resources configured in the channel settings.
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
- For **ElevenLabs**, enter your API key.

> **NOTE:** ElevenLabs is available as speech provider in DRUID 9.0 and higher.

3. By default, the AI Agent replies with text. To have the AI Agent respond with voice, turn on the **Reply with voice messages** toggle.
4. In the table, click the plus icon. A row is added to the table.
5. From the **Language** dropdown list, select the AI Agent language (default or additional) and from the **Voice** drop-down, select the human-like neural or standard voice the AI Agent will use to respond to the user.
6. Click the **Save** icon displayed inline. You can add more languages and different voices per language as best suits your needs.

![](../../Resources/Images/druid%209.0/voice%20support%20whatsapp.png)

7. If the channel has not been published yet, click **Publish**, otherwise, click **Save**.

## Related Topics

- [Internal Actions](../../4_Flows/Internal%20Actions.md)
