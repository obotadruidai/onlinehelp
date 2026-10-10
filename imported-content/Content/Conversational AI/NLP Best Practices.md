---
layout:
  title:
    visible: false
---

<a id="NLPBestPractices"></a>

# NLP Best Practices

There are a few key points to keep in mind when creating your NLP model from scratch. Keep reading to learn the Dos and Don'ts of intent definition.

<a id="Useafewexampleutterances"></a>

## Use a few example utterances

The model needs a few example utterances (training phrases) in each flow in order to learn. Do not add example utterances in bulk from the beginning.

Start with 10 to 30 specific utterance examples (training phrases) and make sure that they have enough variation of word choice and word order to be able to determine which intent the utterance is meant for.

<a id="Avoidsharedintentions"></a>

## Avoid shared intentions!

When defining intents keep in mind to keep only one user intention per intent. Overlapping intentions will lead to bias in the model.

<a id="Keepabalanceofutterancesacrosseachintent"></a>

## Keep a balance of utterances across each intent

The NLP model should have a balance of utterances across each intent; therefore do not define an intent with 10 utterances and another intent with 500 utterances. If you have this situation, review the intent with 500 utterances to see if you can reorganize many of the intents using NER.

<a id="Usesentencesnotkeywordsonlyforsemanticmodel"></a>

## Use sentences, not keywords (only for semantic model)

Add utterances that contain complete statements (sentences). Try to avoid adding only single keywords as a training phrase.

<a id="Addcorrectutterancesonlyforsemanticmodel"></a>

## Add correct utterances (only for semantic model)

When adding an utterance to a flow, try to spell it correctly and use proper diacritics where necessary.

<a id="Dontaddutterancesforspellingerrorsdiacriticswordderivatesandsynonymsonlyforclassicalmodel"></a>

## Don't add utterances for spelling errors, diacritics, word derivates and synonyms (only for classical model)

The default DRUID NLP engine automatically handles specific cases, therefore, do not consider adding training phrases for the following reasons: spelling mistakes, diacritics (diacritics are removed at training time), word derivates (keyword-based form, lemma variants): playing -> play, eating -> eat, etc.

<a id="Addonlyonesentenceasatrainingphrase"></a>

## Add only one sentence as a training phrase

Currently, if the author inserts more than one sentence as a training phrase, only the first sentence (split by “.”) will be taken into consideration at training time.

<a id="FAQs"></a>

## FAQs

If you already have documents with frequently asked questions, we recommend you to:

- Use them as an inspiration to create global user intentions by adding sufficient training phrases per intent.
- Upload the more specific questions into the [Knowledge Base](../Knowledgebase/Knowledgebase.md).
