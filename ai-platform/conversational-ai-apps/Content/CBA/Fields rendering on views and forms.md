---
title: "Fields Rendering on Views and Forms"
---

<a id="FieldsRenderingonViewsandForms"></a>


This sections describes how the different types of fields are rendered on views and forms.

| Field Type | Rendering |
| --- | --- |
| Boolean | A switch on / off button. After the user switches on / off the form displays **True**/**False**. |
| Currency | The fields of type currency display the name of the currency at the right of the amount.  **NOTE:** The rendering of the Currency fields is available in DRUID 5.20 and higher. |
| String | Aligned to left. |
| Integer | Aligned to the right. |
| Decimal | Aligned to the right. |
| URL | Clickable link, which when clicked will redirect you to a new browser page. |
| Email | Email format. When clicked, the user’s email client opens and the **To** field is automatically filled in with the email from the form. |
| Date | Date and Time format. The date and time is aligned with the user's profile time zone or user's Language selection. |
| InvariantDate | Date and Time format in UTC. |
| Lookup | Loads the default view of the referenced entity and displays in the list the property Name from where the user can choose a record.  **NOTE:** The fields of type **Lookup** are only available on forms. In DRUID 5.16 and higher you can set a view different than the default view of the referenced entity. |
| File (an entity field of type Entity referencing the File system entity) | Web forms allows uploading files, similar to how the Flow Engine captures files via chat. Web views and forms display the links to download the respective files.  **NOTE:** DRUID is not a File repository; it only handles the files in transit. DRUID captures files from the user (via chat and web forms) and passes them to integrations that further store the files file and responds back with the links. Example: Azure Blob storage, Azure File storage, SharePoint, other Document Management System. Learn how to [use file upload on web views and forms](FileUpload.md). |
