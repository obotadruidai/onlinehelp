---
layout:
  title:
    visible: false
---

<a id="UiPathAddEntity"></a>

# UiPath Add Entity

Creates a new entity record in UiPath Data Service using data stored in conversations.

> **IMPORTANT!** Before defining the integration task, make sure that you have mapped the UiPath Data Service entity to the Druid request entity; otherwise, you won’t be able to set the integration task response.

<a id="GeneralSettings"></a>

## General Settings

The Edit Connector Task page appears by default on the **General** tab.

Set the general parameters:

| Parameter | Description |
| --- | --- |
| Description | Provide a brief relevant description of the task to be performed. |
| ConnectionCode | Select the UiPath Data Service connection string. |

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Add%20Entity.png)

<a id="Request"></a>

## Request

Click the **Request** tab. The Request page provides you with the mapping of Druid request entity fields to UiPath Data Service entity fields.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Add%20Entity_1.png)

You can remove entity fields from the request by clicking the Delete icon displayed inline (![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Add%20Entity_2.png)); however, we recommend you to leave all mapped fields in the request.

<a id="Response"></a>

## Response

Click the **Response** tab. By default, the Request page does not show any fields mapping.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Add%20Entity_3.png)

From the **Expansion level** drop-down, select the depth of the related records to be retrieved. The default value is **2**.

Click the **Map All fields** button (![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Add%20Entity_4.png)).

Druid displays the entity schema tree mapping (the request entity and its child fields) in a single table with nested rows based on the selected **Expansion level**.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Add%20Entity_5.png)

You can remove fields from the mapping table.

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.

Use the connector task on desired flow step(s). Whenever in a conversation, the AI Agent reaches that / those step(s), record(s) will be added in UiPath Data Service for the UipPath Data Service entity mapped with the Druid request entity.
