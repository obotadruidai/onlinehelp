<a id="LabResultsSkill"></a>

# Lab Results Skill

The **Lab Results Skill** is an intelligent clinical workflow layer built on top of the Healthcare Agentic Solution. It automates the lab result lifecycle — from order creation by the medical provider, through patient self-service status checks, to escalation when a patient wants to discuss a result with their provider — transforming test result management into a guided, conversational experience for both medics and patients. By combining structured order creation, guided result presentation, and automated provider escalation routing, the solution reduces administrative overhead while improving patient self-service and keeping providers looped in when a patient needs more than a status update.

The solution is made up of two cooperating AI Agents: the **Lab Order Creation Agent**, triggered by the medic using an automation in order to build a lab order, and the **Lab Results Status Agent**, a patient-facing agent that lets patients check the status of their results across chat and voice channels, and can hand off to appointment booking when a patient is concerned about a result.

<a id="KeyCapabilities"></a>

## Key Capabilities

- **Lab Order Creation** — Guided flow for the medic to build a lab order after a completed appointment: selecting the tests to order, the medical service and linking a clinical reason.
- **Patient Self-Service Result Status** — Patients can check the status of their lab results at any time, see which tests have come back and which are still pending, and request the full detailed results by email once available.
- **Multilingual Support** — The AI Agent detects and switches to any language instantly, ensuring a comfortable experience for every medic and patient.

<a id="KeyComponents"></a>

## Key Components

The main components of the solution include:

- Business Workflows:

- **Lab Order Creation** — guided flow for the medic to build and finalize a new lab order after a completed appointment.
- **Result Status Check** — patient-facing guided flow to identify the correct lab order, confirm it, and present its results, either for a specific test or all tests in the order.

- Two dedicated workspaces:

- **Lab Results Admin** workspace — used by admins to configure nomenclatures, tests, and other solution variables.
- **Lab Results Management** workspace — a provider-focused view used to manage lab orders and lab results.

- **Data Model**. Contains all essential test result entities (OrderedTests, LabOrder, LabResult, and supporting nomenclatures).
