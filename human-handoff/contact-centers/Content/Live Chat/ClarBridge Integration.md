---
title: "Clarabridge"
---


Clarabridge is a contact center, which acts like a proxy between DRUID and Sunshine routing the conversations between the two parties.

Agents can follow the tickets that the client has logged in and easily navigate through the conversation the client had with the AI Agent.

![](<../../.gitbook/assets/ClarBridge Integration.png>)

This section provides information on how to integrate AI Agents with Clarabridge. It does not cover Live Chat specific configuration within the conversational flow design.

### Prerequisites

* You built and published an AI Agent.
* You have a Qualtrics Connect account (Clarabridge developer account).
* You have registered an application in Clarabridge for the AI Agent integration. For information on how to register your application in ClaraBridge, see [Clarabridge documentation](https://app.engagor.com/developers/documentation/steps/).
* You have set up routing between Sunshine Conversations and Clarabridge.

## Step 1. Configure the Connection strings to your Clarabridge application

Log into your Clarabridge account and go to your application details page.

![](<../../.gitbook/assets/ClarBridge Integration_1.png>)

Copy the **Client ID** and the **Client Secret**.

Log into the Druid Portal and select your AI Agent. In the AI Agent details page, click the LiveChatSettings section header. The section expands and you can configure the AI Agent for Clarabridge integration. From the **LiveChatProvider** field, select **Clarabridge**, then configure the connection strings to your Clarabridge application, by filling in the fields provided in the table below:

| Field                   | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| ApplicationClientID     | Enter Client ID of your Clarabridge application.     |
| ApplicationClientSecret | Enter Client Secret of your Clarabridge application. |

![](<../../.gitbook/assets/ClarBridge Integration_2.png>)

Copy the **TriggerWebhook**, you will need at the next step.

## Step 2. Configure automation recipes in Clarabridge

In Clarabridge, click **Automation Recipes** on the main menu.

In the On Case Update section, add an automation recipe for cases resolution (when cases are closed). To do so, in the On Case Update section, click the **Add Automation Recipe** button. The webhook configuration page appears.

Provide a name and tick on **Enabled**. Select the Trigger “Case” when “Status was changed to” “Resolved”.

In the actions area, select action **Trigger Webhook** and enter (paste) the TriggerWebhook you copied from Druid Portal (from your AI Agent details, LiveChatSettings section).

![](<../../.gitbook/assets/ClarBridge Integration_3.png>)

Click the **Save** button at the bottom of the page.

## Step 3. Configure Sunshine integration in Clarabridge for your AI Agent

In the Druid Portal, go to the AI Agent settings, click the **Channels** tab and click on **Sunshine Platform (by Zendesk)**. The section expands. Copy the **Webhook Inbound URL**.

In Clarabridge, on the main menu click **Integrations**. At the top-right corner of the Integrations page, click **Zendesk Sunshine Conversations** button (![](<../../.gitbook/assets/ClarBridge Integration_4.png>)). A pop-up appears.

In the **AI Agent Endpoint** field, enter the **Webhook Inbound URL** you copied from DRUID.

![](<../../.gitbook/assets/ClarBridge Integration_5.png>)

Click **Save**. The webhook is created and appears in the Integrations list. A new Clarabridge application is automatically created in Sunshine.

Click the edit icon at the right side.

![](<../../.gitbook/assets/ClarBridge Integration_6.png>)

The webhook editor page appears.

Copy the **Webhook Secret**, **Api Key** and **Api Secret**, you will need them in DRUID. Clarabridge automatically generated these values when you added the webhook.

![](<../../.gitbook/assets/ClarBridge Integration_7.png>)

Continue with the next step.

## Step 4. Activate the Sunshine channel in DRUID

**Prerequisite**:

* Log into Sunshine and get / copy the **App ID** of the application that was created when you added the webhook in Clarabridge.

To activate the sunshine channel:

1. In the Druid Portal, select your AI Agent. The AI Agent configuration page appears by default on the **Details** tab.
2. Click the **Channels** tab, and then click **Sunshine Platform (by Zendesk)**. The Sunshine Platform (by Zendesk) Info section expands.
3. Enter the **App ID** you copied from Sunshine and enter the **Webhook Secret**, the **API key ID** and **API keys Secret** you copied from the Clarabridge webhook. In the Sunshine URL field, enter [https://app.smooch.io](https://app.smooch.io/).
4. Click the **Publish** button. The channel activation might take up to 1 minute.

## Step 5. Save the AI Agent

## Step 6. Import solution template Clarabridge Live Chat and configure it.

For information on how to configure the solution template, see [Clarabridge Live Chat](https://druidai.gitbook.io/druid-ai-docs/solution-library/solution-templates/live-chat/clarabridge-live-chat).
