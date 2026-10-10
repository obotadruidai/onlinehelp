---
layout:
  title:
    visible: false
---

<a id="DRUID86"></a>

# DRUID 8.6

Deployment Dates

The table below lists the deployment date of DRUID v8.6 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| December 19, 2024 | January 16, 2024 | January 16, 2024 | January 16, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Knowledge Base - Handling deleted data source elements and extraction workflow**. This release introduces the following KB features:

- **Enhanced handling of deleted elements**. Deleting articles or nodes from trained data sources no longer removes them immediately from the UI. Deleted elements are now marked in red, indicating their pending removal. If the predictive or search functionality within the data source matches an article marked for deletion, it will appear highlighted in red, along with an icon signaling its marked status. A re-training of the data source is required to finalize the removal.

![](../../Resources/Images/Druid%208.6/deleted%20article.png)

- **Improved extraction workflow**. When extracting articles or nodes from trained data sources, existing articles marked for deletion remain visible, while newly extracted articles are listed below them. This allows users to compare the existing articles with the newly extracted ones and track changes effectively. The predict and search will be done in the articles that are marked for deletion.

![](../../Resources/Images/Druid%208.6/extract%20again.png)

- **Streamlined UX for element removal**. A pop-up notification now informs users that re-training the KB is required when removing an article or node.

![](../../Resources/Images/Druid%208.6/delete%20po-up.png)

A warning message below the data source predict area indicates that train is required.

![](../../Resources/Images/Druid%208.6/warning.png)

> **NOTE:**  After re-training a data source, elements marked for deletion within that specific source will be permanently removed. To delete elements marked for deletion across multiple data sources, you must train the entire KB.

- **Start multiple conversations**. You can now initiate multiple DRUID conversations simultaneously using the `/api/Druid/{botId}/StartFlowBulk` API endpoint. This is especially useful for starting conversations with multiple users in a single API call.

![](../../Resources/Images/Druid%208.6/new%20webhook.png)

For more information, see [Start multiple DRUID conversations by API](../../How%20to/Start%20multiple%20DRUID%20conversations%20by%20API.md).

- **Vonage Voice channel**. The Vonage Voice channel now allows you to integrate AI Agents for seamless voice-based conversations, automated call handling, and efficient call routing. This enhancement improves customer interactions and engagement while reducing operational costs. For more information, see [Vonage Voice](../../Channels/Vonage_Voice.md).

<a id="Improvements"></a>

## Improvements

- **Knowledge Base - HTML Website Data Extraction**. By default, when extracting paragraphs from an HTML website, the extractor excludes content from specific HTML tags, elements with certain roles, and elements with specific attributes or classes.

With this release, you can configure the **HtmlSelectorTagsToIgnore** parameter under the "featureFlags" collection in the KB **Advanced Settings JSON** field. This parameter gives you control over which HTML elements are excluded during content extraction. Set it to an empty list (**[]**) to include all content, or specify values to filter out unwanted elements.

![](../../Resources/Images/Druid%208.6/ignore%20tag.png)

For more information, see [Website data sources](../../Knowledgebase/Website%20data%20sources.md).

- **Cuedesk channel - support for Cue web chat channel**. You can now integrate AI Agents with Cue to handle user requests through the Cue web chat channel, in addition to WhatsApp and Facebook Messenger.
- **Document Builder - generate PDF with attachments**. With this release, you can generate PDFs with attachments using Word templates. This feature streamlines document creation, enhances flexibility, and ensures all relevant information is consolidated into a single, professional PDF file.

![](../../Resources/Images/Druid%208.6/GENERATE%20PDF%20WITH%20ATATCH.png)

For more information, see [Generate word, excel and PDF files using document templates](../../7_Integrations/Document%20Builder/Generate%20word%2C%20excel%20and%20PDF%20files%20using%20document%20templates.md).

- **Integrations filtering improvement**. Integration Filtering now includes a **Scope** filter, allowing you to easily filter integrations that have at least one integration task with a **Local** or **Global** scope.

![](../../Resources/Images/Druid%208.6/scope%20filter.png)

- **Workspace - preview image/video in forms**. A new **Preview in form (image/video)** parameter is now available for fields of type [[File]], allowing you to preview images and play video files directly within forms.

![](../../Resources/Images/Druid%208.6/preview%20parameter.png)

![](../../Resources/Images/Druid%208.6/preview%20image.png)

![](../../Resources/Images/Druid%208.6/preview%20image%20in%20form.png)
