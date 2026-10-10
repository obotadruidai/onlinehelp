---
title: "Clarabridge Live Chat"
---

<a id="ClarabridgeLiveChat"></a>


<a id="Step1SetupSunshinechannel"></a>

## Step 1. Set up Sunshine channel

If you want your clients to start the conversation from WhatsApp, and the agent to use Clarabridge portal, you need to activate your bot Sunshine channel. For information on how to activate the channel, see [ClaraBridge Integration](../../Live%20Chat/ClarBridge%20Integration.md).

<a id="Step2SetLiveChatsettings"></a>

## Step 2. Set Live Chat settings

In the **LiveChatConversationIdleTimeoutMins** field, enter the idle time limit for which a client can be idle (i.e. does not respond) in an ongoing conversation with an agent. Once the time limit is reached, the dialog times out and the client is automatically returned to bot context.

In the Special Flows section, from the **LiveChatClientDisconnectedFlowId** field, select **disconnect-client-from-clara**.

![](../../Resources/Images/Clarabridge%20Solution/Set%20up%20sunshine%20channel_1.png)

<a id="Step3ConfigureClarabridgeApps"></a>

## Step 3. Configure Clarabridge Apps

To configure the REST connector used for Clarabrodge, from Clarabridge Apps, click **Clarabridge**.

![](../../Resources/Images/Clarabridge%20Solution/Set%20up%20sunshine%20channel_2.png)

The Edit Connector page appears.

In the **Base URL** field, enter https://api.engagor.com/, from the **SecurityType** drop-down, select Custom and from the **AuthorizeRequestConnectorAction** field, select **authorize\_clara**.

![](../../Resources/Images/Clarabridge%20Solution/Set%20up%20sunshine%20channel_3.png)

In the Variables section, add the integration context variables associated to your Clarabridge account: access\_token, AccountId (your account ID) and TopicId (your topic ID).

![](../../Resources/Images/Clarabridge%20Solution/Set%20up%20sunshine%20channel_4.png)

Click **Save and Close**.
