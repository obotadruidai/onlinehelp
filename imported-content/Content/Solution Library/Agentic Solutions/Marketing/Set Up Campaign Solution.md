---
layout:
  title:
    visible: false
---

<a id="SetUptheSolution"></a>

# Set Up the Solution

This section will walk you through the steps to import and configure the solution to ensure a smooth setup and operation.

<a id="MandatoryPrerequisites"></a>

## Mandatory Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a published AI Agent. For information on how to create an AI Agent, see   [Creating AI Agents](../../../2_AI%20Agents/Creating%20AI%20Agents.md).
- A dedicated web page that hosts the WebChat snippet for the Direct Line channel.

<a id="OptionalPrerequisites"></a>

## Optional Prerequisites

- The Twilio SMS channel configured for your AI Agent. For setup instructions, see [Twilio SMS](../../../Channels/Twillio/TwilioSMS_Channel.md).
- The Audiocodes channel configured for your AI Agent. For setup instructions, see [Voice AudioCodes Channel](../../../Channels/Voice%20Audio%20Codes/Voice%20Audio%20Codes%20Channel.md).
- The Vonage WhatsApp channel configured for your AI Agent. For setup instructions, see [WhatsApp Integration](../../../Channels/WhatsApp%20Integration/WhatsApp%20Integration.md).

<a id="Installationandsetupprocedure"></a>

## Installation and setup procedure

To configure the solution, follow these steps:

<a id="Step1Installthesolution"></a>

### Step 1. Install the solution

Go to the Solutions Library, search for solution **Campaign Management Agentic Solution** and import it following the instructions provided in section [Installing Solution Templates](../../Installing%20Solution%20Templates.md).

Wait until the import status shows as “Success”.

<a id="Step2SetuptheAIAgentspecialflows"></a>

### Step 2. Set up the AI Agent special flows

Go to the AI Agent settings, Details page and click on **Dialog management**. The section expands. Select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome flow | check-initial-setup |
| Intent not found flow | System\_Intent not recognized |
| Intent rephrase flow | intent-rephrase |
| Inactivity end conversation flow | - **deliver-campaign-message** - Mandatory for Marketing Campaigns. - **early-termination-flow** - Mandatory for Survey Campaigns that a user did not complete, across channels such as SMS and Direct Line. |
| Voice call terminate flow | early-termination-flow |

Scroll down and click **Save & Close**.

<a id="Step3Configuretheappconnections"></a>

### Step 3. Configure the app connections

Go to solution **Apps** and configure the following connections with your credentials:

| App | Description | Setup required |
| --- | --- | --- |
| Audiocodes | Enables automated outbound voice calling through AudioCodes integration.  Configure the following variables in the Variables table:   - **key**- AudioCodes API token. - **agentName**- The name the AI agent uses to introduce and identify itself to callers. - **audiocodesPhoneNumber**- The phone number from AudioCodes associated with your AI Agent. - **audiocodesBotId**- The Bot ID provided by AudioCodes. - **callbackConnectorId**- The**Connector action id** retrieved from the **synchronize-outbound-call-status-webhook** integration (**Solution Contents** > **Integrations**).  ![](../../../Resources/Images/Campaign%20Management/connector%20action%20id.png) - **tenantSecret** - Organization secret key retrieved from Druid Services (**Administration** > **Druid Services**).  ![](../../../Resources/Images/Campaign%20Management/tenant%20secret.png)   For information on how to configure the Audiocodes channel, see [Voice AudioCodes Channel](../../../Channels/Voice%20Audio%20Codes/Voice%20Audio%20Codes%20Channel.md). | Optional |
| Druid-LLM 4.1 | Configure this app using one of the following options:   - **Druid-dedicated LLM resources**. Retrieve the required details from **Administration** > **Druid Services**.  **NOTE:**  If the DRUID.LLM resource does not appear, contact your sales representative to activate Druid-dedicated resources for one of the following providers on your tenant: Azure OpenAI, Mistral, or Google. - **Custom LLM**. Connect the app to your own LLM deployment provided by Microsoft Azure, OpenAI, or another provider that supports tools or function calling. | Mandatory |
| Druid\_Sendgrid | Used to send emails to users. Enter the **SendGrid API key**. | Mandatory for the Web and Email channels |
| Twilio | Used to send SMSes. In the variables table, enter Twilio values for: AccountId, SID, key and BotPhoneNumber.  ![](../../../Resources/Images/Campaign%20Management/Set%20Up%20the%20Solution_2.png)  For information on how to get these details, see[Step 2. Retrieve Twilio Account Details](../../../Channels/Twillio/TwilioSMS_Channel.md#Step).  You should also hardcode the SID in the SMS sending integration: campaign-send-activities-sms.  ![](../../../Resources/Images/Campaign%20Management/Set%20Up%20the%20Solution_3.png)  For information on how to configure the Twilio SMS channel , see [Twilio SMS](../../../Channels/Twillio/TwilioSMS_Channel.md). | Mandatory only for creating custom SMS campaigns |
| Vonage | Used to send messages. In the variables table, enter your **WhatsApp Vonage token**.  ![](../../../Resources/Images/Campaign%20Management/Set%20Up%20the%20Solution_4.png)  For information on how to configure the Vonage WhatsApp channel , see [WhatsApp Integration](../../../Channels/WhatsApp%20Integration/WhatsApp%20Integration.md). | Mandatory only for creating custom WhatsApp campaigns |

After you configure the connections, click Publish.

<a id="Step4Importdefaultsettings"></a>

### Step 4. Import default settings

1. Select the **Administrators - Campaign Management Settings** workspace.
2. Click **Campaign Settings** on the workspace menu.
3. Click the **Import Settings** button.

![](../../../Resources/Images/Campaign%20Management/Set%20Up%20the%20Solution_5.png)

This automation provisions the default app settings.

> **NOTE:** The provisioning form enables dynamic credential management. Once the provisioning automation completes the initial test setup, replace the default credentials to finalize the configuration. Modifying the email, WebChatURL, AudioCodes Id, and WhatsApp number directly within this form ensures changes apply across the entire application.
>
> ![](../../../Resources/Images/Campaign%20Management/Set%20Up%20the%20Solution_6.png)

<a id="Step5VerifyDemoData"></a>

### Step 5. Verify Demo Data

Select the Admin workspace and review all demo data, including initial GPT prompts.

![](../../../Resources/Images/Campaign%20Management/Set%20Up%20the%20Solution_7.png)

<a id="Step6ConfigureAudienceFilters"></a>

### Step 6. Configure Audience Filters

Audience Filters enable the dynamic creation of audiences during campaign setup. These filters map directly to fields that exist on the [[Contact]] entity. The system uses these mappings to build dynamic queries such as “GPA should be over 3.5” or “Enrollment city should be Bucharest” during conversational audience creation.

While the application includes a dedicated contact entity field for the Audience Filter, you can create a custom filter field for the Audience Filter to reference.

#### Create custom filter field

To create a custom filter field, follow these steps:

1. Select your solution, then go to **Solution Contents** > **Entities**.
2. Search for the **Contact** entity and click on it.
3. Click on the **Fields** tab.
4. Create the new field with the required schema name.
5. Save and publish your changes.

#### Create Audience Filter

To create an audience filter, follow these steps:

1. Go to the **Admin** workspace, and from the left menu, select **Audience Filters**.

![](../../../Resources/Images/Campaign%20Management/Set%20Up%20the%20Solution_8.png)

2. Click the **New Audience Filter** icon at the top-right corner of the page. The audience filter configuration pane appears.
3. Enter the audience filter details:

- **Name** - Enter the unique internal name for this filter record. This value must exactly match the schema name of the existing field on the Contact entity that the filter is based on.
> **NOTE:** The match is case-sensitive and must include the same capitalization, spacing, and underscores. If the names don’t match, the Audience Filter integration will fail because the dynamic audience generator won’t be able to correctly query and filter Contact records.

- **Display Name** - The user-friendly name of the filter.
- **Description** - A short, clear summary of the filter's purpose and criteria. This helps you easily identify the specific function or rules of the filter at a glance in the main AudienceFilter view.

4. Save the filter.

Once configured, these Audience Filters provide users with the ability to dynamically build custom audiences during conversational creation (e.g., combining criteria like "GPA > 3.5" and "Enrollment City = Bucharest").

The filters appear as available options, allowing a seamless transition into the content generation step handled by the next agent. If no custom filters exist, users are limited to selecting only predefined Audiences.

You can now build your first campaign.

<a id="SetupRingCentralCXoutboundcampaigns"></a>

## Set up RingCentral CX outbound campaigns

For information on setting up RingCentral CX outbound campaigns, see
