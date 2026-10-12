---
title: Customize AI Agent Flows
---


The RingCentral CX outbound campaign solution includes a preconfigured AI Agent with trigger flow steps that support key interactions during outbound calls. You can customize these interactions by creating and linking dedicated flows that implement your specific business requirements.

By default, the following three trigger flow steps are included in the agent-ring-central-campaign agentic flow, but they are not mapped to any subflows:

* **Verify Person** – Handles identity verification during an outbound call.
* **Schedule Appointment** – Handles appointment scheduling requests.
* **Live Agent** – Handles requests to transfer the conversation to a live agent.

{% hint style="info" %}
**NOTE:** The three trigger flow steps are provided as configuration points only. Their associated functionality becomes available once you create and link the appropriate custom flows.
{% endhint %}

To enable these capabilities, you must create the corresponding custom flows and associate them with the predefined trigger flow steps:

1. Create the custom flows for the scenarios you want the AI Agent to handle: Verify Person, Schedule Appointment, and Live Agent. Configure each flow according to your business requirements.
2. Navigate to **Solution Contents** > **Flows**, search for the **agent-ring-central-campaign**  flow and click on it.
3. Select the trigger flow step you want to configure.
4. In the properties panel on the right, expand the **Metadata** section.
5.  In the **Subflow** dropdown, select the custom flow you created for the corresponding scenario.

    ![](<../../../../.gitbook/assets/Customize AI Agent Flows.png>)
6. Repeat steps 3–5 for each remaining trigger flow step you want to configure.
7. Save your changes.

Once configured, the AI Agent invokes the corresponding custom flow when it makes the relevant function call during an outbound call. This enables you to tailor identity verification, appointment scheduling, and live agent handoff to your organization's processes while retaining the solution's predefined orchestration structure.
