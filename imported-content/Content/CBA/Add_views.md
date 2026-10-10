<a id="AddViews"></a>

# Add Views

At authoring time, you can create multiple views for an entity, but only one can be set as the default. When business users click the entity in the workspace menu, the default view is displayed first. All other views defined for the entity appear as separate tabs, allowing users to switch between them as needed.

![](../Resources/Images/CBA/default%20view.png)

> **Info:** To automatically generate a view that retrieves data from DRUID Data Services, use the CRUD Template. Applying the CRUD Template to entity integrations automatically creates a default view and form, preconfigured with the necessary integrations. For more details, see  [CRUD Template](Entity%20Data%20Integration.md).

Follow these steps to add a view to an entity:

1. In the Solution drop-down, select the desired solution.
2. In the **Solution Contents** menu, click **Entities** to display the list of entities associated with the solution.

![](../Resources/Images/CBA/access%20entities%20list.png)

3. Select the entity for which you will add a link in the workspace. The entity configuration page opens on the **Details** tab.
4. Click the **Views** tab. The list of existing views for the entity appears. If no views have been defined, the page is empty.

![](../Resources/Images/CBA/views%20list.png)

5. In the top-right corner, click **Create new view**. The Create New View pop-up appears.
6. Enter a name and a brief description for the view. The description helps identify the type of data the view contains.
7. In the **Type** field, select the desired view type. **Table View** is selected by default.

![](../Resources/Images/CBA/create%20view%20pop-up.png)

8. Click **Save**.

The first view created for an entity is automatically set as the default. When users click the entity link in the workspace menu, this default view is shown.

You can now define the view's properties, columns, and layout.
