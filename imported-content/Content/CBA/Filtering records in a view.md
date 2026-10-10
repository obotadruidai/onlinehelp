---
title: Filtering records in a view
---

# Filtering records in a view

{% hint style="warning" %}
**IMPORTANT!** You need to upgrade both the DRUID Connector Host to version 5.29 or higher and the entity associated with the web view; otherwise, loading the web view will fail.
{% endhint %}

You can filter all columns in a view regardless the data type in ascending or descending order.

For data of type string, integer and decimal you can use filters to help you narrow down the records you want to see.

![](<../../.gitbook/assets/filetring rules.png>)

{% hint style="info" %}
**NOTE:** Extended filters are available in DRUID 5.22 and higher.
{% endhint %}

To filter the records in a view by applying filters on a specific column, click the **Filter** icon in the column header, then select the condition and define the filter rule(s) and click **Apply**.

The view displays the records based on the selected filtering criteria.

![](<../../.gitbook/assets/filtered view.png>)

{% hint style="info" %}
**Info:** You can add maximum two filter rules.
{% endhint %}

### Choose the filtering condition (logical operator)

The first step in creating filter criteria is to select the type of condition you want to use. The following conditions are available:

* **Match All** provides you with "And" functionality. Choose this option when you want all of the filter rules to be met.
* **Match Any** provides you with "Or" functionality. Choose this option when you have two filter rules and at least one condition has to be met.

### Define the filter rules

To define the filter rule, select the desired operator and specify a single value. The table below provides the list of operators that are available for columns that contain data of type string, integer and decimal.

| Operator     | Description                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Starts with  | The results include only the records where the data in the column starts with the value specified in the filter rule.      |
| Contains     | The results include only the records where the data in the column contains the value specified in the filter rule.         |
| Not contains | The results include only the records where the data in the column does not contain the value specified in the filter rule. |
| Ends with    | The results include only the records where the data in the column ends with the value specified in the filter rule.        |
| Equals       | The results include only the records where the data in the column matches the value in the filter.                         |
| Not equals   | The results include only records where the data in the column does not match the value in the filter.                      |

To remove a filter rule, click **Remove rule**. To remove the filter, click **Clear** in the filter.

### Automatically take into consideration the server-side web view filtering and pagination

{% hint style="warning" %}
**IMPORTANT!** Automatic server-side filtering and pagination is available only for web views that contain data from DRUID Data Service.
{% endhint %}

Filtering and pagination are seamlessly handled server-side, harmonizing with any client-side settings. The user's applied filters and pagination on the web view synchronize with the Query entity integration defined on the server-side, ensuring a unified experience.

{% hint style="info" %}
**NOTE:** To make use of this feature, you'll need to upgrade both the DRUID Connector Host to version 5.29 or higher, and the entity associated with the web view.
{% endhint %}

To upgrade the entity associated with the web view, go to the entity details, click the **Fields** tab and in the notification displayed on top of the page, click the **Upgrade** button.

![](<../../.gitbook/assets/upgrade entity (1).png>)

A window appears. Review the new fields that will be added to your entity and click **Upgrade** again.

![](<../../.gitbook/assets/updrage new field.png>)

Following the upgrades, a new system field of type 'Entity', **PageInfo**, becomes available in the upgraded entity. PageInfo references \[\[PageInfo]], a new system entity. This field facilitates the transfer of specific page-related information from the client-side to the server-side (the Query entity task defined on the web view).

![](<../../.gitbook/assets/page info added.png>)

For more information about the \[\[PageInfo]] system entity, see [System Entities](<../5_Entities/System Entities.md>).

### Server-side pagination for non-DRUID Data Service databases

For efficient handling of large amounts of data, use server-side pagination on web views. Follow these steps to enable server-side pagination in web views that display data from non-Druid Data Service databases like MS SQL:

#### Step 1: Upgrade Connector Host and Data Service to version 5.29 or higher

Ensure both the Connector Host and Data Service are upgraded to the latest version.

#### Step 2: Alter the integration task for Server-Side Pagination.

Modify the integration task (SQL, REST, CRM, etc.) to retrieve data, including the aggregated “totalCount” value in the response.

Here's an example SQL integration task:

**Request - SQL statement**

```
declare @totalCount int 
set @totalCount = (select count(*) from keyword)
 
select @totalCount as totalCount, b.* from 
    (select lower(keyphrase) as Keyphrase
    from keyword
    order by keyphrase
    OFFSET @PageStartIndex ROWS
    FETCH NEXT @NumberOfRecords ROWS ONLY)
as b
```

![](<../../.gitbook/assets/sql pagination request.png>)

Map the "totalCount" value to a local response variable in the **Response** tab.

![](<../../.gitbook/assets/SQL RESPONSE.png>)

#### Step 3: Add Custom Code for "totalCount" Mapping

Use a Custom Code integration task to send the aggregated total number of available records ("totalCount") from the connector integration towards the DRUID web view.

In the Custom Code task, add the following JavaScript code:

**Custom Code task**

```
(function main(){
    let totalCount = Context.GetContextVariable("totalCount");
    Context.SetPageInfoTotalCount(parseInt(totalCount));
})()
```

Ensure the "totalCount" variable is delivered as an integer to the `SetPageInfoTotalCount()` method. In the example above, we used the `parseInt()` JavaScript function to convert the value to an integer.

{% hint style="info" %}
**Info:** The Custom Code task adds the parameter value to the response of the connector integration, without altering the response entity.
{% endhint %}

![](<../../.gitbook/assets/custom code (1).png>)

#### Step 4: Verify the web view pagination

Verify your configuration and ensure that the pagination works in client-server mode, especially for large data sets (larger than 1000 records).
