<a id="UiPathQueryRelatedEntity"></a>

# UiPath Query Related Entity

Queries the request entity's records and returns a collection.

> **IMPORTANT!** Before defining the integration task, make sure that you have mapped the UiPath Data Service entity to the Druid request entity; otherwise, you won’t be able to set the integration task response:
>
> - The response entity should have a field of type Entity list referencing the UiPath entity.
> - The Druid entity mapped to a UiPath entity should have a field of type Entity referencing the entity in which you want to receive the response.

<a id="GeneralSettings"></a>

## General Settings

The Edit Connector Task page appears by default on the **General** tab.

Set the general parameters:

| Parameter | Description |
| --- | --- |
| Description | Provide a brief relevant description of the task to be performed. |
| ConnectionCode | Select the UiPath Data Service connection string. |

![](../../Resources/Images/UiPath%20Query%20Related%20Entity/UiPath%20Query%20Related%20Entity.png)

<a id="Request"></a>

## Request

Click the **Request** tab. Provide the parameters described in the table below.

| Parameter | Description |
| --- | --- |
| Request entity Id | The ID of the request entity field based on which you want to retrieve the collection of records.  **Info:**  We recommend you to use the Query UiPath entity task to retrieve the field ID. |
| BodyTemplate | By default, the field is filled in with a JSON query.  If you want to filter the response, in the **BodyTemplate** field, in the query, specify the filtering parameters and in the mapping table, map the parameters values dynamic content to Druid request entity fields.  If you leave this field empty, the response retrieves all records.  For more information about the Request Body Schemas, see [UiPath Data Service documentation](https://docs.uipath.com/data-service/reference/query-entity-endpoint). |

<a id="Response"></a>

## Response

Click the **Response** tab. From the **Project result to Entity path** drop-down, select the field of type Entity list defined on the response Druid entity, the one that references the UiPath entity.

From the **Expansion level** drop-down, select the depth of the related records to be retrieved. The default value is **2**.

Druid displays the entity schema tree mapping (the request entity and its child fields) in a single table with nested rows based on the selected Expansion level.

You can remove fields from the mapping table if you want to retrieve only specific data from UiPath Data Service.

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.

<a id="Example"></a>

### Example

In this example:

- We’ll get the list of cards associated to an account.
- [[Account]] Druid entity  will be used as request and response entity.
- UiPath Data Service entity is mapped to the Druid request entity, as follows:

- The [[Account]] Druid entity has a field of type Entity list named “Cards” (ProjectResulttoEntityPath) referencing the [[Card]] entityin which all the cards corresponding to and Account will be retrieved in response.

![](../../Resources/Images/UiPath%20Query%20Related%20Entity/UiPath%20Query%20Related%20Entity_1.png)

- The Druid  [[Card]] entity has a field of type Entity called “Account” referencing the [[Account]] entity, which will be mapped in UiPath corresponding Card entity.

![](../../Resources/Images/UiPath%20Query%20Related%20Entity/UiPath%20Query%20Related%20Entity_2.png)

![Graphical user interface, application Description automatically generated](../../Resources/Images/UiPath%20Query%20Related%20Entity/UiPath%20Query%20Related%20Entity_3.png)

#### Request

![](../../Resources/Images/UiPath%20Query%20Related%20Entity/UiPath%20Query%20Related%20Entity_4.png)

#### Response

![](../../Resources/Images/UiPath%20Query%20Related%20Entity/UiPath%20Query%20Related%20Entity_5.png)

#### Response – Test

![](../../Resources/Images/UiPath%20Query%20Related%20Entity/UiPath%20Query%20Related%20Entity_6.png)
