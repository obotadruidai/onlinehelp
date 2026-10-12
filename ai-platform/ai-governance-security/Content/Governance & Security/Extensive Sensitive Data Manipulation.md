---
title: Extensive Sensitive Data Manipulation
---


Druid provides authors with extensive options to create AI Agents able to securely capture sensitive data from chat users (passwords, credit card numbers, etc.) / receive secure data from external systems and transfer it in an encrypted way to third party applications using connector integrations.

This section describes how you can author the AI Agent so that you address data encryption on different layers throughout a conversation.

## Capturing sensitive data securely

{% hint style="info" %}
**NOTE:** Sensitive data manipulation is only available on prompt steps on both direct line and MS Teams channel. For sensitive data manipulation in MS Teams channel, an additional configuration step is required. For more information, see [Configuration for Sensitive Data Manipulation](https://druidai.gitbook.io/druid-ai-docs/channels/social-media-and-chat/ms-teams-integration/teamschannel_sensitivedatamanipulation).
{% endhint %}

To securely capture user sensitive data / receive sensitive data from external systems, in Input Mapping on prompt steps, use fields which have **Holds Sensitive Data** selected.

![](<../../.gitbook/assets/entity holds sens data.png>)

By default, the maximum security configuration for sensitive data manipulation. In default configuration, Druid masks the sensitive data in the web chat (the value provided by the user and sent by the AI Agent to the user), in the conversation history (including Chat Activity Data) and in connector logs. You can select the configuration that suits your needs best. For more information on how to configure the entity fields that will store sensitive data and the different configurations available, see [Manipulate Sensitive Data](<Extensive Sensitive Data Manipulation.md#Manipulate_Sensitive_Data>).

The figure below provides a prompt step example where the user is asked to provide the password (that is, sensitive data).

![](../../.gitbook/assets/sensitive.png)

Whenever a prompt step that will store sensitive data is executed, the **Cancel** button is automatically displayed in the chat giving the user the possibility to continue the conversation without proving the requested sensitive data.

If the user clicks the **Cancel** button, the following string is stored in the entity field specified in Input mapping on the prompt step: “UserCanceledInput”. You can use this value at authoring time to provide alternative conversation paths.

The user data will be encrypted using a Druid proprietary encryption method from the moment the user inputs data in the chat and remains encrypted while being transmitted to the connector. The connector will decrypt the data using a Druid proprietary decryption method and send the data to external systems (if data encryption is not set on connectors).

When an AI Agent deployed in the MS Teams channel asks the user to enter sensitive data, it has a channel-specific behavior. For more information, see [Prompt Steps Configuration](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/conversational-flows/flow-steps/prompt-steps-configuration).

## Manipulate Sensitive Data <a href="#manipulate_sensitive_data" id="manipulate_sensitive_data"></a>

Druid offers robust options for managing sensitive data within entity fields, ensuring maximum security and compliance. By effectively managing entity fields and sensitive data, you can optimize your AI Agent functionality while upholding stringent security standards.

Enable the **Holds Sensitive Data** option to encrypt user data using proprietary encryption methods.

{% hint style="info" %}
**NOTE:** Tapping on **Holds Sensitive Data** activates the first three options to ensure by default maximum security configuration when it comes to manipulating sensitive data. In default configuration, Druid masks the sensitive data in the web chat (the value provided by the user and sent by the AI Agent to the user), in the conversation history (including Chat Activity Data) and in connector logs.
{% endhint %}

Regardless which configuration you use for sensitive data manipulation, Druid always encrypts the data using a proprietary encryption method from the moment the user inputs data in the chat and remains encrypted while being transmitted to the connector. The connector will decrypt the data using a Druid proprietary decryption method and send the data to external systems.

### Hide In Web Chat

Druid masks in the web chat both the value provided by the user, and the one sent by the AI Agent to the user.

![](<../../.gitbook/assets/Manipulating Sensitive Data.png>)

{% hint style="info" %}
**NOTE:** Ticking off this option, Druid will mask the user input in the chat but the AI Agent will send the value in clear to the user in the chat.

<img src="../../.gitbook/assets/unhide from chat.png" alt="" data-size="original">
{% endhint %}

### Encrypt In Conversation History

Druid encrypts the value provided by the user in the Conversation History database and in the Chat Activity Data.

### Encrypt In Connector Logs

Druid encrypts the value provided by the user in the Connector logs.

{% hint style="info" %}
**NOTE:** If the Encrypt In Connector Logs option is not selected, by default, user’s value will be available for operations in Flows.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** For debugging and auditing purposes, decrypting the sensitive data from Conversation History and Connector Logs is possible, but requires **Decrypt Sensitive Data** privileges.
{% endhint %}

### Available For Operations In Flows

You can use the user’s value during the conversation flow runtime, to manipulate the context data stored in sensitive fields: alter the data, perform RegEx validation, calculations, show the information in a message, etc.).

{% hint style="warning" %}
**IMPORTANT!** The Druid AI Platform decrypts the data from the sensitive entity fields ONLY during the execution of the required operation (validation, calculations, etc) – in the rest of the time, sensitive data remains encrypted in the conversation context.
{% endhint %}

When working with Set variables, authors must assure that, when moving values form one entity field  to another, both entity fields involved have IDENTICAL sensitive data configuration (“Available for operations in flows” attribute is the same for both entity fields).

![](<../../.gitbook/assets/Manipulating Sensitive Data_1.png>)

The table below provides the allow manipulation matrix of the two fields used in Set Variables.

|                                            |                                           |                                            |
| ------------------------------------------ | ----------------------------------------- | ------------------------------------------ |
|                                            | Field A – Available for operations = TRUE | Field A – Available for operations = FALSE |
| Field B – Available for operations = TRUE  | same encrypted value                      | double encrypted                           |
| Field B – Available for operations = FALSE | same encrypted value                      | same encrypted value                       |
| Field B does not hold sensitive data       | data in clear                             | same encrypted value                       |

{% hint style="warning" %}
**IMPORTANT!** Set variables between two encrypted entity fields is possible as long as both entity fields have the same setting to allow or not manipulation (**Available For Operations In Flows** option); otherwise, irreversible double encryption or even decryption of data might occur.
{% endhint %}

## Transmitting sensitive data to third party applications in a secure way

DRUID enables authors to address the cases when third party applications require that specific user information is transmitted in a secure way to ensure that unauthorized parties do not tamper or spoof the data.

![](<../../.gitbook/assets/extensive integration.png>)

You can achieve this by designing your AI Agent to encrypt the data transmitted by Druid connectors using the AES GCM encryption algorithm.

Constructed from the Advanced Encryption Standard (AES) algorithm with a block size of 128 bits, AES with Galois/Counter Mode (AES-GCM), a state of the art encryption algorithm, that is a block cipher mode of operation that provides high speed of authenticated encryption and data integrity.

To achieve data transmission to third party systems in a secure way, follow these two steps:

### Step 1. Set data encryption when defining the connection strings (app)

On the connector app, select the encryption type AES CGM and generate an encryption key.

![](<../../.gitbook/assets/conn encryption.png>)

If you want to encrypt the data with a higher level of security, on connector apps, select **Secure encryption with salt**. By doing so, Druid will alter the fields with a random 64-bit salt and then will encrypt the data using the AES CGM algorithm and the encryption key from the connector app specified in the Encrypt Data integration task.

### Step 2. Use the Encrypt Data integration task

Use **Encrypt Data** as the first integration task on all connector actions (if needed) to encrypt user data stored in specific Druid entity fields (fields from the request entity set on the connector action), and store the encrypted data temporarily at runtime during the execution of the integration tasks within that connector action.

When defining the connector actions, you first encrypt the data based on your needs by using the Encrypt Data integration task, and then use that data on subsequent tasks.

![](<../../.gitbook/assets/encrypt data.png>)

If you want to add data encryption on existing connector actions, add the **Encrypt Data** task, configure it and then use the drag and drop functionality to make it the first integration task to be executed in that connector action.

{% hint style="info" %}
**NOTE:** Use Encrypt Data as the first integration task on a connector action only if you are using the encrypted data on subsequent integration tasks within that action; otherwise, the encrypted data remains inside the connector, Druid will not transmit it to 3rd party systems.
{% endhint %}

For more information on the Encrypt Data integration task and how clients receiving the encrypted data can decrypt it, see [Encrypt Data](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/identity-and-encryption/encryptdata).
