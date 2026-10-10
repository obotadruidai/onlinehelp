---
layout:
  title:
    visible: false
---

<a id="ConversationInsights"></a>

# Conversation Insights

Chat Activities are conversation sessions. When a user starts chatting with the AI Agent, a chat activity is created. Then, a new chat activity is created if more than 60 mins of idle time passed from the last message in that conversation. A new chat activity is also created if the user and the AI Agent talk on a new channel.

The conversation insights provides you with extensive chat activity logs: who chatted with the AI Agent and for how long, if the user was in live chat, all activities performed during chat, all the data provided in chat via entity attributes, the conversation messages and detailed information on the flows and the steps being executed.

To view extensive insights of the chat activity, click the **Conversation insights** tab.

![](../../../Resources/Images/Conversation%20History%20v2/Activities%20grouped%20by%20conversations_20.png)

The Details section provides you with an overview of the conversation activity. The message insights are also available in the Flow Editor when debugging a specific message.

The Activity Data section displays the data stored from the context of the [[ChatActivityData]] entity (default data stored in this entity is listed in the table below).

| Name | Description |
| --- | --- |
| App | The name of the browser from which the web chat is initiated. |
| AppVersion | The version of the browser. |
| DeviceModel | The name of the device from which the users initiate webchat, if they're on mobile web; available only if device discovery finds enough information about this attribute. |
| isMobile | “True” if the user is initiating the chat from a mobile device, “false” otherwise. |
| origin | The base URL of the webpage where the web chat is hosted. |
| OSVersion | Platform of the operating system running on the machine/device on which the web chat is initiated. This indicates specific operating systems, including variations within the same family, such as Windows 11, Windows 10 and Windows 7. |
| pathName | The full path to the web page from which the user initiates the chat. |

The Activity Events section provides you with the list of activity events raised during the conversation activity and the time when they were raised.

The following is the complete list of activity evens that can occur during a conversation activity:

| Activity Event | Description |
| --- | --- |
| ActivityInit | The user opened the webchat widget. |
| UserEngaged | The user sent a message in the chat. |
| UserAuthenticatedInConversation | The AI Agent authenticated the user. |
| ClientInQueue | The client was placed in a waiting queue. |
| ClientConnectedToAgent | A helpdesk agent connects in live chat with the client. |
| AgentDisconnect | Helpdesk agent disconnected from live chat activity. |
| ClientTransferedToQueue | The client was transferred to another queue. |
| ActivityEnded | The chat activity ended. |
