---
title: Add Quick Search to Table Views
---

# Add Quick Search to Table Views

Authors can enhance table views by adding a Quick Search bar, allowing users to efficiently search for specific records. The search bar retrieves data from the **Data** tab defined on the entity or from **Workspaces**.

![](<../../.gitbook/assets/search in workspaces.png>)

Adding the quick search to a view involves four main steps:

1. Add a **Kanban** view.
2. Define the view properties.
3. Add and configure columns.
4. Define the data through Integrations.

### Step 1. Add Quick Search view

To enable search, first add a new view of type **Quick Search** to the desired entity.

![](<../../.gitbook/assets/quck search add view.png>)

To define the Quick Search view, follow the instructions provided in section [Create and Design Views](https://docs.druidai.com/docs/Content/CBA/Create%20and%20Design%20Views.htm) with the following special particularities:

### Step 2. Define the view properties

In the **Details** field, enter the text that will appear when users hover over the search bar.

![](<../../.gitbook/assets/search view details.png>)

{% hint style="info" %}
**Info:** We recommend providing relevant information about what users can search for.
{% endhint %}

### Step 3. Define the view columns

Add the entity fields that users should be able to search by. For example, if users need to search views by name and description, add the Name and Description fields as columns in the Quick Search view.

![](<../../.gitbook/assets/quick search columns.png>)

### Step 4. Define search view data through integrations

{% hint style="info" %}
**NOTE:** Before creating a Query Entity integration for quick search, add the **SearchText** field of type String to the entity.
{% endhint %}

Create a Query Entity integration and configure the filtering as follows:

| Filter Property | Description                                                                                                                                                                                                                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Field Name      | Specify the field to filter. For example, to allow searching for cases by name, add \[\[Case]].Name.                                                                                                                                                                                                                           |
| Operator        | Select **contains**.                                                                                                                                                                                                                                                                                                           |
| Functions       | Two functions are available: - **Case Insensitive**: Treats uppercase and lowercase letters as the same.. ![](<../../.gitbook/assets/case insensitive search.png>) - **Normalized Accents**: Treats accented characters and their non-accented counterparts as the same. . ![](<../../.gitbook/assets/normalized accents.png>) |
| Value           | Specify the filtering value: \[\[]].SearchText.                                                                                                                                                                                                                                                                                |

![](<../../.gitbook/assets/quick search query.png>)

Next, add the Query Entity integration in the **Read Data** section of the Quick Search view.

In the **Delete Data** section, select the appropriate integration to handle record deletion from the quick search view.

![](<../../.gitbook/assets/quick search integrations.png>)

{% hint style="info" %}
**Info:** If you leave the **Delete Data** section empty (i.e., no integration selected), users will not be able to delete records from the Quick Search view, and the **Delete** icon will not appear.
{% endhint %}
