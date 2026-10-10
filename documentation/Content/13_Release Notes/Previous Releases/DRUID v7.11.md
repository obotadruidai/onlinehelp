<a id="DRUID711"></a>

# DRUID 7.11

Deployment Dates

The table below lists the deployment date of DRUID v7.11 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| June 20, 2024 | July 04, 2024 | July 04, 2024 | July 04, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Cuedesk channel**. With this release, you can integrate AI Agents with Cue to handle user requests within the chosen channels in Cuedesk flows.  For more information, see [Cuedesk Integration](../../Channels/Cuedesk/Cuedesk%20Integration.md).

<a id="Improvements"></a>

## Improvements

- **Knowledge Base improvements**. This release introduces various enhancements to the Knowledge Base:

- **Advanced settings - parameter renaming**. The parameter 'trainableColumns' has been renamed to 'trainableElements'.
- **SharePoint data source improvements**:

- You can now specify the crawling depth.
- All nodes are excluded from scraping by default to ensure only relevant content is captured and added to the Knowledge Base.
- When creating a SharePoint data source, the last folder you specify in the SharePoint URL will be set as the data source root.

![](../../Resources/Images/druid%207.11/sharepoint%20root.png)

- **Bulk actions - new action**. A new bulk action, **Extract Unprocessed**, is now available at the data source level and for root and node elements. This action allows you to extract data that has either not been processed or failed during extraction.

![](../../Resources/Images/druid%207.11/unprocessed.png)

- **Download file integration task - dynamic file name**. With this release, you can now specify a custom name for the downloaded file when using the Download File integration task. You can set this name in the Response, either as a static name (string) or by using a value stored in an entity field or variable. If no custom name is specified, the downloaded file will retain its original name.

![](../../Resources/Images/druid%207.11/file%20name%20dynamic.png)

- **Slack channel - added support for chat in Slack channels**. Members of a Slack channel can now interact with the AI Agent by starting their messages with **@**<AI Agent name>. This action creates a thread within the channel, allowing them to continue the conversation seamlessly.

![](../../Resources/Images/druid%207.11/bot%20thread.png)

For more information, see [Slack Integration](../../Channels/Slack%20Integration/Slack%20Integration.md).

- **OAuth apps - added support for variables**. You can now add variables to OAuth apps, in addition to the authorization fields. These variables can be kept secret throughout the integrations, enhancing security and flexibility.

![](../../Resources/Images/druid%207.11/oauth%20app.png)

- **Connector: Read excel integration - Intuitive error messages for column mappings**. The Read excel integration task now provides intuitive error messages for column mappings, making it easier to identify and resolve issues.
- **BluePrim integration improvements**

- The request now supports 'Field Mapping' in addition to 'Body Template' options in the 'Request type' field.

![](../../Resources/Images/druid%207.11/use%20field%20mapping.png)

- You can place an item directly on a queue by entering the queue name in the **Exchange/Queue** field and leaving the **Routing Key** field empty.

- **Warning message for insufficient utterances with NER in a flow**. A warning message will now appear if there are fewer than five utterances with Named Entity Recognition (NER) in a flow. This helps ensure adequate data for effective processing.
- **Enhanced webchat behavior for "Typing" indicator label**. The webchat's "typing" indicator label has been improved to eliminate unnecessary fluctuations during sequential integrations. This enhancement prevents the label from repeatedly showing and disappearing, providing a smoother user experience without text movement disruptions.
- **Data Service - Query related entity without parent entity**
  - **Enhanced Query related entity task functionality**: The QueryRelated function now supports receiving entity information related to the parent entity without requiring the parent entity to be reloaded.
  - **Optimized query mechanism**: The query mechanism has been adjusted to load only the IDs and NAME for specific parent entities, improving efficiency and performance.
- **Flow Diagram Facelift**. Icons on steps now maintain their specific positions and are color-coded to distinguish Set Variables from Pre/Post actions.

![](../../Resources/Images/BluePrism/floe%20diagram.png)

<a id="BugFixes"></a>

## Bug Fixes

- **Knowledge Base: File Repository**: When all files are deleted from a File Repository data source, its status now properly changes to 'New'.
- **Authentication Flow**: The authentication flow is now triggered correctly on the Druid Conductor when a child AI Agent flow requires authentication.
- **Custom Code**: Fixed an issue where custom code threw errors when trying to get or set a value directly on a list.
- **REST with Local Scope**: The "Project To" option now displays the selected option correctly.
- **Web Views**: Relation fields are now displayed correctly at runtime.
- **Web Views**: Percentage type fields now display as percentages.
- **Portal Chat Snippet**: The portal chat snippet is no longer shown while in workspaces (web views and forms) or KB data sources.

<a id="KnownIssueTeamsChannelIntegration"></a>

## Known Issue: Teams Channel Integration

The latest Teams mobile app update causes hero cards to not render properly.

**Workaround**

To view hero cards correctly, rotate your mobile device to a horizontal orientation.

**Status**

We will update you once Microsoft releases a new version of the Teams mobile app that resolves this issue.
