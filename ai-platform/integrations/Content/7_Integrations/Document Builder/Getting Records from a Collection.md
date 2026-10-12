---
title: "Getting Records from a Collection (table)"
---

<a id="GettingRecordsfromaCollectiontable"></a>


If you want to add more detailed information in your Word template, create a table that will return records from a collection:

1. Create the table header (if any needed).
2. In the first cell of the first row, add a merge field to specify the field of type Entity List, which is a field of the request entity (selected on the DRUID connector). Use the following **TableStart:**The name of the field of type Entity List to let the Document\_Generator connector know that you request data from a collection. Then in the same cell add a merge field for your specific field from the referenced entity (collection).
3. In the other cells on the same row, enter merge fields for the referenced entity fields you want to include in the table.
4. In the last column, also include a merge field for the closing tag **TableEnd:**The name of the field of type Entity List.

{% hint style="info" %}
**NOTE:**

- DRUID’s Document\_Generator connector will generate as many rows in the table as records are in the collection (the invoked Entity List field).
- You can also insert basic text in the table together with the merge fields or in different columns. The basic text that is the same in all of the generated documents.
{% endhint %}

The table below provides you with an overview of what a table might look like.

| Table Header | Table Header | Table Header | Table Header |
| --- | --- | --- | --- |
| <<TableStart:The name of the field of type Entity List>> <<Field from Referenced Entity>> | <<Field from Referenced Entity>> | Basic text <<Field from Referenced Entity>> | <<Field from Referenced Entity>> <<TableEnd:The name of the field of type Entity List>> |
