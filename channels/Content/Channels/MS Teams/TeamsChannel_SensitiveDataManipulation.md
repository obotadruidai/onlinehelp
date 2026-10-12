---
title: Configuration for Sensitive Data Manipulation
---


DRUID provides authors with extensive options to create AI Agents able to securely capture sensitive data from chat users (passwords, credit card numbers, etc.) / receive secure data from external systems and transfer it in an encrypted way to third party applications using connector integrations.

## Sensitive data manipulation in MS Teams channel

{% hint style="info" %}
**NOTE:** This feature is available in DRUID version 1.63 for AI Agents using Bot framework version 4. Sensitive data manipulation is only available on prompt steps on both direct line and MS Teams channel. For information on how to configure the prompt steps to manipulate sensitive data, see [Prompt Steps Configuration](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/conversational-flows/flow-steps/prompt-steps-configuration).
{% endhint %}

When the AI Agent deployed in the MS Teams channel asks the user to enter sensitive data (a prompt message that will capture sensitive data is executed), MS Teams will automatically generate a Teams built-in card that asks for the user confirmation to continue.

![](<../../../.gitbook/assets/Sensitive data manipulation.png>)

After the user confirms, MS Teams renders a dedicated DRUID built-in page, which enables the user to enter sensitive data in a secure way.

![](<../../../.gitbook/assets/Sensitive data manipulation_1.png>)

{% hint style="warning" %}
**IMPORTANT!** The sensitive data passes directly to DRUID platform, always encrypted, bypassing the MS Teams channel. After the user sends the sensitive data in the DRUID built-in page, the data is not shown in the chat.
{% endhint %}

## MS Teams channel configuration for sensitive data manipulation

For AI Agents deployed in the MS Teams channel to benefit the sensitive data manipulation:

1. In the Teams client, open the Developer Portal. From the **...** overflow menu on the left, click **Developer Portal**.
2. On the main menu, click **Apps** and click the app you created for your AI Agent integration.
3. On the **Configure** menu, click **Domains**.
4. Add the following domains:

* `token.botframework.com`
* DRUID API domain specific to the DRUID Cloud you are using:

| Druid Community                      | PROD Europe                        | PROD US                         | PROD Australia                  |
| ------------------------------------ | ---------------------------------- | ------------------------------- | ------------------------------- |
| `druidapi.comm.eu.druidplatform.com` | `prod-DRUID-api.azurewebsites.net` | `druidapi.us.druidplatform.com` | `druidapi.au.druidplatform.com` |

_Example: DRUID Community Cloud_

![](<../../../.gitbook/assets/api domains.png>)

5. At the top right corner of the page, click the **Publish** button. A pop-up appears.

![](<../../../.gitbook/assets/MS Teams Integration_18.png>)

6. Click **Download the app package**.
7. Validate your app package manifest and install the AI Agent in MS Teams following Step 3 and Step 4 described in [MS Teams Integration](<MS Teams Integration.md>).

## Related Topics

* [Extensive Sensitive Data Manipulation](https://druidai.gitbook.io/druid-ai-docs/ai-platform/ai-governance-and-security/data-security-and-privacy/extensive-sensitive-data-manipulation)
* [Managing Entity Fields](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/ai-agent-informational-model/managing-entity-fields)
* [Prompt](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/conversational-flows/flow-steps/prompt-steps-configuration)
