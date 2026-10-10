---
title: "Mapping Input Fields in User Expressions"
---

<a id="MappingInputFieldsinUserExpressions"></a>


Expressions in input mapping fields are similar to flow training phrases; the difference is that the AI Agent uses them at a flow step level. Users chatting with a AI Agent can provide information in the form of expressions, not only exact-match responses. In order for AI Agents to extract information when the user answers with an expression, authors can define training phrases on flow steps of type Prompt to provide the AI Agent with alternative ways for capturing user input.

{% hint style="info" %}
**NOTE:**  This feature is only available in Druid version 1.73 and higher and only on flow steps of type Prompt.
{% endhint %}

To map input fields in user expressions on Prompt steps, click the Training Phrases section and add variations of what the user might answer in the chat. Each training phrase on the step should contain the entity provided on the step in the **Input Mapping** field (General section).

![](../Resources/Images/Mapping%20Input%20Fields%20in%20User%20Expressions/Mapping%20Input%20Fields%20in%20User.png)

![](../Resources/Images/Mapping%20Input%20Fields%20in%20User%20Expressions/Mapping%20Input%20Fields%20in%20User_1.png)

<a id="MultipleInputsinuserexpressions"></a>

### Multiple Inputs in user expressions

In DRUID version 1.74 and higher, you can provide multiple entity fields in a training phrase on a flow step. DRUID Machine Learning extractor identifies multiple values, but the Flow Engine only sets within the conversation context the one associated to the entity field mentioned in input mapping on the flow step. For example:

**AI Agent**: "What do you want to order?"

**User**: "I would like 3 bottles of Cola, please".

To address the example above, we have a flow step with [[Product]].Name in input mapping and with the following training phrase:"I would like [[Product].Qty [[Product]].Unit of [[Product]].Name, please".

NER will extract from user input multiple records and the Flow Engine will store the extracted values in the appropriate entity fields (the ones provided in training phrases).

If the Flow Engine extracts the value of at least one entity field provided in the training phrase but not the one from Input mapping, the AI Agent keeps the user in the loop, raising the special message "InputValueInterpretationError".

If the Flow Engine does not extract any value, it proceeds to data validation. If the data is string, the Flow Engine sets the user input in the entity provided in Input mapping; otherwise, it proceeds to child intents, intent switch, etc.).

<a id="Testtrainingphrasesonflowsteps"></a>

### Test training phrases on flow steps

You can test the training phrases on the flow step by entering an expression and clicking the **Test** icon and selecting the desired AI Agent language.

![](../Resources/Images/Mapping%20Input%20Fields%20in%20User%20Expressions/Mapping%20Input%20Fields%20in%20User_2.png)

Below the test area, you will see the information AI Agent extracted in the entity provided in Input mapping (and in the step training phrases).

![](../Resources/Images/Mapping%20Input%20Fields%20in%20User%20Expressions/Mapping%20Input%20Fields%20in%20User_3.png)
