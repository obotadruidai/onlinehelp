---
title: "Set Up the Retail Solution (for solution admins)"
---

<a id="SetUptheRetailSolutionforsolutionadmins"></a>


This section will walk you through the steps to import and configure the solution to ensure a smooth setup and operation.

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have an AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../../2_AI%20Agents/Creating%20AI%20Agents.md).
- API resources enabled for Druid WebView and Druid Data Service.
- Druid LLM API resources activated for **Becus 1.0** and **GPT-4.1**. Contact your Druid sales representative to enable these resources and generate API tokens.
- Azure subscription credentials for the Blob Storage service to enable image upload in the claim process.

<a id="Installationandsetupprocedure"></a>

## Installation and setup procedure

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution "Retail Agentic Solution" and import it following the instructions provided in section [Installing Solution Templates](../../Installing%20Solution%20Templates.md).

Wait until the import status shows as “Success”.

<a id="Step2Configureappconnections"></a>

### Step 2. Configure app connections

Navigate to **Solution Contents** > **Apps** and configure the apps as follows:

| App | Description | Connection Details | Mandatory |
| --- | --- | --- | --- |
| Druid-SLM\_Becus 1.0 | Used for anonymization of PII. | Enter only the key the Variables tab. Take the key value from **Administration** > **Druid Services**. | Yes |
| GPT 4.1 | Used for conversational orchestration. | If provisioned via Druid Service Gateway, enter only the key the Variables tab. Take the key value from **Administration** > **Druid Services**.  If you're using your own LLM resources, configure the details. | Yes |
| Gemini | Used for image preview. | Enter your API key in the Variables tab. | Yes - for image preview only |
| AzureStorage | Used for file storage. | Enter your Account Name and Account Key for claim images.  If you use this app, tap the **Use HTTPS** toggle.  ![](../../../Resources/Images/Retail/azure%20app%20config.png) | Yes - for file storage |
| SendGrid App Rest | Used for all the emails that are sent in the environment. | Enter your Azure subscription details: **Account Name** and **Account Key**. | Yes |

Click **Publish** to make the apps available.

<a id="Step3SetuptheAIAgentspecialflowsandoptionallytheAbandonedCart"></a>

### <a id="Step"></a>Step 3. Set up the AI Agent special flows and optionally the Abandoned Cart

Go to the AI Agent details page and configure the following special flows:

| Special flow | Value | Mandatory |
| --- | --- | --- |
| Welcome flow | first-welcome-flow  **Info:** When a chat starts, this flow initializes the retail demo database. | Yes |
| Intent not found flow | switch-intent | Yes |
| Inactivity End Conversation flow | create-draft-order | No. Only if you will activate the Abandoned Cart Automation, that automatically converts abandoned carts into draft orders for reporting. |
| Conversation Timeout (in minutes) | Define inactivity duration (e.g., 20 minutes) that triggers the Inactivity End Conversation flow.  At runtime, when the configured inactivity period is reached:   - **If the user still has the AI Agent open and items in the cart:**  - The AI Agent asks if the user wants to continue with the cart. - If the user selects Yes, no order is created. - If the user selects No, an order is created with Abandoned status for reporting.  - **If the user no longer has the AI Agent open:**  - The AI Agent automatically creates an order with the cart contents in Draft status. - When the user later logs in or searches for a product:  - If they choose to keep the cart, the current cart is replaced by the draft order (and the draft is deleted). - If they choose not to keep it, the cart is cleared and the draft order is marked as Abandoned.   This ensures abandoned carts are properly tracked and reported, giving you actionable insights to recover potential lost sales. | Yes only if you will activate the Abandoned Cart Automation. |

Save the AI Agent configuration.

<a id="Step4ConfigureNLUIntentsClassificationwithLLM"></a>

### Step 4. Configure NLU Intents Classification with LLM

To configure NLU intents classification with LLM, follow these steps:

1. Navigate to **NLU** > **Configurations** > **Intents** tab.
2. Click on **Thresholds and parameters**.
3. Add the **NLU.NER.Classification.ModelType** parameter and set it to **LLM**.

![](../../../Resources/Images/druid%208.10/nlu%20with%20llm.png)

Click the link that appears in the message below the NLP parameters. The NLU Intents Classification with LLM expands.

![](../../../Resources/Images/NLU%20with%20llm/set%20nlu%20with%20llm.png)

4. From the **Endpoint Type** field, select **Druid**.
5. From the **Model Name** field, select **GPT 4.1**.
6. For both prompts, click the **Set default** button. The default Druid prompts will be automatically filled in.
7. Click **Save** at the bottom of the page to apply the NLU configuration.
8. Train the AI Agent.

<a id="Step5Provisionthedata"></a>

### Step 5. Provision the data

To provision all the required information for the AI Agent, follow these steps:

1. Select the **Admin** workspace.
2. Click **RetailSettings** on the workspace menu.
3. Click the **Provision Data** button.

![](../../../Resources/Images/Retail/provision%20data.png)

The default settings include a predefined set of values and records. You can extend the configuration at any time by manually adding new data records.

<a id="Step6ConfigureAdvancedSettingsAnonymizationImagePreviewandAttachmentStorageoptional"></a>

### Step 6. Configure Advanced Settings: Anonymization, Image Preview, and Attachment Storage (optional)

#### Data Anonymization

The **Data Anonymization** feature adds a privacy layer between your users and any external AI services. When enabled, it automatically detects and redacts personally identifiable information (PII) — such as names, email addresses, and phone numbers — from user input before it is sent to a large language model (LLM). This is powered by Becus 1.0 and ensures that no identifiable data ever reaches an external AI context.

{% hint style="info" %}
**Info:** Use this feature if your environment handles sensitive customer data and you need to comply with data privacy regulations or internal security policies.
{% endhint %}

#### AI-Generated Visuals

The Image Preview feature allows users to visualize how a product would look in their own environment while browsing. For example, a user can see how a book would appear sitting on their desk. The preview is generated by Gemini, which composites a realistic image of the product into the user's defined context.

{% hint style="info" %}
**Info:** Use this feature if you want to offer a visual shopping experience.
{% endhint %}

#### Azure Attachment Storage

The **Save Attachments Azure** setting determines where the solution stores images and files uploaded by users (for example, during a claim process).

#### How to activate

1. Select the **Admin** workspace.
2. Click **RetailSettings** on the workspace menu.
3. Click the **Current Value** record to open it.
4. On the settings form:

- Toggle **Data Anonymization** on to enable PII redaction before LLM transmission.
- Toggle **Image Preview** on to enable AI-generated product previews.
- Toggle **Save Attachments Azure** on if you wish to use Azure Blob Storage for user attachments. If set to false, this functionality is disabled.

![](../../../Resources/Images/Retail/data%20anonym.png)

5. Click **Save**.

{% hint style="info" %}
**Info:** You can enable either feature independently or both together.
{% endhint %}

<a id="AdditionalSetupforKnowledgeBaseandLiveChat"></a>

## Additional Setup for Knowledge Base and Live Chat

The current solution version does not include preconfigured Knowledge Base (KB) or Live Chat functionality.

Within the **switch-intent** flow, two conversation paths are already defined, but are not implemented by default and remain currently inactive:

- Knowledge Base support
- Live Chat escalation

![](../../../Resources/Images/Retail/SWITHC%20INTENT%20KB.png)

To enable these capabilities, you must configure them manually. Two approaches are available:

<a id="RecommendedApproach"></a>

### Recommended Approach

1. Import [Knowledge Base](../../Knowledge%20Base/Knowledgebase%20with%20GPT%20V4.md) and/or [Live Chat Advanced](../../Live%20Chat%20Advanced.md) solutions from the Solutions Library and set them up.
2. Use the flows provided by those solutions.
3. Reference or connect those flows directly from the **switch-intent** flow (using the trigger flow functionality).

<a id="AlternativeApproach"></a>

### Alternative Approach

1. Build and configure your own flows for KB search or Live Chat escalation.
2. Use the custom flows in the existing placeholder paths in the **switch-intent** flow using the trigger flow functionality.

Until configured, these branches remain empty placeholders and are not triggered during conversations.

<a id="RunningtheSolution"></a>

## Running the Solution

Start a conversation with the assistant. Examples:

- “I’m in the mood for reading, what book do you recommend?”
- “I want to search for a product and I have an image” (upload an image).
- “I want to file a claim” (where the user has the option to add files).
