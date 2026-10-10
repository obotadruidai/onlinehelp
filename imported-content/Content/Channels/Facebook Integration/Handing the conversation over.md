---
title: Handing the conversation over to FB Page Inbox or to another AI Agent
---

# Handing the conversation over to FB Page Inbox or to another AI Agent

A botdeployed on Facebook will manage all conversations initiated through Facebook Messenger on the integrated Facebook Page.

By using the Facebook Handover Protocol, you can enhance the Messenger experience by allowing the AI Agent and the Page owner or administrator to share control of the conversation. This lets you seamlessly pass control between the AI Agent and the Facebook Page Inbox, enabling users to interact directly with the Page administrator when needed.

This is especially useful when you want to allow users to communicate with the Page Inbox administrator while still having a AI Agent deployed.

### Prerequisite

* You need the access token you generated when connecting the Facebook page with you app.

To handover the conversation from a AI Agent to a Facebook page Inbox or to another AI Agent:

### Step 1. Adjust your Facebook Page app webhook subscriptions

1. In Facebook Developer Portal, go to your app details.
2. On the main, click **Messenger** > **API Settings**.
3. In the **Generate access tokens** section, hover the mouse over the info icon below Webhook Subscription and click the Edit button. The Edit Page Subscriptions pop-up appears.
4. Select **messaging\_handovers** and click **Confirm**.

![](<../../../.gitbook/assets/Handing the conversation over_1.png>)

### Step 2. Assign the FB app as the Primary Receiver for your FB page

To assign the Facebook app as the Primary Receiver for your Facebook page:

1. Access the Facebook page and go to the page settings.
2. On the **Audience and visibility** menu, click **Page setup**.
3. Click the **View** button next to **Advanced Messaging**.
4. In the **App settings** - Handover Protocol sections, click the **Configure** button next to the **Messenger receiver**. A pop-up appears.

![](<../../../.gitbook/assets/Handing the conversation over_2.png>)

5. Select your Facebook app as the primary receiver for the handover protocol.

![](<../../../.gitbook/assets/Handing the conversation over_3.png>)

{% hint style="info" %}
**Info:** If you have multiple AI Agents deployed in the Facebook channel, select the Facebook app created for the specific AI Agent you want to handle conversations by default in Messenger as the primary receiver.
{% endhint %}

6. Close the pop-up.

### Step 3. Configure the integration for passing thread control

Create an integration task with a POST request to the Facebook Handover API endpoint and place the integration for passing thread control on the flow step where you do the handover.

This section provides you with the information needed to configure the integration for passing thread control.

#### Prerequisite

* Create a REST connector app, which has the [https://graph.facebook.com](https://graph.facebook.com) as **Base URL** and in the variable section has **PageAccessToken** (the access token of the Facebook page where the AI Agent was deployed).

Create a REST connector action for passing thread control and select **\[\[ChatUser]]** as Request and Response entity.

![](<../../../.gitbook/assets/Handing the conversation over_4.png>)

Create a REST integration task and configure the Request for passing thread control as described below.

Make a POST request to Facebook **pass\_thread\_control** endpoint: `/v2.6/me/pass_thread_control?access_token={access_token}`

In the **Parameters** tab, map the **access\_token** parameter to DRUID local variable **@PageAccessToken**.

![](<../../../.gitbook/assets/Handing the conversation over_5.png>)

Select **UseBodyTemplate** as RequestType and in the **BodyTemplate** field, enter the following code:

```
{
    "recipient":{"id":"{{userId}}"},
    "target_app_id":263902037430900
}
```

Set the target\_app\_id property of the request to specific value as follows:

* To handover the conversations to the Facebook Page Inbox, enter “263902037430900”
* To hand over the conversations to another AI Agent, enter the App ID of the Facebook app created for that AI Agent.

Click the **Body** tab and map the **userId** provided in the request (BodyTemplate field) to **\[\[ChatUser]].UserId**, which will store the values returned by the API call.

![](<../../../.gitbook/assets/Handing the conversation over_6.png>)

{% hint style="info" %}
**NOTE:** The conversations are handed over from the AI Agent to the Facebook Inbox page (or to another AI Agent as configured in the REST API request) for 24 hours. If the conversations are handed over from the AI Agent to the Facebook page Inbox, when the Facebook page owner marks the conversation as DONE (in the Page Inbox), it is handed back to the AI Agent.
{% endhint %}

Place the integration for passing thread control on the flow step where you do the handover.

### Step 4. (Optional) Author the AI Agent to handle the conversation hand over back to it

Whenever the conversation is handed back to the AI Agent, DRUID Platform triggers the Welcome flow and sets \[\[ChatUser]].ReturningFromFacebookHandover = true.

{% hint style="warning" %}
**IMPORTANT!** Set **\[\[ChatUser]].ReturningFromFacebookHandover** to false on the same step where you place the integration for passing thread control (to make sure that \[\[ChatUser]].ReturningFromFacebookHandover becomes true only when the conversation is returned to the AI Agent (or to clean up any older context).
{% endhint %}

You can create a dedicated branch in the Welcome flow to address the cases when you want to let the users know that they’re talking to the AI Agent again, a branch step that will be executed when \[\[ChatUser]].ReturningFromFacebookHandover = true (set condition on step).

If you don’t want to let the user know, add an empty step to the Welcome flow or simply do nothing.

{% hint style="info" %}
**NOTE:** If you handle this situation as a separate branch in the Welcome flow, perform a cleanup of **\[\[ChatUser]].ReturningFromFacebookHandover** for further accessing the Welcome flow from the conversation (from other areas than Facebook handover). To do the cleanup, make sure to set \[\[ChatUser]].ReturningFromFacebookHandover back to “false” after the branch was reached in conversation (set variable `[[ChatUser]].ReturningFromFacebookHandover = false`).
{% endhint %}
