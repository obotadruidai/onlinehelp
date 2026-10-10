---
title: Add Entity
---

# Add Entity

Use the Add Entity integration task to create a new entity record in DRUID Data Service using data stored in conversations.

### General Tab

The Edit Connector Task page opens by default on the General tab. Use this tab to provide a brief, relevant description of the task.

![](<../../../.gitbook/assets/add brief description add entity.png>)

{% hint style="info" %}
**Info:** For optimal execution time and to reduce database load, select **Disable Connector Audit Logging** if the task handles large payloads.
{% endhint %}

### Request

Click on the **Request** tab to configure how data is passed to the integration task.

If you want the integration to run in the context of the global request entity set on the connector action, leave the **Scope** field set to **Global**.

If you want to run the integration on a local context:

1. Set Scope to Local.
2. From the Request entity field, select the desired entity.

Using Local scope allows you to handle queries directly within the connector action—eliminating the need to construct a larger context in Flow Designer and reducing the number of intermediate steps.

The Request page shows all available fields on the selected request entity.

![](<../../../.gitbook/assets/Add Entity_5.png>)

#### Batch Execution

When you need to add multiple related records at once (for example, a list of child entities associated with a parent entity), DRUID offers efficient batch processing. To set this, you'll interact with the **Batch execution entity list** field in your integration task.

This field displays all entity list-type fields defined on the request entity you've selected for your integration task. Choosing an entity list field here signals to DRUID that the integration should operate in batch mode, processing multiple child records related to a single parent record.

{% hint style="info" %}
**NOTE:** In DRUID versions older than 8.14, automatically setting the link between child and parent records during batch processing is not available. You have to manually configure this relationship using a Custom Code integration task. This involved using expressions to explicitly set the foreign key field. For example: `[[CampaignActivity]].Campaign.Id = [[Campaign]].Id`.
{% endhint %}

**Automatically set parent references**

DRUID version 8.14 introduced the ability to automatically set the reference to parent records for all children in a batch. This simplifies the integration process significantly.

{% hint style="warning" %}
**IMPORTANT!** Before you can leverage the automatic parent reference setting, you must first define the relationship between the parent and child entities. This involves configuring a foreign key field in the child entity that points to the parent entity.
{% endhint %}

**How to Define the Foreign Key**

This configuration requires you to create a specific field within the child entity with the following characteristics:

* The field's data type must be 'Entity'.
* This field must explicitly reference the parent entity.

DRUID uses this defined foreign key to correctly associate each child record with its corresponding parent record during batch processing.

_Example Scenario: Adding Closed Campaign Activities_

Suppose you want to add all closed CampaignActivity records related to a Campaign in DRUID Data Service. Here's the entity relationship:

* You have two entities: **\[\[Campaign]]** (Parent) and **\[\[CampaignActivity]]** (Child).
* The **\[\[CampaignActivity]].Campaign** field is of type entity and references the parent entity **\[\[Campaign]]**.
* The **\[\[Campaign]].ClosedActivities** field is of type entity list and is defined as follows:
* **Referenced Entity**: \[\[CampaignActivity]]
* **Referenced to Entity Field**: Campaign

![](<../../../.gitbook/assets/create entity field.png>)

In this example, the foreign key is **\[\[CampaignActivity]].Campaign**.

{% hint style="info" %}
**Info:** The \[\[Campaign]].ClosedActivities field is not the foreign key. Instead, it's a reverse lookup list that displays related \[\[CampaignActivity]] records based on the Campaign reference.
{% endhint %}

To automatically populate the foreign key for each child record during batch execution:

1. Select the appropriate entity list field from the **Batch execution entity list** field. This identifies the list of child records you are processing in batch (e.g., ClosedActivities).
2. Tap on **Set parent reference for Batch** option.

![](<../../../.gitbook/assets/set parent reference.png>)

When you execute the integration task, DRUID will automatically populate the foreign key field in each new child record (e.g., \[\[CampaignActivity]].Campaign.Id) with the ID of the corresponding parent record (e.g., the current \[\[Campaign]].Id).

#### Map the request fields

To map all entity fields existing on the request entity, tap on **Map All Fields**.

![](<../../../.gitbook/assets/map all fields.png>)

If you choose to map only specific entity fields in the request, additional field mapping actions are available:

![](<../../../.gitbook/assets/field mapping actions.png>)

* **Refresh fields** - If you added new entity fields to the request entity, this action will load all entity fields.
* **Select all fields** - Selects all existing entity fields to be included in the request. Use it when you want to map many entity fields and exclude the desired entity fields from the request by clicking the check mark in front of the entity field(s).

![](<../../../.gitbook/assets/excluded field.png>)

* **Deselect all fields**. Deselects the entity fields mapped in the request. Use it when you want to manually select a few entity fields in the request.
* **Show all mapped fields**. Only displays the list of entity fields mapped in the request.

### Response

Click the **Response** tab. By default, the integration task output will be saved in the global context, that is, the Response entity set on the connector action. If you want to save the response in an entity different from the global one set on the connector action, than from the **Scope** field, select **Local** and from the **Response entity** field, select the desired entity. The Request page also displays all entity fields existing on the selected response entity.

To map all entity fields existing on the request entity, tap on **Map All Fields**.

If you choose to map only specific entity fields in the response, additional field mapping actions are available:

* **Refresh fields** - If you added new entity fields to the request entity, this action will load all entity fields.
* **Select all fields** - Selects all existing entity fields to be included in the response. Use it when you want to map many entity fields and exclude the desired entity fields from the response by clicking the check mark in front of the entity field(s).
* **Deselect all fields**. Deselects the entity fields mapped in the response. Use it when you want to manually select a few entity fields in the response.
* **Show all mapped fields**. Only displays the list of entity fields mapped in the response.

Click the **Save** button to save the integration task and remain on the page or the **Save & Close** button to save and return to Connector Steps.

Use the connector task on desired flow step(s). Whenever in a conversation, the AI Agent reaches that / those step(s), DRUID will add entity record(s) in DRUID Data Service for the entity specified on the connector action.

### Test the integration task

You can test the integration task by clicking the **Test** tab and clicking the **Test** button (![](<../../../.gitbook/assets/Add Entity_8.png>)). The response will return the following system entity fields: OperatedByBotId, Id and CreatedOn. For description of these fields, see [System Entity Fields](<../../5_Entities/System Entity Fields.md>). The Id of the entity record is saved within the conversation context and is particularly useful when you want to query, update or delete entity records.

![](<../../../.gitbook/assets/Add Entity_9.png>)
