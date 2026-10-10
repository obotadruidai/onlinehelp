---
title: "Multichat for Helpdesk Agents"
---

<a id="MultichatforHelpdeskAgents"></a>


The figure below shows Multichat for a helpdesk agent who connected in a live chat session with a client.

![](../Resources/Images/Live%20Chat/multichat%202%20overview.png)

<a id="MultichatElements"></a>

## Multichat Elements

Multichat contains the following elements:

- The Live conversations and the customers waiting in the queue (if any), on the left.
- The chat area in the middle, which contains the conversation transcript and the currently active conversation.
- Menu options on the right. Two options are available:

- Backchannel events

![](../Resources/Images/Multichat%20v2%20for%20Helpdesk%20Agentsdocx/Multichat%20v2%20for%20Helpdesk_1.png)

{% hint style="info" %}
**NOTE:** Authors can add custom tabs to agents' page to enable them to access and manage records in web views and forms. For more information, see [Handling live chat on agent side](Handling%20live%20chat%20on%20Agent%20side.md).
{% endhint %}

- AI Agent Assistant. The AI Agent Assistant gives agents the possibility to ask for additional information, perform additional actions or transfer live chat to another queue or agent.

![](../Resources/Images/Multichat%20v2%20for%20Helpdesk%20Agentsdocx/Multichat%20v2%20for%20Helpdesk_2.png)

Multichat appears by default with the **Backchannel events** option selected.

To collapse the right menu, click the ![](../Resources/Images/Multichat%20v2%20for%20Helpdesk%20Agentsdocx/Multichat%20v2%20for%20Helpdesk_3.png) icon on the right.

![](../Resources/Images/Multichat%20v2%20for%20Helpdesk%20Agentsdocx/Multichat%20v2%20for%20Helpdesk_4.png)

The conversation transcript brings the history from the current client chat activity ID. An agent connected in a live chat session with a client will see the client conversation with the AI Agent prior to live chat session initiation and the conversation with others agent if the live chat session has been transferred from another helpdesk agent. This enables the helpdesk agents provide better client assistance.

The Active conversation label (![](../Resources/Images/Multichat%20v2%20for%20Helpdesk%20Agentsdocx/Multichat%20v2%20for%20Helpdesk_5_140x25.png)) separates the conversation transcript from the live conversation between current helpdesk agent and the client.

<a id="Pauseordisconnectalivechatconversation"></a>

## Pause or disconnect a live chat conversation

During a live chat conversation, helpdesk agents can pause or disconnect the current live chat session by clicking the buttons displayed at the top of the chat area.

![](../Resources/Images/Multichat%20v2%20for%20Helpdesk%20Agentsdocx/Multichat%20v2%20for%20Helpdesk_6.png)

The agent can put the conversation on hold only when in live chat conversation by clicking the **Pause** button. When the agent clicks the **Pause** button, the **LiveChatConversationIdleTimeoutMins** clock is put on hold to avoid automatically disconnecting the conversation. The click is reactivated only after the agent clicks again the Pause button and sends a message.

{% hint style="info" %}
**NOTE:** If the client sends messages during the pause period, the agent will receive the client messages but the conversation clock will still be on hold.
{% endhint %}

<a id="Reconnectwithuserstakingoverpastconversations"></a>

## Reconnect with users - taking over past conversations

Reconnecting with users becomes valuable when agents require additional time to perform specific tasks outside the Druid Platform and need to inform users once these tasks are completed.

{% hint style="info" %}
**NOTE:** To seamlessly incorporate this functionality without the need for additional flow authoring, we recommend upgrading the **Live Chat Advanced** solution template from the Solution Library.
{% endhint %}

Agents can reconnect to past live chat conversations on all persisted channels (WhatsApp, Facebook, Telegram, Viber, GoogleChat, Instagram, Slack, and Twilio SMS) under the following conditions:

- The user is not engaged in a conversation with the AI Agent.
- The channel-specific limit for the last user interaction with the AI Agent has not reached the maximum value (if any). For instance, agents can reconnect to a past live chat conversation within a 24-hour time-frame from the last user interaction.

On the left side of the interface, agents can view their last 20 past conversations. To reconnect to one of these conversations, the agent clicks the **Activate** button displayed next to the desired conversation.

![](../Resources/Images/druid%207.1/past%20conversations.png)

{% hint style="info" %}
**NOTE:** Helpdesk agents can take over past WhatsApp conversations older than 24 hours. These conversations are marked with the label '> 24h', allowing agents to quickly identify them. The label appears in both the advanced search result list and within the conversation card in the agent's page left menu under the 'Past' conversations section.

Upon activating such conversations, user input in the primary conversation with the client is blocked if the last message in the chat is older than 24 hours. This proactive measure ensures agents are informed of the conversation's status, prompting them to send a template message before further engaging with the users.
{% endhint %}

If an agent wishes to reconnect to a past conversation not listed among the last 20 or to a past conversation of another agent, an advanced search is available. In the Past area, click the **Search** button and in the Search filters pop-up, enter the filtering criteria, then click the **Activate** button corresponding to the desired past conversation.

![](../Resources/Images/druid%207.1/advanced%20search%20past%20conv.png)

<a id="Temporarilyenablefileuploadduringlivesessions"></a>

## <a id="Temporar"></a>Temporarily enable file upload during live sessions

If file uploads have been disabled before the conversation is transferred to a helpdesk agent, helpdesk agents can temporarily enable file uploads for the current live chat session. This allows clients to securely share documents or other files only when requested by the helpdesk agent.

{% hint style="info" %}
**Info:** This feature is available starting with Druid 9.27.
{% endhint %}

To temporarily enable file uploads:

1. During the live chat session, click **Enable file upload**.
2. Select one or more file types that the client is allowed to upload.

![](../Resources/Images/druid%209.27/file%20upload%20type.png)

3. Click **Enable file upload** again.

![](../Resources/Images/druid%209.27/file%20upload.png)

The customer can now upload files matching the selected extensions.

After receiving the required files, click **Disable file upload** to prevent any additional file uploads during the remainder of the live chat session.

{% hint style="info" %}
**NOTE:** The file types selected by the helpdesk agent apply only to the current live chat session. This temporary configuration overrides the upload restriction while file upload is enabled and does not permanently change the file upload configuration.
{% endhint %}

<a id="AIAgentAssistantCharacteristics"></a>

## AI Agent Assistant Characteristics

- The conversation with the AI Agent Assistant is unique to each live chat session. This means that the ConversationID is unique for each client.
- To identify a conversation, the AI Agent verifies the [[ChatUser]].IsCommandChannel attribute on either the Welcome flow or on the Welcome agent flow.
- The client context data transfers to the context of the conversation between the agent and the AI Agent Assistant; therefore, the Assistant always knows to which client the agent is talking.

{% hint style="info" %}
**NOTE:** The AI Agent Assistant is available to agents regardless the number of queues you define in the system, or whether you defined a transfer flow or not. This way, your agents are able to quickly talk to the AI Agent.
{% endhint %}

The AI Agent Assistant is available as an option on the options menu in every live chat conversation.

![](../Resources/Images/Multichat%20v2%20for%20Helpdesk%20Agentsdocx/Multichat%20v2%20for%20Helpdesk_7.png)

While agents are in a live chat session with the client, they can talk to the AI Agent Assistant by clicking on the widget. The widget expands and the agents can tell the AI Agent what they need.

<a id="AIAgentAssistantSpecificJavaScriptFunctions"></a>

## AI Agent Assistant Specific JavaScript Functions

You can configure the following JavaScript functions in BackChannel steps (on the client connected flow) which agents can use when chatting with the AI Agent Assistant:

- **sendMessage (text)**. Enable the agent to send predefined messages.

**Example: Predefined messages in a drop-down**

```
<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
    <a class="dropdown-item" onclick='sendMessage("Thank you for waiting! How may I help you?")'>Thank you for waiting</a>
    <a class="dropdown-item" onclick='sendMessage("Thank you for your time. To help us improve the quality of our services please give feedback. Have a nice day!")'>Ask feedback</a>
</div>
```

If you want to provide the agents with the possibility to preview and edit predefined messages before sending them in the chat, then use the following syntax: `sendMessage ("text",true)`.

**Example: Previewing predefined messages**

```
<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
    <a class="dropdown-item" onclick='sendMessage("Thank you for waiting! How may I help you?",true)'>Thank you for waiting</a>
    <a class="dropdown-item" onclick='sendMessage("Thank you for your time. To help us improve the quality of our services please give feedback. Have a nice day!",true)'>Ask feedback</a>
</div>
```

- **sendMessageToBot(message)** similar with “sendMessage” used on the **Disconnect**, **Pause** or **Send predefined message** buttons.

**Example - Transfer**

```
<button type="button" onclick='sendMessageToBot("Transfer")' class="btn btn-danger">Transfer</button>
```

- **changeChatVisibility(isVisible)**. Set to false to hide the **AI Agent Assistant** option.

<a id="AgentsRequestingBreaks"></a>

## Agents Requesting Breaks

To request a break, an agent will click the **Break** button displayed on the left, below the agent name.

![](../Resources/Images/Multichat%20v2%20for%20Helpdesk%20Agentsdocx/ask%20break.png)

The agent’s break will start immediately after all live sessions have ended.

If an agent requests a break while having ongoing conversations and decides to cancel the break, the agent can do so by clicking the **Cancel** button.

While in break, a pop-up displays on screen with a break timer (showing the time consumed in break). The pop-up also contains the **I’m back** button, which allows the agent to end the break.

{% hint style="info" %}
**NOTE:** Druid will no longer automatically allocate live chat sessions to the agents while in break.
{% endhint %}

![](../Resources/Images/Multichat%20v2%20for%20Helpdesk%20Agentsdocx/break.png)

{% hint style="warning" %}
**IMPORTANT!** Helpdesk agents who requested a break are prohibited from manually connecting to clients. If a break or logout is requested, the **Connect** button is disabled or removed from the waiting clients list. The button is re-enabled if the request for break is canceled. To prohibit agents manually connect to clients when a break or logout is requested requires page upgrade.
{% endhint %}

<a id="AgentsLoggingout"></a>

## Agents Logging out

To log out, an agent will click the **Log out** button displayed on the left, below the agent name.

![](../Resources/Images/Druid%201.58/Druid%201%2058_4.png)

If an agent clicks to log out while having ongoing conversations or when engaged in a conversation and automatic allocation is active, a log out request is initiated and the agent will be logged out after all live sessions have ended.

{% hint style="warning" %}
**IMPORTANT!** Agents who requested logout are prohibited from manually connecting to clients. If logout is requested, the **Connect** button is disabled or removed from the waiting clients list. The button is re-enabled if the logout is canceled. To prohibit agents manually connect to clients when when a break or logout is requested requires page upgrade.
{% endhint %}

## Related Topics

- [Automatically Allocating Clients to Agents](Automatically%20Allocating%20Clients%20to%20Agents.md)
- [Changing the Agent Name Shown in the Chat](../How%20to/Changing%20the%20agent%20user%20name.md)
- [Live Chat With Multiple Queues](Live%20Chat%20Multiple%20Queues.md)
- [Sending the Conversation Transcript to External Systems](../How%20to/Sending%20the%20conversation%20transcript%20to%20external%20systems.md)
