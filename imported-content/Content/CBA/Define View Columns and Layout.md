---
title: Define View Columns and Layout
---

# Define View Columns and Layout

To configure a view, you need to define the columns and adjust their layout.

### Access the View Designer

On the entity’s Views page, click the Edit icon (![](<../../.gitbook/assets/edit icon.png>)) next to the view you want to configure.

The View Designer opens, where you can define the columns and structure of your view.

![](<../../.gitbook/assets/view designer.png>)

The View Designer consists of the following elements:

* **Field Selector** – Displays a list of fields and relationships for the selected entity. By default, it shows the entity’s fields (![](<../../.gitbook/assets/entity fields icon.png>)).

![](<../../.gitbook/assets/entity fields (1).png>)

* **Relations Panel** – Displays referenced entities. Click the Relations icon (![](<../../.gitbook/assets/relations icon.png>)) to view them. Expand an entity by clicking the **Plus** icon (![](<../../.gitbook/assets/plus icon.png>)) to see its available fields.

![](<../../.gitbook/assets/entity relations.png>)

* **View Diagram** – The workspace where you design the view by adding and arranging columns.
* **View Editor** – Allows you to configure column properties, including layout settings.

### Define Columns and Layout

1. Add Columns.
2. In the Field Selector, find the fields you want to include as columns.
3. Drag and drop them into the View Diagram before the first column.
4. Once a field is added, it turns gray in the Field Selector to indicate it has been used.

![](<../../.gitbook/assets/define view columns.png>)

2. Reorder columns. Drag and drop columns within the View Diagram to rearrange them as needed.
3. Remove columns. Click on a column in the View Diagram and press **Delete** on your keyboard.
4. Adjust column layout:
5. Click on a column to access its settings.
6.  Configure the following properties:

    * **Column Width** – Default width is 200px, but you can adjust it as needed.
    * **Visibility on Mobile** – Choose whether to hide the column when accessed from mobile devices.

    ![](<../../.gitbook/assets/column settings.png>)

{% hint style="info" %}
**Info:** In order to nicely render fields on views by properly setting the fields’ layout, you might want to check [how the different fields are rendered on the views and forms](<Fields rendering on views and forms.md>) at usage time.
{% endhint %}

5. Click the **Save** icon at the top-right corner of the editor to apply the changes.
6. To ensure proper layout and formatting, preview the view to see how different field types appear at runtime.

After defining the columns, you can populate the view with data by adding integrations.
