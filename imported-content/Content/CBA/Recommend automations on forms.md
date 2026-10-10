---
title: Recommend Automations on Forms
---

# Recommend Automations on Forms

Empower your business users to seamlessly trigger conversational flows and integrations directly from forms by providing a curated set of recommended automations—shortcuts or links to specific flows or integrations—tailored to the context of the form(s).

![](<../../.gitbook/assets/select automation.png>)

When users select a recommended automation, it triggers the conversation in the chat on the form, and the AI Agent executes the selected flow or integration on the current form.

![](<../../.gitbook/assets/automation selected.png>)

### Recommending automations

To recommend automations to users on forms, follow these steps:

1. Navigate to the desired form configuration page.
2. Click the Automations icon (![](<../../.gitbook/assets/automations icon_26x24.png>)) in the right-side editor.

![](<../../.gitbook/assets/empty automations editor.png>)

3. In the Dialogues/Conversations editor , click **Add New**.
4. In the **Flow / Integration** field, select the flow or integration you want to use. To make the automation available as a button or icon on the toolbar for quick access, select **Use as button**, then configure the button or icon by following the steps in [Making automations available as action buttons / icons](<Recommend automations on forms.md#Making_automations_available_as_action_buttons_/_icons>).

![](<../../.gitbook/assets/form select automation.png>)

5. Click the **Save** button.
6. Add as many automations as needed to the list. You can reorder them using drag and drop.

![](<../../.gitbook/assets/form automations.png>)

7. Click the Save icon (![](<../../.gitbook/assets/save properties_21x18.png>)) located at the top-right corner of the editor to apply the changes.

### Making automations available as action buttons / icons <a href="#making_automations_available_as_action_buttons_-_icons" id="making_automations_available_as_action_buttons_-_icons"></a>

Action buttons and icons at the top of views and forms let users trigger recommended automations with a single click. Instead of opening the Automations menu and selecting an action, users can quickly execute key actions from the top-right corner of the page. This feature reduces extra steps and improves efficiency, helping users complete tasks faster.

![](<../../.gitbook/assets/user action.png>)

{% hint style="info" %}
**NOTE:** This feature is available in DRUID 8.11 onwards.
{% endhint %}

When creating a new recommended automation or editing an existing one, follow these steps to make it available as a button or icon in the view:

1. Select **Use as button**.
2. Choose how you want to display the quick action:

* As a button – Enter a button name and select a color. The default color is DRUID green.

![](<../../.gitbook/assets/button on form.png>)

![](<../../.gitbook/assets/form action button set.png>)

* As an icon with hover text – Enter a button name and select an icon from the available library.

![](<../../.gitbook/assets/icon on form.png>)

![](<../../.gitbook/assets/form button with icon.png>)

* As an icon only – Select an icon and leave the button name field empty.

3. Click **Save**.
4. Click the Save icon (![](<../../.gitbook/assets/save properties_21x18.png>)) located at the top-right corner of the editor to apply your changes.
