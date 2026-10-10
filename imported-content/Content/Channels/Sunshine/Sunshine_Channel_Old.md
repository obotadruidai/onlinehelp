---
layout:
  title:
    visible: false
---

<a id="SunshineOldSunshineConversationsapps"></a>

# Sunshine (Old Sunshine Conversations apps)

The Druid Portal allows you to create the AI Agent once and deploy it to Sunshine Conversations apps in the WhatsApp channel.

This section describes how to integrate a AI Agent with old Sunshine Conversations app for WhatsApp in a sandbox environment.

**Prerequisites**:

- You built and published an AI Agent.
- You have an account on [Sunshine Conversations platform](https://app.smooch.io/login). If you haven't got one, create it.
- For DRUID on premise deployments, make sure that you provide access to/from the necessary messaging endpoints as follows:

|  |  |
| --- | --- |
| Outbound | See details here: [https://docs.smooch.io/guide/regions/](https://docs.smooch.io/guide/regions/). |
| Inbound | DRUID.BotApp |

<a id="Step1CreateSunshineConversationApp"></a>

## Step 1. Create Sunshine Conversation App

1. Log into Sunshine Conversations platform and click the **Create new Sunshine Conversations** app button.

![](../../Resources/Images/Sunshine/create%20app.png)

2. Enter the name of the Sunshine Conversations app and click the **Create App** button.

![](../../Resources/Images/Sunshine/create%20sunshine%20app.png)

Your app overview page appears.

3. Click the **Connect channels** button.

![](../../Resources/Images/Sunshine/click%20connect%20channel.png)

The Integrations page appears.

![](../../Resources/Images/Sunshine/integrations.png)

> **NOTE:** While Sunshine Conversations allows integrations with multiple applications, Druid currently supports only the integration via the WhatsApp channel.

4. Click **WhatsApp**. The WhatsApp channel integration page appears.
5. Click the **Connect** button.

![](../../Resources/Images/Sunshine/connect.png)

The WhatsApp integration mode page appears.

![](../../Resources/Images/Sunshine/integration%20mode.png)

> **Info:** If you want to activate the channel in a production environment, click the **Production** tab and follow the on-screen instructions.

6. Click **Activate Sandbox**. The Sandbox Settings appear on the page.

![](../../Resources/Images/Sunshine/sandbox%20settings.png)

7. Join the Sandbox by either sending 'modern mockingbird' to +1 (438) 476-3261 in WhatsApp or by scanning the QR code provided on the screen. After you successfully scan the QR code and send the message, your phone number appears in the Sandbox Settings section.

![](../../Resources/Images/Sunshine/phone%20number.png)

<a id="Step2EnableWebhooks"></a>

## Step 2: Enable Webhooks

> **Info:** Before enabling a webhook in Sunshine, go to Druid Portal, select the AI Agent, go to the Sunshine channel and copy the **Webhook Inbound URL**, you will need it in Sunshine.
>
> ![](../../Resources/Images/Sunshine/webhook%20inbound%20url.png)

To enable the AI Agent webhook in Sunshine Conversations platform, follow these steps:

1. At the top of the page, click the **Integrations** tab.
2. Scroll down to the API & Webhooks section and click **Webhooks**. The Webhooks page appears.
3. Click the **Connect** button on the left.

![](../../Resources/Images/Sunshine/connect%20webhooks.png)

4. Click the **Create a webhook** button.

![](../../Resources/Images/Sunshine/create%20webhook%20page.png)

The Create a webhook page appears.

5. In the **Webhook URL** field, paste the **Webhook Inbound URL** you copied from Druid.
6. Tick **Conversation message** as **Basic Triggers** and click the **Create webhook** button.

![](../../Resources/Images/Sunshine/create%20a%20webhook.png)

A webhook is created for the target Druid Webhook Inbound URL.

![](../../Resources/Images/Sunshine/target%20webhook.png)

<a id="Step3GetwebhookandappdetailsfromSunshineConversations"></a>

## Step 3. Get webhook and app details from Sunshine Conversations

From the Webhooks page, copy the value of the Secret.

![](../../Resources/Images/Sunshine/webhook%20secret.png)

At the top of the page, click the **Settings** tab. Create new API Key. Copy the **App ID**, the API key **ID** and **Secret**.

![](../../Resources/Images/Sunshine/APP%20DETAILS.png)

<a id="Step4ActivatetheSunshinechannelinDruid"></a>

## Step 4. Activate the Sunshine channel in Druid

1. Log in the Druid Portal and from the main menu, select your AI Agent. The AI Agent configuration page appears by default on the **Details** tab.
2. Click the **Channels** tab, then click **Sunshine Platform (by Zendesk)**. The Sunshine Platform (by Zendesk) Info section expands.
3. Enter the **App ID**, Webhook Secret, the API key ID and Secret you copied in the Sunshine Conversations platform and in the **Sunshine URL** field, enter [https://app.smooch.io](https://app.smooch.io/).
4. Click the **Publish** button. The channel activation might take up to 1 minute.

![](../../Resources/Images/Sunshine/configure%20druid%20bot.png)

After the channel’s activation, the following fields are available in DRUID:

- **[[ChatUser]].ChannelId** = "zendesk"
- **[[ChatUser]].UserId** - Stores the unique identifier of the Sunshine user account.

<a id="Step5TalktoyourAIAgent"></a>

## Step 5. Talk to your AI Agent

You can talk to the AI Agent in WhatsApp by sending messages to the phone number associated with the WhatsApp channel in the Sunshine Conversations Platform (the one in WhatsApp settings).

![](../../Resources/Images/Sunshine/talk%20phone.png)
