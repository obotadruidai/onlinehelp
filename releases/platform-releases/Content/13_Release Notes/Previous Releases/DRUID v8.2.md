---
title: DRUID 8.2
---


Deployment Dates

The table below lists the deployment date of DRUID v8.2 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| October 24, 2024                                     | November 21, 2024                      | November 21, 2024                            | November 21, 2024                                   |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

* REST Connector improvement and bug fix

## What's New

* **DRUID Vision – Convert PDF Page to JPEG**. A new endpoint is now available in DRUID Vision, enabling the conversion of individual PDF pages to .jpeg format. For more information, see [Convert PDF Page to JPEG](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/druid-vision/convert-pdf-page-to-jpeg).

## Improvements

* **Salesforce Live Chat - send contact center parameters**. With this release, authors can send contact center parameters to Salesforce Live Chat. For more information, see [Salesforce Live Chat](https://druidai.gitbook.io/druid-ai-docs/contact-centers/salesforce-live-chat).
* **REST Connector - Mapping Entire JSON Payload**. We’ve improved the ability to map entire JSON payloads when the response body content type is JSON. You can now easily map the full JSON response directly to a jObject or jArray field in DRUID. Simply toggle **Map Entire JSON Payload** and select the appropriate jObject or jArray field from the **JSON Field** drop-down to store the payload.

![](<../../../.gitbook/assets/json mapping (1).png>)

* **Knowledge Base improvements**. This release introduces various improvements to the KB:
* **Shared Drive data sources - added support for SFTP**. We’ve added support for SFTP in network shared drive data sources. You can now connect to an SFTP server using SFTP login credentials (username and password). Public key authentication will be supported in a future release.

![](../../../.gitbook/assets/SFTP.png)

For more information, see [Network shared drive data sources](https://druidai.gitbook.io/druid-ai-docs/knowledge-base/knowledgebase/data-sources/network-shared-drive-data-sources).

* **Network shared drive and SharePoint data sources - Download Original File**. In this release, for Network shared drive and SharePoint data sources, users now have the capability to download the original file version that was uploaded into the data source. This feature enables users to access the original version of files, providing them with the ability to compare it with any updated or modified extracted articles.

![](<../../../.gitbook/assets/download file (1).png>)

* **Network shared drive data sources - Export to Excel**. You can now export document-level data to Excel from network shared drive data sources. The export generates a table with two columns: Question (the article title) and Answer (the article body or paragraph). This feature works for all extracted articles from supported documents, including Excel files, Word documents, and PDFs.

![](<../../../.gitbook/assets/export to excel (1).png>)

* **File repository, SharePoint, Network shared drive data sources - file extension and size**. For data sources of type File Repository, SharePoint, and Network Shared Drive, you can now view the file extension and size at the folder level. This new feature is particularly helpful when you need to download original files and want to quickly assess their size.

![](<../../../.gitbook/assets/file size.png>)

{% hint style="info" %}
**NOTE:** There is a maximum file size limit of 20 MB for downloading original files in DRUID
{% endhint %}

* **Data source actions available at the tree element level**. During processes like crawling, extracting, and training, you can perform a limited set of actions specific to the data source type.

Example: File repository data sources

![](<../../../.gitbook/assets/specific action.png>)

* **Portal Indicator for Required Publishing**. An orange vertical bar now appears next to a record when specific changes are made, indicating that a publish is required. The following actions trigger a mandatory publish:
* **Create**: Entity, Entity Field, Document Template, Integration, Integration Task, App.
* **Edit**: Entity Field, Document Template, Integration, Integration Task, App.
* **Delete**: Entity, Entity Field, Document Template, Integration, Integration Task, App.

![](../../../.gitbook/assets/indicator.png)

## Bug Fixes

* **Solution Export/Import fix**. We fixed an issue where REST integrations using SAML Assertion Authentication did not properly include the SAML assertion XML and non-sensitive variables during solution export/import. Now, when exporting or importing solutions, the SAML assertion XML and all non-sensitive variables are included.
