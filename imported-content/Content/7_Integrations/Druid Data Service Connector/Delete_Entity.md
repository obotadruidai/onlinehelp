---
title: Delete Entity
---

# Delete Entity

Deletes an entity record based on the Id saved within the conversation context

The Edit Connector Task page appears by default on the **General** tab. Provide a brief relevant description of the task.

![](<../../../.gitbook/assets/delete enytity general.png>)

For optimal execution time and to conserve database resources, we recommend you select **Disable Connector Audit Logging** when the integration task involves handling substantial payloads.

### Request

Click the **Request** tab. The Request page provides you with options to define the request body:

* [set the context / scope](Delete_Entity.md#Set_the_context_of_the_integration_task) (optional)
* [batch execution entity list](Delete_Entity.md#Batch_execution_entity_list)
* [delete by filter](Delete_Entity.md#Delete_by_filter)

#### Set the context of the integration task <a href="#set_the_context_of_the_integration_task" id="set_the_context_of_the_integration_task"></a>

If you want to perform the integration task in the context of the Request entity set on the connector action, than leave the **Scope** field set to **Global**.

If you want to perform the integration task on a context different from the global context set on the connector action, than from the **Scope** field, select **Local** and from the **Request entity** field, select the desired entity.

Using the **Local** scope, you do all related queries directly inside the connector action instead of building a larger context outside the connector action via additional queries within the Flow Designer to put data inside the request entity and then send the data back to the connector action.

#### Batch execution entity list <a href="#batch_execution_entity_list" id="batch_execution_entity_list"></a>

The **Batch execution entity list** field lists all the fields of type "Entity list" created on the request entity (all entity lists). From the **Batch execution entity list** field, select the desired entity field and click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.

{% hint style="warning" %}
**IMPORTANT!** When deleting a batch execution entity list, all children are deleted. For example, if from the **Batch execution entity list** field, you select "Cases", for the account ID that comes in the conversation context or in a form, all related cases will be deleted.

<img src="../../../.gitbook/assets/batch execution.png" alt="" data-size="original">
{% endhint %}

{% hint style="info" %}
**Info:** You cannot delete by filter if you select an **Batch execution entity list**
{% endhint %}

#### Delete by filter <a href="#delete_by_filter" id="delete_by_filter"></a>

You can delete records based on specific filtering conditions.

The **Delete by filter** field lists all fields of type entity related with the request entity (that is, the parent entity). From the **Delete by filter** field, select the desired entity field. In the Filtering area, click on the **+** icon and select **Add new filter**.

![](<../../../.gitbook/assets/add new filter.png>)

Define a filtering expression. To provide more filtering conditions, click **Add new filter** and enter the filtering expression.

| Filter Property | Data Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Field Name      | string    | From the drop-down, select the field to be filtered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Operator        | string    | Specifies the filter operator. Supports the following: contains, not contains, starts with, ends with, =, !=, >, <,>=, <=, in, not in, exists, not exists. Use the adequate operator for the corresponding field type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Function        |           | Functions you can use to filter data of type string and date: - **Case Insensitive** - Filter data of type string to ensure that results being returned by the query are case-insensitive. Using this function you can enrich the quick search views to enable searching for case insensitive terms. **Info:** If you want the query to return both case sensitive and case insensitive results, add filters with and without the **Case Insensitive** function. - **Date filtering** functions - Filter data of the following types: Date, DateTime, InvariantDateTime and InvariantDate to ensure that results being returned by the query are from a specific day or within a specific time range. For more information, see [Standard Query Date Functions Reference](<Standard Query Date Functions Reference.md>). |
| Value           | string    | Specifies the filtering value. **IMPORTANT!** **DO NOT** provide the value between quotes (e.g., **add - 1** instead of **"add - 1"**). If you want to query for null, then provide **null** (lowercase, no quotes "").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

Example: From \[\[Account]].Cases delete all accounts that have the status "Active" and the account name contains the word "Jane".

![](<../../../.gitbook/assets/delete filter example.png>)

{% hint style="info" %}
**NOTE:** If you select an entity field from **Delete by filter** and you try saving the integration task without providing a filtering expression, you will get an error message. If you want to delete all the records associated with the request entity, tap on **Delete all records** and save the integration task.
{% endhint %}

#### Cascade Delete

When deleting an entity, you often need to ensure that related child records are also deleted to maintain data consistency and prevent orphaned data. The Cascade Delete feature allows you to specify entity lists where the delete operation should automatically propagate.

{% hint style="info" %}
**NOTE:** This feature is available for DRUID 8.18 and higher.
{% endhint %}

To configure cascade delete, from the **Cascade Delete** field, select the entity list(s) to which you want the delete operation to propagate.

![](<../../../.gitbook/assets/cascade delete.png>)

{% hint style="warning" %}
**IMPORTANT!**

* When you select an entity list for cascade delete, all associated child records within that list will be automatically deleted along with the parent record.
* This functionality ensures data integrity by preventing orphaned records, but use it carefully to avoid unintended data loss.
{% endhint %}

### Test the integration task

{% hint style="info" %}
**NOTE:** In order to test the Delete entity task, you first need to test the Add entity task and from the **TestResult** copy the value of the entity record **Id**.

<img src="../../../.gitbook/assets/Get Entity_4.png" alt="" data-size="original">
{% endhint %}

To test the Delete entity integration task, click the **Test** tab. In the RequestEntity, provide the Id of the entity record you copied from the TestResult of the Add entity task and click the **Test** button (![](<../../../.gitbook/assets/Add Entity_8.png>)).

![](<../../../.gitbook/assets/Delete Entity_1.png>)
