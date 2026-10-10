---
title: "Druid 9.0"
---

<a id="Druid90"></a>


Deployment Dates

The table below lists the deployment date of DRUID v9.0 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| July 3, 2025 | July 31, 2025 | July 31, 2025 | July 31, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- DRUID Connector Host - File Manipulation Support

<a id="WhatsNew"></a>

## What's New

- **DRUID Connector Host - File Manipulation Support**. This release introduces file manipulation capabilities within the DRUID Connector Host for hybrid and on-premise deployments. You can now seamlessly **save files to** and **read files from** local disks or network locations, enabling richer file-based interactions in your conversations.

![](../../Resources/Images/Read%20File/options.png)

For more information, see [Read Files with the DRUID Connector Host](../../7_Integrations/Read%20File.md) and [Save Files with the DRUID Connector Host](../../7_Integrations/Save%20File.md).

<a id="Improvements"></a>

## Improvements

- Debug message available in Code Extension. With this release you can add debug messages to steps using Code Extension as well. To add a debug message, use the following syntax: `thisStep.Metadata.DebugMessage = string;`

![](../../Resources/Images/druid%209.0/debug%20message.png)

- **Channels - ElevenLabs speech provider supported**. ElevenLabs is now available as a speech provider on the following voice-enabled channels: WhatsApp Meta, WhatsApp Vonage, RingCentral, CueDesk and Sprinklr). For more information, see the channel-specific documentation.

![](../../Resources/Images/druid%209.0/eleven.png)

- **Conversation Trace - enhanced predict event visibility**. We've improved the Conversation Trace to provide clearer insight into Predict events. A new icon now highlights when a prediction occurs, and clicking it reveals details such as the prediction source (e.g., flow name or knowledge base article) and the matching score. This enhancement significantly simplifies tracing and debugging the impact of predictions on conversation flow.

![](../../Resources/Images/druid%209.0/predict%20event.png)

- **Knowledge Base improvements**. This release introduces two improvements:

- Expand predicted answer when clicking to expand the matching score.

![](../../Resources/Images/druid%209.0/expand%20score.png)

![](../../Resources/Images/druid%209.0/expanded%20predict%20answer.png)

- **Filters – Double-click to locate in data source tree**. You can now double-click any node or leaf in the Success, Error, or Not Processed data source filters to quickly locate it in the data source tree. A new tab opens, showing the selected item in its exact position within the tree structure for easier navigation and context.

![](../../Resources/Images/druid%209.0/filter%20tree.png)

- **Flow Steps Metadata – Advanced Code editor enhancement**. With this release, you can maximize Advanced Code Editor in Flow Steps Metadata for a better editing experience.

![](../../Resources/Images/druid%209.0/maximize%20advanced%20editor.png)

![](../../Resources/Images/druid%209.0/maximized%20editor.png)

<a id="BugFixes"></a>

## Bug Fixes

- **Salesforce MIAW Contact Center integration – Long message handling**. Fixed an issue where messages longer than 4,000 characters caused the Salesforce API to fail—commonly occurring with long conversation transcripts. Messages are now automatically split if they exceed the 4,000-character limit.
- **Solution Export/Import – Command Phrase fix**. Fixed an issue where command phrases were not included during solution import. With this release, all configured command phrases are now correctly exported and imported as part of the solution deployment process.
- **Knowledge Base – Tree navigation from Search result fixed**. Fixed an issue where selecting a search result in the Knowledge Base did not correctly navigate to the corresponding node in the data source tree. Previously, the tree expanded only to level 1, and the matched node was not visible especially when the result belonged to a deeper-level or paginated parent node. The tree now expands automatically to reveal and highlight the selected node.
