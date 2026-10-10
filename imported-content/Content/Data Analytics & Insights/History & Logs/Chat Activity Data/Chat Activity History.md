<a id="ChatActivityHistory"></a>

# Chat Activity History

Chat Activities are conversation sessions. When a user starts chatting with the AI Agent, a chat activity is created. Then, a new chat activity is created if more than 60 mins of idle time passed from the last message in that conversation. A new chat activity is also created if the user and the AI Agent talk on a new channel.

The Chat Activity History feature provides you with extensive chat activity logs: who chatted with the AI Agent and for how long, if the user was in live chat, all activities performed during chat, all the data provided in chat via entity attributes, the conversation messages and detailed information on the flows and the steps being executed.

<a id="ViewChatActivityHistory"></a>

## View Chat Activity History

To access the Chat Activity History, on the main menu, click **History & Logs** > **Chat Activity History**. The Chat Activity History page appears which provides you with extensive filtering options.

![](../../../Resources/Images/Chat%20Activity%20History/filter%20page.png)

Selecting a AI Agent is mandatory to view the chat activity history. The other filtering options are optional and you can use them as best suits your needs. After you select filtering options, the table displays a list of all chat activity records matching the filtering criteria.

![](../../../Resources/Images/Chat%20Activity%20History/bot%20filtering%20activity.png)

To view the full activity of a specific chat activity record, click the magnify icon in front of the desired record.

![](../../../Resources/Images/Chat%20Activity%20History/view%20full%20activity.png)

<a id="ActivityDetails"></a>

### Activity Details

The Chat Activity Details page appears by default on the **Activity Details** tab. This section provides you with detailed information on the selected chat activity. If the user / client was in a live chat session, you see the queue(s) the user was assigned to, how much time the client was waiting for an agent to connect, the agent(s) who connected and if live chat was transferred to different queues.

![](../../../Resources/Images/Chat%20Activity%20History/activity%20details.png)

<a id="ActivityData"></a>

### Activity Data

The **Activity Data** tab displays the data stored from the context of the ChatActivityData entity. You can use this data for future reporting.

Druid version 1.59 or higher automatically collects the following information related to the device used by the user to chat with the AI Agent:

| Name | Business Type | Description |
| --- | --- | --- |
| App | String | The name of the browser from which the web chat is initiated. |
| AppVersion | String | The version of the browser. |
| DeviceModel | String | The name of the device from which the users initiate webchat, if they're on mobile web; available only if device discovery finds enough information about this attribute. |
| isMobile | Boolean | “True” if the user is initiating the chat from a mobile device; “false” otherwise. |
| origin | String | The base URL of the webpage where the web chat is hosted. |
| OSVersion | String | Platform of the operating system running on the machine/device on which the web chat is initiated. This indicates specific operating systems, including variations within the same family, such as Windows 11, Windows 10 and Windows 7. |
| pathName | String | The full path to the web page from which the user initiates the chat. |

![](../../../Resources/Images/history%20activity%20data.png)

<a id="ConversationHistory"></a>

### Conversation History

The conversation history of a chat activity is a subset of the AI Agent Conversation History (**Administration** > **Conversation History**), so you can access it in the Database anytime.

The **Conversation History** tab provides with the complete conversation history of a chat activity, including the message status, who sent the message, the message content, when it was sent, the flow and the flow step which was executed.

![](../../../Resources/Images/Chat%20Activity%20History/conversation%20history.png)

If there are any errors during the chat activity (marked with ![](../../../Resources/Images/Chat%20Activity%20History/error.png)) and you want to troubleshoot what happened, at the top-right corner of the page, click the **Detailed Conversation History** button. The Conversation History page appears and provides you with more information for the chat activity record you previously selected.

![](../../../Resources/Images/Chat%20Activity%20History/filtered%20conversation%20history.png)

To find out why the error occurred, click the magnifier icon (![](../../../Resources/Images/troubleshooting/magnifier%20icon.png)) displayed inline with the error icon.

Based on the information provided here, do the proper changes to prevent the error from occurring again. Note the Flow and Flow Step where the error occurs. Go to **Flows** and search for the **Flow name**. Within the flow, search for **Flow Step** and make the needed corrections.
