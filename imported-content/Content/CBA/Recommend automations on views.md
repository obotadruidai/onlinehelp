---
title: "Recommend Automations on Views"
---

<a id="RecommendAutomationsonViews"></a>


Empower your business users to seamlessly trigger conversational flows and integrations directly from views by providing a curated set of recommended automations—shortcuts or links to specific flows or integrations—tailored to the context of the view(s).

![](../Resources/Images/druid%207.4/run%20autom%20on%20views.png)

When users select a recommended automation, it triggers the conversation in the chat on the view, and the AI Agent executes the selected flow or integration on the current view or on selected records.

![](../Resources/Images/CBA/automation%20selected.png)

<a id="Recommendingautomations"></a>

## Recommending automations

To recommend automations to users on views, follow these steps:

1. Navigate to the desired view configuration page.
2. Click the Automations icon (![](../Resources/Images/CBA/automations%20icon_26x24.png)) in the right-side editor.

![](../Resources/Images/druid%205.26/add%20automations%20on%20view.png)

3. In the Dialogues/Conversations editor , click **Add New**.
4. In the **Flow / Integration** field, select the flow or integration you want to use. To make the automation available as a button or icon on the toolbar for quick access, select **Use as button**, then configure the button or icon by following the steps in [Making automations available as action buttons / icons](#Make_automations_available_as_action_buttons_%2F_icons).

![](../Resources/Images/druid%208.11/add%20automation.png)

5. Click the **Save** button.
6. Add as many automations as needed to the list. You can reorder them using drag and drop.

![](../Resources/Images/druid%207.4/view%20automations%20list.png)

7. Click the Save icon (![](../Resources/Images/CBA/save%20properties_21x18.png)) located at the top-right corner of the editor to save your changes.

<a id="Makingautomationsavailableasactionbuttonsicons"></a>

## <a id="Make_automations_available_as_action_buttons_/_icons"></a>Making automations available as action buttons / icons

Action buttons and icons at the top of views and forms let users trigger recommended automations with a single click. Instead of opening the Automations menu and selecting an action, users can quickly execute key actions from the top-right corner of the page. This feature reduces extra steps and improves efficiency, helping users complete tasks faster.

![](../Resources/Images/druid%208.11/user%20action.png)

{% hint style="info" %}
**NOTE:** This feature is available in DRUID 8.11 onwards.
{% endhint %}

When creating a new recommended automation or editing an existing one, follow these steps to make it available as a button or icon in the view:

1. Select **Use as button**.
2. Choose how you want to display the quick action:

- As a button – Enter a button name and select a color. The default color is DRUID green.

![](../Resources/Images/druid%208.11/user%20action.png)

![](../Resources/Images/druid%208.11/button.png)

- As an icon with hover text – Enter a button name and select an icon from the available library.

![](../Resources/Images/druid%208.11/icon%20tooltip.png)

![](../Resources/Images/druid%208.11/icon%20with%20tooltip.png)

- As an icon only – Select an icon and leave the button name field empty.

3. Click **Save**.
4. Click the Save icon (![](../Resources/Images/CBA/save%20properties_21x18.png)) located at the top-right corner of the editor to apply your changes.
