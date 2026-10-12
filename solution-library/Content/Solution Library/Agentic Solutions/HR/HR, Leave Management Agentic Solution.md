---
title: "HR, Leave Management Agentic Solution"
---

<a id="HRLeaveManagementAgenticSolution"></a>


The **HR, Leave Management Agentic Solution** is a pre-built AI Agent designed to manage common HR processes, primarily focusing on employee leave. It is built on DRUID’s proprietary Agentic framework and is compatible with external models such as GPT-4. This solution enables users to create and manage leave requests through natural, conversational interactions.

<a id="FeaturesandKeyComponents"></a>

## Features and Key Components

This core solution provides the following functionality:

- **Business Workflows**:

- **Leave Request Management**: Manages the full lifecycle of employee leave and vacation requests, including submission, backend validation, and request cancellation (if not yet approved).
- **Vacation Sharing**: Allows employees to configure a team of colleagues who can view their vacation information.
- **Manager Actions**: Managers can check team members' leave requests by period and approve or reject vacation requests.
- **HR Partner Actions**: HR Partners can approve or reject leave requests for employees within the company.
- **Authentication**: Supports user authentication for both Teams and web channels.
- **Small Talk**: Includes support for informal conversations.
- **Multilingual Support**: The AI Agent can respond to user queries in any language.
- **Data Synchronization**: Automates synchronizing Employee data and Vacation Balances from external systems (e.g., Workday, Bamboo).
- **Reports**: Enables exporting Leave Request data.

- **Settings Workflows**:

- **Setup Flow**: Automatically provisions the business database with demo data, such as National Holidays, Metro Cities, Leave Request Statuses, etc.

- **Data and Access**:

- **Data Model**: Contains the essential entities required for the solution's core functionalities.
- **Workspaces**: Includes two workspaces that allow access to the back-end database:

- **Admin Workspace**: Used for setting up and managing data lists (e.g., holiday calendars, cities, roles).
- **Business Workspace**: Provides a Manager View to access and manage employee information and leave request data.

- **Integrations**: Includes all necessary LLM and Druid Data Service integrations.

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/creating-ai-agents).

<a id="ConfiguringtheSkillTemplate"></a>

## Configuring the Skill Template

To configure the skill template, follow these steps:

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution "HR, Leave Management Agentic Solution" and import it following the instructions provided in section [Installing Solution Templates](../../Installing%20Solution%20Templates.md).

Wait until the import status shows as “Success”.

Once the import is successful, click **Save & Close**.

<a id="Step2Configuretheappconnection"></a>

### Step 2. Configure the app connection

To configure the app connection, follow these steps:

1. Go to **Solution Content** > **Apps** and configure the connections with your credentials.

| App | Description | Your details |
| --- | --- | --- |
| Druid-LLM 4.1 | Used for external LLM processing. | This app is provisioned by DRUID. Get the claims and token from Administration > Druid Services. |
| Druid-LLM 4o mini | Used for external LLM processing. | This app is provisioned by DRUID. Get the claims and token from Administration > Druid Services. |

{% hint style="info" %}
**NOTE:** If the DRUID.LLM resource does not appear, contact your sales representative to activate these resources.
{% endhint %}

2. Click **Save** to complete the configuration.
3. Once the app is configured, click **Publish**.

<a id="Step3Runsetupflow"></a>

### Step 3. Run setup flow

Open the AI Agent and type in the chat "ds-setup" to run the flow that loads demo data to the HR DataService backend.

<a id="Step4SetuptheAIAgent"></a>

### Step 4. Set up the AI Agent

1. Go to the AI Agent details page, and in the Languages section, select the default language. Only one language is necessary, since the AI Agent will answer in any user language.
2. Click on the Dialogue management section and set the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome | hr-welcome |
| Intend not found flow | small-talk-other-replies |
| Authentication flow | email-authentication-agent |

3. Click the **Save** button at the bottom of the page.
4. Click on the **Roles** tab and assign the needed user roles to the AI Agent: User, Admin, Employee, Manager and HR Partner.
5. Click the **Save & Close** button at the bottom of the page.

<a id="Step5ConfigureNLUIntentClassificationwithLLM"></a>

### Step 5. Configure NLU Intent Classification with LLM

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **Classification Model Type**.
3. Set the **Model Type** field to **Llm**.
4. Set **Endpoint Type** to **Druid**. If you’re using your own LLM resource, select your resource instead. Then choose the **Model Name**.
5. Set the **Api Type** to **Chat Completions (Legacy)**.
6. Click **Set default** for both prompts to automatically fill in instructions.
7. Save and train the AI Agent.

<a id="TheAIAgentatruntime"></a>

## The AI Agent at runtime

Access the AI Agent directly from the **Land AI Agent** page inside the Druid Portal or through the **Teams** channel. If the AI Agent is published in Teams, see [MS Teams Integration](https://druidai.gitbook.io/druid-ai-docs/channels/social-media-and-chat/ms-teams-integration) for guidance.

When a user first accesses the AI Agent, the **Authentication flow** automatically triggers. This flow links the user's email address to the corresponding Employee entry in the Employee business table. After successful authentication, the user can start submitting leave requests and asking questions.
