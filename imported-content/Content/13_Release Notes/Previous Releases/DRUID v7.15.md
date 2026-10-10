---
title: "DRUID 7.15"
---

<a id="DRUID715"></a>


Deployment Dates

The table below lists the deployment date of DRUID v7.15 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| August 16, 2024 | August 29, 2024 | August 29, 2024 | August 29, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="Improvements"></a>

## Improvements

- Knowledge Base Improvements. This release brings several enhancements to the Knowledge Base:

- **Advanced Settings at Data Source Level**. You can now configure Advanced Settings at both the unstructured data source level and the node/leaf level. This added flexibility offers several benefits:

- **Granular Control**: Adjust settings specifically for each data source or individual node/leaf, allowing for more precise tuning of extractors and trainable elements.
- **Enhanced Accuracy**: Tailor configurations to the unique requirements of each data source or node/leaf, leading to more accurate predictions and better overall performance.
- **Streamlined Authoring**: By optimizing settings at these more specific levels, you simplify and accelerate the authoring process, making it easier to manage and refine your data.

In contrast to setting configurations at the Knowledge Base (KB) level, which applies changes broadly, the new approach ensures that each data source element can be finely adjusted according to its specific needs.

![](../../Resources/Images/DRUID%207.15/DATA%20SOURCE%20SETTINGS.png)

![](../../Resources/Images/DRUID%207.15/leaf%20settings.png)

- **Test Data Source Credentials**. You can now test credentials and URIs for all data sources that require them during creation. This feature helps you confirm the connection is working correctly, reducing the need for troubleshooting later if there are issues with the credentials.

![](../../Resources/Images/DRUID%207.15/test%20ds.png)

You can also test the connection from the Data Source Details tab after creation, which is useful if you update your credentials.

![](../../Resources/Images/DRUID%207.15/details%20test.png)

- **SharePoint Online Data Sources - Certificate Authentication**. You can now add online SharePoint data sources using DRUID-generated SSL certificates instead of the SharePoint client secret.

![](../../Resources/Images/DRUID%207.15/sharepoint%20certificate.png)

For more information, see [SharePoint data sources](../../Knowledgebase/SharePoint%20data%20sources.md).

- **Knowledge Base Logs**. Logs are now available for unstructured data source, providing insights into all actions performed on the data source.

![](../../Resources/Images/DRUID%207.15/logs.png)

For more information, see [View the Logs of Unstructured Data Sources](../../Knowledgebase/Unstructured%20Data%20Source%20Logs.md).

- **Flow diagram improvements**. We've enhanced the flow diagram functionality. Now, clicking on the icons in a flow step performs the following actions:

- **Set Variable** icon: Opens the right-side editor and focuses on the Set Variable section.

![](../../Resources/Images/DRUID%207.15/set%20var%20icon.png)

- **Code Extension** icon: Opens the right-side editor and focuses on the Code Extension section.

![](../../Resources/Images/DRUID%207.15/code%20extension%20icon.png)

- **Limit Intent Switch** icon: Opens the right-side editor and focuses on the **Disable intent switch** parameter within the General section.

![](../../Resources/Images/DRUID%207.15/limit%20switch.png)

- **Pre/Post Actions** icon: Expands the flow step to show additional details in the Pre/Post Action section.

![](../../Resources/Images/DRUID%207.15/post%20actions.png)

- **Hide views from Workspaces**. To simplify navigation and avoid confusion, you can now hide views created solely for custom dashboards from both workspaces and the Entity Data tab.

![](../../Resources/Images/DRUID%207.15/custom%20dashboard%20view.png)

For information on how to create custom dashboards, see [Custom dashboards](../../Data%20Analytics%20%26%20Insights/Track%20Business%20KPIs.md).

- **NLP Parameters Now Standard**. We're excited to announce that the following experimental NLP parameters are now standard: **NLU.NER.Classification.UseReranker** and **NLU.NER.Classification.Reranker.JoinUtterances**.

These parameters provide enhanced flow matching capabilities using the Reranker and are now available for general use.

- **KB: Structured Excel and Unstructured data sources**. We have improved the extraction process for structured Excel files. The system now supports Excel files with table headers containing spaces, such as in "Question " and "Answer ". The platform automatically trims these spaces, ensuring accurate data extraction. Additionally, the system can now handle Excel documents with multiple sheets, capturing the sheet name in the "sheetName" property for each extracted article. This is particularly useful when importing these documents into unstructured data sources.

<a id="BugFixes"></a>

## Bug Fixes

- **KB: Counter in Menu** - Resolved an issue where the counter in the menu did not update after creating a new data source.
- **KB: Portal Predict** - Fixed a problem where the score color did not align with the target threshold.
