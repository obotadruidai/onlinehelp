---
title: UiPath Delete File from Entity
---

# UiPath Delete File from Entity

Deletes the specified file from the specified field of an existing UiPath entity record.

{% hint style="warning" %}
**IMPORTANT!** Before defining the integration task, make sure that you have mapped the UiPath Data Service entity to the Druid request entity; otherwise, you won’t be able to set the integration task.
{% endhint %}

### General Settings

The Edit Connector Task page appears by default on the **General** tab.

Set the general parameters:

| Parameter      | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| Description    | Provide a brief relevant description of the task to be performed. |
| ConnectionCode | Select the UiPath Data Service connection string.                 |

![](<../../../.gitbook/assets/UiPath Delete File from Entity.png>)

### Request

Click the **Request** tab.  In the **Request entity Id** field, select the field that stores the Id of the Druid Request entity (the Druid entity mapped with the Data Service entity's record you want to remove the file from).

From the **UiPath** field, select the name of the File type field where the record you want to upload the file to is found. In Druid column, type the Druid file field that stores the files you want to upload to Data Service. Save the mapping by clicking the **Save** icon displayed inline.

![](<../../../.gitbook/assets/UiPath Delete File from Entity_1.png>)

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.
