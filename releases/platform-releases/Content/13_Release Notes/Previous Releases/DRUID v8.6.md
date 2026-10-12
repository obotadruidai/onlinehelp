---
title: DRUID 8.6
---


Deployment Dates

The table below lists the deployment date of DRUID v8.6 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| December 19, 2024                                    | January 16, 2024                       | January 16, 2024                             | January 16, 2024                                    |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

## What's New

* **Knowledge Base - Handling deleted data source elements and extraction workflow**. This release introduces the following KB features:
* **Enhanced handling of deleted elements**. Deleting articles or nodes from trained data sources no longer removes them immediately from the UI. Deleted elements are now marked in red, indicating their pending removal. If the predictive or search functionality within the data source matches an article marked for deletion, it will appear highlighted in red, along with an icon signaling its marked status. A re-training of the data source is required to finalize the removal.

![](<../../../.gitbook/assets/deleted article.png>)

* **Improved extraction workflow**. When extracting articles or nodes from trained data sources, existing articles marked for deletion remain visible, while newly extracted articles are listed below them. This allows users to compare the existing articles with the newly extracted ones and track changes effectively. The predict and search will be done in the articles that are marked for deletion.

![](<../../../.gitbook/assets/extract again.png>)

* **Streamlined UX for element removal**. A pop-up notification now informs users that re-training the KB is required when removing an article or node.

![](<../../../.gitbook/assets/delete po-up.png>)

A warning message below the data source predict area indicates that train is required.

![](../../../.gitbook/assets/warning.png)

{% hint style="info" %}
**NOTE:** After re-training a data source, elements marked for deletion within that specific source will be permanently removed. To delete elements marked for deletion across multiple data sources, you must train the entire KB.
{% endhint %}

* **Start multiple conversations**. You can now initiate multiple DRUID conversations simultaneously using the `/api/Druid/{botId}/StartFlowBulk` API endpoint. This is especially useful for starting conversations with multiple users in a single API call.

![](<../../../.gitbook/assets/new webhook.png>)

For more information, see [Start multiple DRUID conversations by API](https://druidai.gitbook.io/druid-ai-docs/how-to/start-multiple-druid-conversations-by-api).

* **Vonage Voice channel**. The Vonage Voice channel now allows you to integrate AI Agents for seamless voice-based conversations, automated call handling, and efficient call routing. This enhancement improves customer interactions and engagement while reducing operational costs. For more information, see [Vonage Voice](https://druidai.gitbook.io/druid-ai-docs/channels/voice-and-telephony/vonage_voice).

## Improvements

* **Knowledge Base - HTML Website Data Extraction**. By default, when extracting paragraphs from an HTML website, the extractor excludes content from specific HTML tags, elements with certain roles, and elements with specific attributes or classes.

With this release, you can configure the **HtmlSelectorTagsToIgnore** parameter under the "featureFlags" collection in the KB **Advanced Settings JSON** field. This parameter gives you control over which HTML elements are excluded during content extraction. Set it to an empty list (**\[]**) to include all content, or specify values to filter out unwanted elements.

![](<../../../.gitbook/assets/ignore tag.png>)

For more information, see [Website data sources](https://druidai.gitbook.io/druid-ai-docs/knowledge-base/knowledgebase/data-sources/website-data-sources).

* **Cuedesk channel - support for Cue web chat channel**. You can now integrate AI Agents with Cue to handle user requests through the Cue web chat channel, in addition to WhatsApp and Facebook Messenger.
* **Document Builder - generate PDF with attachments**. With this release, you can generate PDFs with attachments using Word templates. This feature streamlines document creation, enhances flexibility, and ensures all relevant information is consolidated into a single, professional PDF file.

![](<../../../.gitbook/assets/GENERATE PDF WITH ATATCH.png>)

For more information, see [Generate word, excel and PDF files using document templates](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/document-builder/generate-word-excel-and-pdf-files-using-document-templates).

* **Integrations filtering improvement**. Integration Filtering now includes a **Scope** filter, allowing you to easily filter integrations that have at least one integration task with a **Local** or **Global** scope.

![](<../../../.gitbook/assets/scope filter.png>)

* **Workspace - preview image/video in forms**. A new **Preview in form (image/video)** parameter is now available for fields of type \[\[File]], allowing you to preview images and play video files directly within forms.

![](<../../../.gitbook/assets/preview parameter.png>)

![](<../../../.gitbook/assets/preview image.png>)

![](<../../../.gitbook/assets/preview image in form.png>)
