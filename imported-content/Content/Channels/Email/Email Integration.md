---
layout:
  title:
    visible: false
---

<a id="Email"></a>

# Email

> **IMPORTANT!** The Email channel is deprecated starting with Druid 9.11. If you already have it configured from an earlier version, it will continue to work. However, you won’t be able to create new configurations in later versions. Use the [Outlook channel](../Outlook.md) instead.

You can configure your AI Agent to communicate with users via email through the Bot Framework. By configuring your AI Agent to access an email account, it receives a message when a new email arrives. This enables the AI Agent to use email as a channel for responding to user inquiries, such as sending an email reply to a user message.

> **NOTE:**
>
> - The Email channel works with Office 365 only. Other email services are not currently supported.
> - This channel is available in DRUID version 7.0 and higher and only in cloud and hybrid DRUID deployments. You cannot activate the channel in DRUID on-premise deployments.
> - The Email channel only supports message steps. Rich content flow steps (such as hero cards or choice steps) are not supported.

<a id="Prerequisites"></a>

## Prerequisites

Before configuring the Email channel, ensure you have:

- A published a AI Agent.
- A dedicated M365 email account for the AI Agent. This account must use Modern authentication (OAuth). Contact your company's email administrator to obtain this dedicated M365 email account.
- The AI Agent M365 email account must be logged into any Microsoft 365 product in your browser before you start configuration.

<a id="ConfiguringtheEmailchannel"></a>

## Configuring the Email channel

To configure the Email channel, follow these steps:

1. Log in to the Druid Portal and select your AI Agent.
2. Click the **Channels** tab.
3. Search for 'email' and click the **Email** card.

![](../../Resources/Images/Email%20channel/email%20card.png)

The channel configuration modal appears.

4. In the **Email address** field, enter the dedicated Office 365 email account for the AI Agent and click **Authorize**.

![](../../Resources/Images/Email%20channel/email%20field.png)

> **IMPORTANT!** Do not enter your own personal email account, as every message sent to that email account will be forwarded to the AI Agent. This can result in the AI Agent inappropriately sending a response to a sender. For this reason, AI Agents should only use dedicated M365 email accounts.

5. The 'Sign in to your account' pop-up opens.
> **NOTE:**  If the pop-up does not open, check that your browser is not blocking pop-ups. Always allow pop-ups and redirects from the Druid AI Platform.

6. Sign in with the dedicated M365 email account.

![](../../Resources/Images/Email%20channel/sigend%20in.png)

7. After successful sign-in, a page opens displaying a validation code. Copy this code.

![](../../Resources/Images/Email%20channel/validation%20code.png)

8. Return to the Druid Portal. In the **Code** field, paste the validation code to finish authorizing the AI Agent email address.

![](../../Resources/Images/Email%20channel/code%20field.png)

9. Click the **Publish** button. The channel activation might take up to 1 minute.

After the channel activates, the following fields are available in Druid:

- **[[ChatUser]].ChannelId** = "email"
- **[[ChatUser]].UserId** - Stores the email address of the sender.

<a id="Inactivatingthechannel"></a>

## Inactivating the channel

To inactivate the channel, follow these steps:

1. Go to the Channels page, and click on the **Email** card.
2. Click **Authorize** and sign in with the dedicated Office 365 email account .
3. After successful sign-in, a page opens displaying a validation code. Copy this code.

![](../../Resources/Images/Email%20channel/validation%20code.png)

4. Return to the Druid Portal. In the **Code** field, paste the validation code.

![](../../Resources/Images/Email%20channel/disable.png)

5. Click **Disable** to inactivate the channel.
