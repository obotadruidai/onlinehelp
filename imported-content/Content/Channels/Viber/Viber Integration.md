---
title: "Viber"
---

<a id="Viber"></a>


Druid authors can integrate AI Agents with Viber to allow their customers to start a conversation with the AI Agent in the Viber app.

> **IMPORTANT!** The Welcome flow will be triggered at the user's first conversation with the AI Agent; the predict with the initial "user says" is dropped.

<a id="Prerequisite"></a>

## Prerequisite

- You need to have an Active Viber account on a platform which supports AI Agents (iOS/Android). This account will automatically be set as the account administrator during the account creation process.
- For DRUID on premise deployments, make sure that you provide access to/from the necessary messaging endpoints as follows:

|  |  |
| --- | --- |
| Outbound | chatapi.viber.com |
| Inbound | DRUID.BotApp |

<a id="IntegratingyourAIAgentwithViber"></a>

## Integrating your AI Agent with Viber

This section describes how to integrate your AI Agent with Viber.

<a id="Step1CreateanewViberbot"></a>

### Step 1. Create a new Viber bot

1. Go to [https://partners.viber.com](https://partners.viber.com/) and enter the mobile number associated to your active Viber account. You will receive a message with a code in the Viber messaging app.
2. Enter the code to
   activate access to the Public Chat Admin. You are logged in Viber's Public Chat Admin.

![](../../Resources/Images/Viber%20Integration/viber%20about.png)

3. On the left menu, click **Create Bot Account**.
4. On the right side of the screen, provide the mandatory information, accept the Terms and conditions and select the two Viber acknowledgements.

![](../../Resources/Images/Viber%20Integration/create%20viber%20bot_1.png)

![](../../Resources/Images/Viber%20Integration/create%20viber%20bot_2.png)

5. Click **Create**. Your Viber bot account is created and the token associated to your Viber bot is generated.
> **NOTE:** Copy the access token as you will need it in the Druid Portal.

![](../../Resources/Images/Viber%20Integration/account%20created.png)

<a id="Step2ConnectyourAIAgenttotheViberChatAPI"></a>

### Step 2. Connect your AI Agent to the Viber Chat API

1. In the Druid Portal, go to AI Agent settings, and then click the **Channels** tab.
2. Search for 'Viber' and click the **Viber** card.

![](../../Resources/Images/Viber%20Integration/viber%20card.png)

The channel configuration modal appears.

3. Enter / Paste the access token you copied when creating the Viber bot.

![](../../Resources/Images/Viber%20Integration/viber%20druid.png)

4. Click the **Publish** button. The channel activation might take up to 1 minute, wait until it completes.

After the channel's activation, two fields are available in DRUID:

- **[[ChatUser]].ChannelId** = "viber"
- **[[ChatUser]].UserId** - Stores an unique identifier of the Viber user account.

<a id="Step3TalktoyourAIAgent"></a>

### Step 3. Talk to your AI Agent

To open the AI Agent in the Viber channel, in the Druid Portal, go to the AI Agent settings, click the **Channels** tab and click on the Viber channel icon. You can start talking to the AI Agent.

<a id="Step4PublishyourViberbot"></a>

### Step 4. Publish your Viber bot

1. On your mobile device, open the Viber app.
2. At the bottom, tap on **More**.

![](../../Resources/Images/Viber%20Integration/viber%20app%201.jpg)

3. Tap on **Settings**.

![](../../Resources/Images/Viber%20Integration/viber%20app%202.jpg)

4. Tap on **My AI Agents**.

![](../../Resources/Images/Viber%20Integration/viber%20app%203.jpg)

5. Tap on your Viber bot.

![](../../Resources/Images/Viber%20Integration/viber%20app%204.jpg)

6. Tap on **Publish**.

![](../../Resources/Images/Viber%20Integration/viber%20app%205.jpg)

<a id="Step5MaketheViberbotQRCodepublic"></a>

### Step 5. Make the Viber bot QR Code public

After you successfully complete the Viber integration, you have to make the Viber bot QR code available for your customers (either on your website or printed on a paper in the shop).

![](../../Resources/Images/Viber%20Integration/qr%20code.jpg)

Your customers will open the Viber messaging app and scan the QR code to chat with your AI Agent.

> **NOTE:** In DRUID 7.4 and higher, when a user initiates a conversation with the AI Agent, the Welcome flow will be automatically triggered. Regardless of the user's subscription status to the AI Agent channel, the welcome message will be promptly sent to the user, ensuring a seamless and engaging interaction experience.

<a id="StartingspecificDruidFlowsviaViberDeepLinks"></a>

## Starting specific Druid Flows via Viber DeepLinks

Viber DeepLinks are a powerful mechanism to launch your AI Agent and immediately trigger a specific Druid flow by providing the associated flow Intent. This key capability moves beyond the default behavior of simply triggering the Welcome flow when a user initiates a chat. By allowing you to create targeted entry points, DeepLinks are ideal for QR code campaigns, enabling you to generate custom codes that direct users to specific actions or flows within your AI Agent.

> **NOTE:** Viber DeepLinks support is available in Druid version 9.9 and later.

<a id="DeepLinkFormat"></a>

### DeepLink Format

The link format used to generate QR codes that trigger a specific flow is: `viber://pa?chatURI=<URI>&context=<intent>`.

| Parameter | Description |
| --- | --- |
| <URI> | The name of the Viber bot that you created in the Viber Admin Panel. |
| <intent> | The intent of the flow you want to start when users scan the QR code generated with the DeepLink. |

<a id="GenericProcedure"></a>

### Generic Procedure

1. Identify the unique name (<URI>) of your Viber bot from the Viber Admin Panel.
2. Identify the exact name of the Druid flow intent that you want to be executed when the user scans the QR code.
3. Construct the DeepLink. Combine your AI Agent URI and target intent into the standard DeepLink format. E.g., `viber://pa?chatURI=my_druid_bot&context=check_product_info`.
4. Use a third-party QR code generator tool and input the complete DeepLink URL to create the scannable code.
5. Make the QR Code available for your users.

> **IMPORTANT!** DeepLinks are not directly accessible via a web browser. To start a specific DRUID flow via a Viber DeepLink, you must first use the DeepLink URL to generate a QR code, which users will scan. It requires the Viber application to be installed on the user's device to execute and launch the targeted Druid flow. If Viber is not installed, the link will fail or direct the user to an error message.
