---
title: "Delete Entity"
---

<a id="DeleteEntity"></a>


Deletes an entity record based on the Id saved within the conversation context

The Edit Connector Task page appears by default on the **General** tab. Provide a brief relevant description of the task.

![](../../Resources/Images/Druid%20Data%20Service%20Connector/delete%20enytity%20general.png)

For optimal execution time and to conserve database resources, we recommend you select **Disable Connector Audit Logging** when the integration task involves handling substantial payloads.

<a id="Request"></a>

## Request

Click the **Request** tab. The Request page provides you with options to define the request body:

- [set the context / scope](#Set_the_context_of_the_integration_task) (optional)
- [batch execution entity list](#Batch_execution_entity_list)
- [delete by filter](#Delete_by_filter)

<a id="Setthecontextoftheintegrationtask"></a>

### <a id="Set_the_context_of_the_integration_task"></a>Set the context of the integration task

If you want to perform the integration task in the context of the Request entity set on the connector action, than leave the **Scope** field set to **Global**.

If you want to perform the integration task on a context different from the global context set on the connector action, than from the **Scope** field, select **Local** and from the **Request entity** field, select the desired entity.

Using the **Local** scope, you do all related queries directly inside the connector action instead of building a larger context outside the connector action via additional queries within the Flow Designer to put data inside the request entity and then send the data back to the connector action.

<a id="Batchexecutionentitylist"></a>

### <a id="Batch_execution_entity_list"></a>Batch execution entity list

The **Batch execution entity list** field lists all the fields of type "Entity list" created on the request entity (all entity lists). From the **Batch execution entity list** field, select the desired entity field and click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.

> **IMPORTANT!** When deleting a batch execution entity list, all children are deleted. For example, if from the **Batch execution entity list** field, you select "Cases", for the account ID that comes in the conversation context or in a form, all related cases will be deleted.
>
> ![](../../Resources/Images/Druid%20Data%20Service%20Connector/batch%20execution.png)

> **Info:** You cannot delete by filter if you select an **Batch execution entity list**

<a id="Deletebyfilter"></a>

### <a id="Delete_by_filter"></a>Delete by filter

You can delete records based on specific filtering conditions.

The **Delete by filter** field lists all fields of type entity related with the request entity (that is, the parent entity). From the **Delete by filter** field, select the desired entity field. In the Filtering area, click on the **+** icon and select **Add new filter**.

![](../../Resources/Images/Druid%20Data%20Service%20Connector/add%20new%20filter.png)

Define a filtering expression. To provide more filtering conditions, click **Add new filter** and enter the filtering expression.

| Filter Property | Data Type | Description |
| --- | --- | --- |
| Field Name | string | From the drop-down, select the field to be filtered. |
| Operator | string | Specifies the filter operator. Supports the following: contains, not contains, starts with, ends with, =, !=, >, <,>=, <=, in, not in, exists, not exists. Use the adequate operator for the corresponding field type. |
| Function |  | Functions you can use to filter data of type string and date:   - **Case Insensitive** - Filter data of type string to ensure that results being returned by the query are case-insensitive. Using this function you can enrich the quick search views to enable searching for case insensitive terms.  **Info:** If you want the query to return both case sensitive and case insensitive results, add filters with and without the **Case Insensitive** function. - **Date filtering** functions - Filter data of the following types: Date, DateTime, InvariantDateTime and InvariantDate to ensure that results being returned by the query are from a specific day or within a specific time range. For more information, see [Standard Query Date Functions Reference](Standard%20Query%20Date%20Functions%20Reference.md). |
| Value | string | Specifies the filtering value.  **IMPORTANT!** **DO NOT** provide the value between quotes (e.g., **add - 1** instead of **"add - 1"**). If you want to query for null, then provide **null** (lowercase, no quotes ""). |

Example: From [[Account]].Cases delete all accounts that have the status "Active" and the account name contains the word "Jane".

![](../../Resources/Images/Druid%20Data%20Service%20Connector/delete%20filter%20example.png)

> **NOTE:** If you select an entity field from **Delete by filter** and you try saving the integration task without providing a filtering expression, you will get an error message. If you want to delete all the records associated with the request entity, tap on **Delete all records** and save the integration task.

<a id="CascadeDelete"></a>

### Cascade Delete

When deleting an entity, you often need to ensure that related child records are also deleted to maintain data consistency and prevent orphaned data. The Cascade Delete feature allows you to specify entity lists where the delete operation should automatically propagate.

> **NOTE:** This feature is available for DRUID 8.18 and higher.

To configure cascade delete, from the **Cascade Delete** field, select the entity list(s) to which you want the delete operation to propagate.

![](../../Resources/Images/druid%208.18/cascade%20delete.png)

> **IMPORTANT!**
>
> - When you select an entity list for cascade delete, all associated child records within that list will be automatically deleted along with the parent record.
> - This functionality ensures data integrity by preventing orphaned records, but use it carefully to avoid unintended data loss.

<a id="Testtheintegrationtask"></a>

## Test the integration task

> **NOTE:** In order to test the Delete entity task, you first need to test the Add entity task and from the **TestResult** copy the value of the entity record **Id**.
>
> ![](../../Resources/Images/Druid%20Data%20Service%20Connector/Get%20Entity_4.png)

To test the Delete entity integration task, click the **Test** tab. In the RequestEntity, provide the Id of the entity record you copied from the TestResult of the Add entity task and click the **Test** button (![](../../Resources/Images/Druid%20Data%20Service%20Connector/Add%20Entity_8.png)).

![](../../Resources/Images/Druid%20Data%20Service%20Connector/Delete%20Entity_1.png)
