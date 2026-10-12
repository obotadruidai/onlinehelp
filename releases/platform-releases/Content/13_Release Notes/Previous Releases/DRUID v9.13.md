---
title: Druid 9.13
---


Deployment Dates

The table below lists the deployment date of DRUID v9.13 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| January 15, 2025                                     | February 12, 2026                      | February 12, 2026                            | February 12, 2026                                   |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

**Recommended!** This release includes features and bug fixes that require upgrade of your Druid Connector Host and Druid Data Service:

* DRUID Connector Host – Enhanced file manipulation support
* Web Forms – Dynamic Filtering and Update of Automations
* bug fixes

## What's New

* **Talkdesk Live Chat**. Added Talkdesk Live Chat integration, allowing AI Agents to handle initial customer interactions and seamlessly transfer conversations to Talkdesk agents, while preserving full chat history and customer context. For more information, see [Talkdesk Live Chat](https://druidai.gitbook.io/druid-ai-docs/contact-centers/talkdesk-live-chat).
* **Druid Vision - JPEG to PDF Conversion**. We have introduced two new endpoints to Druid Vision for converting image files (.jpg, .jpeg, .png) into high-quality PDF documents. This update provides developers with the flexibility to choose the most efficient output for their use case:
* **Standard Conversion**: Returns the PDF as a byte array, perfect for immediate storage or simple file sharing.
* **Streamed Conversion**: Optimized for performance and low memory overhead, making it the preferred choice for high-volume or large-file conversions.

Both endpoints support multi-file uploads to create multi-page PDFs and offer customizable parameters for DPI, color mode, and scaling. For more information, see [Convert JPEG to PDF](https://druidai.gitbook.io/druid-ai-docs/integrations/druid-vision/convert-jpeg-to-pdf).

* **DRUID Connector Host – Enhanced file manipulation support.** This release extends file management capabilities in the DRUID Connector Host for hybrid and on-premises deployments. You can now list files from directories and delete files from local disks or network locations. These enhancements complement the existing Read File and Save File tasks, enabling more complete file-based workflow automation.
* **List Files** task. Retrieves a list of files from a specified directory, similar to the Linux ls command. This task is useful for discovering available files before reading, processing, or applying additional logic to them. For more information, see [List Files with the Druid Connector Host](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/list-files).
* **Delete File** task. Deletes a single file from a local disk or network location. Each task execution removes one file, ensuring controlled and intentional deletion operations. For more information, see [Delete File with the Druid Connector Host](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/delete-file).

## Improvements

* **Portal administration - Editable 'admin' username**. With this release you have the possibility to change the user name of the default admin user. This decreases the chances of hackers accessing your Druid Portal account by hacking the default admin account. In previous Druid versions, the **User name** is a non-editable field for the default admin user account.

![](../../../.gitbook/assets/username.png)

* **NLU Evaluation – Improved phrase validation**. This release introduces consistent duplicate-phrase validation across the platform.
* Validation is enforced in NLU Evaluation for both Train and Test sets.
* Validation is also applied in Flows when adding or editing training phrases.
* Duplicate phrases are blocked during manual entry, editing, and training set imports.
* A clear warning message is displayed when a duplicate is detected.
* **Knowledge Base - improvements**. This release introduces various improvements to the KB:
* **Node Level Trainable Elements for LLM Content Chunker**. Building upon the Content Chunker with LLM features introduced in our previous release, Druid now offers even more granular control. The Trainable Elements options—specifically **Train generated summary** and **Train generated questions**—have been extended from Global and Data Source levels to the node level and leaf level.

![](<../../../.gitbook/assets/node elem.png>)

* **EML Content Extraction – Antimalware Check Improvement**. Druid has enhanced the Antimalware Check logic for .eml documents. Previously, if a single attachment within an email file failed security protocols (such as containing a virus, a restricted extension, or a password-protected file), the entire .eml document was discarded.

With this release, the Antimalware Engine treats .eml files as archives. If a security risk is detected within an attachment, the system now isolates and discards only the problematic file while permitting the extraction of all other safe elements, including the email body, other clean attachments, and nested email content.

* **Website Data Source – Granular Page Extraction**. Authors now have precise control over website page extraction and indexing. Previously, initiating an extraction on a parent page automatically triggered an extraction for every child page beneath it. With this release, you can extract individual parent pages independently. This provides the same targeted extraction capability available across all other Data Sources. This enhancement allows the update of specific pages without reprocessing the entire site hierarchy, resulting in significant time savings and reduced system resource consumption.

![](<../../../.gitbook/assets/web page extract.png>)

* **Web Forms – Dynamic Filtering and Update of Automations**. This release introduces enhanced programmatic control over how automations appear on forms. Authors can now use the Code Editor to dynamically manage the Automation List, allowing for a more personalized and context-aware user experience. For more information, see [Filter and update automations on forms](https://druidai.gitbook.io/druid-ai-docs/conversational-ai-apps/forms/trigger-events-on-forms#Filter).
* **Webchat – New language support**. This release adds support for Sinhala in the webchat, improving accessibility for Sinhala-speaking users.

## Bug Fixes

* **Viber File Transfer**: Resolved an issue where file uploads sent by customers via the Viber Channel were not displayed on the Agent Side.
* **Data Service Filtering**: Fixed a bug where applying a filter on decimal fields within the Data Service triggered a system error.
* **Data Service JSON Serialization**: Corrected serialization errors occurring during Data Service Update or Insert operations involving JObject and JArray structures.
* **Training Set Management**: Fixed a failure in the Evaluation module where attempts to delete a training phrase containing diacritics resulted in an "Utterance not found" warning.
* **Knowledge Base Search**: Resolved an issue where searching for the name of a structured data source returned no results despite a match existing in the system.
