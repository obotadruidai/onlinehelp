---
title: "Mobile App"
---

<a id="MobileApp"></a>


AI Agents can be deployed in mobile applications using the existing web channel (also called Direct Line) through a WebView implementation, which allows the display of web content (HTML, CSS, JavaScript).

> **NOTE:** Druid does not currently offer a native Software Development Kit (SDK) for mobile app integration.

Optionally, push notifications can also be configured to notify users about chat related events like new unread messages.

<a id="PlatformCompatibility"></a>

## Platform Compatibility

- iOS and Android platforms are supported.
- Cross-platform frameworks (like, React Native, Flutter, Ionic, etc.) can integrate AI Agents using WebViews, though some framework-specific limitations may apply.
- While AI Agents have not been extensively tested in mobile apps using the frameworks above, no major incompatibilities are currently known.
- Each platform and framework combination may behave uniquely due to variations in the WebView implementations.

<a id="TechnicalConsiderations"></a>

## Technical Considerations

AI Agents rely on standard web technologies, which may behave differently in WebView environments. Consider the following limitations when integrating with mobile applications:

- **Network Communication**. The AI Agent uses WebSockets for real-time communication with Druid backend services. Mobile operating systems may terminate these connections when the app is sent to the background to save battery.
- **Data Persistence**. Conversation history and user data are stored using browser cookies and local storage. This means reliability across all WebView implementations may not be consistent, potentially affecting data persistence.
- **Browser APIs**. The AI Agent may use browser-specific APIs (such as Web Speech API) that are not available or behave differently in WebView environments.
- **User Interface Behavior**. Input handling, virtual keyboard behavior, and element rendering may differ from standard web browsers.
- **URL Navigation**. URLs may open either within the WebView or in the device’s default browser, depending on platform behavior and the mobile app's implementation.
- **File Downloads**. The behavior of file download links varies by platform and the WebView implementation.

<a id="TestingandTroubleshooting"></a>

## Testing and Troubleshooting

Issues that cannot be reproduced in standard web browsers (Chrome, Safari, Edge, Firefox etc.) are considered WebView implementation-specific and must be addressed by the mobile development team. Druid can provide guidance on the AI Agent configuration but cannot troubleshoot WebView-specific behavior.

<a id="BackendServices"></a>

## Backend Services

The diagram below shows the communication flow within a mobile app integration.

![](../Resources/Images/Mobile%20Channel/mobile%20diagram.png)

Druid doesn't communicate directly with the mobile app. Instead, it securely connects through the Druid Connector Host, which interacts with the mobile app's backend service, part of the client’s internal systems. The Connector Host transmits the conversation ID and any new or unread messages to ensure users receive notifications when chatting with the AI Agent in the app. If the app is closed, new or unread messages are delivered via the app’s push notification system (Firebase for Android, APNs for iOS).

Additionally, the WebChat reports the number of read messages to the Conversational Engine through the AI Agent API.

<a id="PushNotifications"></a>

### Push Notifications

AI Agents can notify your backend system when new messages arrive. It is your backend’s responsibility to trigger the actual push notification to the mobile devices.

<a id="Authentication"></a>

### Authentication

Druid supports JWT tokens, SSO, and custom query parameters for user authentication during chat sessions. These can help the AI Agent identify and respond to authenticated users. For more information, see [Authenticating Users in the DRUID Webchat](WebChat/Authenticate%20Users%20in%20the%20Webchat.md).

<a id="Integration"></a>

## Integration

<a id="EmbedtheWebChatsnippetintheMobileApp"></a>

### Embed the Web Chat snippet in the Mobile App

1. On the **Channels** tab, in the WebChat section, customize the web chat snippet parameters as needed.  For more details, see [WebChat Common Styling and Behavior](WebChat/WebChat_Common_Styling_and_Behavior_v4.md).
2. Copy the web chat snippet and add it to your mobile app.

Users can now interact with the AI Agent directly from the mobile app.

<a id="AlternativeoptionCustomChatInterfaceviaAPI"></a>

### Alternative option: Custom Chat Interface via API

If you want to build your own custom chat interface instead of using the WebChat widget, the Druid AI Platform also exposes messaging APIs you can use to send and receive chat messages programmatically.

These APIs are part of the same backend services used for Druid voice channels (including Speech-to-Text and Text-to-Speech). While they have primarily been used for custom voice integrations so far, they can be adapted to support custom-built conversation interfaces in mobile or web applications.

> **NOTE:**  This integration path requires custom development effort and a deeper understanding of the Druid messaging layer. We recommend you to use this alternative only if the current integration does not meet your use case. Druid can provide technical guidance upon request.

<a id="Pushnotifications"></a>

## Push notifications

To enable push notifications for a mobile app deployment, follow these steps:

<a id="Step1Configureappandintegration"></a>

### <a id="Step_1"></a>Step 1. Configure app and integration

1. From the Solution Library, import solution **Bot message notifications**.
   The solution includes a predefined app and integration.
2. On the **Solution Contents** menu, click **Apps**, then select the **Message Notification** app.
3. Enter the **Base URL** of the mobile app backend service.

![](../Resources/Images/Mobile%20Channel/app%20details.png)

4. On the **Solution Contents** menu, click **Integrations**, then click on the **Send message status notifications** integration.
5. Update the request with the mobile app specific push notification endpoint. Map the following mandatory **MessageNotification** fields:

- [[MessageNotification]].ConversationId
- [[MessageNotification]].IncomingMessagesCount
- [[MessageNotification]].LastMessageOn

![](../Resources/Images/Mobile%20Channel/map%20fields.png)

6. Publish the integration.

<a id="Step2EnabletheAIAgentAPI"></a>

### Step 2. Enable the AI Agent API

Make sure the AI Agent API is enabled to facilitate communication between the AI Agent and the app for handling message notifications. To do this, go to **Administration** > **Settings**. Click the **Druid AI Agent API** tab and check the **Is enabled** option.

![](../Resources/Images/Mobile%20Channel/bot%20api.png)

<a id="Step3Enablemessagenotifications"></a>

### Step 3. Enable message notifications

1. Go to the AI Agent details and click the **Channels** tab
2. Search for **WebChat** and click on the channel card.
3. Select **Enable message notification**.
4. In the **Message notification integration** field, choose the integration you configured at [Step 1. Configure app and integration](#Step_1).

![](../Resources/Images/Mobile%20Channel/select%20integration.png)

5. Click **Save**.

## Related Topics

- [System Entities](../5_Entities/System%20Entities.md)
- [WebChat Common Styling and Behavior](WebChat/WebChat_Common_Styling_and_Behavior_v4.md)
