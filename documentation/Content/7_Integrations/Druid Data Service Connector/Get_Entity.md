<a id="GetEntity"></a>

# Get Entity

Retrieves a single Druid Data Service entity record by the ID saved within the conversation context.

The Edit Connector Task page appears by default on the **General** tab. Provide a brief relevant description of the task.

![](../../Resources/Images/Druid%20Data%20Service%20Connector/get%20entity%20general.png)

For optimal execution time and to conserve database resources, we recommend you select **Disable Connector Audit Logging** when the integration task involves handling substantial payloads.

In the **Request** tab, the request field is filled in with the request entity set on the connector.

<a id="Response"></a>

## Response

Click the **Response** tab. From the **Expansion level** drop-down, select the depth of the related records to be retrieved.

Druid displays the entity schema (the request entity and its child fields) in a single table with nested rows based on the selected Expansion level.

The entity fields list includes 'Entity List' type fields. This optimizes performance by enabling the retrieval of data related to the root (response) entity within the Get entity integration without the need for multiple Query related entity integration tasks.

You can select specific fields to bring, simplifying processes such as fetching all activities for a campaign and obtaining specific details for each activity.

To bring a collection of records, select the desired 'Entity List' type field and from the corresponding drop-down, select the foreign key that is the field from the base entity of the collection (e.g., CampaignActivity) that refers the response entity (e.g., Campaign).

![](../../Resources/Images/druid%205.29/getentity.png)

> **NOTE:** Mapping all fields ignores the 'Entity List' type fields.

To map all entity scalar fields and 'Entity' type existing on the request entity, tap on **Map All Fields**.

If you choose to get only specific data records from Druid Data Service, additional field mapping actions are available:

- **Refresh fields** - If you added new entity fields to the request entity, this action will load all entity fields.
- **Select all fields** - Selects all existing entity fields to be included in the response. Use it when you want to map many entity fields and exclude the desired entity fields from the response by clicking the check mark in front of the entity field(s).
- **Deselect all fields**. Deselects the entity fields mapped in the response. Use it when you want to manually select a few entity fields in the response.
- **Show all mapped fields**. Only displays the list of entity fields mapped in the response.

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.

<a id="Testtheintegrationtask"></a>

## Test the integration task

> **NOTE:** In order to test the Get entity task, you first need to test the Add entity task and from the **TestResult** copy the value of the entity record **Id**.
>
> ![](../../Resources/Images/Druid%20Data%20Service%20Connector/Get%20Entity_4.png)

To test the Get entity integration task, click the Test tab. In the **RequestEntity**, provide the **Id** of the entity record you copied from the TestResult of the Add entity task and click the **Test** button (![](../../Resources/Images/Druid%20Data%20Service%20Connector/Add%20Entity_8.png)).

![](../../Resources/Images/Druid%20Data%20Service%20Connector/test%20query.png)
