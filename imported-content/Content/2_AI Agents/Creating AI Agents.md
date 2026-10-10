---
title: "Creating AI Agents"
---

<a id="CreatingAIAgents"></a>


Welcome to the process of building your first AI Agent! This guide provides the essential, step-by-step instructions needed to go from an initial setup to a fully published conversational AI Agent with foundational conversational flows.

<a id="Step1SetupandnameyourAIAgent"></a>

## Step 1: Set up and name your AI Agent

1. Log in to your Druid tenant.
2. In the header, click on AI Agent and select **Create AI Agent**.

![](../Resources/Images/Bots/create%20new%20bot.png)

3. In the **Create New AI Agent** modal:

- Enter a unique name for your AI Agent in the **Name** field.

**NOTE:** Names must be unique within your tenant. If a name is already in use, the creation process will fail.

- Choose the **Default Language** for the AI Agent.

![](../Resources/Images/Bots/cerate%20bot.png)

To ensure the integrity of your AI Agent configuration, once an AI Agent initial configuration is saved, the default language becomes read-only. Introduced in Druid 9.19, this restriction prevents accidental changes that could break existing flows, intent recognition, or language-specific entity configurations.

> **Info:** Always verify the primary language of your AI Agent during the initial creation process. If a different default language is required for a new project, a new AI Agent must be created.

4. Click **Save**. The page refreshes, opening the AI Agent settings on the **Details** tab.

![](../Resources/Images/Bots/bot%20details%20page.png)

<a id="Step2ConfiguretheAIAgentappearance"></a>

## Step 2: Configure the AI Agent appearance

On the settings page (**Details** tab), configure the AI Agent appearance:

1. Click the **Theme** section header.
2. Enter an image URL in the **Avatar image URL** field to set your AI Agent avatar.
3. For advanced configuration, click **Customize webchat** and configure the desired web chat settings. For more information, see [WebChat Common Styling and Behavior (Bot framework v4)](../Channels/WebChat/WebChat_Common_Styling_and_Behavior_v4.md).

![](../Resources/Images/Bots/default%20theme.png)

4. Click **Save** at the bottom of the page to apply these settings.

<a id="Step3Selectuserroles"></a>

## Step 3: Select user roles

AI Agents interact only with users who are assigned specific security roles. Define which roles can access the AI Agent.

1. Click the **Security** tab.
2. Click the **Used by** section header.
3. Verify the default **Admin** and **User** roles are checked to allow all authenticated and unauthenticated users to interact with the AI Agent.
4. Select any additional roles based on your target audience.

![](../Resources/Images/Bots/bot%20roles.png)

5. Click **Save**.

<a id="Step4PublishtheAIAgent"></a>

## Step 4: Publish the AI Agent

Publishing the AI Agent is essential to make it functional and provision all the required resources in your Druid environment.

1. Click the **Details** tab.
2. Click the **Publish** button at the bottom of the page.
> **IMPORTANT!** AI Agent publishing can take up to a minute. You can continue creating solutions and other configurations, but you can only chat with the AI Agent after it is successfully published.

3. After clicking **Publish**, a notification appears at the top of the page: “Request for provisioning was successfully sent!”. Monitor the AI Agent provisioning status using the following color indicators:

- Orange: The request is in progress.
- Green: The request has been successfully completed.

![](../Resources/Images/Bots/bot%20published.png)

- Red: The process has failed. If the publishing fails, please contact the [DRUID Technical Team](<mailto:support@druidai.com?subject=My bot publishing has failed>).

4. After publishing, you can test the AI Agent. Open the chat bubble on the right side and type your messages.

> **NOTE:** The newly created AI Agent currently lacks conversation flows, so it will respond with "Sorry, I don’t understand". You need to create / import a solution.

<a id="Step5ImportDruidStartersolution"></a>

## Step 5: Import Druid Starter solution

After publishing, the AI Agent lacks conversation flows. Import the Druid Starter solution to give your AI Agent foundational intelligence.

1. On the header, click the **Solution** dropdown, and then select **Import solution**.
2. In the Solution Library, search for **DRUID Starter** and import the solution. The solution includes definitions of system entities and common flows.

![](../Resources/Images/Bots/IMPORT%20STARTER.png)

3. Navigate back to the AI Agent settings page and click the **Dialogue management** section header.
4. Select the imported flows from the **Welcome flow** dropdown and the **Intent not found flow** dropdown.

![](../Resources/Images/Bots/dialogue%20management.png)

5. Click **Save** at the bottom of the page to save the AI Agent configuration.

## Related Topics

- [AI Agent Authoring Privileges via RBAC Policy](../Governance%20%26%20Security/User%20Management/AI%20Agent%20Authoring%20Privileges%20via.md)
- [Configuring AI Agent Shortcut Keys](Configuring%20AI%20Agent%20Shortcut%20Keys.md)
- [Creating Authoring Users (Portal Users)](../Governance%20%26%20Security/User%20Management/Creating%20Authoring%20Users.md)
