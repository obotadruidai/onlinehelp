---
title: "Zendesk Sunshine"
---

<a id="ZendeskSunshine"></a>


You can deploy AI Agents across any Zendesk Sunshine-supported channels, offering greater flexibility to empower your clients and users to engage with you effectively.

> **NOTE:** Previously, Sunshine Conversations apps integration only supported [AI Agent deployment in WhatsApp](Sunshine_Channel_Old.md). However, starting with DRUID 8.9, you can deploy AI Agents across multiple Sunshine-supported channels, expanding your communication options.

<a id="Prerequisites"></a>

## Prerequisites

- You have built and published a AI Agent.
- Your Zendesk subscription is either Suite Professional or Suite Enterprise, as only these plans provide access to Sunshine Conversations.
- You have an admin account for your company's Zendesk tenant.

<a id="DeployingtheAIAgentinaZendeskSunshinesupportedchannel"></a>

## Deploying the AI Agent in a Zendesk Sunshine-supported channel

To deploy the AI Agent in a Zendesk Sunshine-supported channel, follow these steps:

<a id="Step1CreateConversationsAPI"></a>

### Step 1. Create Conversations API

1. Log into your Zendesk tenant using an admin account and go to **Admin Center**.

![](../../Resources/Images/Zendesk%20channel/admin%20center.png)

2. In the left menu, click **Apps and integrations**, and under APIs, select **Conversations API**.

![](../../Resources/Images/Zendesk%20channel/conv%20apis%20menu.png)

3. Click the **Create API key** button. Follow the wizard instructions to create a Conversations API and save it.
4. Click the actions button inline with your conversations API and select **View details**.

![](../../Resources/Images/Zendesk%20channel/conv%20api%20details%20edit.png)

5. The API details appear.

![](../../Resources/Images/Zendesk%20channel/conv%20api%20credentials.png)

6. Copy the credentials as you will need to configure the Zendesk Sunshine channel in DRUID.

![](../../Resources/Images/Zendesk%20channel/api%20credentials.png)

<a id="Step2Createwebhook"></a>

### Step 2. Create webhook

1. In the left menu, click **Apps and integrations**, and under Integrations, select **Conversations integrations**.

![](../../Resources/Images/Zendesk%20channel/conv%20inetgr.png)

2. Click the **Create integration** button. The integration creation page appears.
3. Give the integration a name to help identify it.
4. In the **Webhook endpoint URL**, enter the **WebhookInboundURL** you take from the Druid Portal, AI Agent channel Sunshine Platform (by Zendesk).
5. Select what to include in the webhook payloads.
6. Select the following webhook subscription:

- Conversation created
- Conversation message
- Switchboard pass control
- Switchboard pass control failure
- Switchboard accept control
- Switchboard accept control failure
- Switchboard offer control
- Switchboard offer control failure
- Delivery failure
- Participant joined conversation
- Participant left conversation

![](../../Resources/Images/Zendesk%20channel/cerate%20webhook.png)

7. Save the webhook. It will now appear on the Conversations Integrations page. Next, retrieve the webhook secret, as you’ll need it to configure the channel in the Druid Portal.
8. Click the actions button inline with your webhook integration and select **View details**.

![](../../Resources/Images/Zendesk%20channel/webhook%20details.png)

9. Copy the **Shared secret** that is the Webhook Secret you will configure in DRUID.

![](../../Resources/Images/Zendesk%20channel/WEBHOOK%20SECRET.png)

<a id="Step3ActivatetheSunshinePlatformByZendeskchannelinDruid"></a>

### Step 3. Activate the Sunshine Platform (By Zendesk) channel in Druid

1. In Druid Portal, go to the AI Agent **Channels**, then click **Sunshine Platform (by Zendesk)**. The channel section expands.
2. Enter the **App ID**, **API Key Id** and **API Key Secret** you copied from your Conversations API details in Zendesk.
3. In the Webhook Secret field, enter the **Shared secret** you copied from the webhook integration details in Zendesk.
4. In the **Sunshine URL** field, enter your Zendesk tenant URL adding /sc at the end: *https://Zendesk\_tenant/sc*.

![](../../Resources/Images/Zendesk%20channel/channel.png)

5. Click the **Publish** button. The channel activation might take up to 1 minute.

After the channel’s activation, the following fields are available in DRUID:

- **[[ChatUser]].ChannelId** = "zendesk"
- **[[ChatUser]].UserId** - Stores the unique identifier of the Zendesk user account.

<a id="Step4CreateZendeskchannel"></a>

### Step 4. Create Zendesk channel

This section describes how to deploy the AI Agent in Zendesk web channel:

1. Log into your Zendesk tenant using an admin account and go to **Admin Center**.
2. In the left menu, click **Channels**, and under **Messaging and social**, select **Messaging**.

![](../../Resources/Images/Zendesk%20channel/channel%20menu.png)

3. Click **Add channel** and select the **Web Widget**.

![](../../Resources/Images/Zendesk%20channel/add%20channel.png)

4. Configure the web widget based on your preferences following the on screen instructions and save it.
5. Click on the channel and in the channel configuration page, click on **Installation** and copy the widget code.

![](../../Resources/Images/Zendesk%20channel/code%20snippet.png)

6. Add the Web Widget code snippet to your website by updating the HTML of every page where you want the widget to appear. Paste the code snippet right before the closing `</body>` tag.

<a id="SendZendesksurveyratingstotheAIAgent"></a>

## Send Zendesk survey ratings to the AI Agent

> **NOTE:** This feature is available in DRUID 9.5 and higher.

When a ticket is resolved or a Zendesk agent disconnects a conversation, Zendesk can automatically send a survey asking the user to rate the interaction. You can configure Zendesk to also send these ratings to your AI Agent:

1. In Zendesk, go to **Admin Center**.
2. In the main menu, search for *Customer satisfaction*.
3. Go to **Objects and rules** > **Business rules**, and then select **Customer satisfaction**.

![](../../Resources/Images/druid%209.5/customer%20satisf.png)

4. Activate the Messaging channel.

![](../../Resources/Images/druid%209.5/activate%20messaging.png)

5. Next to the Messaging channel, select the Actions icon, and then choose **View rules**.

![](../../Resources/Images/druid%209.5/view%20rule.png)

6. In the 'Meet ALL of the following conditions' section, add the following conditions:

| Category | Operator | Value |
| --- | --- | --- |
| Ticket > Satisfaction | Is not | Offered |
| Ticket > Messaging session ended reason | Is | Ended by agent |

7. In the 'Meet ANY of the following conditions' section, add the following conditions:

| Category | Operator | Value |
| --- | --- | --- |
| Ticket > Channel | Is | Messaging |
| Ticket > Channel | Is | Sunshine Conversations API |

![](../../Resources/Images/druid%209.5/conditions.png)

8. Save the configuration.
