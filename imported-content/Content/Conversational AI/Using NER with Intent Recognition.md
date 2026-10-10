---
title: Using NER with Intent Recognition
---

# Using NER with Intent Recognition

Expressions in input mapping fields are similar to flow training phrases. The difference is that they are not used for general model classification.

Users chatting with a AI Agent can provide information in the form of expressions, not only exact-match responses.

![](<../../.gitbook/assets/Expressions in Input Mapping.png>)

The AI Agent will extract the following input field from the user’s expression:

`[[transfer]].Amount = 100`

`[[transfer]].Currency = USD`

`[[transfer]].RecipientName = Mary Bush`

### Configuring NER Parameters

The expressions in input mapping fields feature enables AI Agent developers to configure more human-like conversations.

To configure NER parameters, use Lexicon (index your entities) and set the desired NER parameters. For more information on how to use Lexicon and index entities for NLP, see [Using Lexicon](<Using Lexicon.md>).

In DRUID versions prior to 5.15, set the NER parameters in the AI Agent details, Conversational AI section. and set up entities for NLP following the procedure described in section [Using NER with index entities.](<Using NER with Index Entities (DRUID versions prior to 5.15).md>)

Moreover, expressions used for input mapping are configured similarly to NER training phrases. You can define the NER training phrases on each flow, in the **Details** tab, together with the rest of the flow’s utterances.

In DRUID version 5.0 and higher, you can also add date range in training phrases.

Provide complete training phrases with sample values for start date and end date. E.g.: "how many employees updated their personal data 01-01-2023 - 04-19-2023". In this example, the dates are sample values for the range (start date - end date).

{% hint style="info" %}
**NOTE:** Avoid using words that identity a range (e.g., until, between, etc.), otherwise the NLP Engine will fail extracting the date range.
{% endhint %}

Add target entity for the two sample values: \[\[Entity]]. - \[\[Entity]].. To do that, select the date and click on the selection. In the pop-up that opens, click in the **Target Entity / Entity** field and select the desired entity field (either the entity field that stores the start date or the one that stores the end date) and click **Save**.

The pop-up closes and the sample values are highlighted in blue and marked with the label Date.

Example:

![](<../../.gitbook/assets/end date.png>)

![](<../../.gitbook/assets/date sample values.png>)

{% hint style="info" %}
**NOTE:** Using sample values in training phrases is available in DRUID 5.12 and higher. This feature is backwards compatible, the training phrases with NER on flows and flow steps remain unchanged; however, we recommend you to update the training phrases with NER to provide sample values for entities.
{% endhint %}

Save the settings.

{% hint style="info" %}
**Info:** To see how the NLP engine extracts a date range from the user intent, go to **Evaluation** and test different input phrases. Example:

<img src="../../.gitbook/assets/evaluate user input.png" alt="" data-size="original">
{% endhint %}

### Configuring NER in Training Phrases Example

In this example, we configure a flow for personal data update. The AI Agent will ask the users to give their name and hometown.

The flow will be triggered by the utterance “Please update my personal data”.

For the AI Agent to extract the user’s name from phrases like “My name is John Doe” and the hometown from phrases like “I live in New-York” we will make the flow settings described below.

Select the flow for personal data update and in the **Details** tab, click the **Training Phrases** section header. The section expands.

Add the utterances described in the figure below:

![](<../../.gitbook/assets/ner in training phrases.png>)

Where:

* All training phrases are used for classification, including NER or not.
* When NER is included within the training phrase (the second and the third phrases), the NER content contributes to the training model.

Set the required entities in the corresponding input mapping fields as shown in the figure below:

![](<../../.gitbook/assets/Expressions in Input Mapping_1.png>)

The users chatting with the AI Agent can either respond directly with the expected value “John Doe” or “New York”, or can answer with an expression “My name is John Doe” or “I live in New York”.

To better train the AI Agent for any expression the user might return into an input mapping step, you can add various training phrases on the flow. For example: “Friends call me John Doe”, “My hometown is New York”, etc. In these examples, "John Doe" is sample value for entity \[\[Account]].Name and "New York" is sample value for entity \[\[City]].

The entity extraction can be both:

* **deterministic** when the expected value is just a simple string, numerical or datetime expression (as in the previous example).
* **nondeterministic** when the expected value is an element of an indexed list of elements – in this case, an indexed entity type value.

The **\[\[City]]** entity has the “Name” field indexed and its values are trained using the DRUID entity train mechanism.

![](<../../.gitbook/assets/Expressions in Input Mapping_1.jpg>)

The user will be asked to choose from a list of cities the entity was indexed with.

### Related Topics

* [Managing Entities](<../5_Entities/Managing Entities.md>)
