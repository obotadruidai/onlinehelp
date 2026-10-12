---
title: "Knowledgebase with GPT V4"
---

<a id="KnowledgebasewithGPTV4"></a>


Knowledge Base with GPT V4 integrates Druid flow orchestration capabilities with the power of Druid LLMs (Druid Becus and the Azure OpenAI gpt-4.1-mini model). This combination delivers accurate, conversational answers in real time, eliminating the need for user manual browsing through multiple articles.

The latest version introduces flow awareness, enabling the AI Agent to evaluate Knowledge Base articles and available flows simultaneously. This ensures users receive the exact information they need, alongside direct execution paths to complete tasks seamlessly.

This solution is ideal for teams looking to:

- Streamline information access.
- Trigger transactional business flows directly from natural language questions.
- Improve support efficiency.
- Gain clear visibility into how their AI Agent handles real-world queries.

<a id="WhatsNewinVersion925"></a>

## What’s New in Version 9.25

**Comprehensive NLU (Flows + Knowledge Base)**. The agent now evaluates Knowledge Base articles and available business flows concurrently. When analyzing a query, it pulls intent-matching flows and articles together to construct a highly comprehensive response.

- **Direct Trigger Flow Capability**. A dedicated **trigger\_flow** function lets the agent invoke an explicit business flow using its exact identifier and name whenever a user expresses a desire to perform a transaction or action.
- **Upgraded LLM Model**. System support has been updated to use the Azure OpenAI gpt-4.1-mini model for improved efficiency and matching accuracy, replacing the legacy 4.0-mini model ahead of its deprecation.
- **SharePoint Permission Verification**. When enabled, each KB article is validated against user permissions in SharePoint. Articles without user read access are marked as `[Access: Restricted]` within the prompt context, ensuring the **AI Agent** only references authorized topics. Configure this behavior using the **[[KBResponse]].KBCheckPermissions** and **[[KBResponse]].PermissionsIds** variables. For more information on how to set uper permissions for SharePoint data sources, see [User Permission-based Content Filtering](https://druidai.gitbook.io/druid-ai-docs/knowledge-base/data-sources/sharepoint-data-sources/user-permission-based-content-filtering).
- **Sub-3-Second Latency**. Optimized and purpose-built to deliver sub-3-second responses for real-time conversational flows.
- **Webchat Streaming Experience**. Rich formatted responses are now rendered dynamically within a single, continuous message for a smoother user experience.
- **Voice AI Agent Support**. Full compatibility is now extended to both text and voice AI Agents, expanding applicability beyond traditional text-based interactions.
{% hint style="info" %}
**NOTE:** When using the solution for a voice AI Agent, you must activate the [AudioCodes channel](https://druidai.gitbook.io/druid-ai-docs/channels/voice-and-telephony/voice-audio-codes-channel).
{% endhint %}

<a id="Benefits"></a>

## Benefits

- **Reduced User Friction**. Users receive the information they need and the ability to take action within a single interaction, eliminating unnecessary steps.
- **No More Dead Ends**. If the system does not recognize a specific intent, it prevents dead ends by finding alternative, relevant paths forward through simultaneous Knowledge Base or flow matching.
- **Intelligent Request Routing**. The system automatically routes information requests to Knowledge Base answers and action requests to explicit flow triggers, ensuring precise handling.
- **Natural Ambiguity Resolution**. The agent handles ambiguous user queries naturally. When a request could imply either an informational question or a transactional action, the system seamlessly presents both options to the user.

<a id="KeyFeaturesandComponents"></a>

## Key Features and Components

{% hint style="warning" %}
**IMPORTANT!** This information is for informational purposes only. DO NOT change the configurations.
{% endhint %}

This solution introduces intelligent fallback handling, automated routing, and powerful analytics through the following core components:

- **Intent-Not-Recognized Flows KB V4**. An enhanced fallback flow that evaluates both Knowledge Base (KB) articles and available flows when a user query misses a known intent. This ensures effective routing without creating dead ends.
- **KB Agent V4**. The core response agent containing the decision logic. It registers articles as "available information" and available flows as "available actions," classifies user needs, and manages the conversation flow.
- **KB\_response**. The primary function used to answer user questions from the Knowledge Base. It includes native support for citations, follow-up questions, insights, and user feedback collection.
- **trigger\_flow**. A dedicated function allowing direct invocation of a backend business flow by copying the exact flow identifier and name from the available actions list.
- **intent\_not\_recognized**. A fallback function used when neither resource satisfies the query. It logs the interaction and clears the context for a clean user recovery.
- **GPT Identity**. The configuration flow governing the agent personality, calendar awareness, channel-specific instructions, and function enforcement rules (including combination logic).
- **KB Agent Workspace**. A dedicated dashboard where you can track all intents, view and export collected user feedback, and access detailed reports on KB agent usage.
