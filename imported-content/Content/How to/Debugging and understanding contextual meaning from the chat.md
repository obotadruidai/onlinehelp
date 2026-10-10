---
layout:
  title:
    visible: false
---

<a id="DebuggingandUnderstandingContextualMeaningfromtheChat"></a>

# Debugging and Understanding Contextual Meaning from the Chat

To debug and understand contextual meaning from the chat, use Druid internal system keywords. The table below provides the full list of Druid system keywords that can be used in the chat.

| Druid keyword | Description |
| --- | --- |
| cancel | Cancels the running of a flow. When inputted in the chat, this command keeps the contextual values already registered in the entities.  E.g., If you have a flow containing a message showing [[Case]].Id =='1234', and after this step you have another step of type Prompt and you type "cancel", you will leave that flow and the value registered in the [[Case]] entity will be persisted. |
| @reset | **IMPORTANT!** Only authors should use it for debugging purposes. Do not share this keyword with clients due to the effect it has on the conversation context.  Cancels the running of a flow. When inputted in the chat, this command deletes all the contextual values already registered in the entities.  E.g., If you have a flow containing a message showing [[Case]].Id =='1234', and after this step you have another step of type Prompt, and you type "@reset", you will leave that flow and the value registered in the [[Case]] entity will be deleted. |
| back | Goes back to the previous flow step, of type Prompt or of another type that awaits input from the user. |
| @context | Only users with admin privileges in the Druid Portal should use this keyword to debug the information stored in the entities.  E.g., If you have the [[Case]] entity that has already stored values for [[Case]].Id=='1234' and you are in the middle of a flow and you type "@context [[Case]].Id" you will receive '1234' |
| disconnect | Disconnects the current live chat session. Both agents ad clients can use it. |
