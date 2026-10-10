---
layout:
  title:
    visible: false
---

<a id="DRUID73"></a>

# DRUID 7.3

Deployment Dates

The table below lists the deployment date of DRUID v7.3 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| February 29, 2024 | March 14, 2024 | March 14, 2024 | March 14, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- various connector bug fixes.

<a id="WhatsNew"></a>

## What's New

- **Flow Audit Trail - Technological Preview**. In this release, we are introducing the initial phase of flow version control with the Flow Audit Trail feature. The Audit Trail is available in the Flow Diagram and provides a comprehensive historical record of all changes made by authors to the flow. It offers you with the ability to track and review the changes made to flows.

![](../../Resources/Images/Diagram/selected%20record.png)

![](../../Resources/Images/Diagram/flow%20versions%20compared.png)

For more information, see [Review Flow Changes](../../4_Flows/Review%20flow%20changes.md).

<a id="Improvements"></a>

## Improvements

- **REST apps - unencrypted variables**. In REST apps, you now have the option to exclude encryption for variables if the integration tasks require consuming non-sensitive metadata.
> **NOTE:** Once a variable is encrypted, it cannot be decrypted. Therefore, exercise caution when encrypting variables.

For more information, see [REST Apps](../../7_Integrations/REST/REST%20Apps.md).

![](../../Resources/Images/druid%207.3/CNN%20decrypted%20variables.png)

- **Conversational Business Applications: improved web forms**. In this release, we've enhanced web forms by making the **ControlType** property visible exclusively within the field layout editor when the Data Type is set to 'String'. This feature empowers you to tailor fields of type string to support input in multiple languages such as HTML, JavaScript, JSON, Markdown, XML, and SQL.

![](../../Resources/Images/druid%207.3/control%20type.png)

Additionally, for fields with the Control Type HTML, users can conveniently preview the executed HTML code directly on the forms.

![](../../Resources/Images/druid%207.3/PREVIEW%20HTML%20BUTTON.png)

![](../../Resources/Images/druid%207.3/PREVIEW%20HTML.png)

For more information, see [Create and Design Forms](../../CBA/Create%20and%20Design%20Forms.md).

- **Webchat - new layout parameter**. This release introduces a new layout parameter in the webchat: "showPoweredBy" that enables you to include the text 'Powered by DRUID' at the bottom of the webchat.

![](../../Resources/Images/druid%207.3/layout%20parameter.png)

> **NOTE:** For new AI Agents, this parameter is enabled by default; however, for existing AI Agents, you will need to manually enable it to display the text.

- **Connector Designer - List View**. In the Connector Designer's list view, users can now easily identify the integration type associated with each step when viewing the integration steps of a connector action. The integration type is now displayed next to the step name, helping users navigate integration processes more efficiently.

![](../../Resources/Images/druid%207.3/integration%20type.png)

- **Default bot framework version**. When creating a new AI Agent, the default bot framework version is 4.

![](../../Resources/Images/druid%207.3/BF4.png)

- **Query Entity integration task - clear error message**. When using a custom query on the Query Entity integration and failing to map any parameters, you will now receive a clear error message specifying which parameter requires mapping. This enhancement improves user experience by providing precise guidance to resolve mapping issues efficiently.

![](../../Resources/Images/druid%207.3/mapping1.png)

![](../../Resources/Images/druid%207.3/mapping2.png)

- **Bulk deletion of flows**.
  With this release, users now have the capability to delete multiple flows in bulk. This feature streamlines the management of flows, allowing users to efficiently remove multiple flows at once.

![](../../Resources/Images/druid%207.3/bulk%20delete.png)

- **Bulk deletion in web forms**. You can now perform bulk deletion of records directly within a view displayed on a web form.
- **Knowledge Base - adding unstructured data sources**. This release introduces a new data source type: 'File Repository', enhancing the process for adding data from unstructured Word, Excel, or PDF files, within the Knowledge Base.

![](../../Resources/Images/KB/file%20repository.png)

- **KB advanced settings**. This release introduces Knowledge Base (KB) advanced settings in technological preview. These settings enable authors to customize the behavior of the KB Engine for experimental operations.

![](../../Resources/Images/druid%207.3/kb%20settings.png)

> **NOTE:** It is crucial not to modify the JSON structure; otherwise, KB extraction during runtime may encounter failures. Should you wish to explore the KB advanced settings, please contact DRUID for assistance.

<a id="BugFixes"></a>

## Bug Fixes

- **Channels**: Voice messages & stickers are no longer marked as unsupported files.
- **Solution**: After linking an entity field to a solution, you can now unlink / link it again.
- **REST Connector**. Alternate response no longer fails when the main response has 'Select token query'.
- **CNN Test status**. Testing the integration tasks that have an error are now properly marked with error in the Test tab.
- **Connector**. Using '\_Global' in mappings on integration tasks with local entities is now working.
- **Custom Code**. When testing a custom code integration, you can now see the full name of variables.
- **Large file upload**. The processing of large file uploads in direct line has been corrected. Users can now expect these uploads to be processed accurately without encountering any issues.
