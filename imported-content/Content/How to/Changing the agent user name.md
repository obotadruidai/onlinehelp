---
title: Changing the Agent Name Shown in the Chat
---

# Changing the Agent Name Shown in the Chat

By default, the agent's name shown in the chat is comprised by \[\[ChatUser]].FirstName and \[\[ChatUser]].LastName if the agent is not connecting from the Druid Portal or using Active Directory (AD) authentication.

![](<../../.gitbook/assets/agent name.png>)

If you want to customize your agents real name in the chat you have two options:

### Give your agents a predefined username

On your multichat solution, go to flows and click on the **ConnectToHelpdeskClientMultiChat** agent flow. On the step before the step that connects the agent with the user (the step where the post internal action ConnectToHelpdeskClientMultiChat is called), add the variable **\[\[ChatUser]].Name** and give it the desired value; e.g. "Support Agent". Save the step.

![](<../../.gitbook/assets/set variable (1).png>)

### Remove agents name

1. On your multichat solution, go to flows and click on the **ConnectToHelpdeskClientMultiChat** agent flow. On the step before the step that connects the agent with the user (the step where the post internal action ConnectToHelpdeskClientMultiChat is called), add the variable **\[\[ChatUser]].Name** and give it as value an empty string ("").

![](<../../.gitbook/assets/empty string variable.png>)

2. Save the step.
3. Go to the AI Agent details page, click the **Special Flows** section, scroll down to the **ConnectedToHelpdeskAgent** special message and either remove the "{0}" from the special message (both EN and RO texts) or change the message making sure to exclude the "{0}". This way there will be no agent name in the chat snippet nor in the special message when the agent connects with the client in live chat session.
