---
title: "Creating Excel Templates"
---

<a id="CreatingExcelTemplates"></a>


The excel template contains the basic text that is the same in all of the generated documents and entity-sourced dynamic data that vary from one generated document to another.

Excel templates are useful when you want to generate a document, which contains both flat and detailed information. While flat information refers to getting dynamic data from an entity, detailed information refers to returning records from a collection.

<a id="Prerequisite"></a>

## Prerequisite

- Before creating templates, you need to define the entities from which the Document\_Generator connector will merge entity-sourced dynamic data. If you want to dynamic generate a table, which contains records from a collection, make sure that on your parent entity there is a field of type Entity List, which references a collection entity.

{% hint style="info" %}
**NOTE:**

- Any formatting you do in the excel template (including formatting of entity fields) is kept in the generated document.
- If you have formulas in the excel file, Excel will calculate those formulas providing the formula result in the generated file.
- You should invoke entity fields in single cells, do not invoke entity fields in the same cell where you provide text; otherwise, the document generation will fail.
{% endhint %}

<a id="Sampleinformationusedthroughoutthissection"></a>

## Sample information used throughout this section

To better understand the creation of excel templates; let’s consider the entity [[Client]]. The Client entity is the request entity from which the Document\_Generator connector will merge entity-sourced dynamic data. It contains fields, which store information related to clients.

The field [[Client]].Product is of type Entity List and references the entity [[Article]], which is a collection. The entity [[Article]] contains fields, which store information related to articles.

![](../../Resources/Images/Creating%20Excel%20Templates/Creating%20Excel%20Templates.png)

{% hint style="info" %}
**Info:** If your Excel template needs to pull data from a nested entity within an Entity List (e.g., pulling a category name from a relation field on a product list item), you can use dot-notation paths such as **%ParentEntity.EntityList.ChildEntity.FieldName**.
{% endhint %}
