---
layout:
  title:
    visible: false
---

<a id="VonageRCS"></a>

# Vonage RCS

Vonage RCS (Rich Communication Services) is an advanced messaging channel provided by Vonage that upgrades standard SMS with interactive features like rich cards, carousels, suggested actions, media sharing, and verified branding.

Integrating AI Agents with Vonage RCS enables businesses to deliver engaging, conversational customer experiences directly within native mobile messaging applications, improving user interaction while maintaining secure communication workflows.

> **Info:** This channel is available starting with Druid 9.28.

<a id="Prerequisites"></a>

## Prerequisites

- You built and published an AI Agent.
- You have an active Vonage account with RCS capabilities enabled.

<a id="IntegrateDruidwithVonageRCS"></a>

## Integrate Druid with Vonage RCS

To integrate Druid with Vonage RCS, follow these:

<a id="Step1GetthechannelURLsfromtheDruidPortal"></a>

### Step 1. Get the channel URLs from the Druid Portal

Go to the AI Agent details page and click on the **Channels** tab. Then, search for **RCS** and click on the card.

![](../Resources/Images/rcs/rcs%20card.png)

From the channel configuration modal, copy the **Message Webhook Url** and **Delivery status webhook**, as you’ll need them to configure your Vonage application.

![](../Resources/Images/rcs/channel%20urls.png)

<a id="Step2CreateandconfigureaVonageapplication"></a>

### Step 2. Create and configure a Vonage application

To integrate Vonage RCS with Druid, you need to configure a Vonage application. This involves adding channel URLs from the Druid Portal, and retrieving API private key. Follow the steps below to complete the setup:

1. Log in to the [Vonage Portal](https://dashboard.nexmo.com/).
2. Go to **BUILD** > **Applications**.
3. In Your applications page, click the **Create a new application** button.
4. Enter a name for your application.
5. Turn on the **Messages** toggle and enter the two URLs as follwos:

- **Inbound URL** - Enter the **Message Webhook Url** you copied from the channel configuration modal in the Druid Portal.
- **Status URL** - Enter the **Delivery status webhook** you copied from the channel configuration modal in the Druid Portal.

6. Click the **Generate new application** button to create the app.
7. Note down the **Application ID**, as you’ll need it to configure the channel in the Druid Portal.

![](../Resources/Images/rcs/app%20id.png)

8. Go back to your app configuration page ( **BUILD** menu > **Applications** > your app).
9. Generate public and private key.

![](../Resources/Images/rcs/generate%20key.png)

10. The private key is downloaded on your computer.

<a id="Step3CreateRCSAgent"></a>

### Step 3. Create RCS Agent

1. In the Vonage Portal, go to **Messaging** > **RCS Agent Builder**.
2. Click the **Build a new RCS agent** button at the top-right corner of the page.

If the **Build a new RCS agent** button is unavailable, RCS is not enabled for your account. To request access, click **Contact us to get started with RCS** and follow the on-screen instructions.

3. Configure your RCS Agent by following the Vonage setup wizard. For more information, see [Vonage instructions](https://developer.vonage.com/en/messages/guides/rcs/rcs-agent-builder-guide).
4. On Step 8 of the wizard (**Agent-application settings**), select the application you created for Druid integration from the application list to link the app to RCS messaging.

![](../Resources/Images/rcs/rcs%20agent.png)

5. Save your changes and complete the RCS Agent setup.

<a id="Step4ActivatetheVonageVoicechannelinDruid"></a>

### Step 4. Activate the Vonage Voice channel in Druid

To activate the Vonage Voice channel, follow these steps:

1. Go to the AI Agent details page and click on the **Channels** tab.
2. Search for **RCS** and click on the card.
3. In the channel configuration modal, enter the **Application ID** you copied from Vonage and the **Private Key** from the file you downloaded when generating the app private key in Vonage.
4. Optionally, customize channel display settings as follows:

- **Alias**: Enter a clear, business-friendly display name (e.g., Interactive Messaging). This value is stored in**[[ChatUser]].ChannelDisplayName**, which appears in reporting tools like AI Agent Summary dashboard - Engagement KPIs and can also be referenced in flow business logic.
- **Description**: Enter a brief description. This is particularly helpful when using an alias, as it helps identify the channel's specific purpose within the Druid Portal.
- **Channel Icon**: Upload a custom icon to display on the channel card within the Druid Portal.

5. Click the **Publish** button to activate the channel.

![](../Resources/Images/rcs/rcs%20channel.png)

After the channel’s activation, the following fields are available in Druid:

- **[[ChatUser]].ChannelId** - "vonage-rcs"
- **[[ChatUser]].UserId** - Stores the user's phone number in international format.
- **[[ChatUser]].ChannelDisplayName** - Stores the Alias which is used in AI Agent Summary Dashboard > Engagement KPIs > Channel chart.
