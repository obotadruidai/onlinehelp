---
title: Message
---

# Message

Use Message steps to have the AI Agent respond to users with specific text.

### Adding and configuring Message steps

To add and configure a Message step in a DRUID flow:

1. Open the desired flow in Flow Diagram view.
2. Expand the Flow Palette, then drag the **Message** step from the Dialog category into the main flow window and drop it onto the step you want to link it to.
3. Select the step on the diagram, then click the **Settings** icon from the Actions menu.
4. Set the General parameters:

* **Step name**: Give the step a descriptive name that helps you remember its purpose.
* **Step message**: Enter the message that the AI Agent will display to the user.

5. Click **Save** to save the step configuration.

When the step is executed, the AI Agent will return the message specified in the **Step message** field.

#### Additional configuration options

* **Contextual Information**: You can use input mapping and set variables to pass information within a specific context. For details, see [Set Variable](<Set Variables.md>).
* **Pre and Post Actions**: Configure actions to be executed before or after the step. For more information, see [Pre Actions](<Pre Actions.md>) or [Post Actions](<Post Actions.md>).

### Rendering dynamic elements within a Message step

By default, a Message step displays up to 10 items from a collection. If your collection has more than 10 items, DRUID will generate additional messages to display them.

To display dynamic elements in a Message step based on a collection (entity list):

1. In the desired Message step, click the Metadata section header.
2. Tap on **Is repeater** and enter the name of the entity list (e.g., \[\[]] or \[\[]].).
3. Tap on **Advanced editing**, and adjust the "pageSize" value in the JSON field under "message" to your desired number.

![](<../../.gitbook/assets/Message Steps.png>)

### Related Topics

* [Common Flow Settings](<Common Flow Settings.md>)
