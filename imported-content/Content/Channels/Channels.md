---
title: "Channels"
---

<a id="Channels"></a>


Multi-channel deployment is supported by Druid and offers a wide range of digital channels in multiple languages so you can reach your customers wherever they like to be, in their natural digital way. With Druid conversational platform you will deliver the experience your customers and employees expect.

The Druid AI Platform enables authors and business users with no programming skills to create AI Agents which can be easily exposed in the preferred channels:​

- External channels: Mobile App, [Web](WebChat/WebChat.md), [WhatsApp](WhatsApp%20Integration/WhatsApp%20Integration.md), [Facebook Messenger](Facebook%20Integration/Facebook%20Integration.md) etc.
- Internal channels: [Microsoft Teams](MS%20Teams/MS%20Teams%20Integration.md), Intranet, [Slack](Slack%20Integration/Slack%20Integration.md).​

Cross-channel interaction is also available. In addition to standard channels mentioned above, Druid offers support for other channels:

![](../Resources/Images/Deployment/channels.png)

The table below provides you with an overview of the different channels integration across Druid deployments.

| Channel | Cloud | Hybrid | On premise |
| --- | --- | --- | --- |
| Direct line (WebChat) | Y | Y | Y |
| MS Teams | Y | Y | N |
| WhatsApp | Y | Y | Y\* |
| Facebook Messenger | Y\*\* | Y\*\* | Y\*\* |
| Slack | Y | Y | N |
| GoogleChat | Y | Y | Y |
| WeChat | Y | Y | Y\* |
| Telegram | Y | Y | Y |
| Viber | Y | Y | Y\* |
| Twilio SMS | Y | Y | N |
| Sakari | Y | Y | N |
| Instagram | Y | Y | Y |
| LINE | Y | Y | N |
| WeCom | Y | Y | Y\* |
| Webex | Y | Y | Y |
| Email | Y | Y | N |
| Outlook | Y | Y | N |

\*Only available if specific DRUID services have open connection to the Internet.

\*\*In DRUID hybrid and cloud deployments Facebook channel uses the Microsoft Bot Framework, while in on premise deployments it uses direct DRUID Facebook integration.

<a id="DeactivatingActiveChannels"></a>

## Deactivating Active Channels

Once you activate a channel, you can deactivate it at any time, by following these steps:

1. Log in the Druid Portal and from the main menu, select your AI Agent. The AI Agent configuration page appears by default on the **Details** tab.
2. Click the **Channels** tab, then click the active channel you want to disable. The channel section expands.
3. Click the **Delete channel** button (![](../Resources/Images/disable%20channel.png)). It might take up to a minute until the channel becomes inactive.

You can always re-activate an inactive channel by clicking the **Publish** button in the channel section.
