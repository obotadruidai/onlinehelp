---
title: "Managing Entity Records"
---

<a id="ManagingEntityRecords"></a>


Business users and authors can manage (add, edit and delete) entity records displayed in views based on the workspace permissions granted to the assigned security role. For more information, see [Define specific security roles for business users](Define%20Security%20Roles%20for%20Business%20Users.md).

While business users consume the data in workspace views, the authors consume the data in entity settings. A use case scenario for authors is managing records for entities of type dictionary (e.g., CaseOrigin, CaseStatus, CaseType, etc.) regardless their data source.

To manage records as a business user, in the desired workspace access the view. On the workspace menu, click on the desired link (entity). The default view specific to that link (entity) displays.

{% hint style="warning" %}
**IMPORTANT!** You need to upgrade both the DRUID Connector Host to version 5.29 or higher and the entity associated with the web view to add the PageInfo system entity field; otherwise, loading the web view will fail.
{% endhint %}

If you want to view another view, from the **Views** drop-drop-down select the desired view.

![](../Resources/Images/CBA/helpdesk%20agent%20workspace.png)

To manage entity records as an author, select the solution and workspace from the drop-downs at the top of the Druid Portal. On the **Solution Contents** menu, click **Entities,** In the Entities page, click on the desired entity, then click the **Data** tab. By default, the default view displays. If you want to view another view, from the **Views** drop-drop-down select the desired view.

![](../Resources/Images/CBA/Data%20default%20view.png)

The procedures for managing entity records in a view is the same for both business users and authors.

<a id="Addingrecords"></a>

## Adding records

You have two options for adding a new record to a view:

- From the view by clicking the **New Record** button (![](../Resources/Images/CBA/new%20record%20button.png)) at the top right corner of the view.
- While viewing the details of an entity record by clicking the **New Record** icon at the top-right corner of the form.

![](../Resources/Images/CBA/nrew%20record%20in%20form.png)

Regardless from where you choose to add a new record, the entity record configuration page appears. Complete the form by providing the desired entity record details and click one of the save icons at the top-right corner of the form based on what you want to happen after save.

Fields of specific type or with specific properties have specific particularities when completing a form, as follows:

- **Multilingual fields**. Multilingual fields are marked with a specific icon (![](../Resources/Images/CBA/multilingual%20icon.png)). When clicking a multilingual field, the country flag corresponding to the current user language appears indicating the user that the input value will be saved in the context of that language.

![](../Resources/Images/CBA/set%20up%20multilimgual%20fields.png)

- When clicking a field of type **Date** and **InvariantDate**, the date picker displays allowing you to select the date.
- **Upload file**. When clicking on a field of type entity referencing the File system entity, the **Choose file** button appears.

![](../Resources/Images/CBA/choose%20filebutton.png)

{% hint style="info" %}
**NOTE:**

- DRUID supports uploading the following file extensions: .pdf, .png, .jpg, .jpeg, .doc, .docx, .xls, .xlsx, .odt, .ods, .tiff, .tif, .mp3, .mp4, .mkv, .webm, .txt, .json and .csv.
- After you choose the desired file and click the **Save** icon (![](../Resources/Images/CBA/save%20file%20on%20form.png) ) at the top-right corner of the form, DRUID performs file extension and malware validation. If the validations pass, the file is uploaded and appears as download link in the form.

![](../Resources/Images/CBA/file%20downlaod%20link.png)
{% endhint %}

<a id="Editrecords"></a>

## Edit records

To edit an entity record in a view, go to the desired view and click the **Edit** icon displayed inline with the entity record you want to edit.

![](../Resources/Images/CBA/edit%20record%20icon.png)

The entity record default form in edit mode appears. For fields that have not been set as read-only, you can edit their values. Navigate through the form tabs (if it’s a multi-tab form) and scroll-down sections to edit the field values as you need.

<a id="Deleterecords"></a>

## Delete records

You have two options for deleting entity records:

- From the view by clicking the **Delete** icon (![](../Resources/Images/CBA/delete%20icon.png)) displayed inline with the entity record you want to delete.
- While viewing the record details by clicking the **Delete** icon (![](../Resources/Images/CBA/delete%20icon.png)) at the top-right corner of the form.

![](../Resources/Images/CBA/delete%20record%20from%20form.png)

<a id="Deleterecordsinbulk"></a>

### Delete records in bulk

{% hint style="info" %}
**NOTE:** This feature is available in DRUID 5.27 and higher. It requires DRUID Connector Host upgrade to version 5.27 or higher and DRUID Data Service upgrade to the latest version.
{% endhint %}

In the views that display records from DRUID Data Service only, you can delete multiple records in bulk by selecting the records you want to delete and then clicking the **Delete** button at the top-right corner of the page.

![](../Resources/Images/druid%205.27/view_delete%20bulk.png)
