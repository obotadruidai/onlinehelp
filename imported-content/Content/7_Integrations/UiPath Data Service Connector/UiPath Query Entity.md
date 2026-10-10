---
title: "UiPath Query Entity"
---

<a id="UiPathQueryEntity"></a>


Queries the request entity's records. If you want to get a collection of records from an entity list field, you should use [UiPath Query Related Entity](UiPath%20Query%20Related%20Entity.md) instead.

{% hint style="warning" %}
**IMPORTANT!**  Before defining the integration task, make sure that you have mapped the UiPath Data Service entity to the Druid request entity; otherwise, you won’t be able to set the integration task response.
{% endhint %}

<a id="GeneralSettings"></a>

## General Settings

The Edit Connector Task page appears by default on the **General** tab.

Set the general parameters:

| Parameter | Description |
| --- | --- |
| Description | Provide a brief relevant description of the task to be performed. |
| ConnectionCode | Select the UiPath Data Service connection string. |

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Query%20Entity.png)

<a id="Request"></a>

## Request

Click the **Request** tab. The Body template field is filled in by default with the JSON query.

Specify the filtering parameters and in the mapping table, map the parameters values dynamic content to Druid request entity fields.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Query%20Entity_1.png)

If the BodyTemplate is empty, the response retrieves all records.

For more information about the Request Body Schemas, see [UiPath Data Service documentation](https://docs.uipath.com/data-service/reference/query-entity-endpoint).

<a id="Response"></a>

## Response

Click the **Response** tab.

From the **Expansion level** drop-down, select the depth of the related records to be retrieved. The default value is **2**.

Druid displays the entity schema tree mapping (the request entity and its child fields) in a single table with nested rows based on the selected **Expansion level.**

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Get%20Entity_2.png)

You can remove fields from the mapping table if you want to retrieve only specific data from UiPath Data Service.

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.
