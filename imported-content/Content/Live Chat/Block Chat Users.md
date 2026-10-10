---
title: "Block Chat Users for Live Chat"
---

<a id="BlockChatUsersforLiveChat"></a>


The block chat users feature is useful when you want to provide your helpdesk agents with the possibility to block for a specific period of time the chat users who are disrespectful, offensive or have incorrect behavior. For example, if a customer is using abusive language or sending spam messages, the helpdesk agent can block that user from being placed in the waiting queue.

Once a chat user is blocked for a specific period, the user will no longer be placed in the waiting queue for that period within the current conversation either until the blocking period expires or the user is unblocked.

<a id="Howtoauthortheblockingofchatusers"></a>

## How to author the blocking of chat users

On the Live chat agent disconnected flow, after the helpdesk agent provides the feedback, create a flow path dedicated to blocking the chat users. On that flow path, call the internal action **HelpdeskClient.IsBlockedForLiveChat**, set the period in minutes for which the chat users will be blocked for Live Chat (BlockIntervalMinutes) and provide the reason for blocking the user using a JSON with the following format:

```
{
    "BlockIntervalMinutes":1440,
    "BlockReason":"<string>",
    "SaveToChatActivityData":<boolean>
}
```

By default, BlockIntervalMinutes (the blocking period) is **1440 minutes** (24 hours) and the **SaveToChatActivityData** is **false**, meaning that if an authenticated user is blocked, the blocking information is not saved in the system entity [[ChatActivityData]].

![](../Resources/Images/Live%20Chat/block%20internal%20action.png)

> **NOTE:** Because blocking anonymous users is done within the conversational context, we recommend you to block anonymous users for a shorter period, or leave the **BlockIntervalMinutes** set to the default value that is 1440 minutes (24 hours).

> **Info:** You can also block authenticated users directly in the Druid Portal, (**Administration** menu > **Users**) in the edit user page. Click on the **Live Chat Blacklist** tab enter a reason for blocking the user, set the blocking interval in minutes (default is 1440 minutes) and click the **Block user** button, then click **Save**.
>
> ![](../Resources/Images/Live%20Chat/block%20auth%20user.png)

If an authenticated user is blocked for Live Chat, the user is added to the Live Chat Blacklist. If in the **HelpdeskClient.IsBlockedForLiveChat** internal action, the parameter "SaveToChatActivityData" is set to **true**, the following information is stored in the [[ChatActivityData]] system entity:

- **LiveChatBlockedUntil** - The period for which the user will not be placed on the waiting queue.
  It is the sum between **Blocked at** and the **BlockIntervalMinutes**
- **LiveChatBlockedReason** - The reason why the user has been blocked for Live Chat.
- **LiveChatBlockedAt** - The date and time when the user has been blocked by a helpdesk agent.
- **LiveChatBlockedByAgentName** - The email of the helpdesk agent who blocked the user.

The information above is also available in the user configuration page, **Live Chat Blacklist** tab.

If an anonymous user is blocked for Live Chat, the following information is stored within the conversation context, in the [[ConversationInfo]] system entity:

- **LiveChatBlockedUntil** - The date and time until which the user will not be placed on the waiting queue within the current conversation.
  It is the sum of the time when the user was blocked for Live Chat and the **BlockIntervalMinutes** set in the **HelpdeskClient.IsBlockedForLiveChat** internal action.

When a user who has been blocked for Live Chat will want to connect to a helpdesk agent, the **ConnectToHelpdeskAgent** internal action will return **false** in **@InternalActionResult** and a specific state will also be set on **HelpdeskClient.IsBlockedForLiveChat**, similar with IsOutsideWorkingHours, so authors can handle the situation in the flow.

<a id="Unblockauthenticatedusers"></a>

## Unblock authenticated users

Authenticated users who have been blocked are added to the Live Char Blacklist. Druid Portal users who have privileges to manage users, can easily unblock them.

To unblock an authenticated user, in the Druid Portal, go to the user configuration page (**Administration** menu > **Users**, edit user), click on the **Live Chat Blacklist** tab, click the **Unblock user** button, then click **Save**.

![](../Resources/Images/Live%20Chat/unblock%20auth%20users.png)

<a id="Unblockanonymoususers"></a>

## Unblock anonymous users

The anonymous users are blocked within the conversational context, so you can author flows to allow the anonymous user to unblock themselves. For example, in a flow you, on a flow step, you set variable **[[ConversationInfo]].LiveChatBlockedUntil==null** or **[[ConversationInfo]].LiveChatBlockedUntil==GetDate**. If the anonymous user continues the conversation and reaches that flow step, the user is unblocked.

## Related Topics

- [Internal Actions](../4_Flows/Internal%20Actions.md)
- [System Entities](../5_Entities/System%20Entities.md)
