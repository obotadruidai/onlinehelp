---
title: Set Up the Solution
---

# Set Up the Solution

For solution admins

This section explains how to install and configure the Epic Appointment Management Agent.

### Prerequisites

* Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
* You should have the Druid SIP Channel. For information on how to configure the Druid SIP Channel, see [Configure Druid SIP Connectivity](<../../../Druid Voice/Configure Druid SIP Connectivity.md>).
* Access to an Epic FHIR Sandbox.
* An application created in your Epic FHIR Sandbox.  In the application configuration, make sure to select under the Incoming APIs section, the Epic APIs listed in [Epic API inventory](<Epic API inventory.md#_Epic_API_inventory>)
* Druid Vision key with **convert-pdf-to-jpeg** and **convert-pdf-page-to-jpeg** permissions.
* LLM resource enabled on the tenant; not required if you use your own LLM for configuration instead of Druid Service Gateway.

### Installation and setup procedure

Complete the following steps to install and configure the solution:

#### Step 1. Install the solution from the Solutions Library

1. Go to the **Solutions Library**.
2. Search for **Epic Appointment Management Agent**.
3. Import the solution.

Wait until the import status shows Success.

#### Step 2. Configure app connections

Navigate to **Solution Contents** > **Apps** and configure the apps as follows:

| App                     | Connection Details                                                                                                                                                                             | Mandatory |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| gpt-agent               | Default connection using tenant credentials. No additional configuration required. If you're using your own LLM resources, configure the endpoint and key.                                     | Yes       |
| Druid Vision (optional) | Enter the key inside the Variables tab. Ensure permissions for **convert-pdf-to-jpeg** and **convert-pdf-page-to-jpeg** are active in **Administration** > **Druid Services**.                 | No        |
| Epic                    | Configure the Epic app to establish the connection between Druid and Epic on FHIR. For configuration instructions, see [Epic Integration](<../../../7_Integrations/Epic/Epic Integration.md>). | Yes       |

Click **Publish** to make the apps available.

#### Step 3. Configure AI Agent special flows

To configure the required special flows:

1. Go to the AI Agent details page and click **Dialogue Management**.
2. Set the special flows listed below:

| Special Flow Name | Select                             |
| ----------------- | ---------------------------------- |
| Welcome flow      | epic-connector-appointment-manager |

![](<../../../../.gitbook/assets/Set Up the Solution (1).png>)

3. Save the configuration.

#### Step 4. Import default settings

To provide all the required information for the AI Agent, follow these steps:

1. Select the **Epic Appointment Settings** workspace.
2. Click **Settings** on the workspace menu.
3. Click the **Provision Data** button.

![](<../../../../.gitbook/assets/Set Up the Solution_1 (1).png>)

The default settings include a predefined set of values and records. You can extend the configuration at any time by manually adding new data records.

#### Step 5. Configure NLU Intent Classification with LLM

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **Classification Model Type**.
3. Set **Endpoint Type** to **Druid**. If you’re using your own LLM resource, select your resource instead. Then choose the **Model Name**.
4. Click **Set default** for both prompts to automatically fill in instructions.

[!\[\](../../../Resources/Images/Epic%20Appointment%20Management/Set%20Up%20the%20Solution\_2.png)](../../../Resources/Images/Agentic%20Insurance/nlu%20with%20llm.png)

5. Save and train the AI Agent.
