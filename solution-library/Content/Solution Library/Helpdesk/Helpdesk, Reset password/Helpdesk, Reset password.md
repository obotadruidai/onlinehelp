---
title: Helpdesk, Reset password
---


This solution template enables your AI Agent to assist users resetting their password on request.

## Prerequisites

* Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
* You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/creating-ai-agents).
* UiPath Orchestrator subscription, Community or Enterprise edition.

## Setting up the solution template

### Step 1. Install the solution from the Solutions Library

For information on how to install the solution, see [Installing Solution Templates](<../../Installing Solution Templates.md>).

### Step 2. Download the UiPath process

[!\[\](../../../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/reset-password-helpdesk.1.0.1.nupkg?st=2022-04-05T03%3A50%3A51Z\&se=2026-04-06T03%3A50%3A00Z\&sp=rl\&sv=2018-03-28\&sr=f\&sig=OJVl%2Fs2z%2BCVJGiTNb0dwX%2FOCIukVOtJ4vDNGHulOJLs%3D)

### Step 3. Publish the UiPath process

Go to the UiPath Orchestrator, create a new modern folder and add the UiPath Process.

Click **Publish** to publish the process in your orchestrator.

### Step 4: Set up Druid

1. In Druid, go to **Apps**, search for UiPath Process and configure the connection string to your orchestrator following the procedure described in [Creating the UiPath Connection Strings](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/uipath-connector/creating-the-uipath-connection-strings).
2. Go to the Flows, search for the **reset-password** flow and open it in diagram view. You can use this flow to trigger both attended and unattended UiPath process.
3. For both attended and unattended technology, map the Process input/output parameters to Druid entity fields as follows:

**IN**: EmailAddress --> **\[\[Client]]. EmailAddress**

**OUT**: Status --> **\[\[Client]].Status**.

For more information on how to set up thee flow, see [Starting UiPath Unattended](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/uipath-connector/starting-uipath-unattended), Step 3 from substep (5) onwards.

![](<../../../../.gitbook/assets/reset pass process.png>)

4. Open the AI Agent and type in the chat one the following phrase:

| English (EN)                | Romanian (RO)               |
| --------------------------- | --------------------------- |
| I need to reset my password | Vreau sa imi resetez parola |

## Related Topics

* [Starting UiPath Unattended Processes](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/uipath-connector/starting-uipath-unattended)
