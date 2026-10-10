---
layout:
  title:
    visible: false
---

<a id="CaseManagementAgenticSolution"></a>

# Case Management Agentic Solution

**Case Management Agentic Solution** is a fully agentic business application built entirely on DRUID technology. Powered by Druid's native LLMs like Becus and compatible with external models like GPT-4o mini, this business app delivers end-to-end support case creation and management through natural, conversational interactions.

It showcases Druid's powerful orchestration capabilities, using a multi-agent architecture to manage the entire business process with enhanced flexibility, control, and security.

**Customers and employees can**:

- Create detailed support cases through a guided conversational process.
- Access and manage their existing cases to check status, add comments and close solved cases.
- Attach images to new or existing cases, stored securely in Azure Blob Storage.
- Receive instant potential solutions from an integrated Knowledge Base (KB) before a case is escalated.
- Interact in any language, while all case information is standardized and stored in English (or any other default AI Agent language).

**Helpdesk Agents and Managers can**:

- Review all Cases, add comments (that are sent via email to customers or employees), close Cases and add new resolutions to the AI Agent Knowledge Base.
- Analyze Cases by Status, Categories and SLA compliance over custom time periods.

<a id="WhatsNewinVersion31"></a>

## What’s New in Version 3.1

- **Enhanced Activity Stream Language Support**. The agent’s Activity Stream is now automatically displayed in the AI Agent default language. All internal updates and messages are presented in natural, easy-to-read language, based on the AI Agent current settings.
- **Improved Case Form with Parameters Field**. A new **Parameters** field has been added to the case form. This section gathers key details as a structured JSON object, making collected information clearer and easier to reuse in future processes or system integrations.

<a id="KeyComponents"></a>

## Key Components

This solution includes:

| Component | Description |
| --- | --- |
| Backend Database | Powered by Druid Data Services to store all case and user information. |
| Human Agent and Manager Workspaces | Comprehensive, role-based workspaces for helpdesk staff.   - **Helpdesk Manager** view. Provides unrestricted access to all workspace areas: Reporting, Cases, Contacts, Agents, and Queues for full oversight. - **Helpdesk Agent** view. Offers a focused interface with access limited to Cases and Contacts, streamlining case management tasks. |
| Multi-Agent Orchestrator | Druid’s proprietary LLM-enabled NLU engine that analyzes user intent and routes the conversation to the appropriate specialized agent. |
| Case Creation Agent | A specialized agent that guides users through the process of creating a new case, collecting all necessary details. |
| Case Management Agent | A specialized agent that handles all user requests related to their existing cases. |
| User Authentication Agent | A specialized agent that handles user authentication by email address. |
| Small Talk Agent | A fallback agent designed to handle off-topic queries gracefully. |
| Knowledge Base Integration | An integrated KB with standard responses to resolve common issues automatically. |
| LLM Apps (Becus & GPT-4o mini) | Pre-configured LLM applications that power the agents. The solution can dynamically switch between them. |
| Azure Blob Storage | Secure cloud storage for handling image attachments for cases. |
| Case Export to Excel | Possibility to export filtered Cases to Excel for extended analysis or importing in other systems. |

<a id="BusinessWorkflow"></a>

## Business Workflow

1. **User Interaction** – The AI Agent engages with users seeking support. It first identifies the user by matching them with an existing back-end account or creating a new one.
2. **Intent Routing** – The orchestrator analyzes the user's request. Based on the intent, it passes control to either the Case Creation Agent, the Case Management Agent, or the Small Talk Agent.
3. **Case Creation** – If creating a case, the assistant guides the user through the process, asking relevant questions to gather details like priority, category, and a full description. Users can also attach images.
4. **Automated Initial Response** – After collecting all information, the assistant provides a potential solution based on standard topics from the Knowledge Base.
5. **Feedback & Escalation** – The assistant asks if the provided answer was helpful. If not, it updates the case with a full interaction summary and escalates it for human review.

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

<a id="HumanAgentUserCollaborationWorkflow"></a>

## Human Agent & User Collaboration Workflow

The solution provides a rich workspace where the interaction between human agents and users is logged effectively to resolve cases.

- **Activities Stream**: This is the core of the interaction. All communication, status changes, notes, and attachments from both the user (via the AI Agent) and the agent are logged in a single, chronological stream. This provides a complete and transparent history of the case.
- **Dynamic Case Statuses**: Cases move through a clear lifecycle with various statuses (e.g., New, In Progress, Awaiting User Feedback, Closed), allowing agents to manage their queue efficiently.
- **Image & File Uploads**: Both users and agents can upload pictures or files directly to the case's activity stream, ensuring all relevant information is stored centrally.
- **Automated SLAs**: The system automatically tracks Service Level Agreements (SLAs) for critical metrics like first response time and case closure time, helping teams meet their performance targets.
- **Reporting & Dashboards**: Managers and agents have access to visual charts and dashboards to monitor cases volumes, resolution times, and overall team performance.
- **Knowledge Base Integration**: When resolving a case, an agent can choose to add their final response to the Knowledge Base, enriching the dataset for future automated resolutions.
