---
layout:
  title:
    visible: false
---

<a id="UiPathDeleteEntity"></a>

# UiPath Delete Entity

Deletes an existing Entity record.

> **IMPORTANT!**  Before defining the integration task, make sure that you have mapped the UiPath Data Service entity to the Druid request entity; otherwise, you won’t be able to set the integration task response.

<a id="GeneralSettings"></a>

## General Settings

The Edit Connector Task page appears by default on the **General** tab.

Set the general parameters:

| Parameter | Description |
| --- | --- |
| Description | Provide a brief relevant description of the task to be performed. |
| ConnectionCode | Select the UiPath Data Service connection string. |

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Delete%20Entity.png)

<a id="Request"></a>

## Request

Click the **Request** tab.

In the **Request entity Id** field, select the field that stores the Id of the Druid Request entity.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/UiPath%20Get%20Entity_1.png)

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.
