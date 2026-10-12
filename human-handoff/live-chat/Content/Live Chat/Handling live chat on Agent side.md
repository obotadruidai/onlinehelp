---
title: Handling Live Chat on Agent Side
---


With the Live Chat Starter solution, the AI Agents will do the following on the agent side:

* [Gather client information when the agent picks up the client from the waiting queue](<Handling live chat on Agent side.md#Agent_connects_to_client>).
* [Notify the agent if connecting to a client was successful or not.](<Handling live chat on Agent side.md#Notify_the_agent_if_connecting_to_a_client_was_successful_or_not>)
* [Perform additional automation prior to actually connecting the helpdesk agent with the client](<Handling live chat on Agent side.md#Perform_additional_automations_prior_to_actually_connecting_the_helpdesk_agent_with_the_client>).
* [When an agent disconnects from live chat, capture the closing resolution activity for the live chat](<Handling live chat on Agent side.md#Disconnect_Agent>).

You can further improve the solution for example to [separate the reasons for agent disconnection](<Handling live chat on Agent side.md#Reason_for_Agent_Disconnection>) in your flow logic

## Agent connects to client <a href="#agent_connects_to_client" id="agent_connects_to_client"></a>

When an agent picks up the client live chat from the waiting queue, the flow **live-chat-client-connected** is triggered. The purpose of the flow is to gather client information to be displayed in the chat history and customize the agents’ chat page with elements which enable them to perform specific actions quickly with the click of a button.

![](<../../.gitbook/assets/agent picks up.png>)

The live-chat-client-connected flow is comprised of the following steps:

1. The AI Agent reads the client chat activity in the database.
2. The AI Agent fills in the client basic conversation ID in the helpdesk conversation history.
3. Triggers a backchannel event for erasing the client from the waiting queue.
4. Saves the name of the agent who picked up the client live chat from the waiting queue and the time when the live chat started into the database.
5. Using a backchannel event, the AI Agent adds buttons and other specific elements for agents to use while in a live chat with a client: specific client information, pause, send predefined messages, disconnect or access web views and forms.

![](<../../.gitbook/assets/multichat bot info.png>)

6. The AI Agent connects the agent with the selected user.
7. The AI Agent sends the client a message informing that the live chat session started.

You can configure the following settings:

* The elements available to agents in multi-chat when live chatting with clients. To do so, edit flow step 5 by replacing the default JavaScript code in the **Step message** field. Enter the JavaScript code to display the desired elements in multi-chat for your helpdesk agents.

![](<../../.gitbook/assets/agent elements editing.png>)

* The client information to be shown to agents. To do so, edit flow step 5, in the SetVariables section add the information you want to show to your agents.
* The message that is sent to the client when the agents picks up the client live chat from the waiting queue. Edit the flow step 7 by changing the text provided in the **Step message** field.

![](<../../.gitbook/assets/client connected message.png>)

* The live chat information to be saved to the SQL database (the agent picking up live chat, the time live chat started, etc.). To do so, edit the flow step 4 by clicking on the SetVariables section header and adding the information you want to track for later reporting purposes and for measuring helpdesk KPIs.

## Enable helpdesk agents to use web views and forms

Enabling helpdesk agents to access web views and forms is particularly useful when they need to manage records stored in [conversational business applications](https://druidai.gitbook.io/druid-ai-docs/conversational-ai-apps/conversational-ai-applications)while talking to the users (e.g., update user account details).

![](<../../.gitbook/assets/web form tab.png>)

To enable agents to access and manage specific web views or forms directly in the agent page, in the flow **live-chat-client-connected**, on the backchannel step that manages the agent's page appearance, on the flow step make sure that you include the following code:

```
<script type="text/javascript">
    // Call the function loadLeftContent() at the beginning of the JavaScript code or within  handleIframeLoad() based on your needs
    this.loadLeftContent('left-content');

    var customButtons = [{
        'icon': "fa-info", /* fontawesome code*/
        'title': "<View/form tab title>", /*  Title to be shown when the agent hovers over the right-side tab */
        'url': "<the url of the view/form>"
    }]
    this.loadCustomButtons(customButtons)

  ...

</script>
```

## Notify the agent if connecting to a client was successful or not <a href="#notify_the_agent_if_connecting_to_a_client_was_successful_or_not" id="notify_the_agent_if_connecting_to_a_client_was_successful_or_not"></a>

After an agent picks up a client from the waiting queue, the flow **live-chat-connect-agent-to-waiting-client** is also triggered. It informs the agent if connecting in a live chat session with the client was successful or not.

![](<../../.gitbook/assets/agent connects to client.png>)

The **live-chat-connect-agent-to-waiting-client** flow is comprised of the following steps:

1. The AI Agent adds the post internal action **ConnectToHelpdeskClientMultiChat**. The result of this action is stored in the local variable **@InternalActionResult** (boolean).
2. The AI Agent verifies the result of the internal action.

* If the result is **true**, then the backend channel **HelpdeskClientConnected** is executed and a notification informs the agent that he / she has successfully connected to client \[\[HelpdeskClient]].
* If the result is **false**, then the backend channel **HelpdeskClientNotConnected** is executed and a notification informs the agent that connecting to client \[\[HelpdeskClient]] live chat failed.

{% hint style="info" %}
**NOTE:** The variable **\[\[HelpdeskClient]]** is set in the **Input mapping** field on both flow steps of type Backchannel event.
{% endhint %}

You can configure the messages sent to agents regarding the result of the **ConnectToHelpdeskClientMultiChat** internal action. To do so, click to edit the desired backchannel flow step, click the **General** section header and in the **Step message** field, replace the text with the desired message.

## Perform additional automation prior to actually connecting the helpdesk agent with the client (Optional) <a href="#perform_additional_automations_prior_to_actually_connecting_the_helpdesk_agent_with_the_client" id="perform_additional_automations_prior_to_actually_connecting_the_helpdesk_agent_with_the_client"></a>

In DRUID version 1.55 or higher, additional data is available in \[\[HelpdeskClient]] on the **ConnectToHelpdeskClientMultichat** flow. You can use this data to perform additional automation prior to actually connecting the helpdesk agent with the client (e.g., changing the agent name, salutation, etc.), based on some client information (for example client type, or client queue).

The following fields are now available in \[\[HelpdeskClient]]:

* Subject (\[\[ChatUser]].HelpdeskSubject from client conversation context)
* ClientName (\[\[ChatUser]].Name from client conversation context)
* QueueCode
* EnqueuedAt
* DruidActivityId (\[\[ChatUser]].ActivityId from client conversation context)
* TenantUserId

## Disconnect Agent <a href="#disconnect_agent" id="disconnect_agent"></a>

When agents disconnect from a live chat session with a client, the **live-chat-agent-disconnect** flow is triggered. The agents are required to capture the closing resolution activity for the live chat.

![](<../../.gitbook/assets/agent disconnect flow.png>)

The **live-chat-agent-disconnect** flow is comprised of the following steps:

1. The AI Agent ends the live chat sessions. It also uses the post internal action **ChatActivities\_EndConversation** to store into the SQL database the agent’s name and the time when the live chat ends.
2. Reads the chat closing resolution provided by the agent.
3. Triggers a backchannel event for displaying the closing resolution activity (avatar and success / warning message).
4. Displays a form to agents (by default, a menu) where they can provide the live chat resolution.
5. The AI Agent sends the agent a notification regarding the chosen resolution, sets **\[\[HelpdeskClient]].StatusClient** to "Success Completed" and ends the live chat.
6. The AI Agent triggers a backchannel event for removing the client from the agent’s live chats list. Where possible, we recommend you to replace this step ("DisableChat") with one of type Action which in the PreActions or PostActions section calls the internal action **EndLiveConversation**. This way you ensure that the chat activity is properly logged into the system. **EndLiveConversation** is an upgraded, optimized version of the former "DisableChat" BackChannel step.

You can configure the following:

* The layout of the closing resolution activity (avatar, success / warning message, etc.).
* The form shown to agents where they can provide the live chat resolution.

## Determining the Reason for Agent Disconnection in Live Chat <a href="#reason_for_agent_disconnection" id="reason_for_agent_disconnection"></a>

In the **live-chat-agent-disconnect** flow, you can identify the reason for a live chat disconnection by checking the value of **\[\[ChatUser]].ConversationStatus**. This system entity field stores the current status of a conversation or how the conversation ended. The following statuses are relevant for determining why an agent was disconnected:

* **AgentDisconnected**: This status indicates that the agent manually disconnected from the conversation by clicking the **Disconnect** button.
* **ConversationTimeOut**: This status indicates that the user was disconnected from the live chat conversation due to inactivity, as defined by the **LiveChatConversationIdleTimeoutMins** threshold set on the AI Agent.

By utilizing these statuses, you can effectively distinguish between an agent manually disconnecting and a disconnection due to inactivity. Here is an example of how you might implement this logic in your flow:

* If **\[\[ChatUser]].ConversationStatus == "AgentDisconnected"** then handle manual agent disconnection.
* If **\[\[ChatUser]].ConversationStatus == "ConversationTimeOut"** then handle disconnection due to inactivity.

## Related Topics

* [AI Agent Informational Model](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/ai-agent-informational-model)
* [Live Chat With Multiple Queues](<Live Chat Multiple Queues.md>)
* [Post Actions](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/flows/conversational-flows/flow-steps/common-flow-settings/post-actions)
* [Pre Actions](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/flows/conversational-flows/flow-steps/common-flow-settings/pre-actions)
