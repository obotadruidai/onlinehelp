---
layout:
  title:
    visible: false
---

<a id="IntentRephraseFlow"></a>

# Intent Rephrase Flow

The Intent rephrase flow empowers authors to refine user intent using external services like GPT, enhancing the effectiveness of AI Agent interactions. By configuring this feature, authors can streamline the process of optimizing user intent for their AI Agent models.

This topic provides comprehensive guidance on setting up and leveraging the Intent rephrase flow to ensure accurate predictions and improved user experiences.

> **NOTE:** The "Intent rephrase flow" feature is available in DRUID 5.18 and later versions. DRUID version 7.4 introduces user says pipeline execution changes for Intent rephrase.

Define a flow for intent rephrasing to optimize the user intent for your AI Agent model. Navigate to the AI Agent details page, access the Dialogue Management section, and select the designated flow for intent rephrasing from the **Intent rephrase flow** drop-down menu.

![](../Resources/Images/druid%205.18/REPHRASE%20FLOW.png)

> **IMPORTANT!** The "Intent rephrase flow" is triggered immediately before the Conversation Engine predicts to other parent flows or against the Knowledge Base. If intent switch occurs within parent flows when executing prompt steps with input training phrases, the Intent rephrase flow activates prior to the intent switch.

This special flow does not execute under the following conditions:

- When there is an exact match of the user utterance.
- Within a parent flow, if a child flow is triggered inside or at the end of the flow, the Intent rephrase is skipped.

> **NOTE:** In DRUID versions preceding 7.4, the "Intent rephrase flow" is solely executed when user input is sent during idle conversation periods. Subsequently, the AI Agent uses the rephrased intent stored in [[Intent]].Text to make predictions within the model. Once within a flow, the execution of the flow ceases, ensuring that the user intent remains unaltered.
