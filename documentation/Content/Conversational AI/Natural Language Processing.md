<a id="NaturalLanguageProcessingNLP"></a>

# Natural Language Processing (NLP)

Natural language processing (NLP) is a subfield of AI. It encompasses everything that relates to a machine understanding human input. To do that, Conversational AI uses many tools like: Natural Language Understanding, sentiment analysis, tokenization, and more.

AI Agents are using by default DRUID proprietary NLP technology that focuses on interpreting the user's intent to provide information contextually based on their behavior and preferences. You can set the AI Agent conversational AI to use either external NLP providers or the AI Agent Knowledge Base model.

The platform also allows one-click Conversational AI update independently for each AI Agent.

DRUID platform provides authors with two types of NLP models:

- **Classical Machine Learning** model - This is the default machine learning model used by DRUID platform. It is recommended to be used when there are fewer than 20 user intentions (intents) defined.
- **Semantic Machine Learning** model - This model can be activated by setting the parameter **NLU.NER.Classification.UseSemantic** to true and it is based on a multilingual large language model. It is recommended to be used when you are working with a large number of intents.

## Related Topics

- [NLP Special Parameters](NLP%20Special%20Parameters.md)
- [Setting Up the AI Agent Conversational AI (DRUID versions prior to 5.15)](Setting%20Up%20the%20Conversational%20AI%20%28DRUID%20versions%20prior%20to%205.15%29.md)
