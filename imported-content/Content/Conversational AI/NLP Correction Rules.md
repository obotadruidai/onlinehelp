---
title: "NLP Correction Rules"
---

<a id="NLPCorrectionRules"></a>


When working to make the NLP model better, what you want as an author is to either:

- Add new intentions to the AI Agent (by creating new flows), thus making the chat AI Agent smarter, or
- Reduce AI Agent misunderstanding by reducing bias in the conversational model.

The following are best practices you should consider for NLP correction.

<a id="Generalruleswhencreatingnewintents"></a>

## General rules when creating new intents

When you add intentions by creating new flows, make sure that:

- The new flow does not already exist as another flow. Use domain-specific keywords to search within the flows that already exist for your use case or similar to other use cases.
- The user intention is independent enough from other user intentions.
- You have at least 10/20 training phrases for that specific user intention.
- When the flow you are adding is very similar to another flow, but different, try to put both flows under an umbrella, using child intents, or alternatively, try using entities (E.g., Error flows).

<a id="GeneralruleswhenaddingaphrasefromConversationHistorytoaflow"></a>

## General rules when adding a phrase from Conversation History to a flow

When you add a phrase from the Conversation History to a flow, make sure that:

- The extra phrase does not exceed the 100th phrase on the intent you want to add it into (if you want to add it, delete something else).
- The extra phrase does not contain typos – some of the typos entered by the users will be caught by the default NLP spelling correction algorithm (**NLU.NER.SpellingCorrection.Enabled**).
- The extra phrase is correctly written with diacritics (when using the semantic model).
- The sentence is not a multi-sentence. Currently, training supports only one sentence at a time, and the multi-sentence parameter (**NLU.NER.SpellingCorrection.Enabled**) is considered only at predict time - when a user writes two or more sentences in the same message, each of them will be matched separately into an intent.

## Related Topics

- [NLP Best Practices](NLP%20Best%20Practices.md)
- [NLP Special Parameters](NLP%20Special%20Parameters.md)
