---
title: "Track Business KPIs"
---

<a id="TrackBusinessKPIs"></a>


Custom dashboards give you a flexible, centralized space to visualize the data that matters most to your role — whether that's service desk performance, task monitoring, or business outcomes like cost savings and resolution rates.

Unlike the built-in AI Agent Summary dashboard, which provides ready-made engagement metrics, custom dashboards let you combine conversational data with records from Druid Data Service and third-party systems, and arrange them in a layout tailored to your needs.

You can surface key metrics using Light widgets — including AI Agent KPIs similar to those on the AI Agent Summary Engagement page — alongside tables and charts.

For advanced reporting, you can export data using the /GenericIntegration API and connect it to external tools such as Power BI or other business intelligence platforms, enabling you to build custom reports and align analytics with your organization's reporting standards.

<a id="Creatingcustomdashboards"></a>

## Creating custom dashboards

Before creating custom dashboards, make sure that you created web views and charts and integrations to show records and data from Druid Data Service and third-party systems.

To create a custom dashboard, follow these steps:

1. Select the AI Agent and solution.
2. From **Solution Contents** menu, click **Dashboards**.
3. At the top-right corner of the Dashboards page, click the **Create new dashboard** button.
4. Enter a **Name** and **Description** and click **Save**.

![](../Resources/Images/Custom%20Dashboards/Custom%20Dashboards.png)

The new dashboards appears on the Dashboards page.

![](../Resources/Images/Custom%20Dashboards/Custom%20Dashboards_1.png)

<a id="Customizingthecustomdashboards"></a>

## Customizing the custom dashboards

To edit the dashboard template, on the top-right corner of the Dashboard, tap on **Edit mode**.

The Dashboard becomes editable: a toolbar appears at the bottom and all dashboard widgets become editable. You can navigate through dashboard pages and edit the dashboard pages according to your needs.

The toolbar provides you with the following options:

|  |  |
| --- | --- |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_1.png) | Add a new widget on the dashboard page. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_2.png) | Add a new dashboard page. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_3.png) | Rename the current dashboard page. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_4.png) | Delete the current dashboard page.  **IMPORTANT!**  This action cannot be undone. Make sure that you really want to delete the current dashboard page. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_6.png) | Saves the current dashboard page customization and exists the edit mode. |
| ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_7.png) | Cancels dashboard page customizations (new or existing widgets, reordering, etc.) and exists the edit mode. |

<a id="Addingwidgets"></a>

## Adding widgets

To add a widget, click the **Add widget** button (![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_1.png)) on the toolbar. The Add widget page appears.

Select the desired widget type: Table (web view), Chart or Light widget and click **Save**.

{% hint style="info" %}
**Info:** Use the **Light widget** type to display key metrics like totals, averages, and other unique values on the dashboard. This is similar to the KPIs shown on the **AI Agent Summary** > **Engagement** page.
{% endhint %}

Click the settings icon corresponding to the widget. The widget Settings page appears.

Select the desired entity and entity view and click **Save**.

![](../Resources/Images/druid%208.14/custom%20dash%20widget%20edit.png)

In Druid 9.11 and higher you can choose to **Show view names** in dashboards for light widgets.

![](../Resources/Images/druid%209.11/SELECT%20SHOW%20VIEW%20NAME.png)

![](../Resources/Images/druid%209.11/widget%20name%20view.png)

To configure a Light widget to display a AI Agent KPI, go to the widget configuration page, tap on **isBotKPI**, then select the desired metric, metric name, and trend.

![](../Resources/Images/druid%208.14/knpi%20in%20custom%20dash.png)

{% hint style="warning" %}
**IMPORTANT!** By default, custom dashboards display insights into all records created within the last week, without the option to filter data for a specific period. To enable data filtering in custom dashboards, follow a specific setup. For more information, see the subsequent sections.
{% endhint %}

![](../Resources/Images/Custom%20Dashboards/Custom%20Dashboards_10.png)

<a id="Filteringtablerecordsonthedashboard"></a>

## <a id="Filterin"></a>Filtering table records on the dashboard

You can configure dashboard views (tables) to dynamically update based on the date range selected on the dashboard. This process is simplified and handled directly within the existing view settings:

1. Go to the view configuration page.
2. Locate and switch the **Apply Dashboard Date Filter** toggle to on.
3. From the dropdown, select the specific date-type field (e.g., CreatedOn, ClosedOn, etc.) that the dashboard filter should target.

![](../Resources/Images/Custom%20Dashboards/filter%20views.png)

4. Save the view.

The dashboard table will now automatically synchronize its records whenever a user adjusts the dashboard date range.

<a id="ForDruidversionspriorto918"></a>

### For Druid versions prior to 9.18

In earlier versions, to filter table records on the dashboard within a specific period required a more tedious setup:

1. Add the fields **SearchStartDate** and **SearchEndDate** (DateTime type) to your desired entities.
2. Create a web view (table) dedicated to custom dashboards and select the option **Do not show in Workspace** to prevent the view from appearing in the workspace or on the entity > **Data** tab.

![](../Resources/Images/DRUID%207.15/custom%20dashboard%20view.png)

3. In the view, add an integration that filters by SearchStartDate and SearchEndDate (>= SearchStartDate and <= SearchEndDate).

![](../Resources/Images/Custom%20Dashboards/Filtering%20table%20records%20on.png)

4. Add this table to the dashboard.

You can now filter records based on a specific period.

![](../Resources/Images/Custom%20Dashboards/Filtering%20table%20records%20on_1.png)

<a id="Filteringdataindynamiccharts"></a>

## Filtering data in dynamic charts

{% hint style="info" %}
**NOTE:** This feature is available in DRUID 7.10 onwards.
{% endhint %}

To filter data in dynamic charts on the dashboard:

1. Go to the entity where you created the dynamic chart.
2. Click the **Charts** tab.
3. Click the dynamic chart you added to the custom dashboard.
4. In the General settings, scroll down and select the desired field from **Filter By**.
5. Save the chart configuration.

You can filter data within a specific period in dynamic charts on the dashboard.

<a id="Filteringchartdrilldownviewsbydashboardtimeinterval"></a>

### Filtering chart drill-down views by dashboard time interval

When the **Filter By** field is configured on a dynamic chart, performing a drill-down from that chart automatically displays records within the dashboard time interval currently selected, based on that specific field. No additional integrations are required to filter records in the drill-down view.

{% hint style="info" %}
**NOTE:** In Druid version 9.17 and higher, drill-down views in dynamic charts are filtered by the dashboard time interval by default if the **Filter By** field is set on the chart.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** The drill-down and Filter By fields apply only to dynamic charts. If you are not using dynamic charts, these fields are disregarded. To apply drill-down view grouping, filtering, and the dashboard time interval to non-dynamic charts, you must update the code manually—either in the chart Advanced Editor or in the Custom Code, depending on how the chart was created.
{% endhint %}

<a id="Deletingwidgets"></a>

## Deleting widgets

To delete a widget from the current dashboard page, click the delete icon corresponding to the desired widget.

<a id="ReorderingwidgetsonDashboard"></a>

## Reordering widgets on Dashboard

You can reorder the widgets on a dashboard page by using drag and drop and clicking the **Save** button on the toolbar.

<a id="AddingDashboardPages"></a>

## Adding Dashboard Pages

To add a new dashboard page, click the **Add page** button (![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_2.png)) from the toolbar. A pop-up appears. Type the name of the page and click **Save**. The page is added as a new tab to the dashboard but you remain on the current page.

<a id="RenamingDashboardPages"></a>

## Renaming Dashboard Pages

To rename the current dashboard page, click the **Rename page** button (![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_3.png)) on the toolbar. A pop-up appears. Type the new name of the page and click **Save**. The new page name is saved.

<a id="DeletingDashboardPages"></a>

## Deleting Dashboard Pages

{% hint style="warning" %}
**IMPORTANT!** This action cannot be undone. Make sure that you really want to delete the current dashboard page.
{% endhint %}

To delete the current dashboard page, click the **Delete page** button ( ![](../Resources/Images/Dashboard/Customizing%20Dashboard%20Template_4.png)) from the toolbar. A confirmation dialog appears.

Click **Yes**. The current page is removed from the dashboard.
