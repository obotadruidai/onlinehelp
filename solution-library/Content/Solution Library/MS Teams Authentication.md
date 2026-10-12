---
title: "MS Teams Authentication"
---

<a id="MSTeamsAuthentication"></a>


This solution template enables you to authenticate the users chatting with the AI Agent for the first time in the MS Teams channel.

Install this solution from the Solutions Library. For information on how to install the solution, see [Installing Solution Templates](Installing%20Solution%20Templates.md).

<a id="ChatUserinformationavailableintheconversationcontext"></a>

## ChatUser information available in the conversation context

The AI Agent automatically provisions the following ChatUser parameters in the conversation context:

- ChatUser.Email
- ChatUser.FirstName
- ChatUser.Lastname
- ChatUser.DomainUserName
- ChatUser.UserId – the MS Teams user id.
- Chatuser.UserName – the FullName, delivered by MS Teams.

{% hint style="warning" %}
**IMPORTANT!** For solution demo purposes, the **ChatUser.MasterID** and **ChatUser.DomainUserName** parameters are configured to receive the user's email address. Make sure that you configure these parameters to receive the information associated with your systems and integrations.
{% endhint %}

## Related Topics

- [Handling Authentication](https://druidai.gitbook.io/druid-ai-docs/ai-platform/how-to/handling-authentication)
- [Microsoft Teams](https://druidai.gitbook.io/druid-ai-docs/channels/social-media-and-chat/ms-teams-integration)
