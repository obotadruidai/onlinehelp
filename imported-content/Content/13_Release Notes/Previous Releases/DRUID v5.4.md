---
title: "DRUID 5.4"
---

<a id="DRUID54"></a>


Deployment Dates

The table below lists the deployment date of DRUID v5.4 across Druid Clouds. To view the Druid Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| Canceled - January 05, 2023 | January 05, 2023 | January 05, 2023 | January 05, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

**Required!** This release includes features that require upgrade of your Druid Connector Host to the latest version:

- DRUID Connector Host installer improvements
- DRUID Connectors - maximum execution timeout on integrations
- SQL Connector
- CNN Installer bug - Backup folder

<a id="WhatsNew"></a>

## What's New

- **Charts on forms**. With this release you can add charts on forms by using sub grids. This way you put at business users disposal on forms grouped information about entity records.

![](../../Resources/Images/Adding%20views%20and%20charts%20on%20forms%20by%20using%20sub%20grids/Adding%20views%20and%20charts%20on_1.png)

For more information, see [Adding Views and Charts on forms by Using Sub Grids](../../CBA/Adding%20views%20and%20charts%20on%20Forms.md).

<a id="Improvements"></a>

## Improvements

- **New DRUID supported languages**. With this release, DRUID supports the following APAC native script languages: Burmese, Filipino, Kannada, Khmer, Malagasy, Manipuri (Bengali), Marathi, Punjabi, Sinhala, Telugu and Urdu.
> **NOTE:** You can use these languages only with semantic-based classification; therefore setting the following parameter to "true", **NLU.NER.Classification.UseSemantic = True** is mandatory. For more information about DRUID Supported languages across NLP features, see [DRUID Supported Languages](../../Conversational%20AI/DRUID%20Supported%20Languages.md).

DRUID Stop Words are also available for [Marathi](../../Conversational%20AI/StopWords/MarathiStopWords.md) and [Urdu](../../Conversational%20AI/StopWords/UrduStopWords.md).

- **DRUID Connector Host installer improvements**.

- When upgrading DRUID Connector Host, the installer now reads the existing connection configurations and users performing the upgrade can modify the connection parameters.

![](../../Resources/Images/Install%20Druid%20Connector%20Host/upgrade%20read%20settings.png)

- When upgrading DRUID Connector Host, the installer checks if .NET exists on the machine and if it exists, it also checks the .NET version installed on the machine. It the main .NET version packed in the installer differs from the one installed on the machine, it automatically installs the .NET version packed within it.

![](../../Resources/Images/Install%20Druid%20Connector%20Host/upgrade%20net%20install.png)

- When installing the Connector Host, you can import the installation parameters by clicking the **Import settings** button and uploading the configuration file. This is particularly useful when you have encrypted credentials, when using an encryption certificate, or when you want to install the latest Connector Host version on another machine using the installation parameters from an old installation.

![](../../Resources/Images/Install%20Druid%20Connector%20Host/Install%20Druid%20Connector%20Host_15.png)

![](../../Resources/Images/Install%20Druid%20Connector%20Host/read%20params.png)

- **DRUID Connectors - maximum execution timeout on integrations**. On all DRUID connectors, to avoid long execution time for an integration with many tasks, the maximum sum of all timeouts configured on an integration is now 250 seconds. Whenever this maximum is reached, the execution of the currently running integration task is interrupted and any subsequent integration tasks are no longer executed.
- **SQL Connector**. An additional connection parameter, **ApplicationName** is now available when connecting to an SQL Server and it is useful for debugging purposes. You can use the application name in the SQL profiler to filter the actions performed by the SQL Connector on the database.
- **System entity fields upgrade enhancements**. To highlight that the entity upgrade process is irreversible, the upgrade pop-up now provides more details on what the authors should do before the upgrade.

![](../../Resources/Images/Entities/important%20message.png)

To ensure that authors don't break the AI Agent informational model and conversational flows when doing bulk upgrade, the option to **Upgrade all entities** has been removed.

Also, if you do not upgrade an entity, you have DRUID Data Service active and you try adding a DRUID Data Service integration task on the entity, you will get an error message.

![](../../Resources/Images/Entities/error%20message%20in%20integration%20task.png)

- A new parameter is now available in the Webchat UI editor, **autoScrollSnapOnPage**. Selecting this parameter, you set the snippet focus on the last message sent by the AI Agent and not on the first one, thus eliminating the need for users to scroll down in the chat to read subsequent messages sent in the chat.
- On AI Agents using Bot Framework version 4, you can now also block user input for adaptive cards; **Block User Input** option is now available on adaptive card configuration page.

<a id="BugFixes"></a>

## Bug Fixes

- CNN Installer: Upgrading DRUID Connector Host no longer deletes existing logs. The **Backup** folder is updated before upgrading CNN Host with the logs created from the last upgrade.
- Upgraded DRUID entities, they are now case sensitive compatible.
