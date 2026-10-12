---
title: "Overview"
---

<a id="GovernanceSecurity"></a>


The Druid AI Platform provides a comprehensive governance framework designed to ensure that AI Agent deployments are secure, compliant, and transparent. Rather than treating security as a post-deployment layer, Druid embeds governance directly into the platform architecture. This ensures that every interaction—from the initial user prompt to the final system action—adheres to enterprise safety standards and regulatory requirements.

The AI Governance framework provides administrators and compliance officers with the tools necessary to mitigate risks associated with Generative AI, such as hallucinations, data leakage, and unauthorized access. By consolidating identity management, real-time data masking, and automated testing, Druid allows organizations to scale AI Agent operations while maintaining full control over the AI stack.

This framework provides the "Proof of Trust" necessary for formal audits and compliance with global standards such as the EU AI Act, GDPR, and SOC 2.

<a id="CoreSecurityGovernancePillars"></a>

## Core Security Governance Pillars

Druid Governance is structured around four primary pillars of control:

<a id="DataPrivacyandIdentityProtection"></a>

### Data Privacy and Identity Protection

This pillar establishes a "Zero Trust" environment by securing user identity and enforcing field-level encryption across all conversational data.

- **Identity and Access Management (IAM)**: Implements Role-Based Access Control (RBAC) to govern authoring privileges and user access levels. It supports industry-standard authentication through SSO and MFA.
  For more information, see [Authoring User Management](User%20Management/Authoring%20User%20Management.md).
- **Platform Data Encryption**: All data in transit and at rest is secured using enterprise-grade encryption standards, such as AES-256 and TLS 1.2.
- **Extensive Sensitive Data Manipulation**: Beyond platform-level encryption, Druid allows for field and entity-level masking to ensure sensitive information is never exposed in the UI or plain-text logs.
- **Integration Data Security**: Use the [Encrypt Data Connector](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/encryptdata) to secure data payloads exchanged with third-party systems.
- **PII Data Anonymization**: Using the [Data Anonymization Agentic Solution](https://druidai.gitbook.io/druid-ai-docs/solution-library/business-apps/data-anonymization-agentic-solution), the AI Agent identifies and redacts sensitive information (Personally Identifiable Information) in real time before it is stored or processed by Large Language Models (LLMs). This ensures compliance with GDPR, HIPAA, and CCPA.

<a id="AIEvaluationandResponseGuardrails"></a>

### AI Evaluation and Response Guardrails

To ensure AI Agent reliability, Druid provides native guardrails that govern how models interpret and generate content.

- **Hallucination Prevention**: Leveraging [Knowledgebase with GPT V4](https://druidai.gitbook.io/druid-ai-docs/solution-library/solution-templates/knowledgebase-with-gpt-v4) and Graph RAG to ground every answer and natural-language query in verified enterprise data. This ensures that every response includes built-in source citations for auditability. This prevents the model from generating fabricated information.
- **LLM Resource Management and Governance**: Provides a centralized, LLM-agnostic framework to manage connections across various model providers. This ensures that AI Agent execution is decoupled from specific providers and governed by platform-wide RBAC policies.
- **Content and Policy Enforcement**: Definable topic filters and keyword restrictions to ensure the AI Agent maintains a professional tone and stays within its defined business domain.

<a id="ObservabilityandExplainability"></a>

### Observability and Explainability

Governance requires the ability to explain why an AI Agent made a specific decision.

- **Conversation Trace**: Provides a step-by-step audit of the reasoning chain, showing exactly which knowledge chunks were retrieved, which API calls were made, and which intent was matched.
- **Explainability (LIME)**: Offers feature-level attribution to show which specific words in a user query triggered an intent match, making the "Black Box" of AI transparent for audit purposes.

<a id="GovernanceAcrossAllDeploymentModels"></a>

## Governance Across All Deployment Models

Druid applies the same governance controls regardless of how the platform is deployed. Role-based access, encryption, audit logging, and policy enforcement work identically in cloud, hybrid, on-premises, and air-gapped edge environments. Sensitive data stays where enterprise policy or geography requires it, without changing the security model.

For organizations with strict data residency requirements, the Druid Becus private LLM can be deployed fully on-premises in an air-gapped configuration, so AI responses are never processed by third-party model providers.

<a id="ComplianceStandards"></a>

## Compliance Standards

The Druid AI Platform is designed to support deployments that must meet the following standards:

| Standard | Scope |
| --- | --- |
| SOC 2 Type II | Security, availability, and confidentiality controls |
| ISO 27001:2022 | Information security management |
| GDPR | Data protection and privacy for EU individuals |
| EU AI Act | Risk-based requirements for AI systems in the EU |
| HIPAA | Protected health information handling in healthcare |
| CCPA | Consumer privacy rights for California residents |
| NHS DTAC | Digital Technology Assessment Criteria for NHS deployments |
