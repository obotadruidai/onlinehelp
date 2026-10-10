---
layout:
  title:
    visible: false
---

<a id="TalkdeskLiveChat"></a>

# Talkdesk Live Chat

Integrating Talkdesk as a live chat provider allows your AI Agent to handle initial customer inquiries and, when necessary, transfer the conversation to a human agent within the Talkdesk contact center. This integration ensures that agents have access to chat transcripts and customer context, enabling a more personalized and efficient support experience.

> **NOTE:** Talkdesk Live Chat integration is available in Druid version 9.13 and higher.

<a id="Prerequisites"></a>

## Prerequisites

- You must have an active Talkdesk account with the Digital Connect solution installed.
- Ensure you have the necessary administrative permissions in Talkdesk to generate OAuth credentials and access Touchpoint IDs.
- You have built and published a AI Agent ready for deployment.

<a id="Configuringtheintegration"></a>

## Configuring the integration

This section provides instructions for integrating AI Agents with Talkdesk.

<a id="Step1CreateOAuthClientinTalkdesk"></a>

### <a id="Step_1"></a>Step 1. Create OAuth Client in Talkdesk

In Talkdesk, create an OAuth Client:

1. Go to **Builder** > **OAuth Clients**.
2. Create an OAuth client with the following scopes:

| Scope | Description |
| --- | --- |
| digital-connect:read | Required to read digital engagement data. |
| digital-connect:write | Required to send messages and manage sessions. |
| attachments:download | Required to download file attachments.  Supported in Druid 9.19 and higher for file transfer between users and agents. |
| attachments:read | Required to read file attachment metadata.  Supported in Druid 9.19 and higher for file transfer between users and agents. |
| attachments:request | Required to request file attachment uploads.  Supported in Druid 9.19 and higher for file transfer between users and agents. |
| attachments:write | Required to upload and send file attachments.  Supported in Druid 9.19 and higher for file transfer between users and agents. |

3. Copy the **Client ID** and **Client Secret** as you will need them in the Druid Portal.

![](../Resources/Images/Talkdesk/create%20oauth%20client.png)

<a id="Step2CreatenewTouchpoint"></a>

### <a id="Step_2"></a>Step 2. Create new Touchpoint

To create a new touchpoint for Druid integration, follow these steps in Talkdesk:

1. Go to **Admin** > **Channels** and click **Digital Connect**.

![](../Resources/Images/Talkdesk/digital%20connect.png)

2. Click **Create touchpoint**.

![](../Resources/Images/Talkdesk/create%20touchpoint.png)

3. Enter the mandatory details and save it.
4. Click on the touchpoint you created and copy the **Touchpoint ID** as you will need in the Druid Portal.

![](../Resources/Images/Talkdesk/touchpoint%20id.png)

<a id="Step3ConfigureTalkdeskintheDruidPortal"></a>

### Step 3. Configure Talkdesk in the Druid Portal

Go to AI Agent details page and click the **Live Chat** section header. The section expands.

Set the fields as described in the table below:

| Field | Description |
| --- | --- |
| Live chat provider | Select **Talkdesk**. |
| API Url | Enter your Talkdesk API URL (the url you use to access your talkkdesk account). |
| Client Id | Enter the OAuth Client credentials you copied at [Step 1. Create OAuth Client in Talkdesk](#Step_1). |
| Client Secret |  |
| Touchpoint ID | Enter the value you copied at [Step 2. Create new Touchpoint](#Step_2). |

Click **Save & Close**.

Go to the AI Agent details again, click the **Live Chat** section and copy the **Druid url (webhook)**. You’ll need this URL when creating a custom integration in Talkdesk.

![](../Resources/Images/Talkdesk/webhook%20url.png)

Configure the Live Chat special flows as needed.

<a id="Step4CreateacustomTalkdeskintegration"></a>

### Step 4. Create a custom Talkdesk integration

To create a custom integration, perform the following steps in Talkdesk:

1. In Talkdesk, go to **Builder** > **Integrations** and create a custom integration as follows:
2. Enter a name and description.
3. In the **Base path** field, enter the base domain of the webhook URL you copied from the Druid Portal.

![](../Resources/Images/Talkdesk/custom%20integration.png)

4. Save the integration.
5. Click the **Actions** tab and add the following actions:

- conversation\_started
- conversation\_ended
- message\_created

![](../Resources/Images/Talkdesk/actions.png)

> **NOTE:** These actions are Lifecycle Events available in Digital Connect. Make sure to use the exact action names listed above.

<a id="EnableFileTransferforExistingTalkdeskIntegrations"></a>

## Enable File Transfer for Existing Talkdesk Integrations

If you integrated Talkdesk Live Chat in a version prior to Druid 9.19, you must edit your existing OAuth client in Talkdesk Builder and manually add these four attachment scopes to enable file transfer support between users and Talkdesk agents:

- attachments:download
- attachments:read
- attachments:request
- attachments:write

![](../Resources/Images/Talkdesk/attachment%20scopes.png)

<a id="SendtheconversationtranscripttoTalkdeskAgents"></a>

## Send the conversation transcript to Talkdesk Agents

To save the conversation transcript and make it available for Talkdesk agents, on the flow that connects the client with the agent, make the following settings:

1. On the step where you call the internal action **ConnectToHelpdeskAgent**(Post Actions section), in the **Pre Actions** section, call the internal action **GetConversationTranscript**.
> **IMPORTANT!**  When calling the **GetConversationTranscript** internal action on the same step where you call **ConnectToHelpdeskAgent**, make sure to call it in the PreActions section. Calling it in the PostActions section will not send the conversation transcript to agents.

> **Info:**  You can call the **GetConversationTranscript** internal action on a previous step.

2. On the **ConnectToHelpdeskAgent** internal action add the following:

```
{
  "SendConversationTranscript": true
}
```

> **Info:** You can send additional client information to Talkdesk Agents together with the conversation transcript. For more information, see [Send Contact Center Parameters](#Send_Contact_Center_Parameters).

3. Save the step.

<a id="SendContactCenterParameters"></a>

## <a id="Send_Contact_Center_Parameters"></a>Send Contact Center Parameters

The table below lists the Contact Center parameters authors can send to Talkdesk.

| Parameter | Data Type | Description |
| --- | --- | --- |
| Email | String | The client's email. |
| Phone | String | The client's phone number. |

To send Contact Center parameters to Talkdesk, on the **ConnectToHelpdeskAgent** internal action, provide the desired parameters inside the `ContactCenterParameters` object in JSON format.

> **NOTE:** The payload must follow a key-value format where both the key and value are strings. When using values from DRUID conversation context (entities, local variables) as parameter values, ensure they are enclosed in double quotes ("") to maintain valid JSON formatting.

**Example - Send Contact Center parameters**

```
{
     "SendConversationTranscript":true,
     "ContactCenterParameters":
        {
                "emailAddress": "[[ChatUser]].Email",
                "phone": "[[ChatUser]].Phone"
        }
}
```
