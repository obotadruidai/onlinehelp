---
title: Concepts and Terminology
---

# Concepts and Terminology

This topic introduces the key terms you must know before working with the **Druid AI Platform**.

### Agentic AI

Agentic AI is a framework to building AI systems that use iterative, multi-step reasoning and actions to achieve a goal, rather than a single prompt-and-response interaction.

### AI Agent

An AI Agent is a software system that can interact with users, reason over context, retrieve knowledge, and execute actions within a defined business scope.

In Druid, AI Agents can support both guided conversational experiences and autonomous execution. They can use deterministic, NLP-based flows, agentic AI capabilities powered by large language models, or a combination of both, depending on the business scenario.

AI Agents operate within enterprise boundaries. Their behavior is governed by configured rules, permissions, integrations, available skills, and human or system oversight. This ensures that AI Agents can provide assistance, make decisions, and perform actions reliably, securely, and in line with organizational processes.

### Druid Conductor

Druid Conductor is an orchestration AI Agent that acts as the primary interface in any conversation. It owns the conversation end-to-end — handling requests it can answer directly, and silently triggering specialized AI Agents when needed. The user always talks to one AI Agent. The complexity is invisible.

Think of a healthcare company where Mary is the primary AI Agent that patients always talk to. When a patient needs to book an appointment, Mary delegates to the Appointment Scheduling agent. For a billing question, she routes to the Billing agent. For general support, she calls on the Support agent. The patient just talks to Mary — she handles the rest.

Orchestrated AI Agents work like specialized teams within your organization. Each one is an expert in its own domain. Druid Conductor knows when to handle something itself and when to call in a specialist — preserving full context across every hand off so the conversation always feels continuous.

![](../../.gitbook/assets/Megabots.png)

### Agentic Skill

An Agentic Skill, also referred to as a Skill, is an operational capability that enables a Druid AI Agent to perform a business task reliably and contextually within an enterprise environment.

An Agentic Skill packages the instructions, knowledge, tools, functions, integrations, business rules, and supporting Druid artifacts the AI Agent needs to understand a request, decide what action is needed, interact with enterprise systems, and deliver a business outcome.

Agentic Skills are built from Druid artifacts such as entities, flows, integrations, functions, data models, forms, notification templates, workspaces, and business logic. They do not replace these artifacts. Instead, they bring them together so the AI Agent can use them in context to guide a conversation, execute actions, and complete a process end to end.

For example, an Appointment Management Agent can use multiple Agentic Skills to manage appointment requests. Depending on the user’s intent, the AI Agent can book, confirm, cancel, or reschedule appointments; update patient details; check provider, facility, and slot availability; apply scheduling rules; create or update appointments in connected systems; and send confirmation or reminder notifications.

Compared to traditional agentic skills that mainly provide reusable instructions, tools, or artifacts for automations, Druid Agentic Skills go further by combining those artifacts with enterprise context, governance, integrations, and orchestration. They enable the AI Agent not only to perform tasks, but also to operate inside the enterprise and deliver outcomes across real business processes.

For more information, see [Understanding Agentic Skills](<../AI Agent Orhestration/Druid Conductor.md#Understa>).

### Artificial Intelligence (AI)

Artificial Intelligence (AI) is the intelligence demonstrated by machines. It includes concepts like natural language understanding (NLU) and machine learning.

### Channel

A **channel** is the environment that hosts the AI Agent and enables two-way conversation.

You can build and deploy Druid AI Agents across various channels. For employee-facing AI Agents, consider deploying them on Intranet Web Pages, Microsoft Teams, or Slack. For customer-facing AI Agents, you might deploy them on your public website, Facebook, WhatsApp, Skype, or custom Mobile Apps.

### Context

Similar to natural language **context**, the context controls the flow of a conversation. During a conversation flow, the AI Agent saves information in its memory, which is cached in the form of **entities** and **variables**.

### Flow

A **Flow** configures the dialog between the end-user and the AI Agent. In the Druid AI Platform, a Flow is equivalent to an **Intent** plus a **Dialog**.

A **Flow** uses a tree-like structure where you configure logical decisions to provide different paths based on context, actions, or user input.

### Intent

An **Intent** represents the purpose of a user’s input (an utterance). An **Intent** categorizes the user’s goal for one conversation turn.

You define many Intents and bundle them together with **Dialogs** into **Flows**. You train an AI Agent using **training phrases**, which are examples of what the user might input. When the end user writes or says something, the **Druid AI Agent** matches the user's expression to the best **Intent**.

For each **Intent**, you can define actions that trigger specific behaviors in your system. When the AI Agent matches the **Intent**, it provides the action to your system.

### Dialog

A **Dialog** defines the AI Agent's responses to defined Intents. In the Druid AI Platform, you configure the Dialog as part of the Flow.

### Entities

**Entities** are variables that complement or modify the Intent. An **Entity** is a snippet of information the AI Agent can understand to serve the correct answer.

**Entities** are typed memory slots that keep the conversation context. In the Druid AI Platform, entities are structured objects with attributes (or fields) and relations between them. The collection of entities within the AI Agent creates the **AI Agent Informational Model**.

**Example**: The Account entity represents a person or organization that buys goods or services. It includes fields like Name, First Name, Last Name, Email, Orders (collection of Orders), Invoices (collection of Invoices), and Payments (collection of Payments).

### Utterance

An **Utterance** is whatever the user says or inputs. The **Druid AI Agent** extracts the **Intent** and **Entities** essential to carrying on a conversation from the **Utterance**.

### Druid local variable

**Druid local variables** are defined in **Flows** and persist throughout the conversation during the **Flow** execution.

### Integration context variable

**Integration context variables** persist during the connector task execution and are used for custom authentication. Druid keeps them in memory until using them in the authorization call to the business API.

### Machine learning (ML)

Machine learning (ML) is the field of AI that focuses on making machines learn. In the context of AI Agents, **ML** improves the AI Agent's ability to answer complex user queries over time.

### Natural language processing (NLP)

Natural language processing (NLP) is a field of AI that encompasses everything related to a machine understanding human input. To do this, an **NLP** engine uses tools such as natural language understanding, sentiment analysis, and tokenization.

### Natural language understanding (NLU)

Natural language understanding (NLU) is the process that examines an **utterance** and extracts its **entities** and **intent**. It allows a machine to understand what a user is saying.

### Related Topics

* [Druid AI Platform](<Druid Platform.md>)
* [Druid Portal](<Druid Portal.md>)
