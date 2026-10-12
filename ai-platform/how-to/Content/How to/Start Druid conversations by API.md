---
title: Start Druid Conversations via API
---


You can initiate a Druid conversation through the API `/api/Druid/{botId}/StartFlow`

## Prerequisites

* Contact [DRUID Support](../How%20to/mailto:support@druidai.com) to activate the Druid Endpoints service on your tenant and to generate a token.
* Ensure that you have a Druid Portal admin user account.

## StartFlow API

The StartFlow API starts a DRUID flow and transmits any specified data within the conversation context through the request body.

{% hint style="warning" %}
**IMPORTANT!** The AI Agent triggers the flow on the specified channel only when the user has initiated a conversation with the AI Agent on that same channel.
{% endhint %}

### Syntax

`POST *.https://druidendpoints.druidplatform.com/api/Druid/{botId}/StartFlow`

To get the AI Agent ID, select the desired AI Agent and from the browser get the AI Agent ID. It is placed between `edit/` and `/botdetails`.

![](<../../.gitbook/assets/bot id (1).png>)

### Authorization

To authenticate your request for DRUID Endpoints, ensure inclusion of the Bearer token. Obtain the token by generating a permanent token or utilizing the authentication endpoint. Refer to [Webhooks](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/webhooks) for detailed instructions.

Remember to include the bearer token in the **Authorization** section of your request.

![](../../.gitbook/assets/authorization.png)

{% hint style="info" %}
**Info:** For DRUID version prior to 7.7, get the token corresponding to the 'Druid.Endpoints' from **Administration** > **Druid Services**.

<img src="../../.gitbook/assets/druid serv endpoint.png" alt="" data-size="original">
{% endhint %}

### Request Body

```
{
  "channelId": "string",
  "targetUserMasterId": "string",
  "targetConversationId": "string",
  "targetTenantUserId": "string",
  "entityContextData": "string",
  "flowUtterance": "string",
  "flowId": "string",
  "conversationLanguage": "string"
}
```

| Parameter            | Data Type | Mandatory                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | --------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| channelId            | String    | Yes                       | The ID of the channel where the AI Agent initiates the conversation. Ensure to provide the name exactly as it is stored in **\[\[ChatUser]].ChannelId**.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| targetConversationId | String    | One of them is mandatory. | Enables you to start both authenticated and non-authenticated conversations. **Info:** We recommend you to use it in the callback from a third-party application that has been initially started from a DRUID conversation. E.g., from DRUID you start an UiPath robot that will notify DRUID when the job/task has been completed.                                                                                                                                                                                                                                        |
| targetUserMasterId   | String    |                           | The unique identifier of an authenticated Druid Portal user. Use it when you want to start a flow to a specific authenticated user. To get the Master User ID of a user, in the Druid Portal, from the **Administration** menu, click **Users**, then select to edit the specific user. From the **User Information** tab, scroll-down and get the **Master Id**.                                                                                                                                                                                                          |
| targetTenantUserId   | String    |                           | The TenantUserId is a system entity field that is used by the system in the backend. You can retrieve it from **\[\[ChatUser]].TenantUserId**.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| entityContextData    | String    | Yes                       | In the "entityContextData" object enter provide the data you want to send within the conversation context. **NOTE:** Ensure that the property names provided in 'contextData' match exactly with the DRUID entity field names. Additionally, be mindful of the AI Agent informational model. In DRUID 7.9 onwards, the property names in 'contextData' do not need to match exactly the referred entity name behind the field of type entity / entity list. For a clearer understanding of how the request should be structured, refer to the two examples provided below. |
| flowUtterance        | String    | One of them is mandatory. | The flow utterance. **NOTE:** Use **flowUtterance** instead of the **flowId** as it is much easier to identify a flow by utterance than by ID (assuming that the flow utterance is unique). If you move your AI Agent from a testing environment to PROD, the flow ID will change while the flow utterance remains unchanged.                                                                                                                                                                                                                                              |
| flowId               | String    |                           | The flow ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| conversationLanguage | String    | No                        | Specify the language to start the conversation. Use the same language codes as \[\[ChatUser]].Language, like "en-US" for English (United States). **IMPORTANT!** If the language is not one of the AI Agent languages, the language code is incorrect, or not specified, the conversation will begin in the language the user used to interact with the AI Agent on that channel. **NOTE:** This parameters is available in DRUID 7.10 onwards.                                                                                                                            |

### Response

The request is put on a DRUID waiting queue and will be executed only when the conversation reaches the "Idle" mode.

```
{
    "message": "Druid Endpoint: StartFlow attempt successfully queued for execution",
    "isError": false
}
```

### Error codes

* 401 - the access token is invalid.
* 404 - The syntax of the call is incorrect.
* 500 — Internal server error or a parameter in the contextData does not exist in DRUID. The response provides you with the error details.

## Example: Starting a conversation without sending data within the conversation context

In this example:

* The AI Agent id is **56ca1234-c5ea-480c-a8db-08d8d4b**.
* We will start the conversation with Id **12AA4SifAA2vBBB9BBBpw-eu** in the WhatsApp Meta channel.
* The entity \[\[Client]] is present within the conversation context.
* The flow utterance is "update account".

**Request**

```
{
    "botId": "56ca1234-c5ea-480c-a8db-08d8d4b",
    "channel": "meta-whatsapp",
    "targetConversationId": "12AA4SifAA2vBBB9BBBpw-eu",
    "entityContextData": {},
    "flowUtterance": "update account"
}
```

## Example: Starting a conversation and sending data within the conversation context

In this example:

* The AI Agent id is **56ca1234-c5ea-480c-a8db-08d8d4b**.
* We will start the conversation with the targetTenantUserId **3fa85f64-5717-4562-b3fc-2c963f66afa6** in the MS Teams channel.
* We will send a collection of contracts within the conversation context. In DRUID we have the entity \[\[Client]] which has:
* two scalar fields: \[\[Client]].Name and \[\[Client]].Age.
* a field of type entity, \[\[Client]].PageInfo referencing the system entity \[\[PageInfo]] that stores client-side page information from web views.
* a field of type entity list, \[\[Client]].Contracts that stores a collection of contracts.

The entity \[\[Client]] in JSON format looks like this:

**Data in JSON Format**

```
"entityContextData": {
        "Client": {
            "Name": "John Doe",
            "Age": 25,
            "PageInfo": {
                "NumberOfRecords": 10,
                "PageStartIndex": 0
            },
            "Contract": [
                {
                    "CNumber": 1,
                    "Title": "Cession"
                },
                {
                    "CNumber": 2,
                    "Title": "Loan"
                }
            ]
        }
}
```

* The flow utterance is "add contracts".

**Request Body**

```
{
    "botId": "56ca1234-c5ea-480c-a8db-08d8d4b",
    "channelId": "msteams",
    "targetTenantUserId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "entityContextData": {
        "Client": {
            "Name": "John Doe",
            "Age": 25,
            "PageInfo": {
                "NumberOfRecords": 10,
                "PageStartIndex": 0
            },
            "Contract": [
                {
                    "CNumber": 1,
                    "Title": "Cession"
                },
                {
                    "CNumber": 2,
                    "Title": "Loan"
                }
            ]
        }
    },
    "flowUtterance": "add contracts"
}
```
