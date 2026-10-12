---
title: Entity Designer
---


The Entity Designer serves as an intuitive companion, automatically structuring and presenting the best visualization of entity models to AI Agent authors, facilitating a deeper comprehension of the solution.

It consolidates as an all-in-one graphical tool, offering the following key advantages to authors:

* Enhanced understanding of entity models provided with solution templates.
* Streamlined creation of new entity models through visual representation.
* Increased productivity by seamlessly integrating Entity Designer with Flow Designer or integration editor.

The Entity Designer empowers authors with a comprehensive toolkit for managing and visualizing entity models, optimizing the AI Agent development process. It organizes all entities used for collecting user information, retrieving data, and transmitting data to other systems, categorized for ease of access. These entities are available at the tenant global level, ensuring versatility across various AI Agents. An entity may reference another entity, either a simple entity or a collection entity, fostering interconnectedness within the AI Agent informational model.

{% hint style="info" %}
**NOTE:** You can accelerate your data structure design by using **AI Authoring Agents** instead of building manually. By launching the Data Modeler from the Page Help icon, you can describe your business requirements in natural language to automatically generate or adjust entity models. For more information, see the [AI Authoring Agents](<../2_AI Agents/AI Authoring Agents.md#Create>).
{% endhint %}

## Accessing Entity Designer

To access the Entity Designer, select the AI Agent and solution, then navigate to the main menu and click on **Entities**. The Entity Designer interface appears, contextualized within the selected solution and AI Agent. If no entities are defined for the selected AI Agent, the Entities Designer list is empty.

You have three options to view the AI Agent informational model.

| View                                          | Description                                                                                                                                                                                                                           |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](<../../.gitbook/assets/list view.png>)    | **List view** presents entities in alphabetical order. ![](<../../.gitbook/assets/list entities.png>)                                                                                                                                 |
| ![](<../../.gitbook/assets/diagram view.png>) | **Diagram view** Offers a visual representation of solution entity models. ![](<../../.gitbook/assets/Entity Designer_2.png>)                                                                                                         |
| ![](<../../.gitbook/assets/tree view.png>)    | **Tree view** Displays entity memory slots as they exist in the AI Agent, facilitating productivity during flow and integration configuration. For more details, see [Understanding Entity Models.](<Understanding Entity Models.md>) |

### Available functionality

| Action                          | Description                                                                                                                                                                                                                                                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Search entity                   | Enables searching entities by exact or partial name, available in list, diagram, and tree views. _Search in list view_ ![](<../../.gitbook/assets/search diagram view.png>) _Search in diagram view_ ![](<../../.gitbook/assets/diagram search.png>) _Search in tree view_ ![](<../../.gitbook/assets/select entity.png>) |
| Filter entities                 | Filter entities by a specific field, applicable only in list view.                                                                                                                                                                                                                                                        |
| View entities within a category | Group entities into categories for efficient navigation and management, applicable only in list view.                                                                                                                                                                                                                     |
| Link / Unlink entities          | Add or remove entities to / from the current solution, streamlining solution management.                                                                                                                                                                                                                                  |
| Publish                         | Publish the entity integrations created using the CRUD template. For more information, see [Adding Entity Druid Data Services Integrations](https://druidai.gitbook.io/druid-ai-docs/ai-platform/conversational-ai-apps/entity-data-integration).                                                                                                                                         |
| Create a new entity             | Easily add new entities to the selected solution.                                                                                                                                                                                                                                                                         |
| Edit / Delete an entity         | Modify or delete entities from the selected solution, accessible through inline icons in list view and through node selection in diagram and tree views.                                                                                                                                                                  |

In diagram and tree view you can view the entity model of the current solution by clicking from the toolbar, the **In current solution** icon (![](<../../.gitbook/assets/Entity Designer_5_31x31.png>)) and all entities on your tenant, click the **Outside solution** icon (![](<../../.gitbook/assets/Entity Designer_6.png>)).

The Entity Editor allows updating entity fields seamlessly, particularly efficient in diagram and tree views.
