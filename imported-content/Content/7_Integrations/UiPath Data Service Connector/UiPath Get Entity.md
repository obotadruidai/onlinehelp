---
title: UiPath Get Entity
---

# UiPath Get Entity

Retrieves a single UiPath Data Service entity record by ID.

{% hint style="warning" %}
**IMPORTANT!** Before defining the integration task, make sure that you have mapped the UiPath Data Service entity to the Druid request entity; otherwise, you won’t be able to set the integration task response.
{% endhint %}

### General Settings

The Edit Connector Task page appears by default on the **General** tab.

Set the general parameters:

| Parameter      | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| Description    | Provide a brief relevant description of the task to be performed. |
| ConnectionCode | Select the UiPath Data Service connection string.                 |

![](<../../../.gitbook/assets/UiPath Get Entity.png>)

### Request

Click the **Request** tab.

In the Request entity Id field, select the field that stores the Id of the Druid Request entity.

![](<../../../.gitbook/assets/UiPath Get Entity_1.png>)

### Response

Click the **Response** tab.

![](<../../../.gitbook/assets/UiPath Add Entity_3.png>)

From the **Expansion level** drop-down, select the depth of the related records to be retrieved. The default value is **2**.

Druid displays the entity schema tree mapping (the request entity and its child fields) in a single table with nested rows based on the selected **Expansion level**.

![](<../../../.gitbook/assets/UiPath Get Entity_2.png>)

You can remove fields from the mapping table if you want to get only specific data records from UiPath Data Service.

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.
