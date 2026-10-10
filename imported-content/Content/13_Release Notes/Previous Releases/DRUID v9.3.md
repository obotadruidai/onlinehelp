---
title: "Druid 9.3"
---

<a id="Druid93"></a>


Deployment Dates

The table below lists the deployment date of DRUID v9.3 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| August 14, 2025 | August 28, 2025 | August 28, 2025 | August 28, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- SAML-based SSO authentication - Added support for SAML authentication with certificate signing
- Bug fixes

<a id="Improvements"></a>

## Improvements

- **SAML-based SSO authentication - Added support for SAML authentication with certificate signing**. DRUID can now sign SAML AuthnRequests using its private key, allowing Identity Providers to verify requests with the corresponding public key for enhanced security. For more information, see [SSO Authentication with the SAML Protocol](../../7_Integrations/SamlAuth/SSO%20Authentication%20with%20SAML.md).
- **Knowledge Base improvements**. This release introduces various improvements:

- **Added UI for configuring HTML Selector Tags to Ignore**. You can now manage which HTML elements are excluded during content extraction directly in **Knowledge Base Settings** > **Advanced Settings**, without editing the Advanced Settings JSON configuration.

![](../../Resources/Images/druid%207.14/tags%20to%20ignore.png)

- **Improved KB Search Results**. Search results in the Knowledge Base now display the page URL. For web pages, you can click the link to navigate directly to the page.

![](../../Resources/Images/druid%209.3/search%20result%20url.png)

- **Custom Data Sources – Include/Exclude from Scraping**. You can now choose which file explorer elements DRUID extracts during the extraction process. This update lets you exclude specific elements from scraping or re-include previously excluded ones.

![](../../Resources/Images/druid%209.3/custom%20ds%20exclude.png)

![](../../Resources/Images/druid%209.3/custom%20ds%20include.png)

- **Custom Data Sources – Crawl Path**. The Crawl Path is now available only at the root level, as the Crawler cannot directly crawl file explorer elements located below the root.

![](../../Resources/Images/druid%209.3/crawl%20path.png)

- **Code Extension - Change to DebugMessage property**. The DebugMessage property has been moved from `thisStep.Metadata.DebugMessage` to `thisStep.DebugMessage` to ensure it is not stored in metadata. This change prevents debug messages from being saved in step metadata, reducing unnecessary data in the conversation state and improving performance when handling step data.
{% hint style="info" %}
**NOTE:** While the old field `thisStep.Metadata.DebugMessage` is still accessible, setting it when `thisStep.DebugMessage` also has a value may produce unpredictable results.
{% endhint %}

- **Flow diagram – Preserve layout mode per flow**. Each flow now stores its own layout view preference ( Tree, or Layered Digraph). The selected view applies only to the current flow, allowing different flows to have different layouts. When you reopen a flow, it appears in the view you last selected for that flow. Changing the layout view for one flow no longer affects other flows.

![](../../Resources/Images/druid%209.3/flow%20view.png)

- **Special Flows Authoring**. You can now unmark flows previously set as special flows by clicking the **X** in the **Special flow type** field on the flow configuration page. This sets the flow type to **None**. It helps streamline AI Agent authoring by showing only relevant flows in the special flows list, reducing the need to scroll through long lists.

![](../../Resources/Images/druid%209.3/unmark%20special%20flow.png)

![](../../Resources/Images/druid%209.3/no%20special%20flow.png)

- **Connector Host - Allow File Manipulation via installer**. Enabling file manipulation through the DRUID Connector Host no longer requires manual appsettings.json file updates. You can now enable file manipulation from local disks or network locations directly in the installer UI by selecting **Use local files** and specifying the file access path. This simplifies setup and supports richer file-based interactions in conversations.

![](../../Resources/Images/druid%209.3/file%20manipulation%20ui%20cnn.png)

<a id="BugFixes"></a>

## Bug Fixes

- **AWS Contact Center**: Fixed an issue where users were disconnected when transferred to another agent.
- **Import from single-language to multi-language AI Agents**: Fixed a bug where importing a solution containing connector actions did not properly populate FlowStepTranslation for secondary languages. Connector actions added as PRE and POST actions now correctly map the Connector Action ID in the Metadata field.
- **Telegram channel**: Fixed an issue where some hero cards did not render properly.
- **OAuth**: Fixed a problem where “Session Expired” was incorrectly displayed after following the login link.
