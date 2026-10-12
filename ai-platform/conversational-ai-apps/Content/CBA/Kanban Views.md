---
title: Kanban Views
---


Kanban views provide a visual way to organize and manage records using cards, columns, and colors. This graphical representation helps teams stay focused on completing tasks before starting new ones, ensuring that top-priority work remains the focus and improving overall efficiency.

Kanban views are useful for various use cases, including project management, lead management, bug tracking, and work monitoring.

![](<../../.gitbook/assets/kanban board.png>)

In a Kanban view, each record is represented as a card. These cards are arranged within vertical columns on the board, with each column grouping records based on a specific field.

## Creating Kanban Views

Creating a Kanban view involves four main steps:

1. Add a **Kanban** view.
2. Define the view properties.
3. Add and configure columns.
4. Define the data through Integrations.

### Step 1. Add Kanban View

Before configuring a Kanban view, you must first add a new view of type **Kanban** to the desired entity.

![](<../../.gitbook/assets/create kanban.jpg>)

### Step 2. Define the view properties

To configure the Kanban view, on the entity’s Views page, click the **Edit** icon (![](<../../.gitbook/assets/edit icon.png>))next to the Kanban view you want to define.

![](<../../.gitbook/assets/edit kanban view.jpg>)

The View Designer opens, displaying a default column with an empty card. The right-side editor automatically opens the View Properties panel (![](<../../.gitbook/assets/view properties icon.png>)).

![](<../../.gitbook/assets/view properties.jpg>)

Configure the following properties:

| Parameter    | Description                                                                                                                                                                              | Mandatory |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Name         | The view name (editable).                                                                                                                                                                | Yes       |
| Display Name | If the view contains multilingual records, provide the display name and optional details in all supported languages.                                                                     | No        |
| Details      |                                                                                                                                                                                          | No        |
| SelectForm   | Choose a form that defines the card content. The form name is displayed as the card title. **Info:** It is recommended to use simple forms to ensure key information is clearly visible. | Yes       |
| GroupByField | Select an entity field to group records into columns (e.g., grouping support tickets by status).                                                                                         | Yes       |
| SortByField  | Set a sorting order for cards within each column based on a specific entity field. If left unset, DRUID sorts the cards by their data index.                                             | No        |

Click the Save icon (![](<../../.gitbook/assets/save view icon.png>)) in the top-right corner of the editor to apply the settings.

### Step 3. Add view columns and define their layout

Click the **New Column** button (![](<../../.gitbook/assets/add column.jpg>)) to add as many columns as needed.

To configure a column:

1. Click on the column, then click the **Settings** icon (![](<../../.gitbook/assets/column settings.jpg>)).
2. In the right-side editor, enter the column name in the **Equals** field. This name will be visible as the column title.
3. Set a background color and font color for the column title.

![](<../../.gitbook/assets/column layout.png>)

4. Click the Save icon (![](<../../.gitbook/assets/save view icon.png>)) to apply the settings.

{% hint style="info" %}
**Info:** You can rearrange the columns by dragging and dropping them in the desired order. To remove a column, select it and press **Delete** on your keyboard.
{% endhint %}

### Step 4. Define view data by adding integrations

To configure the data sources for your Kanban view, follow the instructions in [Define View Data by Adding Integrations](<Define View Data by Adding Integrations.md>), with one additional step. In the **Update Data** section, define or select the desired integration based on how you want authors and business users to update records in the view, then save the integration(s).

{% hint style="info" %}
**Info:** If you leave the Update Data section empty, business users and authors will not be able to update records in the Kanban view.
{% endhint %}

You can now preview the Kanban view and make further adjustments if needed.

## Managing records in Kanban views

### Update records

{% hint style="info" %}
**NOTE:** You can update records in a Kanban view only if the **Update Data** integration is defined for the view and you have Edit privileges for the records.
{% endhint %}

You can perform the following actions:

* Move cards from left to right by using drag and drop. When you move a card, for that record DRUID automatically updates the value of the field that groups records into columns (the value of the entity field set in GroupByField).
* Update record details. Double click on the desired card or place the cursor on the card, click the three dots and click Edit.

![](<../../.gitbook/assets/edit delete.png>)

The record details displays in the default form set on the current entity and not the form you selected when creating the Kanban view which is only used to show card information. Make the necessary changes and save the record. The card will be automatically moved to another column only if you update the value of the field that groups records into columns.

### Delete records

{% hint style="info" %}
**NOTE:** You can update records in a Kanban view only if the **Delete Data** integration has been defined on the view and you have Edit privileges to records.
{% endhint %}

You have two options to delete a record from a Kanban view:

* Place the cursor on the card, click the three dots and click **Delete**. You need to confirm record deletion.

![](<../../.gitbook/assets/delete (1).png>)

* Double-click on the desired card and at top-right corner of the form which displays on the right, click the delete icon.

## Related Topics

* [Add Quick Search to Table Views](<Add Search View Bar.md>)
