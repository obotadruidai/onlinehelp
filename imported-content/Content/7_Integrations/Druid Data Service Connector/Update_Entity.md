---
layout:
  title:
    visible: false
---

<a id="UpdateEntity"></a>

# Update Entity

The Update Entity integration task allows you to modify one or more entity records based on the stored Id within the conversation context or update multiple records meeting specific conditions.

The Edit Connector Task page appears by default on the **General** tab. Provide a brief relevant description of the task. Optionally, include a comment for internal reference.

![](../../Resources/Images/Druid%20Data%20Service%20Connector/update%20entity%20general.png)

For optimal execution time and to conserve database resources, we recommend you select **Disable Connector Audit Logging** when handling substantial payloads.

<a id="Request"></a>

## Request

Click the **Request** tab.

If you want to perform the integration task in the context of the Request entity set on the connector action, than leave the **Scope** field set to **Global**.

If you want to perform the integration task on a context different from the global context set on the connector action, than from the **Scope** field, select **Local** and from the **Request entity** field, select the desired entity.

Using **Local** scope allows direct queries within the connector action, eliminating the need for additional queries in the Flow Designer to build a larger context.

<a id="Performupdateongivenrecords"></a>

### Perform update on given records

> **NOTE:** In DRUID versions prior to 7.1, this is the default functionality.

To update a specific record or multiple related records in DRUID Data Service provided in the request entity based on the Id in the conversation context, choose **On given records**.

The **Batch Execution Entity List** field displays all fields of type "Entity list" created within the request entity (all entity lists). To update a specific entity list, select it from the **Batch Execution Entity List** drop-down; otherwise, leave the field empty to exclude entity lists from the update operation.

Enable **Use Upsert mode** when performing an update on given records to handle cases where some records in the request payload may not yet exist — each record will be updated if found, or automatically inserted if it doesn't exist.

> **NOTE:** Use Upsert mode is available in Druid 9.17 and higher.

To map all entity fields existing on the request entity, tap on **Map All Fields**.

If you choose to map only specific entity fields in the request, additional field mapping actions are available:

- **Refresh fields** - If you added new entity fields to the request entity, this action will load all entity fields.
- **Select all fields** - Selects all existing entity fields to be included in the request. Use it when you want to map many entity fields and exclude the desired entity fields from the request by clicking the check mark in front of the entity field(s).
- **Deselect all fields**. Deselects the entity fields mapped in the request. Use it when you want to manually select a few entity fields in the request.
- **Show all mapped fields**. Only displays the list of entity fields mapped in the request.

<a id="UpdatethesamevaluesonmultiplerecordsfromDruidDataService"></a>

### Update the same value(s) on multiple records from Druid Data Service

To update same value(s) on multiple records from Druid Data Service, which result from a conditional query (where clauses / filters), choose **Conditional update**. Click on the **Field Mapping Action** button and click on **Refresh Fields**. The list of scalar entity fields (no entity/entity list fields) existing on the request entity displays.

> **Info:** You cannot update fields of type entity or entity lists.

Select the desired field and in the corresponding input field, enter the desired value.

> **NOTE:** Selecting a field and leaving the corresponding input field empty will use the value from the request entity for that field.

In the Filtering area, add conditions to filter records in the Druid Data Service.

Example: Set Campus for students attending the ASE University

This update using the ‘Update entity’ integration task is similar to the following SQL statement:

**Example**

```
Update Student
Set Campus = ‘Moxa’
Where University = ‘ASE’
```

Rather than obtaining a pre-selected set of records containing all students from ASE in the request payload, the integration task will directly identify them in the database by applying a where clause (filter).

![](../../Resources/Images/Druid%20Data%20Service%20Connector/conditional%20update.png)

<a id="Response"></a>

## Response

Click the **Response** tab. By default, the integration task output will be saved in the global context, that is, the Response entity set on the connector action. If you want to save the response in an entity different from the global one set on the connector action, than from the **Scope** field, select **Local** and from the **Response entity** field, select the desired entity. The Request page also displays all entity fields existing on the selected response entity.

![](../../Resources/Images/Druid%20Data%20Service%20Connector/update%20entity%20response.png)

From the **Expansion level** drop-down, select the depth of the related records to be transmitted.

To map all entity fields existing on the request entity, tap on **Map All Fields**.

If you choose to map only specific entity fields in the response, additional field mapping actions are available:

![](../../Resources/Images/Druid%20Data%20Service%20Connector/update%20entity%20actions.png)

- **Refresh fields** - If you added new entity fields to the request entity, this action will load all entity fields.
- **Select all fields** - Selects all existing entity fields to be included in the response. Use it when you want to map many entity fields and exclude the desired entity fields from the response by clicking the check mark in front of the entity field(s).
- **Deselect all fields**. Deselects the entity fields mapped in the response. Use it when you want to manually select a few entity fields in the response.
- **Show all mapped fields**. Only displays the list of entity fields mapped in the response.

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.

Use the connector task on desired flow step(s) as best suits your needs.

<a id="Testtheintegrationtask"></a>

## Test the integration task

> **NOTE:** In order to test the Update entity task, you first need to test the Add entity task and from the **TestResult** copy the value of the entity record **Id**.
>
> ![](../../Resources/Images/Druid%20Data%20Service%20Connector/Get%20Entity_4.png)

To test the Update entity integration task, click the **Test** tab. In the RequestEntity, provide the **Id** of the entity record you copied from the TestResult of the Add entity task and click the **Test** button (![](../../Resources/Images/Druid%20Data%20Service%20Connector/Add%20Entity_8.png)).

![](../../Resources/Images/Druid%20Data%20Service%20Connector/Update%20Entity_5.png)
