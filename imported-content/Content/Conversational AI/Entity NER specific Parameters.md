---
title: "Entity NER-specific Parameters"
---

<a id="EntityNERspecificParameters"></a>


The table below describes the entity parameters you can set for NER when creating a Lexicon (an entity index).

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.EntityIndex.AlternativeCalculationForProbability | An alternative method for computing the probability of an entity, that favors exact matches within the index.  **IMPORTANT!** In DRUID 5.8 and higher, this parameter provides an alternative method for computing the probability of an entity that favors partial matches within the index. The default value is "false". | false |
| NLU.NER.EntityIndexType | The Lexicon (entity index) type:   - **Inverted** - An optimized algorithm that performs an extended and quick search inside the Lexicon increasing the number of candidates to a user says. - **LinkedSearch** - use this value if the Lexicon contains millions of records and the ML engine has to perform searches in these large sets of data. | Inverted |
| NLU.NER.EntityIndex.UseForClassification | Multiplies the training phrases on the flow (within the model) by the number of entity records (elements) in the Lexicon (indexed entity).  **IMPORTANT!** Because the parameter's default value is too high, we strongly recommend you to use this parameter only together with **NLU.NER.Classification.MaxNoOfUterancesFromEntityValuesForNer**. | 50 |
| NLU.NER.Classification.MaxNoOfUterancesFromEntityValuesForNer | To ensure that the training model is balanced, set this parameter to 3 up to 5. The value will apply per utterances per entity record.  For example, there is a Lexicon for colors, which has 7 elements and there are 3 training phrases on the flow. 21 training phrases will be added to the model; a training phrase per element in the Lexicon. | 100 |

<a id="ExperimentalParameters"></a>

## Experimental Parameters

| Parameter | Description |
| --- | --- |
| NLU.NER.EntityIndex.RescaleProbs | Set the parameter to **true** to increase the extraction score which ensures that NER identifies more entity candidates.  The parameters increases the extraction score as follows:   - 0 remains 0 - 0.1-30 -> 30-60 - 30-60 -> 60-90 - 60-100 -> 90-100   *Example*: In entity index there is a list of smartphones. The user asks for the price of an iPhone. The list of smartphones contains a long list of iPhone models, some with long names. Because the extraction score for long iPhone model names decreases, we set the **NLU.NER.EntityIndex.RescaleProbs** parameter to true to ensure that long iPhone names are also included in the list of candidates identified by NER. |

## Related Topics

- [Using NER with Index Entities (DRUID versions prior to 5.15)](Using%20NER%20with%20Index%20Entities%20%28DRUID%20versions%20prior%20to%205.15%29.md)
