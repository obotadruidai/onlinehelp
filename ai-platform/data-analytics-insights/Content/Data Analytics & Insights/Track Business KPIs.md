---
title: Track Business KPIs
---


Custom dashboards give you a flexible, centralized space to visualize the data that matters most to your role — whether that's service desk performance, task monitoring, or business outcomes like cost savings and resolution rates.

Unlike the built-in AI Agent Summary dashboard, which provides ready-made engagement metrics, custom dashboards let you combine conversational data with records from Druid Data Service and third-party systems, and arrange them in a layout tailored to your needs.

You can surface key metrics using Light widgets — including AI Agent KPIs similar to those on the AI Agent Summary Engagement page — alongside tables and charts.

For advanced reporting, you can export data using the /GenericIntegration API and connect it to external tools such as Power BI or other business intelligence platforms, enabling you to build custom reports and align analytics with your organization's reporting standards.

## Creating custom dashboards

Before creating custom dashboards, make sure that you created web views and charts and integrations to show records and data from Druid Data Service and third-party systems.

To create a custom dashboard, follow these steps:

1. Select the AI Agent and solution.
2. From **Solution Contents** menu, click **Dashboards**.
3. At the top-right corner of the Dashboards page, click the **Create new dashboard** button.
4. Enter a **Name** and **Description** and click **Save**.

![](<../../.gitbook/assets/Custom Dashboards.png>)

The new dashboards appears on the Dashboards page.

![](<../../.gitbook/assets/Custom Dashboards_1.png>)

## Customizing the custom dashboards

To edit the dashboard template, on the top-right corner of the Dashboard, tap on **Edit mode**.

The Dashboard becomes editable: a toolbar appears at the bottom and all dashboard widgets become editable. You can navigate through dashboard pages and edit the dashboard pages according to your needs.

The toolbar provides you with the following options:

|                                                                   |                                                                                                                                                      |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](<../../.gitbook/assets/Live Dashboard_2.png>)                 | Add a new widget on the dashboard page.                                                                                                              |
| ![](<../../.gitbook/assets/Live Dashboard_3.png>)                 | Add a new dashboard page.                                                                                                                            |
| ![](<../../.gitbook/assets/Live Dashboard_4.png>)                 | Rename the current dashboard page.                                                                                                                   |
| ![](<../../.gitbook/assets/Live Dashboard_5.png>)                 | Delete the current dashboard page. **IMPORTANT!** This action cannot be undone. Make sure that you really want to delete the current dashboard page. |
| ![](<../../.gitbook/assets/Customizing Dashboard Template_6.png>) | Saves the current dashboard page customization and exists the edit mode.                                                                             |
| ![](<../../.gitbook/assets/Live Dashboard_8.png>)                 | Cancels dashboard page customizations (new or existing widgets, reordering, etc.) and exists the edit mode.                                          |

## Adding widgets

To add a widget, click the **Add widget** button (![](<../../.gitbook/assets/Live Dashboard_2.png>)) on the toolbar. The Add widget page appears.

Select the desired widget type: Table (web view), Chart or Light widget and click **Save**.

{% hint style="info" %}
**Info:** Use the **Light widget** type to display key metrics like totals, averages, and other unique values on the dashboard. This is similar to the KPIs shown on the **AI Agent Summary** > **Engagement** page.
{% endhint %}

Click the settings icon corresponding to the widget. The widget Settings page appears.

Select the desired entity and entity view and click **Save**.

![](<../../.gitbook/assets/custom dash widget edit.png>)

In Druid 9.11 and higher you can choose to **Show view names** in dashboards for light widgets.

![](<../../.gitbook/assets/SELECT SHOW VIEW NAME.png>)

![](<../../.gitbook/assets/widget name view.png>)

To configure a Light widget to display a AI Agent KPI, go to the widget configuration page, tap on **isBotKPI**, then select the desired metric, metric name, and trend.

![](<../../.gitbook/assets/knpi in custom dash.png>)

{% hint style="warning" %}
**IMPORTANT!** By default, custom dashboards display insights into all records created within the last week, without the option to filter data for a specific period. To enable data filtering in custom dashboards, follow a specific setup. For more information, see the subsequent sections.
{% endhint %}

![](<../../.gitbook/assets/Custom Dashboards_10.png>)

## Filtering table records on the dashboard <a href="#filterin" id="filterin"></a>

You can configure dashboard views (tables) to dynamically update based on the date range selected on the dashboard. This process is simplified and handled directly within the existing view settings:

1. Go to the view configuration page.
2. Locate and switch the **Apply Dashboard Date Filter** toggle to on.
3. From the dropdown, select the specific date-type field (e.g., CreatedOn, ClosedOn, etc.) that the dashboard filter should target.

![](<../../.gitbook/assets/filter views.png>)

4. Save the view.

The dashboard table will now automatically synchronize its records whenever a user adjusts the dashboard date range.

### For Druid versions prior to 9.18

In earlier versions, to filter table records on the dashboard within a specific period required a more tedious setup:

1. Add the fields **SearchStartDate** and **SearchEndDate** (DateTime type) to your desired entities.
2. Create a web view (table) dedicated to custom dashboards and select the option **Do not show in Workspace** to prevent the view from appearing in the workspace or on the entity > **Data** tab.

![](<../../.gitbook/assets/custom dashboard view.png>)

3. In the view, add an integration that filters by SearchStartDate and SearchEndDate (>= SearchStartDate and <= SearchEndDate).

![](<../../.gitbook/assets/Filtering table records on.png>)

4. Add this table to the dashboard.

You can now filter records based on a specific period.

![](<../../.gitbook/assets/Filtering table records on_1.png>)

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

### Filtering chart drill-down views by dashboard time interval

When the **Filter By** field is configured on a dynamic chart, performing a drill-down from that chart automatically displays records within the dashboard time interval currently selected, based on that specific field. No additional integrations are required to filter records in the drill-down view.

{% hint style="info" %}
**NOTE:** In Druid version 9.17 and higher, drill-down views in dynamic charts are filtered by the dashboard time interval by default if the **Filter By** field is set on the chart.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** The drill-down and Filter By fields apply only to dynamic charts. If you are not using dynamic charts, these fields are disregarded. To apply drill-down view grouping, filtering, and the dashboard time interval to non-dynamic charts, you must update the code manually—either in the chart Advanced Editor or in the Custom Code, depending on how the chart was created.
{% endhint %}

## Deleting widgets

To delete a widget from the current dashboard page, click the delete icon corresponding to the desired widget.

## Reordering widgets on Dashboard

You can reorder the widgets on a dashboard page by using drag and drop and clicking the **Save** button on the toolbar.

## Adding Dashboard Pages

To add a new dashboard page, click the **Add page** button (![](<../../.gitbook/assets/Live Dashboard_3.png>)) from the toolbar. A pop-up appears. Type the name of the page and click **Save**. The page is added as a new tab to the dashboard but you remain on the current page.

## Renaming Dashboard Pages

To rename the current dashboard page, click the **Rename page** button (![](<../../.gitbook/assets/Live Dashboard_4.png>)) on the toolbar. A pop-up appears. Type the new name of the page and click **Save**. The new page name is saved.

## Deleting Dashboard Pages

{% hint style="warning" %}
**IMPORTANT!** This action cannot be undone. Make sure that you really want to delete the current dashboard page.
{% endhint %}

To delete the current dashboard page, click the **Delete page** button ( ![](<../../.gitbook/assets/Live Dashboard_5.png>)) from the toolbar. A confirmation dialog appears.

Click **Yes**. The current page is removed from the dashboard.
