---
title: WebChat
---


The WebChat channel is enabled by default in the Druid Portal. This allows you to quickly deploy your AI Agent to any web page using a pre-configured snippet.

## Configure the WebChat Channel

The Druid web chat is comprised of two elements:

* web chat widget
* web chat landing page (expanded widget).

The Druid AI Platform provides you with a default web chat configuration you can embed into your website. You can further style the web chat to comply with your brand style guide.

The default webchat configuration is illustrated in the figures below. By default, the web chat displays collapsed on the page hosting the webchat.

_**Figure:** Collapsed web chat_

![](<../../../.gitbook/assets/collapsed widget.png>)

Clicking the collapsed web chat will expand it:

_**Figure**: Expanded web chat_

![](<../../../.gitbook/assets/expanded web chat.png>)

To configure an AI Agent for web integration, follow these steps:

1. Go to the AI Agent settings.
2. Click the **Channels** tab.
3. In the Channels page, search for **WebChat**.

![](<../../../.gitbook/assets/webchat card.png>)

4. Click the WebChat card to open the channel configuration modal.

![](<../../../.gitbook/assets/webchat snippet.png>)

5. Optionally, in the **Avatar image URL** field, enter the URL for the custom AI Agent profile picture. This avatar will be displayed in the webchat header and for all messages sent by the AI Agent.
6. Click the **Customize webchat** button and customize the WebChat styling and behavior parameters according to preference. For more information, see [WebChat Common Styling and Behavior](WebChat_Common_Styling_and_Behavior_v4.md).
7. Optionally, customize channel display settings as follows:
   * **Alias**: Enter a clear, business-friendly display name (e.g., Interactive Messaging). This value is stored in\*\*\[\[ChatUser]].ChannelDisplayName\*\*, which appears in reporting tools like AI Agent Summary dashboard - Engagement KPIs and can also be referenced in flow business logic.
   * **Description**: Enter a brief description. This is particularly helpful when using an alias, as it helps identify the channel's specific purpose within the Druid Portal.
   * **Channel Icon**: Upload a custom icon to display on the channel card within the Druid Portal.
8. Click **Publish** to activate the channel.

After the channel's activation, the following fields are available in Druid:

* **\[\[ChatUser]].ChannelId** = "directline"
* **\[\[ChatUser]].ChannelDisplayName** - Stores the Alias which is used in AI Agent Summary Dashboard > Engagement KPIs > Channel chart.

## Deploy the WebChat Snippet <a href="#deploy" id="deploy"></a>

Once you have finalized the WebChat configuration, copy the code from the **WebChat snippet** field and embed it into the HTML of your website hosting the AI Agent. Ensure the script is placed within the appropriate tags of your HTML web page (\*\* \*\*and tags) to initialize the chat component.

{% hint style="info" %}
**NOTE:** Do not change anything in the snippet, otherwise the webchat might not be properly embedded into the hosting page(s).
{% endhint %}

{% hint style="info" %}
**Info:** If you don’t see the changes on your website, you clear the cache or exit the incognito mode (if browsing in incognito mode).
{% endhint %}

The default snippet contains:

1. A css file which contains the layout of the webchat widget (under the tag)

![](<../../../.gitbook/assets/css screen 1.png>)

2. A script file which renders the webchat widget (within the tags)

![](<../../../.gitbook/assets/css screen 2.png>)

3. A script which initializes the webchat component on document load.

![](<../../../.gitbook/assets/css screen 3.png>)

{% hint style="warning" %}
**IMPORTANT!** If the default snippet does not display the 3 components make sure that you disable **Single-line initialization**.

<img src="../../../.gitbook/assets/sinle line.png" alt="" data-size="original">
{% endhint %}

## Related Topics

* [Handling Authentication](https://druidai.gitbook.io/druid-ai-docs/ai-platform/how-to/handling-authentication)
* [WebChat Common Styling and Behavior (Bot framework v3)](https://docs.druidai.com/docs/Content/Channels/WebChat/WebChat%20Common%20Styling%20and%20Behavior_v3.htm)
* [WebChat Common Styling and Behavior](WebChat_Common_Styling_and_Behavior_v4.md)
