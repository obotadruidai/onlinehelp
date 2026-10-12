---
title: Understanding Entity Models
---


Entity Diagrams simplify AI Agent authoring by providing a graphical representation of Enterprise Data Models. Druid offers industry-specific predefined templates, empowering users to design rich Data Models comprising hundreds of entities and fields. The Entity Diagram visualizes all business object relations within a solution, offering a familiar and intuitive interface that streamlines entity configurations. This enhances platform versatility and simplifies deployments, even for the most complex use-cases.

In diagram view mode, the Entity Diagram offers insights into the entity models included in solution templates. This visualization authors understand the building blocks necessary for designing, building, testing, and deploying AI Agents.

The Entity Diagram layout is the following:

* Primary entities (nodes) are positioned in the center.
* Referenced entities are displayed on the right side.
* Entities referencing primary entities are shown on the left side.

![](<../../.gitbook/assets/Entity Designer_7.png>)

The table below lists the diagram visual elements.

| Element                                             | Description                                                                                                                                            |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![](<../../.gitbook/assets/Entity Designer_10.png>) | Node (entity)                                                                                                                                          |
| ![](<../../.gitbook/assets/Entity Designer_11.png>) | Indicates a relationship between two entities.                                                                                                         |
| ![](<../../.gitbook/assets/Entity Designer_12.png>) | Indicates entity references another entity (that is, the entity has field of type Entity referencing another entity).                                  |
| ![](<../../.gitbook/assets/Entity Designer_13.png>) | Indicates entity references an entity storing a collection of records. (that is, the entity has field of type Entity List referencing another entity). |
| ![](<../../.gitbook/assets/Entity Designer_14.png>) | **Available for tree view only!** Indicates an entity referencing other entities. To view the referenced entities, click this icon.                    |
| ![](<../../.gitbook/assets/Entity Designer_16.png>) | **Available for tree view only!** Indicates recursion to the primary node (primary entity).                                                            |

The tree view lists all solution entities, with the primary entity displayed at the top. Users can observe entity memory slots as they appear in the AI Agent.

![](<../../.gitbook/assets/Entity Designer_8.png>)

Using the Entity Designer in tree view side-by-side with flows or integrations configuration increases authors productivity as you can copy to clipboard the entity and entity fields label (etiquette) and paste it in the desired flows and integration (in messages, input mapping or fields mapping).

The label has the following format: \[\[Entity]] for entities, \[\[ Entity]]. for fields and \[\[Entity]].\[\*] for collections. When using the label in integrations or on flows, replace the \* with an index.

![](<../../.gitbook/assets/Entity Designer_9.png>)

The Entity Designer (diagram / tree view) provides insights into entity usage, including:

* Number of fields within the entity.
* Number of flows and integrations using the entity.
* Whether the entity is trained for Natural Language Processing (NLP).

You can view detailed entity information by clicking on it.

The Entity Designer facilitates navigation to specific flows or integrations where the selected entity is utilized, enhancing efficiency.

You to easily navigate to a specific flow or integration where the selected entity is utilized. Simply click on either the Flows or Integrations section, and then click on the "go to" link icon (![](<../../.gitbook/assets/Entity Designer_20.png>)). This functionality streamlines the process of locating and accessing relevant flows and integrations associated with the selected entity.

![](<../../.gitbook/assets/Entity Designer_21.png>)

## Related Topics

* [Defining the Integration Actions](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/defining-the-integration-actions)
* [Set Variables](<../4_Flows/Set Variables.md>)
