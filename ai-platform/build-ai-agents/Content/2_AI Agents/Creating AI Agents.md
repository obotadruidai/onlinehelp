---
title: Creating AI Agents
---


Welcome to the process of building your first AI Agent! This guide provides the essential, step-by-step instructions needed to go from an initial setup to a fully published conversational AI Agent with foundational conversational flows.

## Step 1: Set up and name your AI Agent

1. Log in to your Druid tenant.
2. In the header, click on AI Agent and select **Create AI Agent**.

![](<../../.gitbook/assets/create new bot.png>)

3. In the **Create New AI Agent** modal:

* Enter a unique name for your AI Agent in the **Name** field.

**NOTE:** Names must be unique within your tenant. If a name is already in use, the creation process will fail.

* Choose the **Default Language** for the AI Agent.

![](<../../.gitbook/assets/cerate bot.png>)

To ensure the integrity of your AI Agent configuration, once an AI Agent initial configuration is saved, the default language becomes read-only. Introduced in Druid 9.19, this restriction prevents accidental changes that could break existing flows, intent recognition, or language-specific entity configurations.

{% hint style="info" %}
**Info:** Always verify the primary language of your AI Agent during the initial creation process. If a different default language is required for a new project, a new AI Agent must be created.
{% endhint %}

4. Click **Save**. The page refreshes, opening the AI Agent settings on the **Details** tab.

![](<../../.gitbook/assets/bot details page.png>)

## Step 2: Configure the AI Agent appearance

On the settings page (**Details** tab), configure the AI Agent appearance:

1. Click the **Theme** section header.
2. Enter an image URL in the **Avatar image URL** field to set your AI Agent avatar.
3. For advanced configuration, click **Customize webchat** and configure the desired web chat settings. For more information, see [WebChat Common Styling and Behavior (Bot framework v4)](https://druidai.gitbook.io/druid-ai-docs/channels/web-and-email/webchat/webchat_common_styling_and_behavior_v4).

![](<../../.gitbook/assets/default theme.png>)

4. Click **Save** at the bottom of the page to apply these settings.

## Step 3: Select user roles

AI Agents interact only with users who are assigned specific security roles. Define which roles can access the AI Agent.

1. Click the **Security** tab.
2. Click the **Used by** section header.
3. Verify the default **Admin** and **User** roles are checked to allow all authenticated and unauthenticated users to interact with the AI Agent.
4. Select any additional roles based on your target audience.

![](<../../.gitbook/assets/bot roles.png>)

5. Click **Save**.

## Step 4: Publish the AI Agent

Publishing the AI Agent is essential to make it functional and provision all the required resources in your Druid environment.

1. Click the **Details** tab.
2. Click the **Publish** button at the bottom of the page.

{% hint style="warning" %}
**IMPORTANT!** AI Agent publishing can take up to a minute. You can continue creating solutions and other configurations, but you can only chat with the AI Agent after it is successfully published.
{% endhint %}

3. After clicking **Publish**, a notification appears at the top of the page: “Request for provisioning was successfully sent!”. Monitor the AI Agent provisioning status using the following color indicators:

* Orange: The request is in progress.
* Green: The request has been successfully completed.

![](<../../.gitbook/assets/bot published.png>)

* Red: The process has failed. If the publishing fails, please contact the [DRUID Technical Team](../2_AI%20Agents/mailto:support@druidai.com).

4. After publishing, you can test the AI Agent. Open the chat bubble on the right side and type your messages.

{% hint style="info" %}
**NOTE:** The newly created AI Agent currently lacks conversation flows, so it will respond with "Sorry, I don’t understand". You need to create / import a solution.
{% endhint %}

## Step 5: Import Druid Starter solution

After publishing, the AI Agent lacks conversation flows. Import the Druid Starter solution to give your AI Agent foundational intelligence.

1. On the header, click the **Solution** dropdown, and then select **Import solution**.
2. In the Solution Library, search for **DRUID Starter** and import the solution. The solution includes definitions of system entities and common flows.

![](<../../.gitbook/assets/IMPORT STARTER.png>)

3. Navigate back to the AI Agent settings page and click the **Dialogue management** section header.
4. Select the imported flows from the **Welcome flow** dropdown and the **Intent not found flow** dropdown.

![](<../../.gitbook/assets/dialogue management.png>)

5. Click **Save** at the bottom of the page to save the AI Agent configuration.

## Related Topics

* [AI Agent Authoring Privileges via RBAC Policy](https://druidai.gitbook.io/druid-ai-docs/ai-governance-and-security/data-security-and-privacy/authoring-user-management/ai-agent-authoring-privileges-via)
* [Configuring AI Agent Shortcut Keys](<Configuring AI Agent Shortcut Keys.md>)
* [Creating Authoring Users (Portal Users)](https://druidai.gitbook.io/druid-ai-docs/ai-governance-and-security/data-security-and-privacy/authoring-user-management/creating-authoring-users)
