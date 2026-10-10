---
title: "Using Lexicon"
---

<a id="UsingLexicon"></a>


Lexicon enables you to train entities for Natural Language Processing (index entities) and use NER with index entities to validate user input with a list of values predefined for your specific situation.

This section describes how to use the Lexicon in DRUID versions 5.15 and higher.

<a id="Prerequisite"></a>

## Prerequisite

- You must have at least one entity defined in the system used by the AI Agent. The entity you want to index should have a flat data type field (a field of type other than Entity or Entity List).

To use NER with index entities, follow these steps:

<a id="Step1Linkyourentitywithanexternaldatasource"></a>

## Step 1. Link your entity with an external data source

Connect to an external data source. Create a connector action that brings the values from an external data source and stores them in your entity.

When creating the connector action, make sure to select your entity as both the Request and Response Entity and select the **Is Response Collection** option.

As you are using the integration tasks only to read data from the external data source, do not provide any input arguments on the request. In the response, map the field from the data source to the DRUID entity field. You will index your entity by the field you map here.

> **NOTE:** If you are using NER on multi-language AI Agents and you expect language specific values from the external database, make sure that on the Response you map the language specific values (returned from DB fields) to DRUID language-specific field clones.
>
> Example:
>
> ![](../Resources/Images/Flows/response%20ner%20multi.png)

For more information on how to connect to external data sources, see [Integrations](../7_Integrations/Enterprise%20Connectors.md).

<a id="Step2Indextheentity"></a>

## Step 2: Index the entity

Select the AI Agent and from the **NLU** menu, click **Configurations**. The NLU Configurations page appears by default on the **General** tab.

Click the **Entities** tab. The Entities page will load all entities used by the respective AI Agent (any entity which is related to another AI Agent-related element, like flows, connector actions, etc).

![](../Resources/Images/NLU/entities%20page.png)

<a id="AddadditionalentitiesontheAIAgent"></a>

### Add additional entities on the AI Agent

In case an additional entity relation needs to be added (an entity which is not yet used in any other AI Agent-related element), the **Add AI Agent Entity Relation** button can be used to add a new empty line in the table.

<a id="Indexanentity"></a>

### Index an entity

To index an entity for NLP, click on the edit icon displayed inline on the right. A pop-up appears by default on the **Parameters** tab.

![](../Resources/Images/NLU/index%20entity%20params.png)

You can set specific NER parameters for the selected entity. For more information, see [Entity NER-specific Parameters](Entity%20NER%20specific%20Parameters.md).

In the pop-up, click on the **Lexicon** tab and tap on **Uses Lexicon**.

![](../Resources/Images/NLU/uses%20lexicon%20button.png)

Click on the Data Sources section header.

From the **Training sources** drop-down, select the connector action that will pull the selected field values from your external data source (i.e., database, web service, etc.).

From the **Matching Fields** drop-down, select the field you used to map the data from your external data to DRUID entity field.

> **NOTE:**  If you're using an entity on multi-language AI Agents, make sure to select the main field that has language specific field clones (E.g., index the entity [[Account]] by the field Name, where the field [[Account]].Name has the option **Holds multilanguage records** option enabled.

![](../Resources/Images/NLU/data%20sources.png)

Now you have to train NER for the entity, that is creating an entity index.

When you train the entity, DRUID calls the connector action which brings from the data source the list of values which needs to be indexed and saves them in a special DRUID index associated to your entity.

#### Manually train the entity

To manually create an entity index, in the Data Sources section, click the **Train** button.

![](../Resources/Images/NLU/manually%20train%20entity.png)

After the training completes, click the **Save** button.

An entity index is created by the system for the selected entity.

> **Info:** If the external data source updates periodically, we recommend you to schedule the entity index training.

#### Schedule the entity index training

To schedule the training of the entity index, in the Data Sources section, tap on **Is scheduler enabled**.

Set **Start date** and **End date** or tick **No end date** if you do not want to set an end date.

Select the **Frequency** (to run on specific day(s) of the week) or the **Daily frequency**: schedule the job to occur once at a specific hour (in the format HH:MM:SS), or the job runs every specified minutes / hours within a given time frame (hours).

![](../Resources/Images/NLU/schedule%20index%20train.png)

Click the **Save** button at the bottom of the window to save the scheduled job.

The AI Agent-entity relation is created in the system and the entity is trained for NLP.

<a id="Step3Useindexedvaluesonflows"></a>

## Step 3. Use indexed values on flows

> **NOTE:** To use the indexed values on flows in DRUID version prior 5.0, you need to include the entity in an umbrella entity, an entity which has a field of type Entity referencing the indexed entity. On flows, in Input mapping and in flow Training Phrases, use the field of your umbrella entity which references the indexed entity.

Once you added all the needed entities to your AI Agent, select solution and on the main menu click **Flows**. Select a flow and go to the Flow Editor page, click the **Training Phrases** section and add a complete training phrase (including sample value for the indexed entity to be extracted).

In the training phrase, select the word / sequence of words that is sample value.

![](../Resources/Images/Druid%205.12/select%20word.png)

Click on the selected word(s). The Entity Extraction pop-up appears.

Click in the **Target Entity / Entity** field and select the entity that will store the extracted value.

![](../Resources/Images/Druid%205.12/target%20entity.png)

![](../Resources/Images/Druid%205.12/selected%20target.png)

Click the **Save** button. The pop-up closes and the sample value is highlighted in green and marked with the label Entity.

![](../Resources/Images/Druid%205.12/sample%20word.png)

You can also use the indexed entity on flow steps with input mapping (when you want to do input mapping with NER) and for intent recognition.

> **Info:** If your entity field holds multilanguage records, specify the main entity field (that is, the multilingual entity field) in your training phrases and the Flow Engine will extract the language specific value to the appropriate field clone based on the [[ChatUser]].Language.

After the ML model is trained, you can test a phrase with values for the intended entities (either in AI Agent Designer / Details or in the Flows section). The DRUID ML engine will identify the correct intent and extract the values from the indexed entity.

Whenever the AI Agent reaches the flow, it extracts the user input and stores it in the entity you provided in the flow utterance (or in the language specific field clone) and validates that value against the list of indexed values. If the value is found, it is available in the conversation flow and you can further use it on the flow based on your needs.

## Related Topics

- [AI Agent Informational Model](../5_Entities/AI%20Agent%20Informational%20Model.md)
- [Choice](../4_Flows/Choice%20Steps%20Configuration.md)
- [Contextual NER](Contextual%20NER.md)
- [Hero Cards](../4_Flows/Hero%20Steps%20Configuration.md)
- [Managing Entities](../5_Entities/Managing%20Entities.md)
- [Message](../4_Flows/Message%20Steps%20Configuration.md)
- [Prompt](../4_Flows/Prompt%20Steps%20Configuration.md)
