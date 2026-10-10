---
title: Managing Entity Records
---

# Managing Entity Records

Business users and authors can manage (add, edit and delete) entity records displayed in views based on the workspace permissions granted to the assigned security role. For more information, see [Define specific security roles for business users](<Define Security Roles for Business Users.md>).

While business users consume the data in workspace views, the authors consume the data in entity settings. A use case scenario for authors is managing records for entities of type dictionary (e.g., CaseOrigin, CaseStatus, CaseType, etc.) regardless their data source.

To manage records as a business user, in the desired workspace access the view. On the workspace menu, click on the desired link (entity). The default view specific to that link (entity) displays.

{% hint style="warning" %}
**IMPORTANT!** You need to upgrade both the DRUID Connector Host to version 5.29 or higher and the entity associated with the web view to add the PageInfo system entity field; otherwise, loading the web view will fail.
{% endhint %}

If you want to view another view, from the **Views** drop-drop-down select the desired view.

![](<../../.gitbook/assets/helpdesk agent workspace.png>)

To manage entity records as an author, select the solution and workspace from the drop-downs at the top of the Druid Portal. On the **Solution Contents** menu, click **Entities,** In the Entities page, click on the desired entity, then click the **Data** tab. By default, the default view displays. If you want to view another view, from the **Views** drop-drop-down select the desired view.

![](<../../.gitbook/assets/Data default view.png>)

The procedures for managing entity records in a view is the same for both business users and authors.

### Adding records

You have two options for adding a new record to a view:

* From the view by clicking the **New Record** button (![](<../../.gitbook/assets/new record button.png>)) at the top right corner of the view.
* While viewing the details of an entity record by clicking the **New Record** icon at the top-right corner of the form.

![](<../../.gitbook/assets/nrew record in form.png>)

Regardless from where you choose to add a new record, the entity record configuration page appears. Complete the form by providing the desired entity record details and click one of the save icons at the top-right corner of the form based on what you want to happen after save.

Fields of specific type or with specific properties have specific particularities when completing a form, as follows:

* **Multilingual fields**. Multilingual fields are marked with a specific icon (![](<../../.gitbook/assets/multilingual icon.png>)). When clicking a multilingual field, the country flag corresponding to the current user language appears indicating the user that the input value will be saved in the context of that language.

![](<../../.gitbook/assets/set up multilimgual fields.png>)

* When clicking a field of type **Date** and **InvariantDate**, the date picker displays allowing you to select the date.
* **Upload file**. When clicking on a field of type entity referencing the File system entity, the **Choose file** button appears.

![](<../../.gitbook/assets/choose filebutton.png>)

{% hint style="info" %}
**NOTE:**

* DRUID supports uploading the following file extensions: .pdf, .png, .jpg, .jpeg, .doc, .docx, .xls, .xlsx, .odt, .ods, .tiff, .tif, .mp3, .mp4, .mkv, .webm, .txt, .json and .csv.
* After you choose the desired file and click the **Save** icon (![](<../../.gitbook/assets/save file on form.png>) ) at the top-right corner of the form, DRUID performs file extension and malware validation. If the validations pass, the file is uploaded and appears as download link in the form.

<img src="../../.gitbook/assets/file downlaod link.png" alt="" data-size="original">
{% endhint %}

### Edit records

To edit an entity record in a view, go to the desired view and click the **Edit** icon displayed inline with the entity record you want to edit.

![](<../../.gitbook/assets/edit record icon.png>)

The entity record default form in edit mode appears. For fields that have not been set as read-only, you can edit their values. Navigate through the form tabs (if it’s a multi-tab form) and scroll-down sections to edit the field values as you need.

### Delete records

You have two options for deleting entity records:

* From the view by clicking the **Delete** icon (![](<../../.gitbook/assets/delete icon.png>)) displayed inline with the entity record you want to delete.
* While viewing the record details by clicking the **Delete** icon (![](<../../.gitbook/assets/delete icon.png>)) at the top-right corner of the form.

![](<../../.gitbook/assets/delete record from form.png>)

#### Delete records in bulk

{% hint style="info" %}
**NOTE:** This feature is available in DRUID 5.27 and higher. It requires DRUID Connector Host upgrade to version 5.27 or higher and DRUID Data Service upgrade to the latest version.
{% endhint %}

In the views that display records from DRUID Data Service only, you can delete multiple records in bulk by selecting the records you want to delete and then clicking the **Delete** button at the top-right corner of the page.

![](<../../.gitbook/assets/view_delete bulk.png>)
