---
title: "Configuration for Sensitive Data Manipulation"
---

<a id="ConfigurationforSensitiveDataManipulation"></a>


DRUID provides authors with extensive options to create AI Agents able to securely capture sensitive data from chat users (passwords, credit card numbers, etc.) / receive secure data from external systems and transfer it in an encrypted way to third party applications using connector integrations.

<a id="SensitivedatamanipulationinMSTeamschannel"></a>

## Sensitive data manipulation in MS Teams channel

> **NOTE:** This feature is available in DRUID version 1.63 for AI Agents using Bot framework version 4. Sensitive data manipulation is only available on prompt steps on both direct line and MS Teams channel. For information on how to configure the prompt steps to manipulate sensitive data, see [Prompt Steps Configuration](../../4_Flows/Prompt%20Steps%20Configuration.md).

When the AI Agent deployed in the MS Teams channel asks the user to enter sensitive data (a prompt message that will capture sensitive data is executed), MS Teams will automatically generate a Teams built-in card that asks for the user confirmation to continue.

![](../../Resources/Images/Sensitive%20data%20manipulation%20in%20MS%20Teams%20channel/Sensitive%20data%20manipulation.png)

After the user confirms, MS Teams renders a dedicated DRUID built-in page, which enables the user to enter sensitive data in a secure way.

![](../../Resources/Images/Sensitive%20data%20manipulation%20in%20MS%20Teams%20channel/Sensitive%20data%20manipulation_1.png)

> **IMPORTANT!**  The sensitive data passes directly to DRUID platform, always encrypted, bypassing the MS Teams channel. After the user sends the sensitive data in the DRUID built-in page, the data is not shown in the chat.

<a id="MSTeamschannelconfigurationforsensitivedatamanipulation"></a>

## MS Teams channel configuration for sensitive data manipulation

For AI Agents deployed in the MS Teams channel to benefit the sensitive data manipulation:

1. In the Teams client, open the Developer Portal. From the **...** overflow menu on the left, click **Developer Portal**.
2. On the main menu, click **Apps** and click the app you created for your AI Agent integration.
3. On the **Configure** menu, click **Domains**.
4. Add the following domains:

- `token.botframework.com`
- DRUID API domain specific to the DRUID Cloud you are using:

| Druid Community | PROD Europe | PROD US | PROD Australia |
| --- | --- | --- | --- |
| `druidapi.comm.eu.druidplatform.com` | `prod-DRUID-api.azurewebsites.net` | `druidapi.us.druidplatform.com` | `druidapi.au.druidplatform.com` |

*Example: DRUID Community Cloud*

![](../../Resources/Images/MS%20Teams%20Integration_Developer%20Portal/api%20domains.png)

5. At the top right corner of the page, click the **Publish** button. A pop-up appears.

![](../../Resources/Images/MS%20Teams%20Integration_Developer%20Portal/MS%20Teams%20Integration_18.png)

6. Click **Download the app package**.
7. Validate your app package manifest and install the AI Agent in MS Teams following Step 3 and Step 4 described in [MS Teams Integration](MS%20Teams%20Integration.md).

## Related Topics

- [Extensive Sensitive Data Manipulation](../../Governance%20%26%20Security/Extensive%20Sensitive%20Data%20Manipulation.md)
- [Managing Entity Fields](../../5_Entities/Managing%20Entity%20Fields.md)
- [Prompt](../../4_Flows/Prompt%20Steps%20Configuration.md)
