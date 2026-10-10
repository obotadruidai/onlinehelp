<a id="Raffle"></a>

# Raffle

This solution helps with organizing a raffle by allowing participants to register only one time each and extracting one or multiple winners.

The participants will join from a custom page where the AI Agent is hosted and the extraction will be done from the workspace area by an admin user.

This solution template provides a wide range of capabilities:

| Functionality | Target audience | Description |
| --- | --- | --- |
| Register contestant | The participants that want to join the raffle | This flow allows a participant to join the raffle by providing first name, last name and company name. They will be allowed only one entry per participant. |
| Pick a winner | The raffle organizer | This flow allows the raffle organizer to pick one or multiple winners from the contestant list based on their unique index.  After a contestant is selected, he is marked as a winner and won’t be selected in future draws. |
| Generate report | The raffle organizer | You are able to generate an excel report with all the contestants that joined the raffle. Can be done from the Contestant workspace. |
| Format contestant list | The raffle organizer | In case the index for each contestant was generated incorrectly or one/multiple contestants have been selected as winners by accident, this flow serves as a backup solution that will assign new indexes for each contestant and reset their win status.  To be used before starting the raffle extraction. |

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../2_AI%20Agents/Creating%20AI%20Agents.md).
- Enable the API Resources for Druid WebView and Druid Data Service. Then, activate the Druid Data Service in your tenant by navigating to Administration > Settings > Druid Data Service, and selecting Is enabled and clicking the Save all button at the top right of the page.
- Have the DRUID Starter solution imported.

<a id="ConfiguringtheSolutionTemplate"></a>

## Configuring the Solution Template

To configure the solution template, follow these steps:

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution Raffle and import it following the instructions provided in section [Installing Solution Templates](Installing%20Solution%20Templates.md).

Wait until the import status shows as “Success.”

Once the import is successful, click **Save & Close**.

<a id="Step2SetuptheAIAgentspecialflows"></a>

### Step 2. Set up the AI Agent special flows

Go to the AI Agent settings, Details page and click the Dialog management section header. The section expands. Select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome flow | welcomeFlow |
| Intent not found flow | IntentNotRecognizedV2 |

Scroll down and click **Save & Close**.

<a id="Step3Changespecialmessages"></a>

### Step 3. Change special messages

Go to Dialogue Management – Special Messages and change the **InactivityCancelConversation** message to *“Due to inactivity, this conversation has ended. To continue picking winners, say "Pick a winner".”*

<a id="Step4TrainyourAIAgent"></a>

### Step 4. Train your AI Agent

From the **NLU** menu, click **Configurations** and then click the **Intents** tab. Click the **Train** button.

<a id="Step5Settheindexcounter"></a>

### Step 5. Set the index counter

Each participant will get an index when registering for the raffle.

To start the index from 0, before the event begins, go to **Contestants workspace – RaffleHelper** and set the **Counter – Index generator** to **0**.

<a id="Step6DeploytheAIAgentonacustomwebpage"></a>

### Step 6. Deploy the AI Agent on a custom web page

To separate the functionality, deploy the AI Agent on a custom web page where the users can register. Since they only have the “user” role, they will not have access to admin flows.

> **NOTE:** The admin functionality is performed in the Contestants workspace. Ensure that you have both the admin and raffle admin roles assigned.

<a id="SeetheAIAgentinaction"></a>

## See the AI Agent in action

The list below provides you with an extensive list of things you can say to the AI Agent in English.

| Functionality | Intent (EN) |
| --- | --- |
| Pick a winner (raffle admin only, use it from Chat workspace) | Pick a winner / I want to pick a winner |
| Register contestant | I want to join the raffle  How to join the raffle  I want to register |
| Generate report (raffle admin only) | GenerateReport  **NOTE:** The GenerateReport functionality must be initiated from the Contestant view, not from the chat. |
| Format contestant list (raffle admin only) | FormatContestantList  **NOTE:** The FormatContestantList functionality must be initiated from the Contestant view, not from the chat. |
