---
title: "Disabling Flows"
---

<a id="DisablingFlows"></a>


Instead of permanently deleting flows that you might need again later, you can disable them. Disabled flows remain saved in your solution but are temporarily prevented from executing.

You can disable flows individually or in bulk.

<a id="Disableflowsinbulk"></a>

## Disable flows in bulk

{% hint style="info" %}
**Info:** This feature is available starting with Druid 9.29.
{% endhint %}

To disable flows in bulk:

1. In the left navigation menu, expand **Solution Contents** and click **Flows**.
2. Click the checkboxes next to the flows you want to deactivate. Selecting one or more flows displays the bulk action buttons at the top-right of the list view.
3. Click the **Bulk disable selected flows** icon in the action toolbar.

![](../Resources/Images/druid%209.28/bulk%20disable.png)

4. Confirm that you want to disable the selected flows.

The Disabled badge will appear below the floe name in the Flows page to indicate its inactive status.

{% hint style="info" %}
**Info:** To reactivate a disabled flow at any time, select the flow and in the flow configuration panel, uncheck **Is disabled**. Starting with Druid 10.0, you can enable in bulk disabled flows.

![](../Resources/Images/Flows/enable%20in%20bulk.png)
{% endhint %}

<a id="Disablinganindividualflow"></a>

## Disabling an individual flow

To disable a single flow, click on the flow and go to the flow details. Select the **Is Disabled** checkbox and save the flow.

![](../Resources/Images/druid%209.28/is%20disabled.png)
