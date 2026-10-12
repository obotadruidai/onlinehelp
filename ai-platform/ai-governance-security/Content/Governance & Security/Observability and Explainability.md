---
title: "Observability and Explainability"
---

<a id="ObservabilityandExplainability"></a>


Governance requires the technical ability to audit and explain the specific logic behind every AI Agent decision. Druid provides deep visibility into the conversational reasoning process, transforming the "Black Box" of generative AI into a transparent, auditable evidence chain.

By using these tools, administrators and compliance officers can verify that AI Agent execution remains within defined policy boundaries.

<a id="ConversationTrace"></a>

## Conversation Trace

The Conversation Trace provides an immutable, step-by-step audit of the AI Agent reasoning chain for every interaction. This tool allows you to deconstruct a session to verify the exact logic path the system followed.

- **Knowledge Retrieval**: View the specific knowledge chunks retrieved from the Knowledge Base to ground the response.
- **Logic and Intent**: Identify the specific intent matched and the confidence score associated with the match.
- **System Integration**: See exactly which API calls were executed, including the data payloads sent and received from third-party systems.
- **Evidence Chain**: Trace the transformation of a user prompt into a final system action, ensuring full traceability for internal or external reviews.

<a id="ExplainabilityLIME"></a>

## Explainability (LIME)

To satisfy rigorous audit requirements, Druid uses the LIME (Local Interpretable Model-agnostic Explanations) algorithm to provide feature-level attribution for NLU decisions.

- **Visual Attribution**: The platform highlights the specific words or "features" in a user query that triggered an intent match.
- **Decision Transparency**: By showing which terms carried the most weight in the model's decision, administrators can understand why a query was categorized a certain way.
- **Audit Readiness**: This granular visibility allows organizations to prove that the AI Agent is not utilizing biased or irrelevant criteria when processing user requests.

<a id="UsageinGovernanceReviews"></a>

## Usage in Governance Reviews

These observability tools are essential for satisfying the transparency requirements of global standards like the EU AI Act and SOC 2.

- Explainability proves the "Why" behind a match, allowing for model fine-tuning and bias detection.
- Conversation Trace proves the "How" of the execution, documenting the secure handling of data and the factual grounding of the response.
