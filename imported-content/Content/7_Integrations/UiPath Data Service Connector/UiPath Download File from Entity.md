---
title: UiPath Download File from Entity
---

# UiPath Download File from Entity

Downloads the file from the specified UiPath entity field to Druid.

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

![](<../../../.gitbook/assets/UiPath Download File from.png>)

### Request

Click the **Request** tab.  In the **Request entity Id** field, select the field that stores the Id of the Druid Request entity (the Druid entity mapped with the Data Service entity's record you want to download the file from).

From the **UiPath** field, select the name of the File type field where the record you want to download the file from is found. In Druid column, type the Druid file field where to set the downloaded file. Save the mapping by clicking the **Save** icon displayed inline.

![](<../../../.gitbook/assets/UiPath Download File from_1.png>)

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.
