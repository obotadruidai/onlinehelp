---
title: "Oracle B2C Live Agent Integration"
---

<a id="OracleB2CLiveAgentIntegration"></a>


You can integrate AI Agents with Oracle B2C Service Live Chat functionality, for cases when chat clients need to be transferred to helpdesk agents who use the Oracle B2C Agent functionality instead of the DRUID built-in live agent.

This section provides information on how to integrate AI Agents with Oracle Live Agents tool. It does not cover Live Chat specific configuration within the conversational flow design but it provides configuration information related to troubleshooting and sending conversation transcript to Oracle Live Chat Agents.

If you’re using DRUID on premise deployment, the Oracle integration is scalable for high loads.

For technical details about the integration solution between DRUID and Oracle Live Chat, see the specific [Oracle documentation](https://docs.oracle.com/en/cloud/saas/b2c-service/21c/cxscc/api-consumer-interactions.html).

<a id="Howtheintegrationworks"></a>

## How the integration works

![](../Resources/Images/Live%20Chat/Oracle%20Agent/image_1.png)

1. The users chat with the AI Agent.
2. If the AI Agent determines that the user wants to talk to a human, it transfers the chat session to Oracle Service Cloud Chat.
3. Oracle Service Cloud Chat routes the user request to the correct queue based on chat rules.
4. An agent who is monitoring the queue from an Oracle Agent Console accepts the live chat request and provides support to the user. The agents are not using DRUID native live agent.
5. When the live chat session ends, the chat session returns to the AI Agent.

<a id="Prerequisites"></a>

## Prerequisites

- In the Oracle B2C Service administration console, create an Oracle B2C Service Account (Staff Account) with the following settings:
- Interface Access = true

![](../Resources/Images/Live%20Chat/Oracle%20Agent/image_2.png)

- Permissions / Administration:

- Agent Browser User Interface:

- Account Authentication = true

- Public SOAP API:

- Account Authentication = true
- Session Authentication = true

![](../Resources/Images/Live%20Chat/Oracle%20Agent/image_3.png)

- Write down the username and password of the Oracle B2C Service Account, you will need them to integrate with AI Agents.
- Optionally, you might want to configure the working hours of your Live agent service.

![](../Resources/Images/Live%20Chat/Oracle%20Agent/image_4.png)

- In the [Oracle B2C Service Web Console](https://docs.oracle.com/en/cloud/saas/service/19c/index.html), you need to enable chat for the interface you’re using for AI Agent integration.

![](../Resources/Images/Live%20Chat/Oracle%20Agent/image_5.png)

- From Oracle B2C Service Configuration Assistant, get the Oracle Interface Customer Portal, you will need it to configure the AI Agent.

![](../Resources/Images/Live%20Chat/Oracle%20Agent/image_6.png)

- White list the following:

- Oracle Interface Customer Portal - the URL you got from the Oracle B2C Service Configuration Assistant.
- \*.rightnowtech.com - that provides a short lived endpoint for messaging transfer.

<a id="ConfiguringtheAIAgent"></a>

## Configuring the AI Agent

In the Druid Portal, go to the AI Agent settings and click the **LiveChatSettings** section header. The section expands and you can configure the AI Agent for Oracle B2C Service integration. From the **LiveChatProvider** field, select **Oracle B2C Service**, then configure the AI Agent for Oracle B2C Service, following the steps:

<a id="Step1ConfiguretheConnectionstringstoyourOracleB2CServiceinterface"></a>

### Step 1. Configure the Connection strings to your Oracle B2C Service interface

To configure the connection strings to your Oracle B2C Service interface, select fill in the fields provided in the table below:

| Field | Description |
| --- | --- |
| Server URL (Agent’s page base URL) | Enter the Oracle Interface Customer Portal (the one from the prerequisites). The field is mandatory. |
| **User name** and **Password** | The credentials of your Oracle service account (the one from prerequisites). The fields are mandatory. |

![](../Resources/Images/Live%20Chat/Oracle%20Agent/image_7.png)

<a id="Step2SetTimeouts"></a>

### Step 2. Set Timeouts

If similar configurations in Oracle B2C Live Chat application are intended to be used, then set the DRUID Live Chat timeouts to values higher than those in Oracle application.

| Field | Description |
| --- | --- |
| Live Chat Queue Waiting Timeout Mins | The amount of time in minutes that a client could wait until an agent accepts the incoming live chat request. When the timeout is reached, the client goes back in the AI Agent-client conversation. |
| Live Chat Conversation Idle Timeout Mins | The amount of time in minutes after which an engaged live chat conversation is automatically closed due to chat idleness (if both agent and client don’t send any message in their live chat session). |

![](../Resources/Images/Live%20Chat/Oracle%20Agent/image_8.png)

<a id="Step3SetSpecialFlows"></a>

### Step 3. Set Special Flows

| Special Flow | Description |
| --- | --- |
| LiveChatClientDisconnectedFlowId | DRUID triggers this flow in the client’s conversation, after a live chat conversation ends. You can use it to capture client’s feedback about the live chat experience. This special flow is optional. |
| LiveChatClientWaitingInQueueFlowId | DRUID triggers this flow in the client’s conversation every minute while the client is in the waiting queue. Use it to show the client’s position in the queue and estimated waiting time. As long as the client responds to any questions prompted from this flow, the client remains in the waiting queue (and the waiting queue timeout will be overridden), unless the flow configuration will take the client off the waiting queue, using the **TakeClientOffTheQueue** internal action  **IMPORTANT!** The Oracle platform sends periodic waiting queue status information towards the client; therefore, we recommend you not to set up this special flow, as the client will receive messages from both platforms, Oracle Live Chat and DRUID. |

![](../Resources/Images/Live%20Chat/Oracle%20Agent/image_9.png)

<a id="Step4SetSpecialMessages"></a>

### Step 4. Set Special Messages

You can set up specific responses triggered by special Live Chat special flows and events in which a AI Agent might reach out. You can either set the list of responses via the AI Agent Designer or set the flows to provide customized responses via the Flow Designer.

The table below provides you with the list of Live Chat messages you can customize for Oracle Live Agent integration:

| Special Message | Description |
| --- | --- |
| ConnectedToHelpdeskAgent | The default message sent to the client when an agent picks up the live conversation with the client. Use placeholder {0} to show the name of the agent, as send by the Oracle platform. |
| ConversationIdleWarningMessage | The default message sent to the client when the live chat conversation becomes idle. The time when this special message is triggered is half of the time set in LiveChatConversationIdleTimeoutMins. |
| LiveChatAgentDisconnectedFromPool | The default message sent to the agent after signing out Live Chat (who is being taken out from the available agents’ queue). |
| LiveChatAgentDisconnectedSelfConfirmation | The default message sent to the client when either the client or the agent disconnects from live chat. |
| LiveChatAgentError | The default message sent to the client when an error occurs that does not end the live chat. Use the {0} placeholder to show the error message sent by Oracle platform. |
| LiveChatAgentLeft | The default message sent to the client when one of the agents engaged in the live session leaves the conversation (when multiple agents are present in on live chat engagement). |
| LiveChatAgentLeftInformation | The default message sent to the client when the (last remaining) agent disconnects from live chat. |
| LiveChatClientDisconnectedSelfConfirmation | The default message sent to the client when either the client or the agent disconnects from live chat; if not likewise set on the special flow **LiveChatClientDisconnectedFlowId**. |
| LiveChatExpectedWaitTimeInQueue | The default message sent to the client whenever in the waiting queue (on the Oracle platform side). You can change the message to best suite your AI Agent profile. Use the placeholders {0} and {1} to display the position in queue, respectively the waiting time. |
| LiveChatNewLeadAgent | The default message sent to the client whenever a new agent becomes lead agent. Use placeholder {0} to show the name of the agent, as send by the Oracle platform. |
| LiveChatQueueWaitingTimeout | The default message sent to clients when the LiveChatQueueWaitingTimeoutMins is reached, if not likewise set on the live-chat-waiting-message-in-the-queue flow. |
| LiveChatWaitForAvailableAgent | The default message sent to clients when in the waiting queue, if not likewise set on the flow. |

<a id="Step5SavetheAIAgent"></a>

### Step 5. Save the AI Agent

<a id="OracleLiveChatTroubleshooting"></a>

## Oracle Live Chat Troubleshooting

DRUID Oracle Live Chat Agent integration enables AI Agents to place clients in the Oracle Live Chat waiting queue. As there might be situations when DRUID fails placing the client in an Oracle waiting queue or an error occurs during an ongoing conversation, you might want to show friendly messages to the user and easily troubleshoot and handle such cases.

This section provides information on how to handle DRUID and Oracle errors.

<a id="FriendlyhandlingerrorswhenconnectingclientstoOraclewaitingqueues"></a>

### Friendly handling errors when connecting clients to Oracle waiting queues

When issues occur while placing a client in the Oracle queue, DRUID offers you a mechanism to handle errors directly in the connect client to helpdesk agent flow, either by displaying a friendly error message or by trying to reconnect.

On your flow that places clients in the Oracle waiting queue, you can add two child steps to the step that calls the internal action ConnectToHelpdeskAgent, as follows:

- A step for cases when the client is successfully placed in the Oracle waiting queue. Show a message to inform the clients that they've been successfully placed in the waiting queue.
- To avoid interrupting the flow in case connection errors occur between DRUID and Oracle, add a step with the following condition: `@InternalActionResult==false.toString()`. This internal action verifies if the client was successfully placed in the Oracle waiting queue.

For troubleshooting purposes, you might want to register the error details provided by Oracle when placing the client in the Oracle waiting queue fails. As the error message and the error code exist in the conversation context, you can save [[HelpdeskClient]].ExceptionMessage and [[HelpdeskClient]].ExceptionCode in the ChatActivityData entity. To do so, in the SetVariables section, add the following two variables:

- [[ChatActivityData]].LiveChatErrorMessage -> [[HelpdeskClient]].ExceptionMessage
- [[ChatActivityData]].LiveChatErrorCode -> [[HelpdeskClient]].ExceptionCode

![](../Resources/Images/Live%20Chat/Oracle%20Agent/set%20variables.png)

You can see these errors in [ChatActivity History](../Data%20Analytics%20%26%20Insights/History%20%26%20Logs/Chat%20Activity%20Data/Chat%20Activity%20History.md).

<a id="Friendlyhandlingerrorswhileinanongoingconversation"></a>

### Friendly handling errors while in an ongoing conversation

If an error occurs while the client is in an ongoing conversation with an Oracle Live Chat agent, the default special message ReleaseErrorMessage will be displayed (AI Agent details, Special Flow).

![](../Resources/Images/Live%20Chat/Oracle%20Agent/releaseerror.png)

If you want to know if the error was caused by a DRUID technical issue (from a DRUID Live Chat session) and handle such errors in a more friendly manner, you can create a dedicated exception flow with two steps, as follows:

- A step for displaying a friendly message if the error occurs due to a Live Chat session error. For DRUID to identify such cases, add the following step condition:

`[[ChatUser]].ConversationStatus == “ContactCenterError”`

![](../Resources/Images/Live%20Chat/Oracle%20Agent/exception%20flow.png)

- Generic error message. After you create the exception flow, go to AI Agent details, click the **Special Flows** section header and from the **ExceptionFlowId** select the flow you specially designed for cases when technical errors occur during an ongoing notification.

![](../Resources/Images/Live%20Chat/Oracle%20Agent/select%20exeption%20flow.png)

<a id="SendingtheconversationtranscripttoOracleLiveChatAgents"></a>

## Sending the conversation transcript to Oracle Live Chat Agents

Most contact centers want their helpdesk agents to get the transcript of the conversation the client had with the AI Agent prior to being engaged in a live chat session.

In order to save the conversation transcript and make it available for Oracle Live Chat agents, on the flow that connects the client with the agent, make the following settings:

1. On the step where you call the internal action **ConnectToHelpdeskAgent**(Post Actions section), in the **Pre Actions** section, call the internal action **GetConversationTranscript**.
{% hint style="warning" %}
**IMPORTANT!**  When calling the **GetConversationTranscript** internal action on the same step where you call **ConnectToHelpdeskAgent**, make sure to call it in the PreActions section. Calling it in the PostActions section will not send the conversation transcript to agents.
{% endhint %}

{% hint style="info" %}
**Info:**  You can call the **GetConversationTranscript** internal action on a previous step.
{% endhint %}

2. On the **ConnectToHelpdeskAgent** internal action add the following:

```
{
  "SendConversationTranscript": true
}
```

![](../Resources/Images/Live%20Chat/Oracle%20Agent/configrue%20send%20transcript.png)

{% hint style="info" %}
**Info:** You can send additional client information (like Custom Fields) to Oracle Live Chat Agents together with the conversation transcript. For more information, see [Handling multiple queues and sending Contact Center Parameters](#Handling_multiple_queues_and_sending_Contact_Center_Parameters).
{% endhint %}

3. Save the step.

The conversation transcript is rendered in HTML format in Oracle Live Chat Agent.

![](../Resources/Images/Live%20Chat/Oracle%20Agent/html%20transcript.png)

<a id="microcontent1"></a>

<a id="HandlingmultiplequeuesandsendingContactCenterParameters"></a>

## <a id="Handling_multiple_queues_and_sending_Contact_Center_Parameters"></a>Handling multiple queues and sending Contact Center Parameters

Oracle B2C App 21C is dedicated to online shops and AI Agents hosted in these online shops collect client information, which can be useful to Oracle Agents when engaged in a live conversation with the client.

The table below lists the Contact Center Parameters authors can send to Oracle Live Chat.

| Parameter | Data Type | Description |
| --- | --- | --- |
| firstName | String | The first name of the client. |
| lastName | String | The last name of the client. |
| emailAddress | String | The email address of the client. |
| queueId | Long | The ID of the queue to which the client will be assigned.  **NOTE:**  If you have multiple queues, this is the Id of the Oracle Live Chat queue to which the client will be assigned. |
| contactId | Long | The contact ID of the client. |
| organizationId | Long | The client organization ID. |
| productId | Long | The product ID associated with the client's question. |
| categoryId | Long | The category associated with the client's question. |
| incidentId | Long | The unique identifier for an existing incident. |
| question | String | The question asked by the client. |
| auxillaryData | Map | A map of key-value pairs containing the browser, operating system, and user agent information of the end user. As the AI Agent is hosted on a website, the client chat snippet can provide the values for the auxiliary data. The following are the permitted keys:   - BROWSER - The corresponding value indicates the browser used by the end user. - OPERATING\_SYSTEM - The corresponding value indicates the operating system used by the end user. - USER\_AGENT - The corresponding value indicates the user agent of the browser used to make the HTTP request.  ```     { 	"BROWSER":"[[Entity]].Browser", 	“OPERATING_SYSTEM":"[[Entity]].OS", 	"USER_AGENT":"[[Entity]].UserAgent"       } ```   **NOTE:**  Make sure that you provide the above keys in capital letters, otherwise you’ll get a bad request error. |
| customFields | String Array | An array of custom fields passed by the client. For example:   ``` "customFields": [      "inventoryItemId":”[[Inventory]].ItemId”,      “inventoryOrgId":”[[Inventory]].OrgId”,      “prodGroupId":”[[Product]].GroupId”,      "incidentName”:"[[Incident]].Name”,      "incidentType":”[[Incident]].Type” ] ``` |

<a id="HowtosendContactCenterparameters"></a>

### How to send Contact Center parameters

On the **ConnectToHelpdeskAgent** internal action, provide the desired parameters inside the `ContactCenterParameters` object in JSON format.

{% hint style="info" %}
**NOTE:** The payload must follow a key-value format where both the key and value are strings. When using values from DRUID conversation context (entities, local variables) as parameter values, ensure they are enclosed in double quotes ("") to maintain valid JSON formatting.
{% endhint %}

**Example - Send Contact Center parameters**

```
{
     "SendConversationTranscript":true,
     "ContactCenterParameters":
            {
                "firstName":"[[Customer]].FirstName",
                "lastName":"@lastName",
                "question":"[[Customer]].Question",
                "queueId":"[[Entity]].QueueId",
                "contactId":"@contactId",
                "organizationId":"",
                "customFields":
                    [
                        "Age":"[[Entity]].Age",
                        "Location":"[[Entity]].Location",
                        "Role":"@role",
                        "IsManager":true,
                        "EmployeeId":”[[Employee]].ID”
                    ],
                "auxiliaryData":
                    {
                        "BROWSER":"[[Entity]].Browser",
                        "OPERATING_SYSTEM":"[[Entity]].OS",
                        "USER_AGENT":"[[Entity]].UserAgent"
                    }
            }
 }
```

## Related Topics

- [Internal Actions](../4_Flows/Internal%20Actions.md)
- [Post Actions](../4_Flows/Post%20Actions.md)
- [Pre Actions](../4_Flows/Pre%20Actions.md)
