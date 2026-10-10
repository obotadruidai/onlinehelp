---
title: "Configure Chat Activity Data"
---

<a id="ConfigureChatActivityData"></a>


The Chat Activity Data feature enables you to store specific context data in the database and use it for future reporting. For example, you want to store the customer age, specific customer choice and whether the customer has a loan or not.

To configure chat activity data, follow these steps:

1. On the flows where you want to store activity data, configure existing step(s) or create a new one and make sure to:

1. Put the activity data into context by setting variables. For information on how to set variables on flow steps, see [Set Variables](../../../4_Flows/Set%20Variables.md).

Example:

![](../../../Resources/Images/Chat%20Activity%20History/entity%20context.png)

2. Add the InternalAction **SaveActivityData**.

![](../../../Resources/Images/Chat%20Activity%20History/post%20action.png)

3. (Optional) All chat activities end automatically after 60 minutes of inactivity. If you want to allow the AI Agent to decide when to end a chat activity based on the conversation context (e.g., when the client says "good bye"), on the flow step of choice, add the InternalAction **CloseActivity**.
> **NOTE:** Any conversation initiated after a CloseActivity event will generate a new Chat Activity (session).

![](../../../Resources/Images/Chat%20Activity%20History/close%20activ%20post%20action.png)

<a id="Howitworks"></a>

## How it works

The SaveActivityData action looks in the context of the [[ChatActivityData]] entity and saves the data in the DB, in the Chat Activity Data table, on the conversation's chat activity ID (**ONLY** for that conversation session).
