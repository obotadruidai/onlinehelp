---
layout:
  title:
    visible: false
---

<a id="EnableChatinViews"></a>

# Enable Chat in Views

Enabling chat in views allows business users to interact with the AI Agent directly within the context of a specific record. By clicking the **Chat** button, users can ask the AI Agent questions or request actions to be performed, all while staying within the relevant view.

This functionality is particularly useful for providing real-time assistance and automating tasks without requiring users to navigate away from their current workflow.

![](../Resources/Images/druid%205.26/chat%20on%20view.png)

The chat conversation will open in the context of the entity record from which the user opens the chat.

![](../Resources/Images/druid%205.26/chat%20view%20opened.png)

To enable chat in a view:

1. Navigate to the configuration page for the desired view.
2. In the right-side editor, click the Chat icon (![](../Resources/Images/CBA/chat%20bobble.png)). The Chat properties panel will appear.
3. In the Chat properties panel, do the following:

1. Tap on **Active chat** .
2. Keep Visible **On load** selected to ensure the chat option is available when the view loads.
3. Choose the **Appearance** you prefer for the chat button (the default appearance ![](../Resources/Images/CBA/appearance.png) is selected by default).
4. Optionally, select a **Welcome flow** to trigger when users first open the chat conversation in the entity record form. This flow can provide users with helpful prompts or guidance when they start the conversation.

![](../Resources/Images/druid%205.26/chat%20on%20view%20add.png)

4. Once you’ve configured the chat settings, click the **Save** icon (![](../Resources/Images/CBA/save%20properties_21x18.png)) at the top-right corner of the editor to save your changes.

With these steps, your business users can seamlessly initiate chats with the AI Agent directly from the view, enhancing their productivity and improving user experience.
