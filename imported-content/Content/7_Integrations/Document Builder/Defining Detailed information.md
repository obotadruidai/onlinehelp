---
title: "Defining Detailed information - table"
---

<a id="DefiningDetailedinformationtable"></a>


When using the Druid Document Builder to generate Excel reports, you can dynamically populate tables with repeating rows of data. This is achieved by mapping an Entity List (a collection of records under an umbrella request entity) to a designated table area in your Excel template.

The document generator automatically loops through each record in the specified list, rendering a new row in the spreadsheet for every item and maintaining a clean user experience for those reading the generated files.

If you want in the excel template to create a table that will return records from a collection, follow these steps:

1. Create the table header.
2. In the first table row, below the table header, invoke the desired fields from your collection, using the following syntax:

**Nested Fields inside Entity Lists inside Entity Lists**

To traverse relationship/entity-type fields nested inside your repeating collections:

**%EntityName.EntityFieldOfTypeEntityList.ReferencedEntityField(scalar field)**

![](../../Resources/Images/Document%20Builder/Defining%20Detailed%20information.png)

You can map both parent and child properties of the same collection on the same level in the first row of the table. To do so, in a column enter the desired field from your collection using the syntax provided above and in the subsequent columns map the desired low level (child) scalar fields using the following syntax:

**%**EntityName**.**EntityFieldOfTypeEntityList**.**ReferencedEntityFieldofTypeEntity**.**ScalarField - for scalar field in a collection or

**%**EntityName**.**EntityFieldOfTypeEntityList**.**ReferencedEntityFieldofTypeEntityList**.**ScalarField - for scalar field in a collection within another collection.

> **NOTE:** To generate a nicely ordered excel table, only use cascaded collection (collection in collection); using two collections on the same row in a document template will generate a table that is hard to read.

> **Info:** You can use [arguments](#Arguments) to further customize the worksheet.

Example: Generate a report with the list of persons and their street (taken from the person's address)

- We have an entity called **[[Report]]** that a field **Persons** of type Entity List referencing the **[[Person]]** entity.
- The **[[Person]]** entity contains two fields as follows:

- **Name** - a scalar field (string)
- **Address** - a field of type Entity which has a scalar field, **Street**.

In the first table row, below the table header, we invoke the desired **Name** and **Street** fields from our collection as described in the figure below.

![](../../Resources/Images/Document%20Builder/mapping%20parent%20and%20child.png)

> **Info:** The generated document will contain as many rows as records are in the collection (in this case in the [[Persons]] collection).

**Nested Fields inside Entity-type Fields**

> **Info:** This feature is available starting with Druid 9.27.

To pull properties from a related entity directly, without having to use a Set Variable flow step to flat-map them first:

**Syntax**: %[ParentEntity].[RelatedEntityField].[FieldName]

**Example**: **%Airport.Description.Name** (Retrieves the Name field directly from the related Description entity).

3. Use formulas as best suits your needs.

This is an example of how a generated document might look like in pdf format:

![](../../Resources/Images/Document%20Builder/Defining%20Detailed%20information_1.png)

<a id="Arguments"></a>

## <a id="Arguments"></a>Arguments

You can specify the following arguments to customize the worksheet.

<a id="merge"></a>

### merge

This argument merges the cells in the column for each object set while filling in data from nested collections.

#### Syntax

**%EntityName.EntityField**;merge

**%EntityName.EntityFieldOfTypeEntityList.ReferencedEntityFieldofTypeEntityList**;merge

> **Info:** When getting data from a cascaded collection, to ensure that you get a nice output we recommend you not to use **merge** on the last level scalar fields from the collection (in the last column of your table) unless you really want to merge that data.

#### Example

The figure below provides an input template example.

![](../../Resources/Images/Document%20Builder/merge%20syntax.png)

The figure below shows the generated document using the above Excel template example.

![](../../Resources/Images/Document%20Builder/merge%20output.png)

<a id="repeat"></a>

### repeat

This argument repeats the value for the corresponding records in the column while filling in data from nested collections.

#### Syntax

**%EntityName.EntityFieldOfTypeEntityList.ReferencedEntityFieldofTypeEntityList**;repeat

#### Example

The figure below provides an input template example.

![](../../Resources/Images/Document%20Builder/repeat.png)

The figure below shows the generated document using the above Excel template example.

![](../../Resources/Images/Document%20Builder/repeat%20output.png)

<a id="collapsegroup"></a>

### collapsegroup

This argument groups the cells in the column for each object set and collapses the data from nested collections.

#### Syntax

**%EntityName.EntityFieldOfTypeEntityList.ReferencedEntityFieldofTypeEntityList**;collapsegroup

#### Example

The figure below provides an input template example.

![](../../Resources/Images/Document%20Builder/collapse.png)

The figure below shows the generated document using the above Excel template example.

![](../../Resources/Images/Document%20Builder/collapse%20output.png)

<a id="expandgroup"></a>

### expandgroup

This argument groups the cells in the column for each object set and expands the data from nested collections.

#### Syntax

**%EntityName.EntityFieldOfTypeEntityList.ReferencedEntityFieldofTypeEntityList**;expandgroup

#### Example

The figure below provides an input template example.

![](../../Resources/Images/Document%20Builder/expand%20group.png)

The figure below shows the generated document using the above Excel template example.

![](../../Resources/Images/Document%20Builder/merge%20output.png)
