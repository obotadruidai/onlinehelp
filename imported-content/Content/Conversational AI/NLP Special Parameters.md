---
title: "NLP Special Parameters"
---

<a id="NLPSpecialParameters"></a>


To add special NLP parameters, go to the NLU Configurations page and click the **Intents** tab. Click on the Thresholds and parameters section header. In the Parameters table add parameters as best suits your needs.

To add a parameter, click the **Add** icon (+) at the top-right corner of the table. An empty line is added to the Parameters table. From the drop-downs, select the **Parameter** and its **Value**.

![](../Resources/Images/NLU/select%20parameter.png)

If you want to add NLP experimental parameters, tap on **Add experimental parameters** and in the table that appears, add the desired parameters.

Test the NLP model. Write the phrase you want to test (the intent), then click on **Test** and choose the corresponding language. The Conversational AI will return the matching flow (as it would do during a conversation), together with the matching score for that intent. It is a feedback tool for improving the NLP model.

> **NOTE:** The testing functionality only works for trained models!

Train the NLP model by clicking the **Train** button The training model includes ALL training phrases defined on ALL flows associated with the respective AI Agent.

![](../Resources/Images/NLU/train%20model.png)

> **Info:** You can edit or delete a parameter by clicking the Edit / Remove icon displayed inline.

After adding or changing a NLP parameter, click the **Save** button at the bottom of the page to save the parameters, then click the **Train** button to train the ML model using the newly added / updated parameter.

This section describes the NLP special parameters broken down per their usage.

<a id="OtherClassificationAlgorithms"></a>

## Other Classification Algorithms

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.Classification.ModelType | **NOTE:** Starting with Druid 9.20, this parameter is managed in **NLU** > **Configurations** > **Intents** > **NLU intent classification**. The parametere in section **Thresholds and parameters** section is obsolete. For more information, see [NLU Intents Classification](NLU%20Intents%20Classification.md).  This parameter allows you to choose between three model types for NER classification:   - **Non Semantic** - A standard model that does not consider the semantic meaning of words. - **Semantic** - Uses a pre-trained Transformers model that understands word meaning in context. This model offers higher accuracy and is ideal for large datasets. For more information, see Natural Language Understanding.  **NOTE:** All training data must be typos free and must be written with the proper diacritics; otherwise, flow matching might be done erroneously.  **IMPORTANT!** For DRUID on premise deployments, semantic-based classification is not available by default and it requires a special environment configuration including infrastructure upgrade to GPU processors. For more information, reach out to [DRUID Support](<mailto:support@druidai.com?subject=Use Semantic classification in on premise deployment>). - **Semantic Torch** - An enhanced semantic model providing improved performance for NLP tasks. - **LLM** (Technology preview). Enables intent classification using a large language model (LLM). For more information about this NLU model and how to use it, see [NLU Intents Classification with LLM](NLU%20Intents%20Classification.md). | Non Semantic |
| NLU.NER.Classification.ModelEmbeddings | This parameter allows you to select an embedding model.  **NOTE:** This parameter is available in DRUID 8.3 and higher.  An embeddings model is a machine learning model that transforms data, such as text or images, into a vector of numbers (an embedding). This vector representation captures the semantic meaning or relationships within the data, allowing for more efficient comparisons, searches, and analyses.  The following embedding models are available in DRUID:   - **English**: Creates embeddings optimized for English text, capturing semantic meaning in English language inputs. - **English – score correction**: Generates English embeddings with additional score correction, improving the accuracy and relevance of similarity scores. - **HigherEducation.v1** (English): This specialized model is trained on a rich dataset of higher education content in English only, including university-specific information, leading to improved accuracy when dealing with queries related to this domain. - **MultiAspect**: An enhanced version of our existing Multilingual model, MultiAspect offers improved performance across multiple languages and incorporates score correction for more accurate results. - **Multilingual**: Produces embeddings for multiple languages, enabling cross-lingual semantic understanding. - **Multilingual – score correction**: Offers multilingual embeddings with score correction, enhancing the precision of similarity scores across languages. - **Paraphrase**: Specializes in identifying semantically similar phrases, even if they differ in wording, useful for paraphrase detection tasks.   **NOTE:** The HigherEducation.v1 (technology preview) and MultiAspect embedding models are available in Druid version 8.13 and later.  **Info:** The Paraphrase embeddings model processes up to 125 tokens per paragraph and is ideal for short sentences, while other models support up to 512 tokens per paragraph. | MultiAspect |
| NLU.NER.Classification.UseOVA | This parameter, if set to **true**, triggers another machine learning model for classification called One-Versus-All, which consists of separate binary classifiers - one binary classifier for each possible outcome.  You can use it either on the default model, or on the semantic model if **NLU.NER.Classification.UseSemantic** is set to **true**. | false |
| NLU.NER.IndexBasedEntityExtractorV2 | Acts as a fallback additional algorithm when the default extraction algorithm fails to extract. When set to **true**, it searches for more possible candidates from the entire user says inside the Lexicon.  If the CRF algorithm extracts entities with a score under the EntityMinSingleThreshold, than the fallback algorithm searches within the Lexicon (entity index) the already matched words to ensure a higher matching score. The search will be done on the left and on the right of the matched word with a maximum offset of 3 words.  If the algorithm finds better matches in the Lexicon, they will be added or replaced based on the matching score. | true |

<a id="MultisentenceSupport"></a>

## Multi-sentence Support

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.Classification.MultiSentenceSupport | Enables multiple intent detection. Setting this parameter to **true** will detect at predict time if a user has inserted in the AI Agent snippet more than one sentence at once and will predict a match for each detected sentence. For more information, see [Multiple Intents](Multi%20Intent.md).  **NOTE:**  At training time, if this parameter is set to true and the author has inserted multiple sentences as training phrases, only the first sentence in the training phrase will be considered for training! | false |

<a id="SpellingCorrection"></a>

## Spelling Correction

Spelling correction is done by default in AI Agents at predict time. This means that even if a user writes in the AI Agent snippet a phrase that contains an erroneous word, the spelling correction algorithm will search for the correct word within all training words.

If the author changes **NLU.NER.SpellingCorrection.UseGlobalDataset** to **true**, then another global dataset of words will be used for spelling, in the specific AI Agent language. The author can disable spelling correction altogether by either setting **NLU.NER.SpellingCorrection.SimilarityScore** to **1**, or by setting **NLU.NER.SpellingCorrection.Enabled** to **false**.

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.SpellingCorrection.Enabled | Enables spelling correction when predicting an intent. | true |
| NLU.NER.SpellingCorrection.SentenceLevel | Enables spelling correction at a sentence level instead of word level, improving the spelling correction when predicting an intent.  **NOTE:**   - The parameter is valid only if the parameter **NLU.NER.SpellingCorrection.Enabled**  is set to **true**. - This parameter is available in DRUID 5.10 and higher. | false |
| NLU.NER.SpellingCorrection.SimilarityScore | The similarity score the Conversational AI used for misspelling correction.  **NOTE:** The parameter is valid only if the parameter **NLU.NER.SpellingCorrection.Enabled**  is set to **true**.  The default value is **0.8** and the maximum value is **1.0**. The value **1.0** means no spelling correction is done. | 0.8 |
| NLU.NER.SpellingCorrection.UseGlobalDataset | When set to true, the NLP engine does the first spelling correction using the model data set (generated by intents) and the second spelling correction using a global data set / dictionary.  **NOTE:** The parameter is valid only if the parameter **NLU.NER.SpellingCorrection.Enabled**  is set to **true**. | false |

<a id="Punctuationremoval"></a>

## Punctuation removal

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.Utterance.KeepPunctuation | Punctuation is removed both at training and predict time, only if **NLU.NER.Classification.UseSemantic** is set to **false**, meaning that the default algorithm is used for classification.  If **NLU.NER.Classification.UseSemantic** is true, this parameter has the default value **false**.  **NOTE:** This parameter is available in DRUID 5.12 and higher. | true |

<a id="Diacriticsremoval"></a>

## Diacritics removal

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.DiacriticsRemoval.Enabled | The Conversational AI removes the diacritics.  Diacritcs are removed both at training and predict time, only if **NLU.NER.Classification.UseSemantic** is set to **false**, meaning that the default algorithm is used for classification.  If **NLU.NER.Classification.UseSemantic** is **true**, this parameter has the value **False**. | true |

<a id="StopWordsremoval"></a>

## Stop Words removal

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.StopWordsRemoval.Enabled | The Conversational AI removes both default stop words and user added stop words at training and predict time, only if **NLU.NER.Classification.UseSemantic** is set to **false**, meaning that the default algorithm is used for classification.  If **NLU.NER.Classification.UseSemantic** is **true**, this parameter has the value **False**.  **Info:** You might want to check the [predefined list of stop words per language](StopWords/Druid_Default_StopWords.md) available by default in AI Agents. | true |
| NLU.NER.StopWordsRemoval.UseDefaultList | The Conversational AI uses the system predefined list of stop words.  **Info:** You might want to check the [predefined list of stop words per language](StopWords/Druid_Default_StopWords.md) available by default in AI Agents.  If the author wants to add more stop words, he can do that by inserting them one below the other in Settings, Conversation AI area – StopWords. If the parameter **NLU.NER.StopWordsRemoval.UseDefaultList** is set to **false**, then only the stop words provided in the settings area will be taken into account.  If the parameter **NLU.NER.StopWordsRemoval.Enabled** is set to **false**, then no stop words will be removed at training and predict time. | true |
| NLU.NER.StopWordsRemoval.UseLemma | The Conversational AI uses the canonical form of words. When this parameter is set to true, at both training and predict time, the canonical form of the custom stop words list is also removed. | true |

<a id="Evaluation"></a>

## Evaluation

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.Validation.CrossValidate.Enabled | Enables model cross evaluation metrics.  If this parameter is set to **true** at training time, regardless of the classification model used, the training will be done 5 times, by randomly splitting the data in an 80/20 fashion, where 80% is used for training and 20% for testing. After the 5 trainings are done, results are averaged and can be downloaded via the **DownloadTrainLog** button.  **Info:**  By using this method, the training time will multiply by 5. | false |

<a id="Rerankerforflowmatching"></a>

## Reranker for flow matching

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.Classification.UseReranker | Enhances flow matching by evaluating all flows that meet or exceed the threshold specified by the **NLU.NER.Classification.Reranker.MinThreshold** experimental parameter. By default, the MinThreshold parameter is set to 0.1, but you can adjust this value in the Experimental Parameters section.  The DRUID Reranker assesses user inputs against each training phrase within a flow individually, providing a more refined match.  **NOTE:** Enabling the Reranker may significantly increase training time, especially for larger test sets. When the **ModelType** is set to **llm** we recommend leaving this parameter on **false**, as the reranker logic is already covered by the LLM. | false |
| NLU.NER.Classification.Reranker.Model | It acts when **NLU.NER.Classification.ModelType = Semantic/LLM**.  Its values are:   - **Orion**: Improves search quality by re-ordering candidate results after an initial retrieval step. It works best primarily on English&Chinese. It has good accuracy for re-ranking and is reasonably efficient. - **Cygnus**: Better at handling multiple languages while still re-ranking search results. Has better language covering, being multilingual. It has strong cross-language capabilities and is lightweight for fast inference. - **Corvus**: Sorts search results or document lists based on relevance across many languages. It has very good multilingual capabilities and is optimized for cross-language relevance. - **HigherEducation1**: a general reranking model fine-tuned using higher-education data such as course catalogs, academic policies, admissions content, research descriptions, and student services information. Fine-tuning helps the model better understand the specific language used in higher education so it can more accurately rank which documents or answers best match a user’s question. | Cygnus |
| NLU.NER.Classification.Reranker.JoinUtterances | Combines all training phrases of a flow into a single unit. This allows the Reranker to compare user inputs against the overall meaning of the flow, rather than individual phrases, improving the match accuracy. | false |

<a id="Other"></a>

## Other

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.Utterance.Case | This parameter controls how NLP handles the casing of words in user utterances.  Values:   - **Lower**: Converts all words in the utterance to lowercase before performing NLP. - **Upper**: Converts all words in the utterance to uppercase before performing NLP. - **None**: Makes NLP case-insensitive. This means NLP focuses on the meaning of the words rather than their capitalization.     Use this parameter to adjust NLP behavior based on your user experience. | Lower |

<a id="ExperimentalParameters"></a>

## Experimental Parameters

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.Classification.DeterministicTraining | This parameter enhances AI Agent accuracy, allowing the model to provide more precise responses. By default, it is set to False to maintain backward compatibility.  Using this parameter will significantly increase the training duration: roughly double for non-semantic models and up to 20 times longer for semantic models  **NOTE:** This parameter is available in DRUID version 8.6 and higher. | False |
| NLU.NER.Classification.Reranker.MinTreshold | Defines the minimum flow matching score required for the DRUID Reranker to be used. When the flow matching score meets or exceeds this threshold, and if **NLU.NER.Classification.UseReranker** is enabled (set to true), the Reranker will be applied to improve flow matching accuracy. | 0.1 |
| NLU.NER.Classification.UseSemantic | This parameter appears in the Experimental Parameters section for backwards compatibility if it was set to "true" in DRUID versions prior to 7.18. You can either remove this parameter or replace it by setting **NLU\_NER\_CLASSIFICATION\_MODEL\_TYPE** to **Semantic** or **Semantic Torch**. |  |

<a id="Entities"></a>

## Entities

| Parameter | Description | Default value |
| --- | --- | --- |
| NLU.NER.CrfAlgorithmImplementation | The statistical algorithm used by the Conversational AI for structured prediction.  Possible values:   - Crf++ - Crf++V2 - An improved Crf++ algorithm. - CrfSuite - an implementation of Crf++ for labeling sequential data.   The CRF algorithm is used when training entities. If the author is working with large, indexed entities, we recommend to set this parameter to **CrfSuite**. | Crf++V2 |
| NLU.NER.CrfFlowStepInputMappingAlgorithmImplementation | For input mapping training phrases defined on a step level DRUID creates a smaller NLP model. If you define a larger number of training phrases on steps, for better results, we recommend settings the parameter to "Crf++V2".  **NOTE:** This parameter applies on a AI Agent level, input mapping training phrases on all steps. You cannot set it per step. | Crf++V2 |

<a id="DeprecatedParameters"></a>

## Deprecated Parameters

| Parameter | Description |
| --- | --- |
| NLU.NER.Classification.UseAllUtterances | **IMPORTANT!** This parameter has been deprecated due to Child Intents which better addresses the need of this parameter. We strongly recommend you not to use this parameter anymore.  Useful when you have models with input mapping with entity expressions.  This parameter on **True** means that all utterances are considered at training time. If set on **False**, only those phrases that do not contain entities or utterances with entities which have the parameter NLU.NER.EntityIndex.UseForClassification set to **true** (see [NER parameter description](Entity%20NER%20specific%20Parameters.md)) are considered at training. |
