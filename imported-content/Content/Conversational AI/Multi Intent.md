<a id="MultipleIntents"></a>

# Multiple Intents

DRUID Conversational AI breaks user messages down to their essence and can identify and follow-up on multiple flows, or intents, from a single message. If multiple intents are identified, the user is asked to select one of them.

<a id="EnablemultiintentontheAIAgent"></a>

## Enable multi-intent on the AI Agent

In DRUID, multi-intent is disabled by default. To enable the Conversational AI to detect and execute multiple intents identified in a single user utterance:

1. On the **NLU** menu, click **Configurations**.
2. Click the **Intents** tab and click on the Thresholds and parameters section header.
3. Add the NLP parameter **NLU.NER.Classification.MultiSentenceSupport**, set the value to “true” and click the **Save** icon (![](../Resources/Images/Oana/Multi%20Intent_3.png)) displayed inline.
4. At the bottom of the page, click the **Save** button to save the AI Agent settings and stay on the page, or the **Save & Close** button to save and exit the page.
5. Go to the AI Agent details page, **General** tab and click on Dialogue management.
6. Select the desired **Intent not found flow**.
7. Click the **Save & Close** button.

Once enabled, the Conversational AI identifies multiple intents in a user utterance based on the presence of the following characters:

- “.” – Period
- “?” – Question mark
- “!” – Exclamation mark
- “;” – Semicolon

If multiple intents are identified, the AI Agent will ask the user to select one of them.

<a id="EnhancingmultiintentontheAIAgent"></a>

## Enhancing multi-intent on the AI Agent

There might be flow intents with no value for NLP multi-intent detection, for example, the word “Hello” usually set as intent on the Welcome flow. If the user says, for example, “Hello, I need to update my account details”, and the multi-intent is enabled on the AI Agent, the AI Agent  Conversational AI will identify two intents: “Hello” (intent set on the Welcome flow) and “I need to update my account details” (intent set on another flow).

To streamline the multi-intent detection, we recommend you to set as “Smal Talk” the flows with intents that contain irrelevant words/intents (e.g., “Hello”).

To do so, on the flow details page (Details tab), click the **General** section header and tick on the **Small Talk** option.

![](../Resources/Images/Oana/Multi%20Intent_5.png)

At the bottom of the page, click the **Save** button to save the flow settings, or click the **Save & Close** button to save and exit the page.

The flows set as “Smal Talk” will not be taken into account by DRUID Conversational AI when doing the multi-intent classification.
