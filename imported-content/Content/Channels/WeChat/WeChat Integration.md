---
layout:
  title:
    visible: false
---

<a id="WeChat"></a>

# WeChat

WeChat is a widely used messaging application. It’s also the only messaging app used by citizens of China.

To make it easy for your consumers to make purchases and get answers to questions using WeChat, the messaging channel they already use every day, DRUID authors can integrate AI Agents with WeChat. This way, customers will be able to start a conversation with your AI Agent in WeChat.

> **NOTE:** DRUID currently supports only image uploads from WeChat (no image downloads). The supported image formats are .jpg, .jpeg and .png.

This section describes how to integrate your AI Agent with the WeChat channel.

<a id="Prerequisites"></a>

## Prerequisites

- You built and published a AI Agent.
- You have an [official WeChat account](https://mp.weixin.qq.com/?lang=zh_CN&token=).
- Contact [Druid Tech Support](<mailto:support@druidai.com?subject=Need URL for WeChat Integration>) to get the server URL and IP address for WeChat integration.
- For DRUID on premise deployments, make sure that you provide access to/from the necessary messaging endpoints as follows:

|  |  |
| --- | --- |
| Outbound | api.weixin.qq.com |
| Inbound | DRUID.BotApp |

This section describes how to integrate your AI Agent with WeChat.

<a id="Step1ConfigureyourWeChatofficialaccount"></a>

## Step 1: Configure your WeChat official account

1. Go to [WeChat Official Accounts Platform](https://mp.weixin.qq.com/?lang=zh_CN&token=) and log in either by scanning the QR code or by using your WeChat credentials.

![](../../Resources/Images/WeChat/wechat%20log%20in.png)

2. On the main menu, scroll down to Development and click **Basic Configuration**.
3. In the Server Configuration section, click the **Change Configuration** button. The server configuration page appears.
4. In the **URL** field, enter the server address URL provided to you by Druid Tech Support.
5. In the **Token** field, enter a token in English letters or numbers with a length between 3 and 32 characters.
6. Click the **Random Generation** button. An EncodingAESKey is generated.

![](../../Resources/Images/WeChat/wechat%20server%20configuration.png)

7. Write down the token and the EncodingAESKey, you will need them to configure the AI Agent.
8. Select **Plain Text Mode** for message encryption.
9. Click the **Submit** button to save the server configuration. The Basic Configuration page appears.
10. Write-down or copy/paste to a document the **Developer ID (AppID)** and the **Developer Password (AppSecret)**.

    ![](../../Resources/Images/WeChat/developer%20ID.png)

    If you forgot the AppSecret (password), generate a new one by clicking Reset and passing the two-factor authentication:

    1. Scan a QR code on the webpage.
    2. Re-enter your account password.
11. Once you have completed the security verifications, a new App Secret is generated. Write it down or copy/paste it to a document. Then click the **Confirm and Next**.
12. Add the server IP address you received from Druid Tech Support to the **IP Whitelist**. To do, follow these steps:
    1. Click the View link next to the **IP whitelist** field. The Check IP Whitelist page appears.

    ![](../../Resources/Images/WeChat/check%20ip%20whitelist.png)

    2. Click **Modify**. The IP Whitelist Settings page appears.
    3. Enter the IP address you received from Druid Tech Support.

    ![](../../Resources/Images/WeChat/IP%20whitelist.png)

    4. Click **Confirm modification** to save the changes. The page closes.
13. On the main menu, scroll-down to Settings and click **Account Info**. The Account details page appears.
14. Download the QR code. Once you complete the WeChat integration you will have to make the QR code public for customers.

![](../../Resources/Images/WeChat/download%20qr%20code.png)

15. Scroll-down to the Registration information section and write down or copy/paste to a document the value from the **Original ID** field, you will need it for AI Agent configuration.

![](../../Resources/Images/WeChat/original%20id.png)

Check again that you have the values of the following fields: Token, EncodingAESKey, Developer ID (AppID), Developer Password (AppSecret)and Original ID.

<a id="Step2ConfiguretheAIAgent"></a>

## Step 2: Configure the AI Agent

1. Log in the Druid Portal and from the main menu, select your AI Agent. The AI Agent configuration page appears by default on the **Details** tab.
2. Click the **Channels** tab, then click **WeChat**. The WeChat Channel Info section expands.

![](../../Resources/Images/WeChat/WeChat%20Channel%20info.png)

3. Fill in the fields with information from the WeChat official account configuration, as follows:

| Druid Field | WeChat Official Account Field |
| --- | --- |
| Account Id | Original ID |
| App Id | Developer ID (AppID) |
| App Secret | Developer Password (AppSecret) |
| Token | Token |
| Encoding AES Key | EncodingAESKey |

4. Click the **Publish** button. The channel activation might take up to 1 minute, wait until it completes.

After the channel's activation, two fields are available in DRUID:

- **[[ChatUser]].ChannelId** = "wechat"
- **[[ChatUser]].UserId** - Stores the unique identifier of the WeChat user account.

5. Click the **Save & Close** button.

<a id="Step3MaketheWeChatQRCodepublic"></a>

## Step 3: Make the WeChat QR Code public

After you successfully complete the WeChat integration, you have to make the WeChat QR code available for your customers (either on your website or printed on a paper in the shop). Your customers will open the WeChat app and scan the QR code to chat with your AI Agent.

## Related Topics

- [Handling Authentication](../../How%20to/Handling%20Authentication.md)
