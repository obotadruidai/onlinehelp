<a id="SpecialFlows"></a>

# Special Flows

The AI Agent Designer allows you to set specific responses triggered by special events in which a AI Agent might reach out. The predefined list of events is known as special flows. You can either set the list of responses via the AI Agent Designer or set the flows to provide customized responses via the Flow Designer.

To provide customized responses for the special flows, you need to add and configure them using the Flow Designer, then in AI Agent Designer > AI Agent Details > Dialogue management section, for the desired special flow, select the flow defined in the Flow Designer.

The table below provides the list of special flows.

| Special flow | Description |
| --- | --- |
| Welcome flow | The first flow executed at the beginning of each conversation.  In the **Trigger interval** field, specify how often the Welcome flow is triggered in the same conversation. Leave it empty if you want it to trigger only once. |
| Intent not found | Flow triggered when the AI Agent does not find any match to the user intent. |
| Authentication flow | Flow triggered when a non-authenticated conversation reaches a flow that requires authentication. It is used to handle the conversation authentication process. |
| Exception flow | The flow triggered when an error occurs within a conversation flow. It allows authors to handle the error. |
| Language changed flow | Flow triggered when the conversation language is changed via the webchat drop-down menu. It allows authors to additionally handle this event. |
| Inactivity cancel conversation flow | Flow that customizes the actions taken when a conversation is automatically canceled due to user inactivity. This flow is only triggered when the conversation remains inactive inside a flow (at a flow step awaiting user input, like Prompts, Hero Cards, Choices, etc.). |
| Inactivity end conversation flow | Similar to Inactivity cancel flow, but this one is being triggered when inactivity occurs both inside a flow and in “idle” mode (outside any conversational flow). It can be used to gather feedback after a certain time the conversation ended, or to refresh the conversation after a certain inactivity time you specify in the **Conversation timeout (min)** field. |
| Voice call terminate flow | Flow triggered when a telephony-voice call ends (for AudioCodes and other telephony-based channels only). It is generally used to update call statuses in external CRM or ticketing systems, or to perform different post-call automations. |
| Knowledge Base response flow | Flow that is triggered when a user intent is predicted against the Knowledge base content, instead of the NLU model; the flow is used to further handle the retrieved KB content (RAG) and then to display it in chat. |
| Intent rephrase flow | A special flow triggered before the prediction in NLU/KB models, allowing the authors to alter the original user intent (to perform intent rephrasing, or intent PII data cleanup, etc.). When the flow execution ends, the automatic predict operation begins (followed by the trigger of the corresponding identified Flow / Special Flow).  You can also trigger the **Intent rephrase flow** even when the user's input exactly matches an existing intent in the AI Agent’s Knowledge Base by tapping on **Trigger Intent Rephrase flow also for exact matches** . |
| Facebook data deletion flow | Flow triggered automatically when Facebook sends a Data Deletion Callback request. It executes user data anonymization to meet Facebook compliance requirements and allows adding custom audit or notification logic. |
| Social media reactions flow | Flow triggered when a user reacts to a social media story (e.g., Instagram story reactions). If configured, the reaction value (applause, heart, etc.) is passed in [[Intent]].Text for custom handling. If not configured, all story reactions are ignored. |

The predefined responses are listed as keys in the **Keys** table. For each key (response), provide the key in the default and localized key for the additional language(s).

This section covers the following topics:

## Related Topics

- [Configuring AI Agent Advanced Settings](../2_AI%20Agents/Configuring%20AI%20Agent%20Advanced%20Settings.md)
