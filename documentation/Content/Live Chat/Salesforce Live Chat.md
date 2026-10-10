<a id="SalesforceLiveChat"></a>

# Salesforce Live Chat

Salesforce Live Chat is a native Salesforce tool that enables customer service teams to communicate in real-time with their website users.

> **NOTE:** Salesforce Live Chat is in maintenance mode and will retire on February 14, 2026. We recommend switching to Salesforce Messaging for In-App and Web (MIAW), a modern alternative that offers asynchronous, persistent conversations with your customers.

While Salesforce Live Chat is intended to handle smaller, quick issues that can easily be resolved in one interaction, you can use Salesforce Omni-Channel to handle more complex issues and thus help create a seamless connection between all of your customer service channels so your agents can easily handle chat as well as other channels like cases from emails and phones.

This section provides information on how to integrate AI Agents with Salesforce Live Chat.

<a id="Prerequisites"></a>

### Prerequisites

- You built and published an AI Agent.
- You have a Salesforce account (Service Cloud account).

<a id="Step1EnableDigitalExperienceandactivateLiveChatfeaturesinSalesforce"></a>

## Step 1. Enable Digital Experience and activate Live Chat features in Salesforce

Log into Salesforce and enable Digital Experiences and Chat Agent following the instructions provided in [Salesforce documentation](https://trailhead.salesforce.com/content/learn/projects/build-a-community-with-knowledge-and-chat/enable-live-agent-and-communities). After you finish adding the Chat Agent to the Service Console, also [enable Omni-channel](https://help.salesforce.com/s/articleView?id=sf.omnichannel_enable.htm&type=5) and activate it on the agent side ([add the Omni channel utility to the console](https://help.salesforce.com/s/articleView?id=sf.omnichannel_add_utility_to_console.htm&type=5)).

![](../Resources/Images/Salesforce%20chat/omi%20channel.png)

Now you’ve got your chat configuration ready to go; the snippet code is generated.

![](../Resources/Images/Salesforce%20chat/snippet%20code.png)

Copy the snippet code and paste it in a text editor. From the snippet code, copy the following details as you will need them to configure Live Chat in DRUID: organizationId, deploymentId, buttonId and baseLiveAgentURL.

![](../Resources/Images/Salesforce%20chat/DETAILS.png)

<a id="Step2ConfigureSalesforceLiveChatforyourAIAgent"></a>

## Step 2. Configure Salesforce Live Chat for your AI Agent

In the Druid Portal, go to the AI Agent details, click the Live Chat section header and from the **LiveChatProvider** field, select **Salesforce**.

Configure the Salesforce Live Chat as follows:

| Parameter | Description |
| --- | --- |
| Salesforce api URL | The baseLiveAgentURL you copied from the snippet code at Step 1.  **NOTE:** In DRUID 5.19 and higher, DRUID automatically updates this endpoint if Salesforce changed it without notice. |
| Salesforce API version | Salesforce API version(E.g.,56). To check your current organization API version , follow the instructions provided in [Salesforce documentation](https://help.salesforce.com/s/articleView?id=000386929&type=1). |
| Salesforce organization id | The organizationId you copied from the snippet code at Step 1. |
| Salesforce deployment id | The deploymentId you copied from the snippet code at Step 1. |
| Salesforce button id | The buttonId you copied from the snippet code at Step 1. |

In order for Live Chat events to be raised, you need to set up on the AI Agent the timeout parameters provided in the table below.

| Parameter | Description |
| --- | --- |
| LiveChatQueueWaitingTimeoutMins | The amount of time in minutes that a client could wait until an agent accepts the incoming live chat request. When the time limit is reached, the flow selected in field **LiveChatClientWaitingInQueueFlowId** is triggered. |
| LiveChatConversationIdleTimeoutMins | The idle time limit for which a client can be idle (i.e. does not respond) in an ongoing conversation with an agent. Once the time limit is reached, the dialog times out and the client is automatically returned to AI Agent context. |

From the **LiveChatClientDisconnectedFlowId** field you can select the flow you designed specifically to capture client's feedback.

![](../Resources/Images/Salesforce%20chat/live%20chat.png)

After you finish setting up Salesforce Live Chat in DRUID, you need to create a specific flow as described below.

<a id="Step3Createflow"></a>

## Step 3. Create flow

Create a flow with one step which has as Pre Action the internal action **ConnectToHelpdeskAgent**.

You can also set [[ChatUser]].Name and [[ChatUser]].HelpdeskSubject as variables that can be sent to Salesforce.

![](../Resources/Images/Salesforce%20chat/FLOW.png)

<a id="Step4Runtheflow"></a>

## Step 4. Run the flow

Make yourself an available agent in Salesforce and be in your Service Console; otherwise, you won’t see incoming chats.

![](../Resources/Images/Salesforce%20chat/available%20agent.png)

Open the chat and run the flow you created at Step 3 (entering the flow utterance in the chat).

<a id="Step5OptionalGettheEngagementIDintheconversationcontext"></a>

## Step 5. (Optional) Get the Engagement ID in the conversation context

The Salesforce-generated chat session ID (engagement ID) is particularly useful for performing additional configurations in Salesforce while the client is in the waiting queue.

To get the engagement ID in the conversation context, manually add the **[[HelpdeskClient]].ExternalEngagementId** field in the Druid Portal. This field will be automatically populated when the client is placed in the waiting queue.

> **NOTE:** This feature is available in DRUID 8.4 and higher.

<a id="SendingtheconversationtranscripttoSalesforceLiveChatAgents"></a>

## Sending the conversation transcript to Salesforce Live Chat Agents

Most contact centers want their helpdesk agents to get the transcript of the conversation the client had with the AI Agent prior to being engaged in a live chat session.

In order to save the conversation transcript and make it available for Salesforce Live Chat agents, on the flow that connects the client with the agent, make the following settings:

1. On the step where you call the internal action **ConnectToHelpdeskAgent**(Post Actions section), in the **Pre Actions** section, call the internal action **GetConversationTranscript**.
> **IMPORTANT!**  When calling the **GetConversationTranscript** internal action on the same step where you call **ConnectToHelpdeskAgent**, make sure to call it in the PreActions section. Calling it in the PostActions section will not send the conversation transcript to agents.

> **Info:**  You can call the **GetConversationTranscript** internal action on a previous step.

2. On the **ConnectToHelpdeskAgent** internal action add the following:

```
{
  "SendConversationTranscript": true
}
```

> **Info:** You can send additional client information (like Custom Fields) to Salesforce Live Chat Agents together with the conversation transcript. For more information, see [Handling multiple queues and sending Contact Center Parameters](#Handling_multiple_queues_and_sending_Contact_Center_Parameters).

3. Save the step.

<a id="SendingContactCenterParameters"></a>

## <a id="Handling_multiple_queues_and_sending_Contact_Center_Parameters"></a>Sending Contact Center Parameters

> **NOTE:** This feature is available in DRUID 8.2 and higher.

The table below lists the Contact Center Parameters authors can send to Salesforce Live Chat.

| Parameter | Data Type | Description |
| --- | --- | --- |
| buttonId | String | The ID of the button from which the chat originated. |
| language | String | The chat user’s spoken language. |
| agentId | String | The ID of the agent of a transfer-to-agent chat request. For normal chat requests, this field is null. |
| screenResolution | String | The resolution of the chat user’s computer screen. |
| userAgent | String | The chat user’s browser user agent. |
| visitorName | String | The chat user’s custom name. |
| buttonOverrides | Array of Strings | The button override is an ordered list of routing targets and overrides the buttonId, agentId, and doFallback modes. The possible options are:   - **buttonId**- Normal routing. - **agentId** - Direct-to-agent routing with no fallback. - **agentId\_buttonId** - Direct-to-agent routing with fallback to the button.   You can list one or more of these options, where the order specifies the routing target order. The second or third target is attempted only if the previous one fails. |
| prechatEntities | Array of Entity objects | The records created, searched for, or both depending on what [EntityFieldsMaps](https://developer.salesforce.com/docs/atlas.en-us.live_agent_rest.meta/live_agent_rest/live_agent_rest_data_types.htm#EntityFieldMaps) has enabled. |
| prechatDetails | Array of [CustomDetail](https://developer.salesforce.com/docs/atlas.en-us.live_agent_rest.meta/live_agent_rest/live_agent_rest_data_types.htm#CustomDetail) objects | The pre-chat information that was provided by the chat user. |

<a id="HowtosendContactCenterparameters"></a>

### How to send Contact Center parameters

On the **ConnectToHelpdeskAgent** internal action, provide the desired parameters inside the `ContactCenterParameters` object in JSON format.

> **NOTE:** Make sure to provide the parameters values as strings, when using values from DRUID conversation context (entities, local variables), using "", otherwise, the JSON object is invalid.

**Example - Send Contact Center parameters**

```
{
     "SendConversationTranscript":true,
     "ContactCenterParameters": {
       "buttonId": null,
       "language": null,
       "agentId": null,
       "screenResolution" : null,
       "userAgent":"Druid",
       "visitorName":null,
       "buttonOverrides": [ "bntid" ],
       "prechatEntities": [],
        "prechatDetails": [
            {
                "displayToAgent": true,
                "entityFieldMaps": [
                    {
                        "entityName": "[[Variable]].VariableField",
                        "fieldName": "Email",
                        "isAutoQueryable": true,
                        "isExactMatchable": true,
                        "isFastFillable": false
                    }
                ],
                "label": "E-mail Address",
                "transcriptFields": [
                    "c__EmailAddress"
                ],
                "value": "jon@example.com"
            }
        ]
    }
 }
```
