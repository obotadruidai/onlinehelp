<a id="ExplainabilityandUtterancesAnnotation"></a>

# Explainability and Utterances Annotation

Explainability is a language evaluation tool that addresses intent recognition and answers the question: “Why should authors trust the Druid machine learning model?” This tool helps authors get insights into the machine learning model to easily understand the reasons behind AI Agent behavior, figuring out when and why predictions occur. DRUID Explainability provides explanations on why the NLP model associated an utterance to a specific flow and allows authors to further fine-tune the NLP model by annotating utterances, creating a more trustworthy machine learning model.

Druid Explainability uses the Local Interpretable Model-Agnostic Explanations (LIME) algorithm that explains the predictions of the word embedding classifier in an interpretable and faithful manner. The LIME algorithm takes the training phrase, extracts each word within the phrase, and approximates the NLP model locally in the neighborhood of the prediction being explained. It checks how the extracted word matches against the NLP model, puts the word back, and checks again how it performs. If there are differences between the two matching tries, the extracted word contributes positively or negatively to the flow association.

<a id="AccessingExplainability"></a>

## Accessing Explainability

To view the explanation and matching metrics of an utterance:

1. Go to **NLU** > **Evaluation**
2. Click either the **Train Set** tab.
3. Expand the intent that contains the utterance you want to analyze.
4. Click the actions icon displayed inline with the utterance.
5. Select **Explain**.

![](../Resources/Images/Annotation%20Tool/explain%20select.png)

<a id="ExplainabilityatDruidConductorLevel"></a>

## <a id="Explaina"></a>Explainability at Druid Conductor Level

> **Info:** The Explain functionality is extended to the Druid Conductor level starting with Druid 9.25.

The Druid Conductor Explainability provides a centralized overview of all predictions performed across the Druid Conductor and its orchestrated AI Agents.

When reviewing data inside the Druid Conductor evaluation, the **Explain** tab breaks down how the orchestration layer processed the user query.

![](../Resources/Images/Annotation%20Tool/conductor%20explain.png)

> **NOTE:** At the Druid Conductor level, the annotation tool is completely unavailable. While you can review prediction logs, and LLM reasoning steps across all orchestrated AI Agents from the Conductor workspace, you cannot tag, fix, or annotate utterances directly from this centralized view. To annotate an utterance, you must navigate to the specific orchestrated AI Agent where that model is managed.

<a id="ExplainabilityofOrchestratedAIAgents"></a>

## Explainability of Orchestrated AI Agents

When evaluating individual AI Agents, the details within the **Explain** tab change dynamically based on the specific engine type handling the AI Agent logic:

<a id="SemanticNLUUsageWordImportanceChart"></a>

### Semantic / NLU Usage (Word Importance Chart)

For traditional semantic NLU classification, the **Explain** tab provides a list of words from the tested utterance and shows how they contributed to the top matched flows, including their contribution percentage:

- **Positive Contribution**: Words that contributed positively to the flow association are marked with green bars.
- **Negative Contribution**: Words that contributed negatively to the flow association are marked with red bars.

![](../Resources/Images/Annotation%20Tool/semantic%20explain.png)

<a id="LLMUsageExecutionLog"></a>

### LLM Usage (Execution Log)

For AI Agents running on an LLM orchestration pattern, LIME token visualization is not used. Instead, the Explain tab displays a sequential execution log object array tracking how the LLM determined its routing choices.

![](../Resources/Images/Annotation%20Tool/llm%20explain.png)

This log exposes:

- The raw user query and any applied LLM spelling corrections.
- Knowledge base articles or index search results pulled for semantic relevance.
- The system prompt instructions and context data created for the LLM query.
- Raw LLM responses containing the internal reasoning string detailing why specific flows or intents were chosen.

<a id="FinetuningtheNLPmodelbyannotatingutterancesforNLUusage"></a>

## Fine tuning the NLP model by annotating utterances for NLU usage

You can fine-tune the training model directly in the Explain page by making corrections to the training phrases or by deleting phrases.

Click the U icon at the bottom of the **Explain** tab.

The page displays the utterances and training phrases on each top matched flow, with words from the selected training phrase marked where they appear across the matched flows.

![](../Resources/Images/Annotation%20Tool/explain%20annotate.png)

> **Info:**  The color scheme is used only to differentiate the words within the training phrase.

You can correct training phrases or you can delete them as best suits your needs to create a trustworthy model.

<a id="Updatetrainingphrases"></a>

### Update training phrases

To easily spot a specific word from the training phrase, use the browser’s **CTRL+F** function.

![](../Resources/Images/Annotation%20Tool/edit.png)

To update a specific word, hover the mouse over the phrase where you want to make the update and click the **Edit** icon displayed inline.

The phrase becomes editable. Change the word as best suits your needs and click the **Save** icon also displayed inline.

> **NOTE:**  The color scheme does not apply to draft content. The color scheme applies only after compiling the training (after you train the AI Agent NLP model).

Save the modal. In order for the draft content to take effect, you need to train the AI Agent. Go to **NLU** > **Configurations** and click **Train**.

> **NOTE:**  If you click the **Explain** tab again without training the AI Agent, the Explain statistics will show the previous stats. If you try to annotate a corrected utterance, an error message appears informing you that you have to retrain the AI Agent.

<a id="Deletingtrainingphrases"></a>

### Deleting training phrases

If you decide that a training phrase should be removed from the top matching flow, you can remove it. To do so, hover the mouse over the training phrase and click the **Delete** icon, then save the modal.

The training phrase will be removed from the flow; however, in order for the update to take effect in the Evaluation tool, you need to train the AI Agent. Go to **NLU** > **Configurations** and click **Train**.
