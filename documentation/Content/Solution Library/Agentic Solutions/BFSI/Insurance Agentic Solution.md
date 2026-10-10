<a id="InsuranceAgenticSolution"></a>

# Insurance Agentic Solution

The **Insurance Agentic Solution** is an LLM-enabled business application designed to deliver a fully conversational customer experience for modern insurance providers. It transforms the traditional insurance journey—from policy discovery to claim reporting—into a natural, agent-led dialogue that utilizes OCR technology and real-time data processing to automate routine administrative tasks.

<a id="WhatsNewinVersion20"></a>

## What’s New in Version 2.0

The solution has been enhanced with specialized agentic skills to provide expert guidance across key insurance sectors, ensuring personalized and accurate coverage selection.

- **Specialized Health Support**. Guide users through health-specific disclosures and identifies suitable policies using automated ID scanning.
- **Personalized Travel Assistance**. Analyze trip details and traveler requirements to recommend appropriate coverage for international or domestic travel.
- **Enhanced Claim Intelligence**. Expanded capabilities for multi-modal claim registration, including automated visual damage assessment for automotive incidents.

<a id="KeyFeatures"></a>

## Key Features

As the foundation of the new Agentic Insurance Business Suite, this solution supports core insurance processes with the following key features:

- **Customer account access** – Agent-driven conversations to view current policies and claims.
- **Car MTPL insurance** – Agent-driven conversation with OCR to scan car registration and ID documents that guides the user to discover the best insurance policies.
- **Property insurance** – Agent-driven conversation with OCR to scan ID documents that guides the user to discover the best insurance policies for a new apartment or house.
- **Claim reporting** – Agent-driven conversation for registering new claims for car and property incidents based on the active insurance policies. For car claims, the agent provides automatic damage evaluation based on incident images provided by the user.
- **User authentication** – Agent-driven conversations to sign in and create accounts using OTP (one-time password) verification.

<a id="KeyComponents"></a>

## Key Components

This solution includes:

- Insurance database – Hosted on DRUID Data Services, supports all core data operations.
- Insurance Agent workspaces:
  - **Admin Workspace** – Manage insurance product features and customize GPT prompts.
  - **Insurance Workspace** – Access a 360-degree view of customer details.
- LLM-enabled agents – Automate and streamline the main business processes.

<a id="HowtheAIAgentAssistSUsers"></a>

## How the AI Agent AssistS Users

<a id="PolicyAcquisition"></a>

### Policy Acquisition

The AI Agent guide prospective customers through a logical, step-by-step discovery process:

1. **Verification**. The agent introduces the need for identity and asset verification, triggering automated scanning tools to confirm personal and property details.
2. **Needs Assessment**. The AI asks targeted questions to determine eligibility—such as vehicle usage, property characteristics, or travel destinations.
3. **Tiered Offerings**. Based on the gathered data, the agent calculates and presents various coverage tiers, allowing the user to compare benefits and pricing.
4. **Closing**. Once a selection is made, the agent handles document signing and facilitates secure payment or scheduling.

<a id="ClaimsManagement"></a>

### Claims & Management

For existing policyholders, the AI Agent streamlines support and reporting:

- **Claim Registration**. The agent identifies the user's active policies and guides them through documenting the incident.
- **Visual Damage Estimation**. In automotive claims, it prompts for images of the damage and provides a structured estimate of repair costs based on recognized parts.
- **Policy Management**. Users can interact with the AI Agent to view active coverage, check claim statuses, pay outstanding invoices, or update personal contact information.

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../../2_AI%20Agents/Creating%20AI%20Agents.md).
- Druid Vision key with **convert-pdf-to-jpeg** and **convert-pdf-page-to-jpeg** permissions.
- LLM resource enabled on the tenant; not required if you use your own LLM for configuration instead of Druid Service Gateway.

<a id="Configuringthesolution"></a>

## Configuring the solution

To configure the solution, follow these steps:

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution "Insurance Agentic Solution" and import it following the instructions provided in section [Installing Solution Templates](../../Installing%20Solution%20Templates.md).

Wait until the import status shows as “Success”.

<a id="Step2Configureappsconnections"></a>

### Step 2. Configure apps connections

Go to **Solution Contents** > **Apps**. Click the app you want to configure. Follow the setup instructions provided in the sections below.

| App | Description | Setup required |
| --- | --- | --- |
| DRUID-LLM | Default connection using tenant credentials. If using your own LLM, change the base URL and the key in the integration accordingly.  ![](../../../Resources/Images/Agentic%20Insurance/druild%20llm%20url.png)  ![](../../../Resources/Images/Agentic%20Insurance/integration%20auth.png) | Mandatory |
| DRUID Vision OCR | Enables OCR capabilities for car registration and ID documents. Required for Car MTPL insurance conversations. | Mandatory |
| DRUID-Sendgrid | Sends OTP codes and insurance policy emails to users. | Mandatory |
| AzureStorage | Enable AzureStorage capabilities for saving insurance claim pictures. | Optional |

#### Configure the DRUID Vision OCR app

To configure this app connection, follow these steps:

1. Go to **Administration** > **Druid Services**.
2. Copy the Resource URL and the Token corresponding to the DRUID.Vision.Api resource you want to use — you’ll need them to configure the app connection.

![](../../../Resources/Images/agentic%20insurance.png)

> **NOTE:** If the DRUID.Vision.Api resource does not appear, contact your sales representative to activate DRUID Vision on your tenant. The DRUID.Vision.Api resource should have the following three claims: **convert-pdf-page-to-jpeg** and **convert-pdf-to-jpeg**. If any of these claims are missing, ask your Druid representative to update the configuration.

3. Go to **Solution Contents** > **Apps** and click on **DRUID Vision OCR**.
4. In the **Base URL** field, paste the resource URL you copied at step 2. Remove everything after api/, including *engine/{templateName}*. For example, change: *https://druidvision.eu.druidplatform.com/api/engine/{templateName}* to: *https://druidvision.eu.druidplatform.com/api/*.
5. In the Variables table, enter the token you copied at step 2 as the key.
6. Click **Save & Close** to complete the configuration and return to the Apps page.

#### Configure the DRUID-Sendgrid app

Click on the DRUID-Sendgrid app and in the **API key** field, enter your SendGrid API key.

![](../../../Resources/Images/Solutions%20Library/sendgrid%20poly%20key.png)

Click **Save & Close** to apply the configuration and return to the Apps page.

<a id="ConfiguretheAzureStorageapp"></a>

### Configure the AzureStorage app

Click on the **AzureStorage** app and fill in the info in the **Account name** and **Account key** field with your Azure account information. Also make sure to check the **Use HTTPS** toggle.

![](../../../Resources/Images/Agentic%20Insurance/azure%20app.png)

Click **Save & Close** to apply the configuration and return to the Apps page.

> **NOTE:** After configuring all required apps, click **Publish** to apply the changes.

<a id="Step3SetuptheAIAgentspecialflows"></a>

### Step 3. Set up the AI Agent special flows

Go to the AI Agent settings, Details page and click the Dialog management section header. The section expands. Select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome flow | welcome |
| Intent Not Found flow | switch-intent-no-orchestator |

Scroll down and click **Save & Close**.

<a id="Step4ConfigureNLUIntentClassificationwithLLM"></a>

### Step 4. Configure NLU Intent Classification with LLM

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **NLU Intents classification**.
3. Set **Endpoint Type** to **Druid**. If you’re using your own LLM resource, select your resource instead. Then choose the **Model Name**.
4. Click **Set default** for both prompts to automatically fill in instructions.

![](../../../Resources/Images/Agentic%20Insurance/nlu%20with%20llm.png)

5. Save and train the AI Agent.

<a id="Step5Provisionthedata"></a>

### Step 5. Provision the data

To provision all the required information for the AI Agent, follow these steps:

1. Select the **Admin** workspace.
2. Click **InsuranceSettings** on the workspace menu.
3. Click the **Provision Data** button.

![](../../../Resources/Images/Agentic%20Insurance/data%20provision.png)

The default settings include a predefined set of values and records.

<a id="Step6ConfigureAdvancedSettingsEmailandAttachmentStorageoptional"></a>

### Step 6. Configure Advanced Settings: Email and Attachment Storage (optional)

#### Send Emails

The **sendEmails** settings determines if the solution will send emails to the user (for example during OTP).

#### Azure Attachment Storage

The **allowAzure** setting determines where the solution stores images and files uploaded by users (for example, during a claim process).

#### How to activate

1. Select the **Admin** workspace.
2. Click **InsuranceSettings** on the workspace menu.
3. Click the **Current Values** record to open it.
4. On the settings form:

- Toggle **SendEmails** on to enable SendGrid email sending.
- Toggle **allowAzure** on to enable Azure Storage.

5. Click **Save**.

<a id="PreviewtheSolution"></a>

## Preview the Solution

<a id="ClaimSubmission"></a>

### Claim Submission

<a id="PolicyIssuing"></a>

### Policy Issuing
