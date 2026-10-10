---
title: VoiceText
---

# VoiceText

The VoiceText Channel enables voice integration in Contact Centers, supporting scenarios where voice services and voice AI Agents are provided by third-party platforms. It allows seamless interactions between a user and a AI Agent by handling speech-to-text and text-to-speech conversions.

By default, VoiceText uses a synchronous request-response model: when a user message is sent to Druid, the system responds immediately with the full reply (or replies) in a single API response. This approach works well for simple conversations but may introduce delays when integrations or Proactive AI Agent messages are set on flow steps. To address this, Druid supports an asynchronous long polling mechanism that improves responsiveness during more complex interactions.

{% hint style="info" %}
**NOTE:** For Voice Text with LLM Streaming, long polling must be enabled.
{% endhint %}

The diagram below provides a high-level overview on how to integrate voice in Contact centers using external Voice AI Agents.

![](<../../../.gitbook/assets/VoiceText Channel.png>)

Third-party Voice AI Agent delivers SIP connection with the Contact Center (asynchronous communication). Sometimes, the Voice AI Agent role can be delivered by the Contact Center too.

1. The Voice AI Agent delivers Speech to Text and Text to Speech services.
2. The Voice AI Agent sends text request to Druid.
3. Druid responds the Voice AI Agent text response (synchronous response communication).

### Synchronous Request-Response

This is the default and traditional interaction model for the VoiceText channel. In this mode, when the Voice AI Agent sends a user's input to Druid via the POST \*.druidplatform.com/api/voicetext/{botId}/messages API, the connection remains open, and the Voice AI Agent waits for a direct response from Druid on the same API call.

Once Druid processes the request and generates a response (or multiple responses), these messages are typically concatenated into a single string and returned to the Voice AI Agent. The Voice AI Agent then converts this text response to speech and plays it back to the user through the Contact Center.

While straightforward for simple, single-turn interactions, this synchronous model can introduce latency. If a Druid flow involves complex integrations, database lookups, or proactive messages that take time to generate, the Voice AI Agent (and thus the user) will experience a delay until all the AI Agent responses for that conversation turn are ready and returned concatenated in a string. This can lead to a less fluid user experience, as the user might perceive the AI Agent as slow or unresponsive while it waits for a complete response.

The figure below describes the detailed integration sequence.

![](<../../../.gitbook/assets/VoiceText Channel diagram.png>)

1. When there is an incoming call, the Contact Center initiates the conversation with Druid AI Agent to optimize the response with the Welcome message.
2. The Contact Center initiates the conversation with the Voice AI Agent.
3. The Voice AI Agent initiates the conversation with Druid AI Agent, which authenticates the conversation.
4. Druid AI Agent responds with the Welcome Message.
5. The Contact Center picks up the call and responds with the welcome message.
6. Voice AI Agent responds with the Welcome Message.
7. The Contact Center gives the Welcome message to the user.
8. The Contact Center captures the “User says”.
9. The Contact Center sends SIP to the Voice AI Agent.
10. The Voice AI Agent converts Speech to Text and sends the text user says to Druid AI Agent, calling Druid API CreateActivity (user says).
11. Druid AI Agent responds.
12. Druid AI Agent responds synchronously with the AI Agent response (in text format).
13. The Voice AI Agent checks if the response contains instructions to transfer the call to human agent. If the response does not contain instructions to route the call to human, the Voice AI Agent transforms Text to Speech; otherwise, it performs the next step.
14. The Voice AI Agent responds to the Contact Center with voice (SIP connection).
15. The Contact Center responds to the user with voice.
16. The User closes the call.
17. The Contact Center announces the VoiceBot that the conversation is closed.
18. The Voice AI Agent announces Druid AI Agent that the conversation is closed.
19. Transfers the call to Human Agent.
    1. The Voice AI Agent announces the Contact Center to transfer the call to Human.
    2. The Contact Center executes the transfer.
    3. Helpdesk agent and User are now talking directly.

{% hint style="info" %}
**Info:** Whenever a channel timeout occurs (connection is dropped), the following message is logged in Conversation History "\[Channel connection timed out]. The voice channel connection timeout threshold was reached. The previous AI Agent message may have also been dropped before reaching the client's conversation."
{% endhint %}

### Long Polling mechanism

Long Polling offers an asynchronous alternative to the default synchronous request-response model, designed to significantly improve responsiveness and user experience, especially in scenarios involving multi-message replies or delayed AI Agent processing (e.g., due to integrations or proactive messages).

In this mode, when the Voice AI Agent sends a user input to Druid using the `POST *.druidplatform.com/api/voicetext/{botId}/messages` API, it does not wait for a direct response. Instead, immediately after sending the user's input, the Contact Center initiates a continuous polling mechanism by making repetitive POST requests to the dedicated Long Polling endpoint: `POST *.druidplatform.com/api/voicetext/{botId}/messages/getMessages`.

Druid holds these connections open until a AI Agent message or event becomes available. As soon as a message is ready, Druid sends it back to the Contact Center, closing that specific `/getMessages` request. Immediately after that, the Contact Center will initiate a new request to fetch the following message from the AI Agent, and will continue to do so, until the phone call is terminated.

This asynchronous approach ensures that messages are delivered to the Contact Center as soon as they are generated by Druid, without waiting for an entire set of responses or for a slow integration to complete. The GET request will time out after a set period (typically 30 seconds) if no messages are available, at which point the Contact Center should re-initiate the `/getMessages` call to continue polling.

The steps below describe the detailed integration sequence:

1. Initiating the Conversation:
2. When there's an incoming call, the Contact Center (CC) initiates the conversation with the Voice AI Agent.
3. The Voice AI Agent initiates the conversation with Druid AI Agent, which authenticates the conversation.
4. The Druid AI Agent responds with the Welcome Message.
5. Contact Center Handles Welcome Message:
6. The CC picks up the call.
7. The Voice AI Agent responds with the Welcome Message (received from Druid AI Agent).
8. The CC gives the Welcome message to the user.
9. Contact Center Captures User Input:
10. The CC captures the “User says” (speech from the user).
11. The CC sends this audio via SIP to the Voice AI Agent.
12. The Voice AI Agent converts Speech to Text and sends the text user input to the DVA, calling the Druid API CreateActivity (`POST *.druidplatform.com/api/voicetext/{botId}/messages`).

{% hint style="info" %}
**NOTE:** The Voice AI Agent DOES NOT wait for a synchronous response from this API call.
{% endhint %}

4. Contact Center Polling for AI Agent Responses:
5. Immediately after the Voice AI Agent sends the user's input, the CC begins polling for responses by making periodic POST requests to the Long Polling endpoint: `*.druidplatform.com/api/voicetext/{botId}/messages/getMessages`.
6. The Druid AI Agent sends available AI Agent responses (in text format) to the CC via these `getMessages` calls, as soon as they are ready. Each `getMessages` call returns one message/event.
7. If the Druid AI Agent has more messages, the CC immediately makes another POST request to `getMessages` to retrieve the next one. This continues until no more messages are received.

For each response received:

1. The CC passes the text response to the Voice AI Agent.
2. The Voice AI Agent checks if the response contains instructions to transfer the call to a human agent.
3. If it does not contain transfer instructions, the Voice AI Agent transforms Text to Speech.
4. The Voice AI Agent responds to the CC with voice (SIP connection).
5. The CC responds to the user with voice.
6. User Closes the Call:
7. The CC announces the Voice AI Agent that the conversation is closed.
8. The Voice AI Agent announces the Druid AI Agent that the conversation is closed (e.g., by sending a close\_conversation message).
9. Transferring the Call to a Human Agent. If a "route-to-human" event is received via the getMessages polling:
10. The Voice AI Agent announces to the CC to transfer the call to a human.
11. The CC executes the transfer.
12. The helpdesk agent and user are now talking directly.

### Prerequisites

* For DRUID on premise deployments, make sure that you provide inbound access from the following messaging endpoint: DRUID.BotApp.

### VoiceText Channel Integration

The VoiceText channel is active by default in Druid. To integrate your AI Agent with a third-party Voice AI Agent, from Druid Portal, AI Agent settings, go to channels, click **VoiceText** and copy the values of **Authorize URL** and **AI Agent URL**.

![](<../../../.gitbook/assets/2 URLS.png>)

If you want to use the long polling asynchronous mechanism, tap on **Enable long polling** and copy the **URL** as well.

![](<../../../.gitbook/assets/long pulling enable.png>)

Use these values to configure your Voice AI Agent and make API calls to DRUID.

The following fields are available in DRUID:

* **\[\[ChatUser]].ChannelId** = "voicetext"
* **\[\[ChatUser]].UserId** - Stores the user's unique identifier.

### DRUID API Reference

This section describes the DRUID APIs you should use for VoiceText channel integration.

#### Authorize

POST: Use the Authorize URL `*.druidplatform.com/api/services/app/Chat/AuthorizeAnonymousAsync`

**Request Body**

**Authorize API**

```
{
   "botId": "<bot_id>",
   "queryString": "phone=<phone>",
   "channelId": "voicetext"
}
```

**Response**

**Response Example**

```
{
   "botId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
   "userId": "string",
   "conversationId": "string",
   "token": "string"
}
```

The returned token has a validity of 1 hour.

#### Send Messages (Create Activity)

Use this API to send User Says to the Druid AI Agent.

**Syntax**

POST: Use the AI Agent URL `*.druidplatform.com/api/voicetext/``{botId}``/messages`

**Request Header**

In the request header, map the Authorize key to the bearer token obtained from the Authorize API. Use the DRUID-specific `CONCAT` function for the Authorize key value with the following syntax:

**Authorize value mapping**

```
CONCAT('Bearer ',[[Entity]].StringField)
```

Here, `[[Entity]].StringField` represents the field that stores the token obtained from the Authorize API.

![](<../../../.gitbook/assets/authorize concat.png>)

**Request Body**

**Request Body template**

```
{
    "type": "message",
    "channelId": "voicetext",
    "conversation": {
            "id": "<conversationId>"
    },
    "from": {
            "id": "<userId>"
    },
    "text": "<user says>",
    "timeout": 50
 }
```

The timeout parameter enables you to specify a duration in seconds for the system to wait for a response from the Flow Engine. If the Flow Engine doesn't respond within the configured timeout period, the system will log an error in the Conversation History.

**Responds with Message**

```
{
    "type": "message",
    "channelId": "voicetext",
    "conversation": {
            "id": "<conversationId>"
    },
    "to": {
            "id": "<userId>"
    },
    "text": "<AI Agent response>",
    "speak": "<AI Agent response>"
}
```

{% hint style="info" %}
**NOTE:** You should take the content from “speak”. In Druid Portal, you can fine-tune the text response for voice channel in the Voice section on your specific flow step(s). You can include SSML markups as recognized by your TTS service. By default, Druid uses [Microsoft schema](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-synthesis-markup?tabs=csharp).
{% endhint %}

**Responds with Event (transfer to human)**

```
{
     "type": "event",
     "channelId": "voicetext",
     "conversation": {
            "id": "<conversationId>"
     },
     "to": {
           "id": "<userId>"
     },
     "name": "route-to-human",
     "value": "input_mapping_json_object"
 }
```

{% hint style="info" %}
**NOTE:** To transfer calls to humans, in Druid Portal add a step of type Backchannel and name the step with your preferred keyword (e.g. “route-to-human”). In Input mapping on this step, set the Druid entity storing additional information (e.g., subject, queue name, etc.); provide the entity you agreed with the Contact Center. The response sent by Druid to the Voice AI Agent in JSON format will have in the “value” attribute the Druid entity provided in Input mapping.
{% endhint %}

#### Get Messages (Long Polling)

Get messages from the Druid AI Agent when using the long polling mechanism.

**Syntax**

POST `*.druidplatform.com/api/voicetext/{botId}/messages/getMessages`

**Request Header**

In the request header, map the Authorize key to the bearer token obtained from the Authorize API. Use the DRUID-specific `CONCAT` function for the Authorize key value with the following syntax:

**Authorize value mapping**

```
CONCAT('Bearer ',[[Entity]].StringField)
```

Here, `[[Entity]].StringField` represents the field that stores the token obtained from the Authorize API.

![](<../../../.gitbook/assets/authorize concat.png>)

**Request Body**

```
{ 
  "conversationId": "your-conversation-id", 
  "mergedResponse": true 
} 
```

**Parameters**

| Parameter      | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                | Required |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| conversationId | String  | The unique identifier for the ongoing conversation, obtained from the Authorize API response.                                                                                                                                                                                                                                                                                                                              | Yes      |
| mergedResponse | Boolean | Set to true to receive all available AI Agent messages for the current turn combined into a single response payload. This can reduce the number of `getMessages` calls required for multi-message responses. This is the default value, in case the parameter is not sent in the request. If false or omitted, DRUID will return messages one by one, requiring a separate `getMessages` call for each individual message. | No       |

**Response**

The response structure for `getMessages` is identical to the _Responds with Message_ and _Responds with Event (transfer to human)_ sections described for SendMessages API response, containing the AI Agent response or an event.

{% hint style="info" %}
**NOTE:** The getMessages endpoint will return the next available message or event as soon as it's ready, or after a timeout period if no message is available. The Contact Center should continuously poll this endpoint until the conversation is officially closed.
{% endhint %}
