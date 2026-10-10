<a id="Dashboards"></a>

# Dashboards

You can put at business users disposal data from web views and charts by adding multiple dashboards to workspaces.

![](../Resources/Images/CBA/show%20data.png)

<a id="Authoringdashboards"></a>

## Authoring dashboards

To create a dashboard, select the AI Agent and solution and from the **Solution Contents** menu, click **Dashboards**. At the top-right corner of the Dashboards page, click the **Create new dashboard** button. The Create new dashboard page appears.

Enter a dashboard name and description and click **Save**.

![](../Resources/Images/CBA/create%20dashboard.png)

The dashboard is listed in the Dashboards page.

Click the **Edit** icon displayed in line with the dashboard record.

![](../Resources/Images/CBA/all%20dashboards.png)

The dashboard with an empty page appears. Tap on **Edit mode**.

![](../Resources/Images/CBA/empty.png)

The Dashboard becomes editable. A toolbar appears and provides you with the following options:

|  |  |
| --- | --- |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_1.png) | Add a new widget on the dashboard page. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_2.png) | Add a new dashboard page. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_3.png) | Rename the current dashboard page. |
| ![](../Resources/Images/CBA/delete%20page.png) | Delete the current dashboard page.  **IMPORTANT!**  This action cannot be undone. Make sure that you really want to delete the current dashboard page. |
| ![](../Resources/Images/CBA/reset.png) | Restores the current page to default dashboard template.  **IMPORTANT!**  This action cannot be undone; any customizations you did to the current page will be lost! Make sure that you really want to restore the dashboard page to default. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_6.png) | Saves the current dashboard page customization and exists the edit mode. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_7.png) | Cancels dashboard page customizations (new or existing widgets, reordering, etc.) and exists the edit mode. |

<a id="Addingwidgets"></a>

## Adding widgets

To add a widget, click the **Add widget** button (![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_1.png)) on the toolbar. The Add widget page appears.

Select the desired widget type:

- **Chart** – to show an entity chart.
- **Table** – to show an entity view.

Click **Save**.

You need to edit the widget based on the selected widget type.

<a id="Editingwidgets"></a>

## Editing widgets

To edit a widget, click the settings icon corresponding to the desired widget.

![](../Resources/Images/CBA/edit%20widgets.png)

The widget Settings page appears. The page content is different based on the widget type.

<a id="EditTablewidgets"></a>

### Edit Table widgets

In the Settings page, select the entity and the desired web view defined on the entity.

Enable the **Disable record editing** toggle to prevent users from modifying records directly from the dashboard view widget. When turned on:

- The edit icon is removed from the top-right corner of the widget.
- Locks records. Individual rows inside the table become non-clickable and non-editable, ensuring a secure, presentation-only user experience.

![](../Resources/Images/CBA/table%20widget.png)

> **Info:** The **Disable record editing** toggle is available starting with Druid 9.27.

Click **Save**to close the modal. Click the **Save** button from the dashboard toolbar to save the widget on the dashboard page.

<a id="EditChartwidgets"></a>

### Edit Chart widgets

In the Settings page, select the entity and the desired chart defined on the entity.

![](../Resources/Images/CBA/charts%20widget.png)

Click **Save**. The Settings page closes.

Click the **Save** button from the dashboard toolbar to save the widget on the dashboard page.

The figure below provides an example of various widgets of type **Chart**.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_16.png)

<a id="Deletingwidgets"></a>

## Deleting widgets

To delete a widget from the current dashboard page, click the delete icon corresponding to the desired widget.

<a id="ReorderingwidgetsonDashboard"></a>

## Reordering widgets on Dashboard

You can reorder the widgets on a dashboard page by using drag and drop and clicking the **Save** button on the toolbar.

<a id="AddingDashboardPages"></a>

## Adding Dashboard Pages

To add a new dashboard page, click the **Add page** button (![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_2.png)) from the toolbar. A pop-up appears. Type the name of the page and click **Save**.

The page is added as a new tab to the dashboard but you remain on the current page.

<a id="RenamingDashboardPages"></a>

## Renaming Dashboard Pages

To rename the current dashboard page, click the **Rename page** button (![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_3.png)) on the toolbar. A pop-up appears. Type the new name of the page and click **Save**.

<a id="DeletingDashboardPages"></a>

## Deleting Dashboard Pages

> **IMPORTANT!** This action cannot be undone. Make sure that you really want to delete the current dashboard page.

To delete the current dashboard page, click the **Delete page** button ( ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_4.png)) from the toolbar. A confirmation dialog appears.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_27.png)

Click **Yes**. The current page is removed from the dashboard.

<a id="Resetchanges"></a>

## Reset changes

To undo any changes you did to a dashboard page prior to saving the changes, click the **Reset** button from the toolbar.

A pop appears asking you to confirm the action. Click **Yes**.

<a id="Addingdashboardstoworkspaces"></a>

## Adding dashboards to workspaces

Go to the desired workspace (**Solution Contents** menu, **Workspaces**) and in the configuration page, click the **Links** tab. From this section you add the dashboard or multiple dashboards (if multiple defined) to your workspace main menu and thus the dashboard(s) will be accessible to the business users in the workspace.

Click the **Add new** icon. A new editable line appears in the Links page.

From the **Type** drop-down select **Dashboard** and from the **Dashboard** drop-down select the entity dashboard. Click on the check icon, then click the **Save** button.

![](../Resources/Images/CBA/save%20to%20menu.png)
