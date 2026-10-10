---
layout:
  title:
    visible: false
---

<a id="CreateandDesignViews"></a>

# Create and Design Views

At authoring time, the authors can define multiple views for an entity that will be displayed to the business users as a drop-down selection, but they can set only one as default.

![](../Resources/Images/CBA/default%20view.png)

> **Info:** If you want to create a view that consumes data from the DRUID Data Services, use the CRUD Template. For more information, see [CRUD Template](Entity%20Data%20Integration.md).

To create a view for an entity, follow these steps:

<a id="Step1Addviewonentity"></a>

## Step 1. Add view on entity

1. From the **Solution** drop-down, select the desired solution and on the **Solution Contents** menu, click **Entities**. The page displays the list of entities linked to the current solution.

![](../Resources/Images/CBA/access%20entities%20list.png)

2. Select the entity for which you added a link in the workspace. The entity configuration page appears on the **Details** tab.
3. Click the **Views** tab. The list of views created for the current entity appears. If there haven’t been defined any views, the page is empty.

![](../Resources/Images/CBA/views%20list.png)

4. At the top-right corner of the page, click the **CreateNewView** button (![](../Resources/Images/CBA/create%20view%20button.png)). The CreateNewView pop-up appears.
5. Enter the view name and a brief description. The description will help you easily identify what data the view contains.
6. From the **Type** field, select **Table View**.
> **NOTE:** The **Type** field is available in DRUID 5.6 and higher and has been introduced to add the search view bar feature that allows searching for a particular view in the Views list (views consumed either from the **Data** tab on the entity or from Workspaces). For more information, see [Add Search View Bar](Add%20Search%20View%20Bar.md). In DRUID 5.7 and higher you can set up Kanban views. For more information, see [Kanban Views](Kanban%20Views.md).
>
> In DRUID 5.20 and higher, you can create Calendar views to track record events on a calendar. For more information, see [Calendar Views](Calendar%20Views.md).

![](../Resources/Images/CBA/create%20view%20pop-up.png)

7. Click **Save**.

> **Info:** The first view you add on an entity is marked as default, it will be displayed in the workspace when clicking the entity associated link in the workspace menu.

<a id="Step2Definetheviewpropertiesoptional"></a>

## Step 2. Define the view properties (optional)

On the entity’s views page, click the **Edit** icon (![](../Resources/Images/CBA/edit%20icon.png)) displayed in line with the view you want to define. The View Designer appears. The right side editor displays by default on the **View properties** (![](../Resources/Images/CBA/view%20properties%20icon.png)).

![](../Resources/Images/CBA/view%20properties.png)

If you create views which contain multi-lingual entity fields, you might want to provide the view name and details in all languages set on the AI Agent. This way, business users accessing the view in a specific language set on the AI Agent will see the view information (both the view name and description) in that language.

If your view receives data from external sources, enable data auto-refresh to ensure real-time updates without manual intervention. Tap **Enable data auto-refresh** and select the desired refresh interval. This feature is available in DRUID 8.9 and higher.

After you set the view properties, click the **Save** icon (![](../Resources/Images/CBA/save%20view%20icon.png)) at the top-right corner of the editor.

<a id="Step3Definetheviewcolumnsandtheirlayout"></a>

## Step 3. Define the view columns and their layout

On the entity’s views page, click the **Edit** icon (![](../Resources/Images/CBA/edit%20icon.png)) displayed in line with the view you want to define. The View Designer appears.

![](../Resources/Images/CBA/view%20designer.png)

The View Designer is comprised of the following elements:

- Field selector – displays the list of entity fields and relations. By default, it displays the fields of the current entity (![](../Resources/Images/CBA/entity%20fields%20icon.png)).

![](../Resources/Images/CBA/entity%20fields.png)

To see the list of entities referenced by fields of type Entity defined on the current entity, click the **Relation**s icon (![](../Resources/Images/CBA/relations%20icon.png)). The list of referenced entities appears. To see an entity’s fields, click the **Plus** icon (![](../Resources/Images/CBA/plus%20icon.png)) in front of it.

![](../Resources/Images/CBA/entity%20relations.png)

- The View Diagram is the area where you design the view and define its data.
- The View Editor allows you to set the view details and also set the layout of the view columns (when the focus is on a specific view column).

To define the view columns and their layout:

1. On the entity fields and relations selector, identify the fields that you want to include as columns in the view and drag and drop them one by one in the View Diagram before the first column. Add as many fields as you need.
> **Info:**  To provide you with a seamless authoring experience, once you add a field to the view, it becomes gray in the entity fields and relations editor. Also, if you click on a column in the view, the field is highlighted in green in the fields’ selector.
>
> ![](../Resources/Images/CBA/define%20view%20columns.png)

2. Reorder the view based on your preferences by drag and dropping columns in the view.
> **Info:**  You can remove columns from the view by clicking on the desired column and pressing Delete on the keyboard.

3. Set the view layout by defining the view settings for each column in the view. By default, the view columns have a fixed width of 200px and are visible on desktop and mobile devices. You can change the column width (selecting from a set of available widths) and / or hide it on mobile devices (hide the column when authors and business users access the views on mobile devices). To do so, click on the desired column in the view and set the column settings to accommodate your needs.

![](../Resources/Images/CBA/column%20settings.png)

> **NOTE:**  In order to nicely render fields on views by properly setting the fields’ layout, you might want to check [how the different fields are rendered on the views and forms](Fields%20rendering%20on%20views%20and%20forms.md) at usage time.

4. Set the view **Row height**. Choose between **Small**, **Medium**, or **High** row height options. The default is **Medium**.
> **NOTE:** This feature is available in Druid 9.11 and higher.

5. Click the save icon (![](../Resources/Images/CBA/save%20view%20icon.png)) at the top-right corner of the editor to save the column settings.

Now that you defined the view columns, you can populate the view with data by adding integrations on the view.

<a id="Step4Defineviewdatabyaddingintegrations"></a>

## Step 4. Define view data by adding integrations

**Prerequisites**

- In the solution for which you want to get an aggregated view on data coming from various data sources, make sure that you defined integrations with external data sources as best suits your needs.
- As a view provides a list of records, make sure that on the integrations tasks you define, the entity for which you will define the views are set as response entity and it is a collection (in the integration task, Response tab, IsResponseCollection is checked).

Once you defined the view, you need to fetch entity data that will be displayed on the view, by adding integrations with external data sources. This way, your view is populated with entity records.

To define the view data follow these steps:

1. At the top side of the View Diagram, click the **Add Integrations** icon (![](../Resources/Images/CBA/add%20integrations%20iscon.png)). A pop-up appears. The pop-up contains two sections:

- **Read Data** – allows you to define from which data source DRUID reads data and aggregates it in the view.
- **Delete Data** – allows you to define what happens when records are deleted from the view.

![](../Resources/Images/CBA/add%20integrations.png)

2. Click the **Read Data** section. The section expands.
3. Define the integrations to get the view data.

1. Add the integration action by using of the two options below:

- Search for an existing integration action defined in the current solution and press **Enter** on the keyboard.

![](../Resources/Images/CBA/search%20integrations.png)

- Add a new integration action. Click the **Add new** button (![](../Resources/Images/CBA/add%20new%20connector%20action.png)) and define the connector action using the right editor. Make sure to select the current entity as Response entity and select **Is Response Collection** and **Is Active**.

![](../Resources/Images/CBA/define%20integration%20action.png)

Save the integration action by clicking the **Save** icon (![](../Resources/Images/CBA/save%20view%20icon.png)) at the top-right corner of the editor.

> **IMPORTANT!**  You can add only one connector action in the Read Data section and multiple integration tasks to aggregate data coming from various data sources.

2. Add integration tasks. In the Read Data section, click on the **Add task** icon and select the desired integration task from the list where the current entity is Response entity and **Is Response Collection** is selected.

![](../Resources/Images/CBA/select%20integration%20task.png)

![](../Resources/Images/CBA/read%20data.png)

4. Click the **Delete Data** and select the desired integration based on what you want to happen when authors and business users will remove records from the view. Save the integration(s).

![](../Resources/Images/CBA/delete%20data.png)

> **NOTE:**  If you leave the Delete Data section empty (select no integration), business users and authors will not be to delete records from the view; the **Delete** icon will not be displayed in line with the records in the view.
>
> ![](../Resources/Images/CBA/delete%20records.png)

You can now preview the view and make further adjustments if needed.

<a id="Step5Optionallypreviewandchecktheview"></a>

## Step 5. Optionally, preview and check the view

The authors can preview a view by clicking on the **Preview** icon displayed at the top side of the View Diagram.

![](../Resources/Images/CBA/preview%20icon.png)

The view in preview mode opens in a new browser page.

![](../Resources/Images/CBA/view%20preview.png)

> **Info:** If at the time of the preview, a list of records does not exist, or an integration has not been set yet on the view, the preview will render null data in preview mode.

Authors can filter the view and see only the fields that are hidden on mobile devices by tapping on **FieldsOnMobile** the at the top-right corner of the page and then clicking **Refresh**.

![](../Resources/Images/CBA/preview%20on%20mobile.png)
