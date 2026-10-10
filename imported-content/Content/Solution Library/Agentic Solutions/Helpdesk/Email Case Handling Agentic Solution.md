---
title: "Email Case Handling Agentic Solution"
---

<a id="EmailCaseHandlingAgenticSolution"></a>


**Email Case Handling Agentic Solution** is a fully agentic business application built entirely on Druid technology. Powered by Druid’s native LLMs (Becus) and compatible with external models (GPT), this solution automates the email support lifecycle — from intelligent triage and parameter extraction to multilingual responses and case management.

Customers and employees can:

- Send support requests via email in any language.
- Attach images, PDFs, or other documents; attachments are securely stored, translated, and analyzed to extract relevant information.
- Receive automatic Knowledge Base suggestions and translated replies.
- Track case progress and continue the conversation in the same thread.

Helpdesk Agents and Managers can:

- Review automatically-created email cases with original and translated content.
- Validate automatically extracted parameters, reply,, or close cases.
- Monitor SLA compliance, case volumes, and agent performance through dashboards.

<a id="KeyComponents"></a>

## Key Components

The key components of this solution include:

- **Backend Database**. Druid Data Services stores all case records, activity stream, and structured parameters.
- **Human Agent & Manager Workspaces**. Comprehensive, role-based workspaces for Helpdesk staff.
  - **Helpdesk Manager View**: Provides unrestricted access to all workspace areas: Reporting, Cases, Contacts, Agents, and Queues for full oversight.
  - **Helpdesk Agent View**: Offers a focused interface with access limited to Cases and Contacts, streamlining case management tasks.
- **Email Channel**. Integration Processes emails sent to a configured address and creates cases automatically.
- **Knowledge Base Integration**. An integrated KB with standard responses to resolve common issues automatically.
- **Attachment Storage & Processing**. Secure storage for attachments in Azure Blob Storage. Also, the attachments are translated into the AI Agent default language and analyzed to extract parameters.
- **LLM Apps (Becus & Druid GPT)**. Drive text understanding, summarization, and response generation.

<a id="BusinessWorkflow"></a>

## Business Workflow

1. **Email Reception** — Messages arrive at the configured address and are captured by the Email Channel.
2. **Triage & Language Detection** — The system identifies language, intent, and priority, and summarizes the main issue.
3. **Attachment Analysis** — Files and images are securely stored, translated to the AI Agent default language, and analyzed to extract required parameters.
4. **Case Creation** — A case is created in the backend. All collected parameters are stored in the case form for easier integration with other systems, while in the description the interaction history is logged.
5. **KB Suggestion or Request for Info** — A KB match may generate an automatic reply; if required information is missing, the system asks the user for the missing details.
   1. **Human Review & Resolution** — Helpdesk agents review extracted information and attachments, respond if needed, then resolve the case.
6. **Closure & Reporting** — Case closure is logged with timestamps and SLA checks; dashboards provide analytics.

<a id="ReliabilityandLLMRetryMechanism"></a>

## Reliability and LLM Retry Mechanism

To ensure a robust and uninterrupted user experience, the solution has a built-in retry mechanism. During any interaction that requires an LLM, if the primary model fails to respond due to a timeout or error, the system automatically retries the request using a pre-configured fallback LLM. This process is seamless to the user and guarantees business continuity.

<a id="PlugandPlayCustomization"></a>

## Plug and Play Customization

This solution is designed to be "plug and play” but also highly adaptable. An administrator can easily tailor the core components of the ticketing system directly from the Admin Workspace without requiring any code changes. This allows you to quickly align the solution with your specific business processes.

You can modify:

- **Case Statuses**: Define your own case lifecycle stages (e.g., New, Awaiting Triage, Resolved).
- **Queues & Agents**: Create and manage agent queues and assign individual agents to them.
- **Categories & Subcategories**: Customize the case classification taxonomy to match your services.
- **Parameters**: Add or change the specific data fields that need to be collected for different case types.
- **SLAs**: Adjust the time intervals for first response and case closure to meet your business goals.
- **Activity Types**: Define the different types of interactions that can be logged in the activity stream.
