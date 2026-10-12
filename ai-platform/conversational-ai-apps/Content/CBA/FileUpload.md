---
title: File Upload in Web Views and Forms
---


Web views and forms allows uploading files, similar to how the Flow Engine captures files via chat. Web views and forms display the links to download the respective files.

![](<../../.gitbook/assets/choose filebutton.png>)

{% hint style="info" %}
**NOTE:** DRUID is not a File repository; it only handles the files in transit. DRUID captures files from the user (via chat and web views and forms) and passes them to integrations that further store the files file and responds back with the links. Example: Azure Blob storage, Azure File storage, SharePoint, other Document Management System.
{% endhint %}

If you add a field of type File on a view or form, the integrations you add on the view / form require the following special configuration:

* On **Create** and **Update**, add as the first integration task an integration that allows the file creation / upload in an external document management system that you are using.

![](<../../.gitbook/assets/create and update integrations.png>)

* On **Read**, add an integration task to read the file from the document management system and get the URL of the file which has been uploaded.

![](<../../.gitbook/assets/get atatchment.png>)

![](<../../.gitbook/assets/get atatchment 2 response.png>)

## Related Topics

* [Azure Blob Storage Connector](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/azure-blob-storage-connector)
