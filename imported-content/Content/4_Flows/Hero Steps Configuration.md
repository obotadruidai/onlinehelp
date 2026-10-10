---
title: Hero Cards
---

# Hero Cards

Hero Card steps are commonly used to display content like product details, menu options, or any structured data, allowing users to interact by selecting from various options.

In this guide, you’ll learn how to configure a Hero Card step and implement advanced scenarios to tailor the conversation experience to your needs. By following the steps outlined below, you can ensure your AI Agent effectively captures and responds to user selections, creating a more dynamic and interactive dialogue.

| Hero card ![](<../../.gitbook/assets/hero card_example.png>) | Menu options using a hero card ![](<../../.gitbook/assets/Hero Steps Configuration_1.png>) |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |

### Adding and configuring Hero Card steps

To add and configure a Hero Card step in a DRUID flow:

1. Open the desired flow in Flow Diagram view.
2. Expand the Flow Palette, then drag the **Hero** step from the Dialog category into the main flow window and drop it onto the step you want to link it to.
3. Select the step on the diagram, then click the **Settings** icon from the Actions menu.
4. Set the General parameters:

* **Step name**: Give the step a descriptive name that helps you remember its purpose, like "Hero cards".
* **Step message**: Enter the message that the AI Agent will display to the user, such as "Choose from the options below".

5. In the **Input Mapping** field, specify where you want to store the user’s selection, such as a variable or an entity field. For example, you can use a variable like **@option** to capture the user's choice.
6. Go to the Metadata section.
7. If you want to prevent users from clicking the card multiple times, enable **Inactivate card after usage**. This option works only on DirectLine (Web channel).
8. Click the **Edit** button to configure the Hero Cards.
9. Add more cards by clicking the **Add card** button.
10. You can include elements like an image (by entering the image public link), title, subtitle, and description for each card. In the **Navigation URL** field, enter the URL which will open a new page in the browser when the users will click on the image in the card.

{% hint style="info" %}
**Info:** Skip this step if you’re using Hero steps to create menu options.
{% endhint %}

11. To create a menu with multiple options, add interactive buttons to each card by clicking **Add button**. Define the button's tag, visible text, and any custom CSS class for button styling if you are using custom styles. Repeat this step for as many buttons as needed.

You can preview the hero card by clicking the **Preview** button.

12. Click the **Save** button to save the flow step configuration.

If you want to put information into a specific context, you can do so, by setting variables on the step. For more information, see [Set Variable](<Set Variables.md>).

You can also set specific actions to be executed before or after the step execution. For more information see [Pre Actions](<Pre Actions.md>) or [Post Actions](<Post Actions.md>).

The figure below shows how a hero step configuration might look like.

![](<../../.gitbook/assets/Hero Steps Configuration_2.png>)

![](<../../.gitbook/assets/Hero Steps Configuration_3.png>)

![](<../../.gitbook/assets/Hero Steps Configuration_4.png>)

This Hero step provides the users with the possibility to select from a menu which of their data has not been properly processed by the AI Agent in a previous step or select if all data has been properly selected.

### Configuring a hero card with multiple buttons for collection items <a href="#configuring_a_hero_card_with_multiple_buttons" id="configuring_a_hero_card_with_multiple_buttons"></a>

By default, a hero card step with **Is repeater** generates for each item in the provided collection. You have an advanced option to generate a hero card with as many buttons as items are in a collection.

Example:

![](<../../.gitbook/assets/Hero Cards.png>)

To configure a hero card with multiple buttons:

1. In the Metadata section, tap on **Is repeater** and in the **Repeater collection** field, specify the name of the entity list (e.g., \[\[EntityList]], \[\[]].\<EntityListField).
2. Tap on **Advanced editing** and add the following parameter under the hero step: `"isButtonsRepeater":true,`. Create Multiple Buttons. Tap on **Advanced editing**, and in the JSON field, under "hero" add **"isButtonsRepeater": true** to create one card with multiple buttons.

![](<../../.gitbook/assets/Hero Cards_1.png>)

### Configuring hero card buttons to open URLs <a href="#configur" id="configur"></a>

{% hint style="info" %}
**NOTE:** This feature is exclusively available for the web chat and Teams channels.
{% endhint %}

To configure hero card buttons to open specific URLs, navigate to the Metadata section and select **Advanced editing**. Locate the "buttons" object, and for the desired buttons, adjust the following parameters:

* Set the button type to "openUrl".
* Set the button value to the desired website URL.

**Example**

```
"buttons": [
    {
        "title": "Buy",
        "type": "openURL",
        "value": "https://buythisproduct.com"
    }
]
```

When a user clicks the button, the URL will open in a new browser window.

{% hint style="info" %}
**Info:** In DRUID version 7.5 and higher, clicking the button is logged in the Conversation History, and the flow engine refrains from predicting using the button value.
{% endhint %}

### Configuring hero card pagination

By default, a Hero Card displays up to 10 items. If your collection exceeds this, DRUID will create additional cards, showing maxim 10 items per card. You can customize the number of items per page by adjusting the "pageSize" property under “hero” in the step’s JSON settings (**Metadata** > **Advanced editing**).

![](<../../.gitbook/assets/Hero Steps_16.png>)

### Capturing user selections with Is repeater

If you want to capture the entity associated to the item selected by the user after the hero step with **Is repeater**:

1. On the Hero Card step, configure the **Input Mapping** with the appropriate variable or entity.
2. In the Hero Card configuration, in the button configuration, use the same field from the base entity in both the button "name" and "label".

![](<../../.gitbook/assets/Hero Cards_2.png>)

In example above:

* The \[\[Brand]] entity is the base entity for collection \[\[BrandList]].
* \[\[Brand]].Name is a field of type "string" that will store the user's selection from the Hero Card step with **Is repeater**.

![](<../../.gitbook/assets/Hero Cards_3.png>)

By following these steps, you can effectively use Hero Steps to create engaging and interactive experiences for your AI Agent users, offering them clear, actionable choices and a visually appealing interface.

### Related Topics

* [AI Agent Informational Model](<../5_Entities/AI Agent Informational Model.md>)
* [Common Flow Settings](<Common Flow Settings.md>)
* [Handling Input Mapping Exceptions](<Handling Input Mapping Exceptions.md>)
* [Improving AI Agent NER](<../Conversational AI/Improving AI Agent NER.md>)
* [Using NER with Intent Recognition](<../Conversational AI/Using NER with Intent Recognition.md>)
