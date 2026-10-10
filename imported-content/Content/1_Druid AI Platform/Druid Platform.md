---
title: "Druid AI Platform"
---

<a id="DruidAIPlatform"></a>


The Druid AI Platform is an enterprise Conversational AI platform used to build, deploy, and operate industry-specific AI Agents. The platform separates agent intelligence, conversation logic, and enterprise integrations, allowing organizations to scale AI solutions across departments and use cases.

<a id="WhatthePlatformDoes"></a>

## What the Platform Does

The Druid AI Platform enables you to:

- Create AI Agents that go beyond conversational replies to execute business tasks and automate multi-step processes.
- Integrate with enterprise systems such as ERP, CRM, ITSM, HRIS, and custom APIs through open REST, SOAP, SQL, and native connectors.
- Build knowledge-grounded responses with vector search and RAG (retrieval-augmented generation) so agents use accurate, enterprise data in reasoning and decisions.
- Monitor and govern AI performance with dashboards that track KPIs, execution traces, and analytics for continuous improvement.
- The platform supports cloud, hybrid, and on-premises deployment models to meet diverse enterprise infrastructure and security requirements.

<a id="EnterpriseGradeOrchestrationandControl"></a>

## Enterprise-Grade Orchestration and Control

At the core of the platform is Druid Conductor, the agentic AI orchestration engine that coordinates multiple AI agents and workflows. Conductor provides:

- Multi-agent orchestration that routes actions and data across agents and systems
- Governance and observability features such as audit trails, policy enforcement, and role-based access control (RBAC).
- Support for LLM-agnostic intelligence layers, including Azure OpenAI, Claude, Mistral, and custom models.
- Ability to insert human-in-the-loop checkpoints for approvals or exceptions when workflows require oversight.

<a id="Features"></a>

## Features

- **Advanced Natural Language Processing (NLP)**: Leverage proprietary, flexible NLP technology and deep learning models for robust language understanding and context-aware interactions.
- **Agentic AI Platform**: Use AI Agents, which are autonomous, adaptable workers that handle complex, multi-step business processes across various departments.
- **Multi-language Support**: Deploy AI Agents with native NLP support for over 50 international languages and integrate Neural Machine Translation for real-time translation during user-AI Agent interactions.
- **Enterprise Integration and Automation**: Connect AI Agents to enterprise systems, core business applications, and Robotic Process Automation (RPA) tools through an Open API architecture and pre-built connectors (REST, SOAP).
- **Generative AI Knowledge Base**: Transform enterprise data (from documents, emails, etc.) into an intelligent asset, allowing agents to unlock hidden knowledge and provide insightful answers.
- **Enhanced Security and Governance**: Maintain high security with powerful encryption algorithms, Role-Based Access Control (RBAC), and the option for Single Sign-On (SSO) with Active Directory.
- **Low-Code/No-Code Design**: Use a graphical flow and AI Agent designer to simplify authoring and deployment, empowering business users.
- **Dynamic Document Processing**: Integrate Druid Vision for Optical Character Recognition (OCR) and AI-enhanced data extraction from documents, including custom templates.
- **Performance Monitoring and Evaluation**: Use advanced conversation filters and built-in analytical dashboards to monitor AI Agents performance and evaluate the model accuracy based on real user interactions.

<a id="FlexibleDeployment"></a>

## Flexible Deployment

Druid’s deployment architecture is infrastructure-agnostic and supports cloud, on-premises, hybrid, and edge deployments using the same core platform components and operational model.

| Deployment Type | Description |
| --- | --- |
| Cloud | Fully hosted deployment in public cloud environments. |
| Hybrid | Combination of cloud and customer-controlled infrastructure. |
| On Premise | Deployment within customer data centers |
| Edge | Localized deployment close to data sources and users, including private and regulated environments. |

<a id="DRUIDDeploymentComparison"></a>

### DRUID Deployment Comparison

| Category | Feature | Cloud | Hybrid | On premise | Edge\*\*\* |
| --- | --- | --- | --- | --- | --- |
| Platform | Requires installations | N | Y | Y | **Y** |
|  | Release cycle | Monthly (automatically applied) | Monthly (manually, at your choice) | Monthly (manually, at your choice) | Monthly (manually, at customer choice) |
| Infrastructure | Additional hardware / software required | N | Y | Y | **Y** |
|  | Auto scaling | Y | supported, requires on premise hardware infrastructure | supported, requires on premise hardware infrastructure | supported, requires on premise hardware infrastructure |
|  | High Availability | Y | supported, requires on premise hardware infrastructure | supported, requires on premise hardware infrastructure | supported, requires on premise hardware infrastructure |
|  | Connectivity with on premise apps | Internet calls to your on premise apps | No Internet calls to your on premise apps | No Internet calls to your on premise apps | Local / no Internet required |
|  | Conversation History - Data in transit | By Druid | By Druid | Hosted on premise | Customer-controlled |
|  | Conversation History - Data at rest | By Druid | Hosted on premise | Hosted on premise | Hosted on premise |
| Platform Security | Multi-Factor Authentication | Y | Y | Y | Y |
|  | User access management | Y | Y | Y | Y |
|  | Role based access control | Y | Y | Y | Y |
|  | Data at rest | SQL encryption |  |  | Customer-managed encryption |
|  | Data in transit | SSL, TLS1.2 |  | TLS 1.1, TLS1.2, as per your existing environment | TLS 1.2+, per customer environment |
| Support | Term | on-going | 2 years from release | 2 years from release | 2 years from release |
| Channels | Direct line (WebChat) | Y | Y | Y | Y\* |
|  | MS Teams | Y | Y | N | N |
|  | WhatsApp | Y | Y | Y\* | Y\* |
|  | Facebook Messenger | Y\*\* | Y\*\* | Y\*\* | Y\*\* |
|  | Slack | Y | Y | N | N |
|  | GoogleChat | Y | Y | Y | Y |
|  | WeChat | Y | Y | Y\* | Y\* |
|  | Telegram | Y | Y | N | N |
|  | Viber | Y | Y | Y\* | Y\* |
|  | Twilio | Y | Y | N | N |
|  | Instagram | Y | Y | Y | Y |
|  | LINE | Y | Y | N | N |
|  | WeCom | Y | Y | Y\* | Y\* |
|  | Webex | Y | Y | Y | Y |
|  | Office 365 Email | Y | Y | N | N |

\*Only available if specific Druid services have open connection to the Internet.

\*\*In Druid hybrid and cloud deployments Facebook channel uses the Microsoft Bot Framework, while in on-premises deployments it uses direct Druid Facebook integration.

## Related Topics

- [Concepts and Terminology](Concepts%20and%20Terminology.md)
- [Druid Deployment](../Druid%20Deployment/Druid%20Deployment.md)
- [Druid Portal](Druid%20Portal.md)
