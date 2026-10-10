---
title: Query Entity
---

# Query Entity

Queries the request entity to get a collection of records from DRUID Data Services.

The Edit Connector Task page appears by default on the **General** tab. Provide a brief relevant description of the task.

![](<../../../.gitbook/assets/query entity general.png>)

For optimal execution time and to conserve database resources, we recommend you select **Disable Connector Audit Logging** when the integration task involves handling substantial payloads.

### Request

Click the **Request** tab. The Request page provides you with options to define the request body:

* [set the context / scope](Query_Entity.md#Define_the_context) (optional)
* [filter the query](Query_Entity.md#Filter_the_query_\(mandatory\)) (mandatory)
* [set records pagination](Query_Entity.md#Set_records_pagination) (optional)
* [set records sorting order](Query_Entity.md#Set_records_sorting_order) (optional)

![](<../../../.gitbook/assets/query sorting and stuff.png>)

#### Define the context <a href="#define_the_context" id="define_the_context"></a>

If you want to perform the integration task in the context of the Request entity set on the connector action, than leave the **Scope** field set to **Global**.

If you want to perform the integration task on a context different from the global context set on the connector action, than from the **Scope** field, select **Local** and from the **Request entity** field, select the desired entity.

Using the **Local** scope, you do all related queries directly inside the connector action instead of building a larger context outside the connector action via additional queries within the Flow Designer to put data inside the request entity and then send the data back to the connector action.

#### Filter the query (mandatory) <a href="#filter_the_query_-mandatory" id="filter_the_query_-mandatory"></a>

You have two options to filter the query:

* by using the standard query.
* by using Druid custom query. Use custom query to interrogate entities other than the request entity without using the Query-related entity integration task. For more information, see [Filter data using Druid custom query](<Filter using DRUID custom query.md>).

![](<../../../.gitbook/assets/filtering options.png>)

To filter the query using the standard query, in the Filtering section, **Filter Group** tab, set the filtering properties for the query. You can use the following properties:

* **Logical Operator** (optional) - A property of type int32 that specifies if all the filters and filter groups apply to the query. Use AND (0) to apply all the filters and filter groups. Use OR(1) to apply any of the filters and filter groups. Default value is AND (0).
* **Filter**(mandatory) - helps you define the filtering expression. It has the following properties:

| Filter Property | Data Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Field Name      | string    | Specifies the name of the field that is to be filtered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Operator        | string    | Specifies the filter operator. Supports the following: contains, not contains, startswith, endswith, =, !=, >, <,>=, <=, in, not in, exists, not exists. Use the adequate operator for the corresponding field type. **IMPORTANT!** When using the **in** or **not in** operators to filter by multiple values, provide the values as a JSON array using square brackets, with each value enclosed in double quotes and separated by commas. **Example**: \[ "New", "Confirmed" ] **NOTE:** The operators **exists / not exists** allow you to validate that a field of type entity is instanced within the actual entity object. For example: \[\[Account\[\[.Contact.Id **not exists** means that \[\[Account]].Contact has not been instanced (the property Contacts does not exist in the actual \[\[Account]] entity object.                                                                                                                                                                                                                                              |
| Function        |           | Functions you can use to filter data of type string and date, as follows: - **Case Insensitive** - Filter data of type string to ensure that results being returned by the query are case-insensitive. Using this function you can enrich the quick search views to enable searching for case insensitive terms. ![](<../../../.gitbook/assets/query insensitive.png>) **Info:** If you want the query to return both case sensitive and case insensitive results, add filters with and without the **Case Insensitive** function. - **Date filtering functions** - Filter data of the following types: Date, DateTime, InvariantDateTime and InvariantDate to ensure that results being returned by the query are from a specific day or within a specific time range. For more information, see [Standard Query Date Functions Reference](<Standard Query Date Functions Reference.md>). ![](<../../../.gitbook/assets/filter by date.png>) Example: get the list of brands which have been created within the last 6 months. ![](<../../../.gitbook/assets/get brands.png>) |
| Value           | string    | Specifies the filtering value. **IMPORTANT!** **DO NOT** provide the value between quotes (e.g., **0760463181** instead of **"0760463181"**). If you want to query for null, then provide **null** (lowercase, no quotes ""). ![](<../../../.gitbook/assets/value no string.png>)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

![](../../../.gitbook/assets/filtering.png)

To set another filtering option to the query, click the **AddFilterGroup** (![](<../../../.gitbook/assets/add filter group.png>)) button. Another filtering group tab appears that contains the filtering properties described above.

#### Set records pagination (optional) <a href="#set_records_pagination" id="set_records_pagination"></a>

| Pagination Property               | Data Type | Description                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Start at record number            | int32     | Specifies the number of records to skip before starting to return records from the query. Use it with the **Limit number of retrieved records** property to implement pagination. Default value is 0 if not specified. The records are ordered ascending by the Id field. To change the records sorting order, set the properties in the Sorting section. |
| Limit number of retrieved records | int32     | Specifies the maximum number of records to read from DRUID Data Service. Use it with the **Start at record number** property to implement pagination. Default value is 100 if not specified. The maximum value can be 1000.                                                                                                                               |
| Expansion level                   | int32     | Specifies the depth of the records to be retrieved.                                                                                                                                                                                                                                                                                                       |

![](<../../../.gitbook/assets/query pagination.png>)

#### Set records sorting order (optional) <a href="#set_records_sorting_order" id="set_records_sorting_order"></a>

By default, all records are ordered ascending by the Id field. You can sort the returned records by one or multiple fields. To change the records sorting order, in the Sorting section, set the following properties:

| Pagination Property          | Data Type | Description                                                                                                                                         |
| ---------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Field Name                   | string    | Specifies the field used to sort the returned records. The name must correspond to a valid field, and it is case-sensitive.                         |
| Sort in descending direction | boolean   | By default, the records retrieved from the query are ordered ascendingly. To sort the records descending, set the value of this property to "true". |

![](<../../../.gitbook/assets/query sorting.png>)

### Response

Click the **Response** tab. By default, the integration task output will be saved in the global context, that is, the Response entity set on the connector action. If you want to save the response in an entity different from the global one set on the connector action, than from the **Scope** field, select **Local** and from the **Response entity** field, select the desired entity.

{% hint style="info" %}
**NOTE:** For Query Entity tasks with custom query filtering requests, you can now save the response in the **Local** scope using an entity different from the request entity.

<img src="../../../.gitbook/assets/differ response entity.png" alt="" data-size="original">
{% endhint %}

Druid displays the entity schema tree mapping (the request entity and its child fields) in a single table with nested rows based on the **Expansion level** set on the request (pagination section).

The entity fields list includes 'Entity List' type fields. This optimizes performance by enabling the retrieval of data related to the root (response) entity within the Get entity integration without the need for multiple Query related entity integration tasks.

{% hint style="info" %}
**NOTE:** To leverage this feature, an upgrade of the DRUID Connector Host to version 5.29 or higher is required.
{% endhint %}

You can select specific fields to bring, simplifying processes such as fetching all activities for a campaign and obtaining specific details for each activity.

To bring a collection of records, select the desired 'Entity List' type field and from the corresponding drop-down, select the foreign key that is the field from the base entity of the collection (e.g., CampaignActivity) that refers the response entity (e.g., Campaign).

{% hint style="warning" %}
**IMPORTANT!** Be careful of the payload size when manually mapping 'Entity List' type fields in Query entity, as it retrieves all records, including child records.
{% endhint %}

![](../../../.gitbook/assets/getentity.png)

{% hint style="info" %}
**NOTE:** Mapping all fields ignores the 'Entity List' type fields.
{% endhint %}

To map all entity scalar fields and "Entity" type existing on the request entity, tap on **Map All Fields**.

If you choose to map only specific entity fields in the response, additional field mapping actions are available:

* **Refresh fields** - If you added new entity fields to the request entity, this action will load all entity fields.
* **Select all fields** - Selects all existing entity fields to be included in the response. Use it when you want to map many entity fields and exclude the desired entity fields from the response by clicking the check mark in front of the entity field(s).
* **Deselect all fields**. Deselects the entity fields mapped in the response. Use it when you want to manually select a few entity fields in the response.
* **Show all mapped fields**. Only displays the list of entity fields mapped in the response.

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.

### Test the integration task

You can test the integration task by clicking the **Test** tab and then the **Test** button (![](<../../../.gitbook/assets/Add Entity_8.png>)).

![](<../../../.gitbook/assets/Query Entity_5.png>)
