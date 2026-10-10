<a id="UnderstandingAIAgentRoutingLogic"></a>

# Understanding AI Agent Routing Logic

The following diagram illustrates how the AI Agent determines the most appropriate way to respond to a user request. The decision process combines intent recognition, flow matching, Knowledge Base (KB) search, and generative AI fallback to ensure the user receives the best possible answer.

![](../../Resources/Images/Knowledge%20Base%20with%20GPT/diagram.png)

<a id="Userrequestprocessing"></a>

## User request processing

Every conversation follows the same initial processing steps:

1. The user submits a request.
2. The system rephrases the user message to improve clarity and normalize the input.
3. The system performs intent recognition and evaluates the available resources, including conversation flows and the Knowledge Base.
4. Based on the evaluation, the system selects the best response strategy.

<a id="TheCoreRoutingDecision"></a>

## The Core Routing Decision

After intent recognition, the system checks whether a KB article, a flow, both, or neither were found.

<a id="Path1SingleflowmatchedActionDrivenPath"></a>

### Path 1: Single flow matched (Action-Driven Path)

If a flow matches perfectly but the Knowledge Base has no relevant information, the system triggers the flow immediately.

<a id="Path2KBarticlefoundInformationDrivenPath"></a>

### Path 2: KB article found (Information-Driven Path)

If a KB article is found, the system triggers the KB Agent. The KB Agent evaluates the best match and decides how to respond:

- **Only the KB article is relevant**: The agent answers directly from the Knowledge Base.
- **Only the flow is relevant**: The agent triggers the matched flow.
- **Both KB and flow are relevant**: The agent answers from the Knowledge Base and recommends the related flow as a follow-up action.
- **No match**: The request is routed to the **Intent not recognized** flow for fallback handling.

<a id="Path3NoresourcefoundormultipleresourcesfoundFallbackPath"></a>

### Path 3: No resource found or multiple resources found (Fallback Path)

> **IMPORTANT!** The core logic of this solution relies on a critical underlying mechanic: at the exact moment a prediction occurs, both matching flows and KB articles must be found simultaneously. The **intent\_not\_recognized** function is only invoked when both resources are detected. Once invoked, it routes the data to the KB Agent v4 flow, which applies the evaluation logic below to decide the final execution path.

If the system finds no clear match, or if multiple KB and flow candidates are detected, it triggers the Intent not recognized flow. This flow checks whether multiple intents were detected.

If **multiple intents are detected**, the request is routed back to the KB Agent (Path 2) for another evaluation. If the KB Agent identifies a valid match, it continues with the appropriate KB or flow response path.

If **multiple intents are not detected**, the system checks the fallback configuration:

- **Ask OpenAI fallback enabled**. The conversation routes to the Ask OpenAI module within its pre-configured system scope.
- **Ask OpenAI fallback not enabled**. The agent reaches a "Don't know how to answer" state and informs the user that it cannot help with that specific request.

<a id="ResponseCombinationRulesSummary"></a>

## Response Combination Rules Summary

The following table outlines exactly how information and actions are grouped together based on what the system detects:

| User Intent | Resource Availability | Agent Action & Response Delivery |
| --- | --- | --- |
| Equally matches Flow and KB | A matching flow exists and the Knowledge Base has useful context. | Returns the Knowledge Base information and triggers the matched flow simultaneously.  ![](../../Resources/Images/Knowledge%20Base%20with%20GPT/simultaneous%20match.png) |
| Best matches with a flow | A matching flow exists, but the Knowledge Base has no relevant information. | Triggers the matched flow directly.  ![](../../Resources/Images/Knowledge%20Base%20with%20GPT/flow%20only.png) |
| Best matches with KB | The Knowledge Base has the answer, and a flow can help the user. | Responds using Knowledge Base information and suggests the related flow as a follow-up.  ![](../../Resources/Images/Knowledge%20Base%20with%20GPT/kb%20and%20followup%20flow.png) |
| Only KB has the answer | The Knowledge Base has the answer. | Responds using Knowledge Base information.  ![](../../Resources/Images/Knowledge%20Base%20with%20GPT/kn%20response.png) |
| No match | Neither Knowledge Base articles nor flows match. | Routes to the intent-not-recognized flow. |
