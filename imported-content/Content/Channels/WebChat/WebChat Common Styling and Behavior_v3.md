---
layout:
  title:
    visible: false
---

<a id="WebChatCommonStylingandBehaviorBotframeworkv3"></a>

# WebChat Common Styling and Behavior (Bot framework v3)

When configuring the webchat widget, you can configure specific widget parameters. To do so, click the **Edit Parameters** button.

![](../../Resources/Images/WebChat/edit%20parameters.png)

The WebChat widget parameters display in JSON format. Make the desired value changes and click the **Update** button.

![](../../Resources/Images/WebChat/update%20widget%20parameters.png)

If you don’t want to save the changes, click **Cancel**.

<a id="WebChatCommonStylingParameters"></a>

## WebChat Common Styling Parameters

The Druid Portal provides you with parameters which allow you to set the basic UI styling of your webchat.

![](../../Resources/Images/WebChat/UI%20parameters.png)

| Parameter | Default value | Description |
| --- | --- | --- |
| autoExpandEnabled | False | When set to true, it sets the web chat to always expand (open), independent of **DruidWebChatIsOpenedEnabled**. Useful when used together with "fullScreenMode" set to true, it will automatically expand the chat widget directly in full screen mode. |
| chatHeaderHeight | 38px | The height of the widget header. |
| chatTitle | Webchat | The webchat title. |
| chatTitle\_faIcon |  | The [favicon](https://fontawesome.com/icons?d=gallery&m=free) displayed in front of the webchat title.  Example: "chatTitle\_faIcon": "fa-commenting" |
| containerElement | Null | Specifies the web chat expand DOM element. Must be set in the format: " document.getElementById('DruidContainerElement') ", where DruidContainerElement is the container element. |
| contextMenuIcon | fa-plus-circle | Sets the fa icon for the context button. For the list of available icons, see [Font awesome](https://fontawesome.com/icons?d=gallery&m=free). |
| DruidShowGroupTimestamp | 10000 | The timestamp of the messages, in chat widget, can be displayed for each and every message, or only once, for a group of messages received from the AI Agent in a certain time interval. In case the AI Agent will send 4 messages in a row, all within 3 seconds, then only the timestamp of the last message will be displayed.  The value of this parameter sets the time interval for which only one timestamp will be displayed:   - **false** - hides all timestamps. - **0** - hides all timestamps for consecutive sent/received messages except the last one if the difference between them is less than the specified value. |
| expandWidth | Unset | The width of the chat widget when expanded. When set to "unset" it will inherit the default value. |
| extendedLocalizedString - timeSent |  | Sets the characters placed between AI Agent Name and timestamp. Ex: " @ %1" will display "BotName @ 14:25:07" Note: %1 represents the timestamp. It must NOT be deleted or edited. Only the characters in front of %1 can be changed. Examples: " -- %1" " @ %1" " at %1" |
| floatRight | 10% | The distance between the widget and the browser's right border, expressed in percentage of the screen width. |
| fullScreenMode | False | Overlaps covering entire page. |
| fullScreenMode\_leftRightClass | col-md-3 | Keeps the right side space. You ca use it to dynamically load content during the conversations using the Back Channel step. |
| fullScreenMode\_mainChatClass | col-md-6 | The space used by the chat control in full page mode. |
| goBackButton | False | When set to true, renders the "Back" button instead of the contextual menu. |
| height | 60vh | The height of the collapsed web chat widget. |
| iconCloseChat | fa-angle-down | Font awesome chat title close icon. |
| iconSendSvgType | 2 | Sets the "send message" icon type. Values: 1 or 2. |
| inputIconsAlignment | Left | Sets the "Send message" and "Upload file" buttons alignment left or right. Values: left, right. |
| inputPlaceholder | Type your message here... |  |
| loadingOverlayActive | false | Enables the "loading..." animation at chat activation in case the conversation takes longer to initiate than usual. |
| minWidth | 25vw | Minimum width of the web chat widget. |
| position | right | The web chat’s position relative to the bottom of the page. Values: left, right. |
| suggestedActionsInputPlaceholder |  | Sets the text to be displayed over the text input are, when conversation reaches a step with the **BlockUserInput** option enabled (see [Flow Step](../../4_Flows/Common%20Flow%20Settings.md)). |
| typingMessageBackground | Null | The background color of the "typing" message bubble. Values: HTML color codes.  Ex: "typingMessageBackground": "red".  ![](../../Resources/Images/WebChat/typing%20message%20background.png) |
| visibleAtScrollTop | false | When set to true, the webchat is hidden on page opening and it will become visible only when the user scrolls down. |
| width | 430px | The width of the collapsed web chat widget. |

<a id="WebChatCommonBehaviorParameters"></a>

## WebChat Common Behavior Parameters

| Parameter | Default value | Description |
| --- | --- | --- |
| backgroundTrafficEnabled | true | When set to true, the webchat control sends telemetry information to the Druid AI Platform. Telemetry information includes the timestamp when a message was sent or received. |
| cookieDomain |  | The two Druid cookies are linked with the specified domain. |
| conversationTokenEnabled | true | Saves the conversation token in browser cookie to remember the user when returning in webchat. |
| DruidCookiesExpirationInDays | 1 | The two Druid cookies, **conversationTokenEnabled** and **DruidCookieConsentEnabled** expire after X days. |
| DruidWebChatIsOpenedEnabled | true | Automatically expands the webchat control. It is useful to the conversation with the AI Agent when navigating between web pages. |
| instrumentationKey |  | Provided by Druid for telemetry logging. Contact [Druid Tech Support](<mailto:support@druidai.com?subject=Telemetry logging: Need instrumentationKey>) to get one.  **NOTE:** This parameter is obsolete starting with Druid 8.1. |
| notificationsEnabled | false | Sends a sound notification when a new message is received in the chat. |
| queryParams |  | ?param1=value&param2=value  The params are sent within the conversation context and are mapped with entity QueryParams.  Create string fields in the QueryParams entity with the param names to address the conversation slots and use them in your flows: QueryParams.params1, QueryParams.params2  **NOTE:**  For directline (web channel), Druid version 1.59 or higher automatically collects the following information related to the device used by the user to chat with the AI Agent. For more information, see [System Entities](../../5_Entities/System%20Entities.md), [[QueryParams]] system entity. |
| serviceNetworkStatusEnabled | true | Locks the chat control and displays “Network lost” messages when the Internet connection is lost. |
