---
title: "Web Authentication"
---

<a id="WebAuthentication"></a>


This solution template enables you to authenticate the users chatting for the first time with the AI Agent available in your public website.

Install this solution from the Solutions Library. For information on how to install the solution, see [Installing Solution Templates](Installing%20Solution%20Templates.md).

<a id="ChatUserinformationavailableintheconversationcontext"></a>

## ChatUser information available in the conversation context

The AI Agent automatically provisions the following ChatUser parameters in the conversation context:

- ChatUser.UserId – holds the incoming phone number.

{% hint style="warning" %}
**IMPORTANT!** For solution demo purposes, the **ChatUser.MasterID** and **ChatUser.DomainUserName** parameters are configured to receive the user's email address. Make sure that you configure these parameters to receive the information associated with your systems and integrations.
{% endhint %}

## Related Topics

- [Handling Authentication](https://druidai.gitbook.io/druid-ai-docs/ai-platform/how-to/handling-authentication)
- [WebChat](https://druidai.gitbook.io/druid-ai-docs/channels/web-and-email/webchat)
