---
layout:
  title:
    visible: false
---

<a id="SetUptheSolution"></a>

# Set Up the Solution

For solution admins

This section explains how to install and configure the Case Management Agentic Solution.

<a id="Prerequisites"></a>

## Prerequisites

Before installing the solution, verify that the following requirements are met:

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- A published AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../../../2_AI%20Agents/Creating%20AI%20Agents.md).
- Microsoft Office 365 email is configured and activated as [Email Channel](../../../../Channels/Email/Email%20Integration.md).
- LLM and translation resources enabled on your tenant.
- Azure subscription credentials for the Blob Storage service for secure attachment handling.

<a id="Installationandsetupprocedure"></a>

## Installation and setup procedure

Complete the following steps to install and configure the solution:

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

1. Go to the **Solutions Library**.
2. Search for **Email Case Handling Agentic Solution**.
3. Import the solution.
4. Wait until the import status shows Success.

<a id="Step2ActivateEmailchannel"></a>

### Step 2. Activate Email channel

After importing the solution, navigate to AI Agent Settings. Click the **Channels** tab and activate the Outlook channel by following the instructions described in [Outlook Channel](../../../../Channels/Outlook.md).

<a id="Step3SetuptheAIAgentspecialflowsandenableKBusage"></a>

### Step 3. Set up the AI Agent special flows and enable KB usage

1. Go to the AI Agent details page and click **Dialogue Management**.
2. Set the special flows listed below:

| Special Flow | Select |
| --- | --- |
| Welcome flow | welcome-email |
| Exception flow | global-exception-flow |
| Intent rephrase flow | rephrase-flow-email-handling |

3. Turn on the **Use Knowledge Base** toggle.
4. Save the configuration.

<a id="Step4Configureappconnections"></a>

### Step 4. Configure app connections

Go to solution Apps and configure the connections with your credentials. After you configure them, click **Publish**.

| App | Description | Your details |
| --- | --- | --- |
| SendGrid | Sends email responses. | API Key or SMTP connection |
| DRUID-SLM\_Becus 1.0 | LLM processing using DRUID-dedicated model. | Claims and token from Druid Services |
| Druid GPT | LLM processing using Open AI model. | Claims and token from Druid Services |
| Azure Blob Storage | Stores attachments. | Account Name and Account Key |
| KB-REST | Adds answers to Knowledge Base | The username and password of a Druid user account. In the Base URL field, enter the url specific to your environment:  - Community: \*.community.druidplatform.com/api - Production West Europe: \*.druidplatform.com/api - Production US: \*.us.druidplatform.com/api - Production Australia: \*.au.druidplatform.com/api |
| DRUID-Translator | Translates PDFs and attachments to AI Agent default language. | Druid support must enable **TranslatePdf** permission; retrieve the auth key from Druid Services and enter in app variable. |

<a id="Step5PreparethestandardanswerKnowledgeBase"></a>

### Step 5. Prepare the standard answer Knowledge Base

1. Navigate to **NLU** > **Knowledge Base**.
2. Click the **Add new** button.
3. Enter the data source **Name** exactly as: "Ticket Management Standard KB".
4. Choose **Structured Documents** as the data source **Type**.
5. Upload the [sample Excel file](<https://druiddocs.file.core.windows.net/docs-shares/PDF/sample excel file.xlsx?sv=2025-07-05&spr=https&st=2025-10-06T09%3A01%3A14Z&se=2030-10-07T09%3A01%3A00Z&sr=f&sp=r&sig=%2F2mWeE4mYeOUVb15T5o85PgHrpsCzN%2FL7Y1gxOCx4Qo%3D>) or your own set of standard answers.
6. Set the **Min score threshold** to **30** and **Target match score** to **60**.
7. Click **Create**, then **Extract**, and finally **Train** the new data source.

Once training is complete, the Knowledge Base is ready to deliver standard responses for various types of case requests.

<a id="Step6Runsetupflow"></a>

### Step 6. Run setup flow

Open a new web chat with the AI Agent. This will trigger the database setup workflow automatically, adding all necessary LLM prompts and demo data to the operational database.

Confirm that Email Cases view and admin records are created.

<a id="Step7ConfigureNLUIntentClassificationwithLLM"></a>

### Step 7. Configure NLU Intent Classification with LLM

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **Classification Model Type**.
3. Set **Endpoint Type** to **Druid**. If you’re using your own LLM resource, select your resource instead. Then choose the **Model Name**.
4. Click **Set default** for both prompts to automatically fill in instructions.
5. Save and train the AI Agent.

<a id="Step8ConfigureLLMModelConnectors"></a>

### Step 8. Configure LLM Model Connectors

> **NOTE:** This is a mandatory step to link the LLM models to their respective integration connectors.

Navigate to **Integrations** to find the provisioned connectors for Druid Becus and GPT-4o mini.

For each integration, copy its unique Connector action ID.

![A screenshot of a computer AI-generated content may be incorrect.](../../../../Resources/Images/Ticketron%20Final/DRUID%20LLM%20Case%20Management_3.png)

Select the **Email Admin** workspace and on the workspace menu, click **LLM Models**.

![A white background with black text AI-generated content may be incorrect.](../../../../Resources/Images/Ticketron%20Final/email%20llm%20models.png)

For each LLM record (Becus and GPT-4o mini), paste the corresponding Connector action IDs into the following fields:

![A screenshot of a computer AI-generated content may be incorrect.](../../../../Resources/Images/Ticketron%20Final/DRUID%20LLM%20Case%20Management_5.png)

For Becus:

- **AgentConnectorId**: Paste the ID from the **DRUID-SLM-agent-run** integration.
- **GenericLlmConnectorId**: Paste the ID from the **DRUID-SLM-generic-connector** integration.
- **KBResponseConnectorId**: Paste the ID from the **DRUID-SLM-KB-response** integration.

For GPT-4o mini:

- **AgentConnectorId**: Paste the ID from the **gpt-agent-run** integration.
- **GenericLlmConnectorId**: Paste the ID from the **GPT-generic-connector** integration.
- **KBResponseConnectorId**: Paste the ID from the **GPT-provide-KB-response** integration.

<a id="Step9SelecttheActiveLLM"></a>

### Step 9. Select the Active LLM

The solution uses a ModelSwitch variable to determine which LLM is active. By default, it is set to **GPT-4o mini**. To change it:

1. From the **Email Admin** workspace menu, select **Model Switch**.

![](../../../../Resources/Images/agentic%20email%20ghandl/model%20switch.png)

2. In the **Model Switch** view, click on the **Current value** record. The Current Value form opens.
3. From the **SelectedModel** field, select the desired LLM (e.g., Becus).

![](../../../../Resources/Images/agentic%20email%20ghandl/model%20swith%20current%20value.png)

4. Click the **Save & close** icon at the top-right corner of the page.

<a id="Step10AssociateDruidUserswithHelpdeskRoles"></a>

### Step 10. Associate Druid Users with Helpdesk Roles

For a helpdesk agent / manager to access the **Helpdesk Dashboard** workspace and all its functionality, their Druid Portal account must be linked to a corresponding helpdesk agent / manager profile within the solution:

1. Select the **Helpdesk Dashboard** workspace.
2. On the workspace menu, click **Helpdesk Agents**.
3. Create an agent record using the same email address as the person's Druid Portal login.

![](../../../../Resources/Images/agentic%20email%20ghandl/agent%20record.png)

4. Go to **Administration** > **Users**.
5. Search for the agent you added in the solution and click to edit the profile.
6. Click the **Roles** tab and assign the necessary platform roles to the Druid user account:

- **Helpdesk Agent**. Assign this role for standard agent access (views for Cases and Contacts).
- **Helpdesk Manager**. Assign this role for full administrative access (views for Reporting, Cases, Contacts, Agents, and Queues).

![A white background with black text AI-generated content may be incorrect.](../../../../Resources/Images/agentic%20email%20ghandl/roles.png)

7. Save the user profile.

The user can now log in to the workspace with the permissions defined by their assigned role.

<a id="RunningtheSolution"></a>

## Running the Solution

To create the first email case:

1. Send an email to the configured Email Channel address.
2. Include details and optionally attach files (images, PDFs).

**Example Email (for demonstration only)**

```
Hello,
My Wi-Fi is acting strangely and I cannot connect at all.
Could you please help?
I have attached an image showing the issue and a log file.
Thank you,
Alex
                
```

3. The AI Agent automatically:

- Detects language
- Classifies category, status, priority, SLA
- Translates attachments and email content
- Extracts parameters
- Generates a KB suggestion if available

4. In the **Email Case** view and forms the agent will be able to find:

- Original Email and attachments
- Translated Email and attachments
- Collected parameter
- Case description with all extracted info, missing parameters, and history

5. Agents can review, reply, or close the case. Responses are automatically translated to the user’s language.
