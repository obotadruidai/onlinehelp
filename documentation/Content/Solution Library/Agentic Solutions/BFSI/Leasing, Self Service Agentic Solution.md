<a id="LeasingSelfServiceAgenticSolution"></a>

# Leasing, Self Service Agentic Solution

**Leasing, Self Service Agentic Solution** is a fully agentic business application built on DRUID technology and powered by LLM. It offers a smooth, conversational experience for managing leasing operations. Users can interact naturally with the assistant to generate documents, review invoices and partner details, make payments, and handle more complex tasks like early terminations or partial reimbursements.

<a id="KeyComponents"></a>

## Key Components

This solution includes:

- A back-end Leasing database powered by DRUID Data Services.
- A workspace for leasing agents to view and process user requests.
- A set of LLM-powered agents that automate leasing workflows and user interactions.

<a id="BusinessWorkflow"></a>

## Business Workflow

1. **Conversational Leasing Support**. The assistant helps users complete tasks such as generating travel or damage authorizations, reviewing due or unpaid invoices, accessing partner details, and making payments.
2. **Ticket-Based Flows**. For more complex processes such as early termination or partial reimbursement, the assistant collects the necessary details from the user and generates a support ticket. These tickets are stored in the back-end database, where human agents can review, process, and close.

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../../2_AI%20Agents/Creating%20AI%20Agents.md).
- Enable the API Resources for Druid WebView and Druid Data Service. Then, activate the Druid Data Service in your tenant by navigating to **Administration** > **Settings** > **Druid Data Service**, and selecting **Is enabled** and clicking the **Save all** button at the top right of the page.
- You need to have the gpt-4.1 and gpt-4o-mini models deployment via Microsoft Azure, OpenAI, or other LLM provider that supports tools / function calling. If you want to use these models via DRUID LLM API resources, they must be activated for Azure OpenAI (models gpt-4.1 and gpt-4o-mini) on your tenant. Contact your DRUID sales representative to enable DRUID-dedicated resources and generate an API token for Druid.LLM.

<a id="ConfiguringtheSkillTemplate"></a>

## Configuring the Skill Template

To configure the skill template, follow these steps:

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution "Leasing, Self Service Agentic Solution" and import it following the instructions provided in section [Installing Solution Templates](../../Installing%20Solution%20Templates.md).

Wait until the import status shows as “Success”.

<a id="Step2Configureappsconnections"></a>

### Step 2. Configure apps connections

Go to solution Apps and configure the following three connections with your credentials:

![](../../../Resources/Images/Solutions%20Library/agentic%20leasing/apps.png)

| App | Description | Setup required |
| --- | --- | --- |
| Druid\_Sendgrid | Used to send emails to users. Enter the SendGrid API key. | Mandatory |
| Druid-LLM 4.1 | Provides integration with GPT-4.1, which is not included as a standard feature in DRUID. Configure this app to connect it to your own GPT-4.1 deployment (via Microsoft Azure, OpenAI, or other LLM provider that supports tools / function calling). | Mandatory |
| Druid-LLM 4.1 mini | Provides integration with GPT-4.1 mini, which is not included as a standard feature in DRUID. Configure this app to connect it to your own GPT-4.1 mini deployment (via Microsoft Azure, OpenAI, or other LLM provider that supports tools / function calling). | Mandatory |

After you configure the connections, click **Publish**.

<a id="Step3SetuptheAIAgentspecialflows"></a>

### Step 3. Set up the AI Agent special flows

1. Go to the AI Agent settings, Details page.
2. Click the Dialog Management section header.
3. In the **Welcome flow** field, select "welcome-flow".
4. In the **Intent not found flow** field, select “switch-intent”.

![](../../../Resources/Images/Solutions%20Library/agentic%20leasing/flows.png)

5. Save the changes.

<a id="Step4ConfigureNLUIntentsClassificationwithLLM"></a>

### Step 4. Configure NLU Intents Classification with LLM

To configure NLU intents classification with LLM, follow these steps:

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **Thresholds and parameters**.
3. Add the **NLU.NER.Classification.ModelType** parameter and set it to **LLM**.

![](../../../Resources/Images/Solutions%20Library/agentic%20leasing/model%20llm.png)

Click the link that appears in the message below the NLP parameters. The NLU Intents Classification with LLM section expands.

4. From the **Endpoint Type** field, select **Druid**.
5. From the **Model Name** field, select **Druid/becus1.0** or another DRUID LLM.
6. For both prompts, click the **Set default** button. The default DRUID prompts will be automatically filled in.

![](../../../Resources/Images/Solutions%20Library/agentic%20leasing/endpoint%20settings.png)

7. Click **Save** at the bottom of the page to apply the NLU configuration.
8. Train the AI Agent.

<a id="Step6Rundatabasesetupworkflow"></a>

### Step 6. Run database setup workflow

Open a new web chat to trigger the database setup workflow. The AI Agent will automatically run the workflow, adding all necessary LLM prompts and demo data to the Leasing database.

Once the setup is complete, your assistant is ready for use in real-world leasing interactions.
