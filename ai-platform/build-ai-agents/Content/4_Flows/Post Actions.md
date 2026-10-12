---
title: Post Actions
---


The Post actions defined on a flow step will be executed after the flow step is completely executed.

DRUID provides authors with two types of actions, as follows:

* **PostAction** – External actions from integrations which are defined using the Connector Designer. You can use the actions to trigger certain actions defined in your external system integrated with the AI Agent.
* **PostInternalAction** – The system has a predefined set of system commands known as internal actions. You can use them to trigger specific system commands. For example, when provisioning an identified user, you want to assign the roles User and Admin. To do so, add the system command **AddUserRoles** and in the text field enter **\["User","Admin"]**.

![](../../.gitbook/assets/actions.png)

To view the PostActions section on a flow step, in the Flow Step editor, click on the PostActions section header.

## Adding external actions on the flow step

{% hint style="info" %}
**NOTE:** If you are viewing the flow steps in list view, before adding external actions on a step, you first need to define the action(s) using the Connector Designer. For more information, see [Integrations](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors). If you're using the diagram view, you can define the action directly within the desired flow step.
{% endhint %}

To add an existing external action on a step using flow steps in diagram view, double-click on the flow step and in the PostActions section, search in integrations and select an existing external action.

![](<../../.gitbook/assets/add post action.png>)

To add a new external action on a flow step by defining it from scratch, click the **AddNew** button, define the connector action and add subsequent integration tasks.

To add an external action on a step using flow steps in list view, follow these steps:

1. In the PostActions section of the step, click **AddNew** and select **ostAction**. The AddNewAction page appears.
2. Click on the **SelectConnector** field. A pop-up appears listing all existing external actions. You can either scroll-down to the desired action or you can use the search functionality to search for the desired action.

![](<../../.gitbook/assets/post action list view.png>)

3. Select the desired action and click the **Add** button. The external action associated with your selection is listed in the PreActions section.

![](<../../.gitbook/assets/added post action.png>)

The actions are executed in the order of their listing in this section.

If you have more actions in this section and you want to change their execution order, you can do so by holding the cursor on the icon (the one with the arrows) and use the drag and drop functionality.

4. Click the **Save** button at the bottom of the page to save the changes.

## Add DRUID internal actions on flow steps

To add a DRUID predefined action (internal action) on a flow step using flow steps in diagram view, double-click on the flow step and in the PostActions section, search in integrations and select the desired predefined action. These actions are marked with the word "INTERNAL".

![](<../../.gitbook/assets/post internal action.png>)

To add an internal action on a step using flow steps in list view, follow these steps:

1. In the PostActions section, click **AddNew**and select **PostInternalAction**. The AddNewAction page appears.
2. Click on the **SelectConnector** field. A pop-up appears which lists the predefined actions available in DRUID.
3. Select the desired action and click the Add button. The selected action is listed in the PostActions section.

The actions are executed in the order of their listing in this section.

If you have more actions in this section and you want to change their execution order, you can do so by holding the cursor on the icon (the one with the arrows) and use the drag and drop functionality.

4. Click the **Save** button at the bottom of the page to save the changes.

## Deleting an action

To delete an action from the PostActions section, click the Delete icon displayed inline with the action.

## Related Topics

* [Common Flow Settings](<Common Flow Settings.md>)
* [Internal Actions](<Internal Actions.md>)
