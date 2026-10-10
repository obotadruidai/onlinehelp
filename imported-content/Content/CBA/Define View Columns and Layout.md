<a id="DefineViewColumnsandLayout"></a>

# Define View Columns and Layout

To configure a view, you need to define the columns and adjust their layout.

<a id="AccesstheViewDesigner"></a>

## Access the View Designer

On the entity’s Views page, click the Edit icon (![](../Resources/Images/CBA/edit%20icon.png)) next to the view you want to configure.

The View Designer opens, where you can define the columns and structure of your view.

![](../Resources/Images/CBA/view%20designer.png)

The View Designer consists of the following elements:

- **Field Selector** – Displays a list of fields and relationships for the selected entity. By default, it shows the entity’s fields (![](../Resources/Images/CBA/entity%20fields%20icon.png)).

![](../Resources/Images/CBA/entity%20fields.png)

- **Relations Panel** – Displays referenced entities. Click the Relations icon (![](../Resources/Images/CBA/relations%20icon.png)) to view them. Expand an entity by clicking the **Plus** icon (![](../Resources/Images/CBA/plus%20icon.png)) to see its available fields.

![](../Resources/Images/CBA/entity%20relations.png)

- **View Diagram** – The workspace where you design the view by adding and arranging columns.
- **View Editor** – Allows you to configure column properties, including layout settings.

<a id="DefineColumnsandLayout"></a>

## Define Columns and Layout

1. Add Columns.

1. In the Field Selector, find the fields you want to include as columns.
2. Drag and drop them into the View Diagram before the first column.
3. Once a field is added, it turns gray in the Field Selector to indicate it has been used.

![](../Resources/Images/CBA/define%20view%20columns.png)

2. Reorder columns. Drag and drop columns within the View Diagram to rearrange them as needed.
3. Remove columns. Click on a column in the View Diagram and press **Delete** on your keyboard.
4. Adjust column layout:

1. Click on a column to access its settings.
2. Configure the following properties:
   - **Column Width** – Default width is 200px, but you can adjust it as needed.
   - **Visibility on Mobile** – Choose whether to hide the column when accessed from mobile devices.

   ![](../Resources/Images/CBA/column%20settings.png)

> **Info:**  In order to nicely render fields on views by properly setting the fields’ layout, you might want to check [how the different fields are rendered on the views and forms](Fields%20rendering%20on%20views%20and%20forms.md) at usage time.

5. Click the **Save** icon at the top-right corner of the editor to apply the changes.
6. To ensure proper layout and formatting, preview the view to see how different field types appear at runtime.

After defining the columns, you can populate the view with data by adding integrations.
