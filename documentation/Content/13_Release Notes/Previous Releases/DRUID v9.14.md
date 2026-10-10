<a id="Druid914"></a>

# Druid 9.14

Deployment Dates

The table below lists the deployment date of DRUID v9.14 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| January 15, 2025 | February 12, 2026 | February 12, 2026 | February 12, 2026 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

**Recommended!** This release includes features and bug fixes that require upgrade of your Druid Connector Host:

- Druid Connector Host – List Files Task Enhancements

<a id="WhatsNew"></a>

## What's New

- **Druid Connector Host – List Files Task Enhancements**. This release introduces powerful improvements to the **List Files** task in the Druid Connector Host, providing greater control and flexibility for file-based workflow automation in hybrid and on-premises deployments. The enhanced List Files task includes:

- **Expansion level**. Control directory traversal depth to list files from the target directory only or include subdirectories at specified levels, enabling more precise file discovery across complex directory structures.
- **Filtering**. Apply filters to retrieve only files that match specific criteria, reducing the need for post-processing.
- **Sorting**. Sort file list by specific attributes, making it easier to identify and process files in a predictable order.
- **Pagination**. Handle large directory listings efficiently by retrieving files in manageable batches, improving performance and resource utilization when working with directories containing numerous files.

For more information, see [List Files with the Druid Connector Host](../../7_Integrations/List%20Files.md).

<a id="BugFixes"></a>

## Bug Fixes

- **Knowledge Base Schedule fix**: Resolved an issue where a Scheduler set up on a data source would halt completely if the Extract task encountered an error. Previously, if a document failed during extraction, the subsequent Train task would not initiate. The system now ensures that Knowledge Base training is handled correctly following scheduled execution attempts.
