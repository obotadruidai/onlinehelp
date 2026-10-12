---
title: Using NER with Index Entities (DRUID versions prior to 5.15)
---


Index entities are entities, which are trained for Natural Language Processing. Use them when you want to validate user input with a list of values predefined for your specific situation.

This section describes how to use NER with index entities in DRUID versions prior to 5.15.

## Prerequisite

* You must have at least one entity defined in the system used by the AI Agent. The entity you want to index should have a flat data type field (a field of type other than Entity or Entity List).

To use NER with Index Entities, follow these steps:

## Step 1. Link your entity with an external data source

Connect to an external data source. Create a connector action that brings the values from an external data source and stores them in your entity.

When creating the connector action, make sure to select your entity as both the Request and Response Entity and select the **Is Response Collection** option.

As you are using the integration tasks only to read data from the external data source, do not provide any input arguments on the request. In the response, map the field from the data source to the DRUID entity field. You will index your entity by the field you map here.

{% hint style="info" %}
**NOTE:** For DRUID version 1.74 and higher, if you are using NER on multi-language AI Agents and you expect language specific values from the external database, make sure that on the Response you map the language specific values (returned from DB fields) to DRUID language-specific field clones.

Example:

<img src="../../.gitbook/assets/response ner multi.png" alt="" data-size="original">
{% endhint %}

For more information on how to connect to external data sources, see [Integrations](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors).

## Step 2: Index the entity

### 2.1. Define AI Agent-entity relation

Select the AI Agent and in AI Agent Designer click the **Entities** tab. Initially, the Entities page is empty.

The Entities page will load all entities used by the respective AI Agent (any entity which is related to another AI Agent-related element, like flows, connector actions, etc). In case an additional entity relation needs to be added (an entity which is not yet used in any other AI Agent-related element), the **Add AI Agent Entity Relation** button can be used to add a new empty line in the table.

Using inline editing, select the Entity, Matching Fields, Training Sources and tick the **Is NLP** check box. The table below describes the parameters for setting up an entity for NLE.

| Parameter        | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entity           | Select the entity you want to index.                                                                                                                                                                                                                                                                                                                                                                                              |
| Matching Fields  | Select the field you used to map the data from your external data to DRUID entity field. **NOTE:** For DRUID version 1.74 and higher, if you're using an entity on multilanguage AI Agents, make sure to select the main field that has language specific field clones (E.g., index the entity \[\[Account]] by the field Name, where the field \[\[Account]].Name has the option **Holds multilanguage records** option enabled. |
| Training Sources | Select the connector action that will pull the selected field values from your external data source (i.e., database, web service, etc.).                                                                                                                                                                                                                                                                                          |
| Is NLP           | Tick the check box if the entity will be used by NLP as well.                                                                                                                                                                                                                                                                                                                                                                     |

![](<../../.gitbook/assets/Setting up Entities for NER_1.png>)

To save the entity, click the **Save** icon displayed inline with the record. The fields become non-editable and the **Edit Schedule** (![](<../../.gitbook/assets/Setting up Entities for NER_2_31x29.png>)) icon displays in the Actions column in line with the entity.

The AI Agent-entity relation is created in the system, but the entity is not trained for NLP.

Now you have to train NER for the entity, that is creating an entity index.

### 2.2. Create entity index

When you train the entity, DRUID calls the connector action which brings from the data source the list of values which needs to be indexed and saves them in a special DRUID index associated to your entity.

To manually create an entity index, click the **Edit Schedule** icon. A window appears. Click the **Train** button.

![](<../../.gitbook/assets/train entity manually.png>)

An entity index is created by the system for the selected entity.

If the external data source updates periodically, we recommend you to schedule the entity index training.

To schedule the training of the entity index, follow these steps:

1. Click the **Edit Schedule** icon displayed inline with your entity. A window appears.
2. Click the **Settings** section header. The Settings area expands.
3. Tick the **Is scheduler enabled** check box.
4. (Optional) Set specific NER parameters for the selected entity. For more information, see [Entity NER-specific Parameters](<Entity NER specific Parameters.md>).
5. Set **Start date** and **End date** or tick **No end date** if you do not want to set an end date.
6. Select the **Frequency** (to run on specific day(s) of the week) or the Daily frequency: schedule the job to occur once at a specific hour (in the format HH:MM:SS), or the job runs every specified minutes / hours within a given time frame (hours).

![](<../../.gitbook/assets/Setting up Entities for NER_4.png>)

7. Click the **Save** button at the bottom of the window to save the scheduled job.

## Step 3. Use indexed values on flows

{% hint style="info" %}
**NOTE:** To use the indexed values on flows in DRUID version prior 5.0, you need to include the entity in an umbrella entity, an entity which has a field of type Entity referencing the indexed entity. On flows, in Input mapping and in flow Training Phrases, use the field of your umbrella entity which references the indexed entity.
{% endhint %}

Once you added all the needed entities to your AI Agent, select solution and on the main menu click **Flows**. Select a flow and go to the Flow Editor page, click the **Training Phrases** section and add a complete training phrase (including sample value for the indexed entity to be extracted).

In the training phrase, select the word / sequence of words that is sample value.

![](<../../.gitbook/assets/select word.png>)

Click on the selected word(s). The Entity Extraction pop-up appears.

Click in the **Target Entity / Entity** field and select the entity that will store the extracted value.

![](<../../.gitbook/assets/target entity.png>)

![](<../../.gitbook/assets/selected target.png>)

Click the **Save** button. The pop-up closes and the sample value is highlighted in green and marked with the label Entity.

![](<../../.gitbook/assets/sample word.png>)

{% hint style="info" %}
**NOTE:** Using sample values in training phrases is available in DRUID 5.12 and higher. This feature is backwards compatible, the training phrases with NER on flows and flow steps remain unchanged; however, we recommend you to update the training phrases with NER to provide sample values.

<img src="../../.gitbook/assets/backwards compatible.png" alt="" data-size="original">
{% endhint %}

You can also use the indexed entity on flow steps with input mapping (when you want to do input mapping with NER) and for intent recognition.

{% hint style="info" %}
**Info:** In Druid version 1.74 and higher, if your entity field holds multilanguage records, specify the main entity field (that is, the multilingual entity field) in your training phrases and the Flow Engine will extract the language specific value to the appropriate field clone based on the \[\[ChatUser]].Language.
{% endhint %}

After the ML model is trained, you can test a phrase with values for the intended entities (either in AI Agent Designer / Details or in the Flows section). The DRUID ML engine will identify the correct intent and extract the values from the indexed entity.

Whenever the AI Agent reaches the flow, it extracts the user input and stores it in the entity you provided in the flow utterance (or in the language specific field clone) and validates that value against the list of indexed values. If the value is found, it is available in the conversation flow and you can further use it on the flow based on your needs.

## Related Topics

* [AI Agent Informational Model](<../5_Entities/AI Agent Informational Model.md>)
* [Choice](<../4_Flows/Choice Steps Configuration.md>)
* [Contextual NER](<Contextual NER.md>)
* [Hero Cards](<../4_Flows/Hero Steps Configuration.md>)
* [Managing Entities](<../5_Entities/Managing Entities.md>)
* [Message](<../4_Flows/Message Steps Configuration.md>)
* [Prompt](<../4_Flows/Prompt Steps Configuration.md>)
