---
title: "Add Quick Search to Table Views"
---

<a id="AddQuickSearchtoTableViews"></a>


Authors can enhance table views by adding a Quick Search bar, allowing users to efficiently search for specific records. The search bar retrieves data from the **Data** tab defined on the entity or from **Workspaces**.

![](../Resources/Images/CBA/search%20in%20workspaces.png)

Adding the quick search to a view involves four main steps:

1. Add a **Kanban** view.
2. Define the view properties.
3. Add and configure columns.
4. Define the data through Integrations.

<a id="Step1AddQuickSearchview"></a>

## Step 1. Add Quick Search view

To enable search, first add a new view of type ****Quick Search**** to the desired entity.

![](../Resources/Images/CBA/quck%20search%20add%20view.png)

To define the Quick Search view, follow the instructions provided in section [Create and Design Views](<https://docs.druidai.com/docs/Content/CBA/Create%20and%20Design%20Views.htm>) with the following special particularities:

<a id="Step2Definetheviewproperties"></a>

## Step 2. Define the view properties

In the **Details** field, enter the text that will appear when users hover over the search bar.

![](../Resources/Images/CBA/search%20view%20details.png)

> **Info:** We recommend providing relevant information about what users can search for.

<a id="Step3Definetheviewcolumns"></a>

## Step 3. Define the view columns

Add the entity fields that users should be able to search by. For example, if users need to search views by name and description, add the Name and Description fields as columns in the Quick Search view.

![](../Resources/Images/CBA/quick%20search%20columns.png)

<a id="Step4Definesearchviewdatathroughintegrations"></a>

## Step 4. Define search view data through integrations

> **NOTE:** Before creating a Query Entity integration for quick search, add the **SearchText** field of type String to the entity.

Create a Query Entity integration and configure the filtering as follows:

| Filter Property | Description |
| --- | --- |
| Field Name | Specify the field to filter. For example, to allow searching for cases by name, add [[Case]].Name. |
| Operator | Select **contains**. |
| Functions | Two functions are available:   - **Case Insensitive**: Treats uppercase and lowercase letters as the same..  ![](../Resources/Images/CBA/case%20insensitive%20search.png) - **Normalized Accents**: Treats accented characters and their non-accented counterparts as the same. .  ![](../Resources/Images/CBA/normalized%20accents.png) |
| Value | Specify the filtering value: [[<Entity>]].SearchText. |

![](../Resources/Images/CBA/quick%20search%20query.png)

Next, add the Query Entity integration in the **Read Data** section of the Quick Search view.

In the **Delete Data** section, select the appropriate integration to handle record deletion from the quick search view.

![](../Resources/Images/CBA/quick%20search%20integrations.png)

> **Info:** If you leave the **Delete Data** section empty (i.e., no integration selected), users will not be able to delete records from the Quick Search view, and the **Delete** icon will not appear.
