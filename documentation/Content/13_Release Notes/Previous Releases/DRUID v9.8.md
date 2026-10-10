<a id="Druid98"></a>

# Druid 9.8

Deployment Dates

The table below lists the deployment date of DRUID v9.8 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| October 23, 2025 | November 20, 2025 | November 20, 2025 | November 20, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Data Service Connector bug fixes

<a id="Improvements"></a>

## Improvements

- **Provisioning Portal - Handling of SSO and manually created users**. When a user logs in via OpenID Connect SSO and an existing Druid Portal user is found with an email address that matches an existing manually-created portal user, the system now merges the user accounts instead of attempting to create a duplicate user. This merging logic ensures:

- **Property update**: User properties (e.g., roles, first name, last name) and security roles provided by the SSO identity provider will be used to update the corresponding properties and roles on the existing Druid Portal user account. The merger operates on a **maximum properties basis**, meaning non-null values from the SSO provider will overwrite existing values.
- **Master ID preservation**: The **masterId** will be preserved. If the existing user has a masterId and the current SSO login request does not provide one, the existing masterId will not be deleted.

For information on how to provision Druid Portal users via OpenID Connect, see [Provisioning Portal Users and SSO Authentication via OpenID Connect](../../Governance%20%26%20Security/User%20Management/Provisioning%20Portal%20Users.md).

- **Conversation History - Faster loading for User filter**. Optimized the User filter drop-down to load faster, improving performance for tenants with large numbers of users.

![](../../Resources/Images/druid%209.9/user%20filter.png)

- **Channels – Streamlined authoring and configuration**. The Channels section has been completely refactorized to deliver a more intuitive and efficient authoring experience, particularly for managing multiple channels.

- **Categorized Channels**: Channels are now logically grouped into Categories, making them easier to find and manage at a glance.

![](../../Resources/Images/druid%209.9/channels.png)

- **Intuitive Configuration**: Channel settings and configuration are now handled cleanly within a dedicated pop-up window, eliminating the previous need to manage complex configurations on a single, crowded page.

![](../../Resources/Images/druid%209.9/channel%20config.png)

- **Knowledge Base – Enhanced Google Drive data sources**. We have refactored Google Drive as a standalone data source type within the Knowledge Base, making it easier to set up and manage.

- **Dedicated data source type**: Google Drive is no longer nested under the "Shared Drive" type. When creating a new data source, select "Google Drive" directly for a clearer setup flow.

![](../../Resources/Images/druid%209.9/google%20drive%20ds.png)

- **Granular folder control**: When configuring your Google Drive data source, you can now select the shared folder or specific subfolder(s) you want to ingest. The **Shared folders** drop-down menu displays the root shared Google Drive folder along with all its subfolders (if any), giving you precise control over what content is included in the Knowledge Base.

![](../../Resources/Images/druid%209.9/shared%20folder.png)

For more information, see [Google Drive Data Sources](../../Knowledgebase/Google%20Drive.md).

<a id="BugFixes"></a>

## Bug Fixes

- **Data Service Connector**. A series of issues related to the Data Service Connector have been resolved to ensure greater stability and accuracy when integrating with external databases:
  - **Currency field persistence**: Fixed an issue where the currency field was not correctly saved (persisted) when updating or adding an entity using the 'Map all fields' option.
  - **Record update count**: The **updateRecord** action in the Response task now correctly reports the number of records that were successfully updated.
  - **SQL operator**: Resolved the issue where the **+** operator in a SQL WHERE clause was incorrectly translated into the **$concat** operator when used with numeric values. It now correctly performs numeric addition.
  - **Multi-task PageInfo handling**: Fixed an issue in the Data Service Connector where using multiple integration tasks resulted in incorrect PageInfo handling.
- **Entity metadata filtering**: Fixed a performance issue in the Set Variables section. When typing an entity name (instead of selecting from the drop-down), only the fields belonging to the selected entity will be listed, preventing massive lists and performance lag on tenants with many entities.
