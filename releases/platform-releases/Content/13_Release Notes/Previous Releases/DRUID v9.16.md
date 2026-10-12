---
title: Druid 9.16
---


Deployment Dates

The table below lists the deployment date of DRUID v9.16 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| February 12, 2026                                    | March 12, 2026                         | March 12, 2026                               | March 12, 2026                                      |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

**Recommended!** This release includes features that require upgrade of your Druid Connector Host:

* Web Views and Forms: Native File Access (Hybrid & On-Premise)

## What's New

* **KB Web Crawler - Authentication Support (Technology preview)**. You can now index password-protected websites and private portals. The web crawler supports authenticated access, allowing you to index content that was previously unreachable behind a login screen.
* To enable authenticated crawling, ensure **Crawl using HTTP requests** is disabled in your crawler configuration.
* Crawl login-protected websites by providing user credentials and the authentication page URL.

![](<../../../.gitbook/assets/web auth.png>)

* Configure authentication during data source creation or update settings anytime in the data source details.

![](<../../../.gitbook/assets/WEB AUTH DETAILS CRAWL.png>)

## Improvements

* **Bypass email confirmation for system users**. Druid now allows system users with specific API permissions to bypass the email confirmation step during login. This change streamlines automated workflows and service-level integrations where manual email verification is impractical.

Users with the following permissions no longer require email confirmation:

* DruidBackendAPI
* DruidServiceAPI
* **Webchat - Multiple file upload support**. The web chat now supports multiple file upload via drag-and-drop. To enable this feature, authors must configure the File Upload steps by entering in Input Mapping an entity list field that references the \[\[File]] entity.

![](<../../../.gitbook/assets/darg and drop.png>)

* **Knowledge Base Schedule Improvements**. We have enhanced the KB scheduler to provide more flexibility:
* **Indefinite scheduling**. The scheduler end date is no longer required by default. Schedules will now run indefinitely unless you choose to specify a stop date.
* **Flexible monthly cadence**. You can now configure the scheduler to trigger monthly on the first day, the last day, or a specific custom date at your preferred time.

![](<../../../.gitbook/assets/start date.png>)

* **Druid Data Service Connector - Aggregating large data sets across entities optimization**. You can now efficiently join related entity fields and aggregate large data sets in Druid custom queries. For more information, see [Joining with Entity Fields for Large Data Volumes](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/data-and-storage/druid_data_-service_connector/filter-using-druid-custom-query#Joining).
* **Optimized Deepgram STT Provider Switching**. If Deepgram is set as the primary STT provider and Azure as fallback, and the user selects a language unsupported by Deepgram, the system falls back to Azure. Once the user changes the language back to one that Deepgram supports, the system will automatically switch back to Deepgram (the primary provider) for the remainder of the session.

This automatic fallback and recovery mechanism happens seamlessly and has no impact on the voice interaction performance or the execution of flows in the active chat session.

* **Webchat - improved user experience**. The Webchat now includes a "typing" animation (three dots) that appears while the AI Agent is generating a response. This indicator ensures users are aware that their input is being processed, providing a seamless conversational experience.

![](<../../../.gitbook/assets/typing event.png>)

* **Druid Vision improvements - Enhanced OCR image validation**. Image OCR endpoints now analyze image quality and return detailed error messages that specify why an input was rejected, helping you quickly resolve validation issues.

## Bug Fixes

* **KB PDF Extraction Fix**. Resolved an issue preventing page numbers from rendering in the Content area during PDF extraction. Backend data synchronization has been restored for all extraction methods.

![](<../../../.gitbook/assets/page number.png>)

* **Druid Vision Document Translation**. Resolved an issue where translated text overlapped the original content on rotated document scans. Translated content now maintains proper positioning regardless of document rotation.
