---
layout:
  title:
    visible: false
---

<a id="BuildingAIAgents"></a>

# Building AI Agents

AI Agents empower employees, customers, and partners to communicate seamlessly with your business and enterprise systems. Leveraging cutting-edge technologies and design principles, these AI Agents deliver an intuitive user experience across all business functions, tasks, and devices. By providing efficient assistance, they reduce user operation time, enhance data quality, and lower overall costs.

With Druid, you can create both simple AI Agents for answering questions and sophisticated digital workers that perform complex business tasks.

<a id="AIAgentOverview"></a>

## AI Agent Overview

An AI Agent is a software system that interacts with users or operates autonomously to perform reasoning, retrieve knowledge, and execute actions within a defined scope. AI Agents can be built using either deterministic, NLP-based flows or the agentic AI framework powered by large language models. All AI Agents remain governed by enterprise rules, integrations, and oversight.

AI Agents are categorized into two types based on their operational mode:

<a id="ConversationalAIAgents"></a>

### Conversational AI Agents

A Conversational AI Agent combines conversational interface capabilities with actionable tools. Key characteristics include:

- Engages in interactive dialogue with users
- Provides conversational interface coupled with tools and API access
- Executes multi-step workflows (such as creating tickets, resetting passwords, or updating CRM systems)
- Can operate using deterministic, NLP-based flows (traditional rule-based approach) or agentic AI reasoning
- Handles complex resolution tasks with clarifying questions
- Incorporates guardrails, approvals, and policy enforcement

Conversational AI Agents are ideal for service desks, customer support, and employee self-service scenarios.

<a id="AutonomousAIAgents"></a>

### Autonomous AI Agents

An Autonomous AI Agent operates as an autonomous digital worker or employee that functions independently. Key characteristics include:

- Plans tasks and calls tools/APIs autonomously
- Operates in the background without requiring user conversation
- May be event-driven (triggering actions when specific conditions occur)
- May involve multi-AI Agent collaboration (such as planner and executor roles)

Autonomous AI Agents are ideal for automation, operations, workflows, and productivity enhancement.

<a id="HowAIAgentsOperate"></a>

## How AI Agents Operate

Equipped with over 250 built-in skills tailored for diverse industries and roles, Druid AI Agents can perform the following actions:

- Respond to inquiries
- Send channel notifications for tasks or workflows
- Generate detailed reports in PDF, MS Word, or Excel formats
- Monitor enterprise systems, check tasks, and issue status alerts
- Aid users in form completion
- Automatically route to a human operator based on predefined rules or when intent recognition fails.

When a user interacts with a Conversational AI Agent, they provide input known as an utterance. Using Natural Language Processing (NLP) or Agentic AI reasoning, the AI Agent analyzes the utterance to extract the intent and entities crucial for effective communication.

- **Data Retrieval**: If the AI Agent identifies specific entities, it retrieves data from integrated third-party systems to provide a tailored response.
- **Action Execution**: Drawing on collected entities, agents can initiate and execute specific actions within third-party systems.

The figure below illustrates how an AI Agent orchestrates a bank transfer intent.

![](../Resources/Images/Getting%20Started%20with%20Bots/chatbot-for-banking-transfer-money.png)

<a id="BuildAIAgents"></a>

## Build AI Agents

Once you create your AI Agent and its container solution, you have two options for building and configuring a fully functional AI Agent:

- **Using AI Authoring Agents**. This modern, automated approach utilizes specialized virtual assistants to drastically increase development efficiency. By simply describing your use case in a natural language, the AI Authoring Agents team automatically generates, models, and orchestrates fully packaged agentic skills out of the box. For more information, see [AI Authoring Agents](AI%20Authoring%20Agents.md).
- **Using Authoring Tools**. This traditional approach uses the core user interface features natively built into the platform. It allows you to manually build, link together, and fine-tune individual conversational flows, entities, and data integrations block by block for full granular control. For more information, see [Authoring Tools](Authoring%20Tools.md).

## Related Topics

- [AI Agent Informational Model](../5_Entities/AI%20Agent%20Informational%20Model.md)
- [Channels](../Channels/Channels.md)
- [Configuring AI Agent Advanced Settings](Configuring%20AI%20Agent%20Advanced%20Settings.md)
- [Configuring AI Agent Shortcut Keys](Configuring%20AI%20Agent%20Shortcut%20Keys.md)
- [Creating AI Agents](Creating%20AI%20Agents.md)
- [Enterprise Connectors](../7_Integrations/Enterprise%20Connectors.md)
- [Flows](../4_Flows/Flows.md)
