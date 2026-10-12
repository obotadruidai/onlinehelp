---
title: UiPath Data Service
---


authors can easily create DRUID information model (at a tenant level) using UiPath schema, easily synchronizing DRUID informational model with UiPath informational model.

A schema represents the metadata of every entity, which contains information such as entity fields (flat data type) or relationships between entity fields (fields of type entity or entity list).

DRUID also provides authors with the option to export DRUID schema in JSON format (containing the entity metadata) they can easily import in UiPath Data Service, eliminating the need to manually create entities in UiPath Data Service to sync DRUID’s informational model.

## Prerequisites

* You need to have configured a [UiPath Data Service Connector](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-data-service-connector) (activate the connection to your UiPath Data Service).

## Create DRUID entities using UiPath schema

1. Load the UiPath entity schema, by clicking the **Actions** drop-down and clicking **Refresh UiPath Schema**. If you want to map certain UiPath fields to specific DRUID entities fields you can do so by following the procedure described in section [Loading UiPath Entity Schema and Mapping Fields](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-data-service-connector/loading-uipath-entity-schema).
2. Click the **Actions** drop-down, and then click **Create Druid Entities**.

![](<../../../.gitbook/assets/UiPath Data Service.png>)

The UiPath entities unmapped to specific DRUID entities are created in DRUID with all associated fields and relationships. DRUID automatically creates the entities under a specific category, that is, **UiPath**. The entities and their fields will have the name of their corresponding UiPath entities.

The reference table below provides you with insights on how DRUID maps different types of UiPath Data Service fields to DRUID field types.

| DRUID field Type  | UiPath Data Service Field type |
| ----------------- | ------------------------------ |
| Boolean           | Yes/No                         |
| Currency          | -                              |
| Date              | Date                           |
| DateTime          | DateTime                       |
| Decimal           | Number                         |
| Email             | Text                           |
| Entity            | Relationship                   |
| Entity List       | Relationship                   |
| Guid              | UniqueId                       |
| Hashtag           | Text                           |
| Integer           | Number                         |
| InvariantDate     | Date                           |
| InvariantDateTime | DateTime                       |
| InvariantTime     | -                              |
| IPAddress         | Text                           |
| Long              | -                              |
| Percentage        | Number                         |
| String            | Text                           |
| Time              | -                              |
| Url               | Text                           |
| Entity            | ChoiceSet                      |
| Entity List       | MultiChoiceSet                 |
| \[\[File]]        | File                           |

## Export DRUID Informational model (all tenant entities)

After you create DRUID entities and/or map specific UiPath entities to specific UiPath entities, you can export DRUID informational model in UiPath schema format and then import it in your UiPath Data Service tenant.

To export DRUID informational model (all entities existing on your DRUID tenant) in UiPath schema format:

1. Go to AI Agent details, **Data Service** tab.
2. Click the **Actions** drop-down and then click **Export UiPath Schema**.

![](<../../../.gitbook/assets/UiPath Data Service_1.png>)

The Confirm Export pop-up appears.

![](<../../../.gitbook/assets/UiPath Data Service_2.png>)

3.  Click **Confirm**. A message informs you how many entities were generated in the export file.

    ![](<../../../.gitbook/assets/UiPath Data Service_3.png>)
4. Click **Download**. After downloading the file, click the **Close** button to close the pop-up.

DRUID downloads all entities existing on your tenant as a JSON file containing the entities metadata. The file is saved on your local machine in the default download folder.

{% hint style="info" %}
**NOTE:** If you have mapped UiPath entities to existing DRUID entities, the JSON file will contain the schema of the UiPath entity and not the schema of the mapped DRUID entity.

For example, I have the UiPath entity, **CardStatus** mapped to DRUID entity, **CardStatus**. The JSON file sill contain the schema of the UiPath entity (with fields: **ChoiceSetId** and **ChoiceSetName**).

<img src="../../../.gitbook/assets/UiPath Data Service_4.png" alt="" data-size="original"> <img src="../../../.gitbook/assets/UiPath Data Service_5.png" alt="" data-size="original">
{% endhint %}

You may import the file in your UiPath Data Service tenant with the click of a button. For information on how to import schema, see [UiPath documentation](mailto:https://docs.uipath.com/data-service/docs/schema-export-and-import).

## Export a specific DRUID entity schema

There are cases, when instead of exporting all entities existing on your DRUID tenant, you need to export only the UiPath schema of a specific DRUID entity.

To export a DRUID entity in JSON format following the UiPath schema:

1. On your solution entities, click on the desired entity. The entity details page appears.
2. Click the **Data Service** tab.
3. Click the **Actions** drop-down and then click **Export UiPath Schema**.

![](<../../../.gitbook/assets/UiPath Data Service_6.png>)

The Confirm Export pop-up appears.

![](<../../../.gitbook/assets/UiPath Data Service_2.png>)

4. Click **Confirm**. A message informs you that one entity was generated in the export file.

![](<../../../.gitbook/assets/UiPath Data Service_7.png>)

5. Click **Download**.

The entity schema JSON file is saved on your local machine in the default download folder.

After downloading the file, click the **Close** button to close the pop-up.
