<a id="AIEvaluationandResponseGuardrails"></a>

# AI Evaluation and Response Guardrails

Druid provides a comprehensive set of native guardrails to ensure AI Agent reliability and factual integrity. These controls govern how models interpret user intent and generate content, ensuring that every interaction remains within authorized business boundaries and adheres to enterprise safety standards.

<a id="HallucinationPreventionKnowledgebasewithGPTV4"></a>

## Hallucination Prevention (Knowledgebase with GPT V4)

To eliminate the risk of fabricated information, Druid uses Retrieval-Augmented Generation (RAG) and Graph RAG to ground AI Agent responses in verified enterprise data.

- **Factual Grounding**: Instead of relying on general model knowledge, the AI Agent specifically queries your uploaded documents and data services to construct answers.
- **Source Citations**: Every response generated through this framework includes built-in citations. These citations provide a transparent link to the source documentation, allowing users and auditors to verify the evidence chain for any given answer.

<a id="LLMResourceManagementandGovernance"></a>

## LLM Resource Management and Governance

Druid features an LLM-agnostic orchestration layer that decouples AI Agent logic from specific model providers. This centralized management ensures that all model activity is auditable and secure.

- **Provider Flexibility**: Administrators can centrally configure and switch between Azure OpenAI, Anthropic Claude, Google Gemini, Mistral, LLaMA, or Druid’s private Becus model without rewriting agent flows.
- **Centralized Control**: By managing resources in a single administrative location, the platform enforces consistent Role-Based Access Control (RBAC) and security policies across all model connections.

<a id="ContentandPolicyEnforcement"></a>

## Content and Policy Enforcement

To maintain a professional tone and ensure the AI Agent stays on task, administrators can define specific boundaries for conversational behavior and response generation.

- **Topic Filtering**: Configure the platform to identify and deflect queries that fall outside the defined business domain or represent a conflict of interest. This prevents the AI Agent from engaging in off-topic discussions that could pose a reputational or legal risk.
- **Keyword and Sentiment Restrictions**: Using System Prompt definitions, administrators can enforce specific linguistic boundaries. By defining strict behavioral instructions within the prompt, you ensure the AI Agent avoids restricted terminology and maintains a neutral or helpful sentiment regardless of the user's tone.
- **NLU Thresholds**: Define the confidence levels required for an AI Agent to trigger a response. This serves as a safety gate to prevent the model from "guessing" user intent during ambiguous or low-confidence interactions.
