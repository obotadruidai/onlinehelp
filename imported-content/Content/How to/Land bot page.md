---
title: Integrate Land AI Agent Page with Telephony Systems
---

# Integrate Land AI Agent Page with Telephony Systems

The Land AI Agent page hosts the chat panel, enabling Portal users to engage with the AI Agent in a secure, authenticated context.

![](<../../.gitbook/assets/landbot page.png>)

Integrating a DRUID Land AI Agent page with telephony systems ensures a smooth transition for agents handling calls while engaging with the AI Agent. Your agents will seamlessly navigate between telephony calls and chat interactions on the DRUID Land AI Agent page, providing an enhanced and contextually rich experience for users.

Instruct the telephony system to open the DRUID Land AI Agent page in a new browser tab each time an agent answers a call in the telephony interface. Use the following format to instruct the telephony system in opening the DRUID Land AI Agent page:

`*druidplatform.com/app/main/landingpage/<landbot page id>/?<query params>&reset-conversation=true`

| URL element             | Description                                                                                                                                                                                                                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                         | The ID of the Land AI Agent page. Replace with the appropriate identifier.                                                                                                                                                                                                                              |
|                         | Include queryParams (separated by &) to provide additional information about the call, enriching the chat experience with relevant details.                                                                                                                                                             |
| reset-conversation=true | Initiates a new conversation when an agent answers a call. **IMPORTANT!** The system parameter `reset-conversation=true` is crucial; omitting it in the URL may result in the telephony system reopening the previous conversation the agent had. This parameter is available in DRUID 5.28 and higher. |

**Example**: Suppose your telephony system is configured to open the DRUID Land AI Agent page for a specific interaction. The URL format would look like this:

`*druidplatform.com/app/main/landingpage/1234/?call-info=5678&user-info=abcd&reset-conversation=true`
