---
title: "Sakari SMS"
---

<a id="SakariSMS"></a>


Enable customers to start and conduct conversations with AI Agents through standard SMS text messaging via Sakari.

> **NOTE:** The Sakari SMS channel is not available in Druid on premise deployments; you cannot activate the channel.

> **IMPORTANT!** During initial user interaction, the Welcome flow triggers automatically. The intent prediction for the first user message is bypassed; the welcome message will be promptly sent to the user, ensuring a seamless and engaging interaction experience.

<a id="Prerequisites"></a>

## Prerequisites

Before configuring the Sakari SMS channel, ensure the following requirements are met:

- A paid Sakari account with an active sender (phone number) configured. For more information on how to add a sender, see the [Sakari Support Center](https://support.sakari.io/hc/en-us/articles/47404687327892-Add-Sender-Buy-Number).
> **NOTE:** When integrating Sakari with Campaign Manager, you must register for A2P 10DLC (Application-to-Person 10-Digit Long Code) messaging to send SMS campaigns to U.S. phone numbers. This registration is required by mobile carriers to reduce spam and ensure reliable message delivery. You can complete the A2P 10DLC registration directly with Sakari. For more information, see [Sakari 10DLC registration](https://support.sakari.io/hc/en-us/articles/360056853072-10DLC-FAQ).

- An active, published AI Agent built within the Druid Portal.

<a id="Integrationprocedure"></a>

## Integration procedure

To integrate an AI Agent with Sakari SMS, follow these steps:

<a id="Step1GetSakariaccountAPIdetails"></a>

### Step 1. Get Sakari account API details

1. Log in to the [Sakari Hub](https://hub.sakari.io/).
2. Navigate to **Settings** > **Account Settings**.

![](../Resources/Images/Sakari/account%20details.png)

3. Click the **API** tab and copy the **Account ID** and **Client ID**.

![](../Resources/Images/Sakari/copy%20details.png)

4. If you do not know your **Client Secret**, click **Refresh Client Secret** to generate a new one, then copy the value.
5. Securely store these details, as you will need them to configure the channel inside the Druid Portal.

<a id="Step2ActivatetheSakariSMSchannelintheDruidPortal"></a>

### Step 2. Activate the Sakari SMS channel in the Druid Portal

1. In the Druid Portal go to your AI Agent settings.
2. Click the **Channels** tab, then search for **SMS** and click on the **SMS by Sakari** card.

![](../Resources/Images/Sakari/CHANNEL%20CARD.png)

The channel configuration modal appears.

3. Enter the **Account ID**, **Client ID** and **Client Secret** retrieved from the Sakari Hub.
4. Optionally, customize channel display settings as follows:

- **Alias**: Enter a clear, business-friendly display name (e.g., Interactive Messaging). This value is stored in**[[ChatUser]].ChannelDisplayName**, which appears in reporting tools like AI Agent Summary dashboard - Engagement KPIs and can also be referenced in flow business logic.
- **Description**: Enter a brief description. This is particularly helpful when using an alias, as it helps identify the channel's specific purpose within the Druid Portal.
- **Channel Icon**: Upload a custom icon to display on the channel card within the Druid Portal.

5. Click **Publish** to activate the channel.
6. Click on the channel card again and from the modal copy the **Inbound SMS webhook** and **Delivery status webhook**.

After the channel activates, the following fields are available in Druid:

- **[[ChatUser]].ChannelId** = “sakari-sms”. It identifies the channel.
- **[[ChatUser]].Phone** – Stores the user’s phone number.
- **[[ChatUser]].CalleePhoneNumber** – Stores the AI Agent phone number.
- **[[ChatUser]].ChannelDisplayName** - Stores the Alias which is used in AI Agent Summary Dashboard > Engagement KPIs > Channel chart.

<a id="Step3ConfigurewebhooksintheSakariHub"></a>

### Step 3. Configure webhooks in the Sakari Hub

1. Navigate to **Settings** > **Account Settings**.
2. Click the **Webhooks** tab.
3. Add two webhooks as follows:

- **Message Received** and in the **Destination** field, enter the **Inbound SMS webhook** your copied from the Druid Portal.

![](../Resources/Images/Sakari/webhook%201.png)

- **Message Status** and in the **Destination** field, enter the **Delivery status webhook** your copied from the Druid Portal.

![](../Resources/Images/Sakari/webhook%202.png)
