<a id="UpsertEntity"></a>

# Upsert Entity

The Upsert Entity integration task combines the functionality of both the Update entity and Add entity tasks, simplifying records management processes. DRUID uses the specified identifying key(s) to check for the existence of records in the database and only conducts bulk insertion or update operations on lists that belong to the request entity, also referred to as the umbrella entity.

Based on the identifying key(s), if a record already exists, it will be updated with new values; if not, a new record will be inserted.

> **NOTE:** This integration task is available in DRUID 7.7 and higher.

The Edit Connector Task page appears by default on the **General** tab. Provide a brief relevant description of the task. Optionally, include a comment for internal reference.

![](../../Resources/Images/druid%207.7/upsert.png)

<a id="Request"></a>

## Request

Click the **Request** tab and configure the request:

1. Select the integration context. To perform the integration task within the context of the Request entity set on the connector action leave the **Scope** field set to **Global**. If performing the task on a context different from the global context set on the connector action, select Local. From the **Request entity** field, choose the desired entity.
> **Info:**  Using **Local** scope allows direct queries within the connector action, eliminating the need for additional queries in the Flow Designer to build a larger context.

2. Choose the list you want to update from the **Batch execution entity list** field.
> **NOTE:** Starting with Druid 9.17, **Upsert** is also supported for single records — when no **Batch execution entity list** is selected, Druid checks the database against the individual records in the request entity using the defined common key (**Common entity field**), updating existing records or inserting new ones as needed.

3. From the **Common entity field** field, select the identifying key used to search if records exist in the database or within the third-party tool.
4. Choose the entity fields to be mapped on the request. To map all entity fields existing on the request entity, tap on **Map All Fields**. To map only specific entity fields in the request, tap off **Map All Fields** and select the desired entity fields.

Additional field mapping actions are available:

- **Refresh fields** - If you added new entity fields to the request entity, this action will load all entity fields.
- **Select all fields** - Selects all existing entity fields to be included in the request. Use it when you want to map many entity fields and exclude the desired entity fields from the request by clicking the check mark in front of the entity field(s).
- **Deselect all fields**. Deselects the entity fields mapped in the request. Use it when you want to manually select a few entity fields in the request.
- **Show all mapped fields**. Only displays the list of entity fields mapped in the request.

Additional Filters can be added to narrow down the records update. If any additional filter is defined, records to be updated are identified by both the 'Common entity field' and the 'Additional Filters'.

<a id="ExampleUpdateListofStudents"></a>

### Example: Update List of Students

In this example:

- The request entity is [[Account]].
- [[Account]] contains an entity list, [[Account]].Students, which references the [[Student]] entity.
- The [[Student]] entity has the field [[Student]].PhoneNumber.
- PhoneNumber serves as the identifying key used to search for records in the database.

![](../../Resources/Images/druid%207.7/simple%20upsert.png)

If students with the phone number exist in the database, their details will be updated; otherwise, they will be inserted.

<a id="ExampleUpdatingtheListofStudentsEnrolledinYear1"></a>

### Example: Updating the List of Students Enrolled in Year 1

In this example:

- The request entity is [[Account]].
- Within [[Account]], there exists an entity list called [[Account]].Students, which references the [[Student]] entity.
- The [[Student]] entity comprises two fields: [[Student]].PhoneNumber and [[Student]].Year.
- PhoneNumber serves as the first identifying key used to search for records in the database.
- The Year servers as the second identifying key used to filter students enrolled in year 1.

![](../../Resources/Images/druid%207.7/additional%20filtering.png)

If students with the phone number are found in the database, a subsequent search is conducted within the retrieved list to filter students enrolled in year 1. The bulk operation on student records will then focus specifically on those enrolled in year 1. If students with phone number and enrolled in year 1 already exist, their records will be updated accordingly; otherwise, new records will be inserted into the database.

<a id="Response"></a>

## Response

Click the **Response** tab and configure the response:

1. Select the context for the response. By default, the integration task output will be saved in the **Global** context, the Response entity set on the connector action. If you want to save the response in a different entity, select **Local**. From the **Response entity** field, choose the desired entity.

![](../../Resources/Images/Druid%20Data%20Service%20Connector/update%20entity%20response.png)

2. Choose the depth of related records to be transmitted from the **Expansion** level drop-down.
3. Choose the entity fields to be mapped on the request. To map all entity fields existing on the request entity, tap on **Map All Fields**. To map only specific entity fields in the request, tap off **Map All Fields** and select the desired entity fields.

Additional field mapping actions are available:

- **Refresh fields** - If you added new entity fields to the request entity, this action will load all entity fields.
- **Select all fields** - Selects all existing entity fields to be included in the request. Use it when you want to map many entity fields and exclude the desired entity fields from the request by clicking the check mark in front of the entity field(s).
- **Deselect all fields**. Deselects the entity fields mapped in the request. Use it when you want to manually select a few entity fields in the request.
- **Show all mapped fields**. Only displays the list of entity fields mapped in the request.

![](../../Resources/Images/Druid%20Data%20Service%20Connector/update%20entity%20actions.png)

4. Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.

Use the connector task on desired flow step(s) or conversational business applications as best suits your needs.

<a id="Testtheintegrationtask"></a>

## Test the integration task

> **NOTE:** In order to test the Update entity task, you first need to test the Add entity task and from the **TestResult** copy the value of the entity record **Id**.

To test the Update entity integration task, click the **Test** tab. In the RequestEntity, provide the **Id** of the entity record you copied from the TestResult of the Add entity task and click the **Test** button (![](../../Resources/Images/Druid%20Data%20Service%20Connector/Add%20Entity_8.png)).
