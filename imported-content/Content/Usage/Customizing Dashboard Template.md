---
title: "Customizing Dashboard Template"
---

<a id="CustomizingDashboardTemplate"></a>


To edit the dashboard template, on the top-right corner of the Dashboard, tap on **Edit mode**.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template.png)

The Dashboard becomes editable: a toolbar appears at the bottom and all dashboard widgets become editable. You can navigate through dashboard pages and edit the dashboard pages according to your needs.

The toolbar provides you with the following options:

|  |  |
| --- | --- |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_1.png) | Add a new widget on the dashboard page. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_2.png) | Add a new dashboard page. Useful when you want to have your custom KPIs on the same page. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_3.png) | Rename the current dashboard page. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_4.png) | Delete the current dashboard page.  **IMPORTANT!**  This action cannot be undone. Make sure that you really want to delete the current dashboard page. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_5.png) | Restores the current page to default dashboard template.  **IMPORTANT!**  This action cannot be undone; any customizations you did to the current page will be lost! Make sure that you really want to restore the dashboard page to default. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_6.png) | Saves the current dashboard page customization and exists the edit mode. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_7.png) | Cancels dashboard page customizations (new or existing widgets, reordering, etc.) and exists the edit mode. |

<a id="Addingwidgets"></a>

## Adding widgets

To add a widget, click the **Add widget** button (![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_1.png)) on the toolbar. The Add widget page appears.

Select the desired widget type:

- **All KPIs** – adds all KPIs: Druid predefined or custom KPIs.
- **KPI** – to show a simple KPI element.
- **Chart** – to show elements/ time series KPIs in a chart.
- **Table** – to show elements/time series KPIs in a table.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_8.png)

Click **Save**. Except for **All KPIs**, the widgets are empty.

You need to edit the widget based on the selected widget type. The next section describes how to edit various types of widgets.

<a id="Editingwidgets"></a>

## Editing widgets

> **Info:**  You will use the widget editing to customize new widgets or edit the details of a Druid predefined widget provided by the Dashboard template or a custom widget you defined.

To edit a widget, click the settings icon corresponding to the desired widget.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_9.png)

The widget Settings page appears. The page content is different based on the widget type. This section provides you with information on how to set up new widgets based on their type:

- KPI Widgets – display simple KPI values.
- Chart Widgets – show in a chart the KPI values over time (time series KPIs) or the KPI values as simple elements.
- Table Widgets – show KPI values in a table.

> **NOTE:**  You can show time series KPIs only in widgets of type **Chart** or **Table**.

<a id="EditKPIwidgets"></a>

### Edit KPI widgets

In the Settings page, select the desired metric (**Metric Name**), the KPI (**Metric Display Name**) and the **Trend Chart**, that is, the way you want to view KPI data on the widget (**Daily/Weekly/Monthly**).

> **NOTE:** The KPIs available in the **Metric Display Name** field depend on the metric selected in the **Metric Name** field.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_10.png)

Click **Save**.

On the dashboard, you can now see the widget details and the KPI.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_11.png)

Click the **Save** button from the dashboard toolbar to save the widget on the dashboard page.

The figure below provides an example of various widgets of type KPI.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_12.png)

<a id="EditChartwidgets"></a>

### Edit Chart widgets

To customize a chart widget, in the widget Settings page:

1. Select the **Chart Type**: Line, Bar or Pie.
2. In DRUID 8.11 and later, you can enable the **Display side by side** option for bar charts to show values as separate bars instead of stacking them. This makes comparisons easier, improves data clarity, and helps you quickly analyze insights.

![](../Resources/Images/druid%208.11/display%20side%20by%20side.png)

![](../Resources/Images/druid%208.11/bar%20charts.png)

3. Select the **Metric Name**.
4. From the **Show** field select how you want Druid to show the KPI values on the dashboard: as **elements** or **time series**.
5. From the **Elements** field, select the KPI elements you want to show on the chart.

> **Info:**  On a chart widget set to show time series, the time is shown on the X axis while the KPI values is shown on the Y axis. For chart widgets set to show elements, the elements are shown on the X axis, while the KPI values are shown on the Y axis.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_13.png)

Click **Save**.

On the dashboard, you can now see the widget details and the KPI.

*Time series example*

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_14.png)

*Elements example*

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_15.png)

Click the **Save** button from the dashboard toolbar to save the widget on the dashboard page.

The figure below provides an example of various widgets of type **Chart**.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_16.png)

<a id="EditTablewidgets"></a>

### Edit Table widgets

Table widgets provide you with the possibility to show KPI data on the dashboard in a table format, both KPI elements and time series KPIs.

To customize a table widget, in the widget Settings page:

1. Select the **Chart Type**: Line, Bar or Pie.
2. Select the **Metric Name**.
3. From the **Show** field select how you want Druid to show the KPI values in on the dashboard: per KPI elements or as time series.
4. From the **Elements** field, select the KPI elements you want to show in the table.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_17.png)

Click **Save**.

On the dashboard, you can now see the widget details and the KPI.

*Time series example*

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_18.png)

*Elements example*

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_19.png)

Click the **Save** button from the dashboard toolbar to save the widget on the dashboard page.

<a id="Deletingwidgets"></a>

## Deleting widgets

To delete a widget from the current dashboard page, click the delete icon corresponding to the desired widget.

<a id="Changingthetrendontimeserieswidgets"></a>

## Changing the trend on time series widgets

By default, time series widgets (table or chart) display data metrics on a daily basis. You can view data on a weekly or monthly trend, as best suits your needs.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_20.png)

Druid automatically saves the widget trend change, so when accessing the dashboard next time, the widget will show data using the updated trend.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_21.png)

<a id="ReorderingwidgetsonDashboard"></a>

## Reordering widgets on Dashboard

You can reorder the widgets on a dashboard page by using drag and drop and clicking the **Save** button on the toolbar.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_22.png)

<a id="AddingDashboardPages"></a>

## Adding Dashboard Pages

To add a new dashboard page, click the **Add page** button (![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_2.png)) from the toolbar. A pop-up appears. Type the name of the page and click **Save**.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_23.png)

The page is added as a new tab to the dashboard but you remain on the current page.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_24.png)

<a id="RenamingDashboardPages"></a>

## Renaming Dashboard Pages

To rename the current dashboard page, click the **Rename page** button (![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_3.png)) on the toolbar. A pop-up appears. Type the new name of the page and click **Save**.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_25.png)

The new page name is saved.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_26.png)

<a id="DeletingDashboardPages"></a>

## Deleting Dashboard Pages

> **IMPORTANT!** This action cannot be undone. Make sure that you really want to delete the current dashboard page.

To delete the current dashboard page, click the **Delete page** button ( ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_4.png)) from the toolbar. A confirmation dialog appears.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_27.png)

Click **Yes**. The current page is removed from the dashboard and the Dashboard Overview appears (in edit mode).

<a id="RestoretoDashboardtemplatepage"></a>

## Restore to Dashboard template page

You can restore a customized dashboard page back to the dashboard template page by selecting the desired page (dashboard tab) and clicking the **Back to Default** button from the toolbar.

A pop appears asking you to confirm the action.

![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_28.png)

Click **Yes**.

> **NOTE:**  Restoring to default a page you added to the dashboard, will remove it from the dashboard.
