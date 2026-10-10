<a id="HandlingLiveChatonClientSide"></a>

# Handling Live Chat on Client Side

With the Live Chat Starter solution, the AI Agents will do the following on the client side:

1. [Add client to the Waiting Queue](#Add_client_to_the_Waiting_Queue).
2. [Notify clients while on the Waiting Queue](#Notify_clients_while_on_the_Waiting_Queue).
3. [Get the client’s feedback](#Get_the_client%E2%80%99s_feedback).

<a id="AddclienttotheWaitingQueue"></a>

## <a id="Add_client_to_the_Waiting_Queue"></a>Add client to the Waiting Queue

While in an automated conversation with the AI Agent, if the clients tell the AI Agent that they wish to talk to a live agent, the **live-chat-connect-to-agent** flow is triggered. Or you can have this flow automatically triggered from the “Intent not recognized” flow.

![](../Resources/Images/Live%20Chat/waiting%20queue.png)

The **live-chat-connect-to-agent** flow is comprised of the following steps:

1. The AI Agent informs the client that the conversation will be registered and asks the client to choose whether they agree or not to the conversation being registered.
2. If the client doesn’t agree, he / she will remain in automatic conversation with the AI Agent.
3. If the client agrees, specific information from the chat is saved into the conversation history DB. This information will be displayed in the conversation history area when an agent will connect to the live chat session.
4. This step is executed only if the client agreed at step 1. The client will be added to the live chat Waiting queue.

You can configure the following settings:

- The messages sent to the clients at steps 1 to 4. To do so, click to edit the desired step, click the **General** section header and in the field, replace the text in the **Step message** field with the desired message.

Example:

![](../Resources/Images/Live%20Chat/message%20for%20client%20added%20to%20waiting%20list.png)

- Add or remove information that will be shown in the conversation history when an agent connects to the client live chat. To do so, edit flow step 3 by adding or removing parameters in the SetVariables section.

<a id="NotifyclientswhileontheWaitingQueue"></a>

## <a id="Notify_clients_while_on_the_Waiting_Queue"></a>Notify clients while on the Waiting Queue

When the clients are in the Waiting queue, the **live-chat-waiting-message-in-the-queue** flow is triggered every 1 minute. The purpose is to have the AI Agent interacting with the client while waiting for a live agent to pick up the live chat.

![](../Resources/Images/Live%20Chat/timeout%20reached%20ask%20client%20to%20wait.png)

The **live-chat-waiting-message-in-the-queue** flow is comprised of the following steps:

1. The AI Agent verifies what number the client is in the Waiting queue.
2. The AI Agent sets the counter of the waiting list to null.
3. The client is added as the last entry to the Waiting list. To respond to client inquiries in a timely manner, the clients are added to the Waiting list in the order they have asked for live chatting with an agent. So, the first customer is the first entry in the Waiting list, the second one is the second entry, etc.
4. The AI Agent informs the client the position on the Waiting queue and asks the client to choose whether he / she will be waiting or not.

1. If the client chooses to disconnect, the AI Agent will try to remove the client from the Waiting list.
2. If for any reason, the AI Agent fails disconnecting the client, a message will be sent to the client.
3. If the AI Agent succeeds disconnecting the client, it will provide the client with the possibility to remain in an automatic conversation with the AI Agent. The client will be able to select from a given menu.
4. If the client chooses to wait, a message will be sent to the client.

5. If the **LiveChatQueueWaitingTimeoutMins** is reached out, the AI Agent takes the current user off the helpdesk waiting queue.

You can configure the following settings:

- The messages sent to the clients at steps 4 and 5. To do so, by either clicking to edit the desired step, the General section header and in the Step message field, replacing the text with the desired message, or from the AI Agent Details page, Special Flows section by changing the default text.
- Configure the **LiveChatQueueWaitingTimeoutMins**. To do so, from the AI Agent Details page, click the **General** tab and change the value of the **LiveChatQueueWaitingTimeoutMins** field.

![](../Resources/Images/Live%20Chat/configure%20live%20chat%20timeout.png)

<a id="Gettheclientsfeedback"></a>

## <a id="Get_the_client’s_feedback"></a>Get the client’s feedback

When agents disconnect from a live chat session with a client or in rare occasions, when the clients disconnect from a live chat, the **live-chat-feedback-client** flow is triggered. The clients are asked to rate the live chat.

![](../Resources/Images/Live%20Chat/client%20feedback.png)

The **live-chat-feedback-client** flow is comprised of the following flow steps:

1. The AI Agent verifies the chat status.
2. Sets to null the entity which will store the client information (the entity provided in the SetVariables section).
3. The AI Agent asks the client to rate the support provided by the agent during live chat.
4. The AI Agent asks the client to rate the waiting time.
5. The AI Agent saves the client’s feedback.
6. The AI Agent sends the client a message and erases the information from the chat context.
7. The AI Agent ends the live chat session.

You can configure the client’s feedback form which is by default comprised of two steps of type choice.

## Related Topics

- [AI Agent Informational Model](../5_Entities/AI%20Agent%20Informational%20Model.md)
- [Post Actions](../4_Flows/Post%20Actions.md)
- [Pre Actions](../4_Flows/Pre%20Actions.md)
