---
title: "Salesforce MIAW"
---


Salesforce MIAW enhances pre-chat support by identifying customer needs and accessing records before agents connect in the Service Console. It also enables real-time communication with clients directly within the Service Console.

{% hint style="info" %}
**NOTE:** Salesforce Live Chat is in maintenance mode and will retire on February 14, 2026. We recommend switching to Salesforce Messaging for In-App and Web (MIAW), a modern alternative that offers asynchronous, persistent conversations with your customers. Messaging conversation history remains in the window beyond a single interaction. With Messaging for In-App and Web, agents and customers can start and stop the conversation, then pick it back up at a later time. Customers can also message across tabs and devices without disconnecting the conversation.
{% endhint %}

{% hint style="info" %}
**NOTE:** This feature is available in DRUID version 7.17 and higher.
{% endhint %}

## Integrating AI Agents with Salesforce MIAW Live Chat

To integrate AI Agents with Salesforce MIAW Live Chat, follow these steps:

### Step 1. Prepare a Salesforce Org

1. Create a Salesforce org and set up Omni-Channel and Omni-Flow.
2. Add your messaging channel and connect to the Service Console.
3. Configure routing to ensure the right agent responds to customers.

For detailed instructions, refer to [Salesforce's documentation](https://help.salesforce.com/s/articleView?id=sf.miaw_prepare_org_1.htm\&type=5).

### Step 2. (Optional) Add User Verification

To enable secure messaging across multiple devices, set up User Verification. For detailed instructions, refer to [Salesforce documentation](https://help.salesforce.com/s/articleView?id=sf.user_verification_setup.htm\&type=5).

### Step 3. Enable Digital Experiences

Enable Digital Experiences in your Salesforce org. For guidance, see [Salesforce documentation](https://help.salesforce.com/s/articleView?id=sf.networks_enable.htm\&language=en_US\&type=5).

### Step 4. Publish and Configure a Messaging Deployment

Connect your messaging channel to a website by creating a new embedded deployment. For step-by-step instructions, refer to [Salesforce documentation](https://help.salesforce.com/s/articleView?id=sf.miaw_configure_web_deployment_1.htm\&type=5).

For mobile deployment, follow [Salesforce's mobile instructions](https://help.salesforce.com/s/articleView?id=sf.miaw_deployment_mobile.htm\&type=5).

### Step 5. Get the Deployment Snippet Code

1. From the Deployment Settings, select **Install Code Snippet**.
2. Click **Copy to Clipboard** and paste the code into a text editor.
3. Extract the following details for DRUID Live Chat configuration:

* **OrganizationId** and **Url** - for DRUID configuration.
* **DeveloperName** - for sending contact center parameters.

### Step 6. Configure Salesforce Live Chat for your AI Agent

In the Druid Portal, go to the AI Agent details, click the **Live Chat** section header and from the **LiveChatProvider** field, select **Salesforce MIAW**.

Configure the Salesforce MIAW Live Chat as follows:

| Parameter               | Description                                                                                                  | Mandatory |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ | --------- |
| Server URL              | The Url you copied from the deployment snippet code at Step 5.                                               | Yes       |
| Organization id         | The organizationId you copied from the snippet code at Step 5.                                               | Yes       |
| Deployment  name        | The name of your Embedded Service deployment, the one you provided when publishing the deployment at Step 4. | Yes       |
| Capabilities version    | Enter **1** as Druid currently supports only version 1 of capabilities.                                      | Yes       |
| Customer identity token | The token issued by the company’s identity provider, if User identification is set in Salesforce Messaging.  | No        |

In order for Live Chat events to be raised, you need to set up on the AI Agent the timeout parameters provided in the table below.

| Parameter                                | Description                                                                                                                                                                                                                             |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Live chat queue waiting timeout mins     | The amount of time in minutes that a client could wait until an agent accepts the incoming live chat request. When the time limit is reached, the flow selected in field Live chat client waiting in queue flow is triggered.           |
| Live chat conversation idle timeout mins | The idle time limit for which a client can be idle (i.e. does not respond) in an ongoing conversation with an agent. Once the time limit is reached, the dialog times out and the client is automatically returned to AI Agent context. |

From the **Live chat client disconnected flow** field you can select the flow you designed specifically to capture client's feedback.

After you finish setting up Salesforce Live Chat in DRUID, you need to create a specific flow as described below.

### Step 7. Create flow

Create a flow with a step that has as Pre Action the internal action **ConnectToHelpdeskAgent**.

You can also set **\[\[ChatUser]].Name** and **\[\[ChatUser]].HelpdeskSubject** as variables that can be sent to Salesforce MIAW.

![](<../../.gitbook/assets/Salesforce MIAW Live Chat.png>)

### Step 8. Run the flow

Set your status to "Available for Chat" in Salesforce and stay in the Service Console to receive incoming chats.

![](<../../.gitbook/assets/Salesforce MIAW Live Chat_1.png>)

Open the chat and run the flow you created at Step 7 (entering the flow utterance in the chat).

## Sending the conversation transcript to Salesforce Live Chat Agents

Most contact centers want their helpdesk agents to get the transcript of the conversation the client had with the AI Agent prior to being engaged in a live chat session.

In order to save the conversation transcript and make it available for Salesforce Live Chat agents, on the flow that connects the client with the agent, make the following settings:

1. On the step where you call the internal action **ConnectToHelpdeskAgent**(Post Actions section), in the **Pre Actions** section, call the internal action **GetConversationTranscript**.

{% hint style="warning" %}
**IMPORTANT!** When calling the **GetConversationTranscript** internal action on the same step where you call **ConnectToHelpdeskAgent**, make sure to call it in the PreActions section. Calling it in the PostActions section will not send the conversation transcript to agents.
{% endhint %}

{% hint style="info" %}
**Info:** You can call the **GetConversationTranscript** internal action on a previous step.
{% endhint %}

2. On the **ConnectToHelpdeskAgent** internal action add the following:

```
{
  "SendConversationTranscript": true
}
```

{% hint style="info" %}
**Info:** You can send additional client information (like Custom Fields) to Salesforce Live Chat Agents together with the conversation transcript.
{% endhint %}

3. Save the step.

## Sending Contact Center Parameters

You can send contact center parameters as long as they are created as pre-chat form data and mapped in the Omni-channel flow in Salesforce. For more details, refer to the Salesforce documentation: [Customize Pre-Chat for Messaging for In-App and Web](https://help.salesforce.com/s/articleView?id=sf.miaw_custom_prechat_2.htm\&type=5) and [Map Pre-Chat Values in Omni-Channel Flow](https://help.salesforce.com/s/articleView?id=sf.miaw_pre_chat_api_2.htm\&type=5).

In the **ConnectToHelpdeskAgent** internal action, in **ContactCenterParameters**, specify the routing values that will be sent to Salesforce:

**Syntax**

```
{
  "ContactCenterParameters": {
      "<key1>": "<value1>",
      "<key2>": "<value2>"
    },
   "SendConversationTranscript": true
}
```

**Example**

```
{
  "ContactCenterParameters": {
    "firstName": "[[Customer]].FirstName",
    "lastName": "[[Customer]].LastName",
    "email": [[Customer]].Email,
    "queueId": "[[Entity]].QueueId"
    },
  "SendConversationTranscript": true
}
```

{% hint style="info" %}
**NOTE:** Make sure to provide the parameters values as strings, when using values from DRUID conversation context (entities, local variables), using "", otherwise, the JSON object is invalid.
{% endhint %}

**Example - Sending Contact Center Parameters**

```
{
  "SendConversationTranscript": true,
  "ContactCenterParameters": {
    "conversationId": "00D2Q223000I0A5",
    "routingAttributes": {
      "firstName": "[[Customer]].FirstName",
      "lastName": "[[Customer]].LastName",
      "email": "[[Customer]].Email",
      "queueId": "[[Entity]].QueueId"
    },
    "esDeveloperName": "MIAW_Deployment"
  }
}
```
