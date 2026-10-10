---
title: Creating Word Document Templates
---

# Creating Word Document Templates

The word document template might contain the basic text that is the same in all of the generated documents. It may contain a letterhead, text, and entity-sourced dynamic data that vary from one generated document to another.

To invoke entity fields within the Word Document, use Merge Fields. The Document\_Generator connector will merge entity-sourced dynamic data into the output documents (doc, docx, pdf).

### Prerequisite

* Before creating templates, you need to define the request entity from which the Document\_Generator connector will merge entity-sourced dynamic data. If you have fields of type Entity or Entity List, you need to define the referenced entities as well.

When invoking entity fields within the Word template, follow these rules:

1. Add a MergeField to specify the request entity (selected on the Druid connector) using the tag **TableStart:**. Use the following syntax: \*\*TableStart:\*\*EntityName.
2. Add MergeFields to include entity fields (flat information). When adding a merge field, provide the name of the entity field.
3. If you also want to include entity fields of type Entity, you need to include the **TableStart** and **TableEnd** tags specifying the name of the field of type Entity. Between the tags, you can add Merge Fields for as many fields you want to include from the referenced entity. For each merged field, provide the name of the field from the referenced entity.

You can also use merge fields in tables, which return a collection of records. For more information, see [Getting Records From a Collection (table)](<Getting Records from a Collection.md>)

4. Add a MergeField to specify end tag **TableEnd:** using the syntax: \*\*TableEnd:\*\*EntityName.

Below is a complex merge fields scheme to use within word templates:

<[TableStart:EntityName](TableStart:EntityName)>

<>

<\<TableStart:The name of the field of type Entity or Entity List>>

<>

<>

<\<TableEnd:The name of the field of type Entity or Entity List>>

<>

<[TableEnd:EntityName](TableEnd:EntityName)>

Example:

![](<../../../.gitbook/assets/Creating Word Document Templates.png>)

{% hint style="info" %}
**NOTE:**

* The **TableStart** and **TableEnd** merge fields (tags) will not appear in the output document.
* Always edit an existing merge field in a document by right clicking on it and clicking **Edit Field…**.

<img src="../../../.gitbook/assets/Creating Word Document Templates_1.png" alt="" data-size="original">

The Field page appears and you can make the desired changes.

* Any formatting you do in the Word template (including merged fields/data) is kept in the output document. To format merge fields, you need to format including the enclosing merge field characters (**<< >>**).
* If you want to include flat information in the template Header or Footer, you can do so by using merge fields as well.
{% endhint %}
