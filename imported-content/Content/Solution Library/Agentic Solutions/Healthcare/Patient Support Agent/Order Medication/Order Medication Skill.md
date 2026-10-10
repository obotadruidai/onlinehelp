---
title: "Order Medication Skill"
---

<a id="OrderMedicationSkill"></a>


The **Order Medication Skill** is an intelligent clinical workflow layer built on top of the Healthcare Agentic Solution. It automates the complete prescription lifecycle — from initial creation, through ongoing changes, to patient-initiated repeat reorders — transforming prescription management into a guided, conversational experience for both medics and patients. By combining structured medication search, guided data collection, and automated provider review routing, the solution reduces administrative overhead while improving prescribing accuracy and patient self-service.

The skill is triggered automatically after the completion of an appointment and manages the entire order medication lifecycle, from prescription generation to medication reordering and patient request processing.

<a id="KeyCapabilities"></a>

## Key Capabilities

- **Complete Prescription Lifecycle**. Manages the full prescription process, including creation, medication additions, instruction updates, medication replacement, removal, and prescription-level updates to end date and refill frequency.
- **Automated Provider Review Routing**. Any prescription changes requested by the patient — a disputed dosage, an early refill request, a medication not on the patient's repeat list — is automatically routed to the prescribing provider for review, and an order is only sent to the pharmacy once approved.
- **Repeat Prescription Self-Service**. Lets patients reorder from their existing repeat prescriptions independently, including eligibility checks, dosage confirmation, and pharmacy selection, without needing to contact the practice directly.
- **Multilingual Support**. The AI Agent detects and switches to any language instantly, ensuring a comfortable experience for every medic and patient.

<a id="KeyComponents"></a>

## Key Components

The main components of the solution include:

- **Business Workflows**:

- **Prescription Creation** - guided flow for building and finalizing a new prescription after a completed appointment.
- **Prescription Management** - guided flow for adding, updating, replacing, or removing medications, and updating prescription-level fields, on an existing prescription.
- **Repeat Prescription Reorder** - patient-facing flow for reordering existing repeat prescription medications.
- **Provider Request Routing** - handles escalation of early refills, dosage disputes, off-list medications, and order approvals to the prescribing provider.

- **Two dedicated workspaces**:

- **Order Medication Admin** workspace - Used by admins to configure nomenclatures, medications, settings, and other variables.
- **Order Medication Management** workspace - A provider-focused view used to manage appointments, prescriptions, prescription orders, and prescription requests.

- **Data Model**. Contains all essential prescription entities (Prescription, PrescribedMedication, ProviderRequest, and supporting nomenclatures).
