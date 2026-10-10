<a id="DRUID512"></a>

# DRUID 5.12

Deployment Dates

The table below lists the deployment date of DRUID v5.12 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| April 20, 2023 | May 11, 2023 | May 11, 2023 | May 11, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host to the latest version:

- Connector Designer

<a id="WhatsNew"></a>

## What's New

- **Added support for sample value in NER mark element**. Providing sample values for NER in flow or flow step utterances offers complete training phrases, which improves the quality of the trained NLP model (useful especially for the semantic model). Providing sample values for NER is simple. You provide complete training phrases, then in each of the training phrases with NER, select the word / sequence of words where the NLP engine should extract entity values, click on selection and select the target entity where the values will be stored.

![](../../Resources/Images/Druid%205.12/select%20word.png)

![](../../Resources/Images/Druid%205.12/selected%20target.png)

The sample value will be highlighted (in green for entity and entity list and in blue for flat data type - integer, string, etc.) and marked with a label based on the selected entity type.

![](../../Resources/Images/Druid%205.12/sample%20word.png)

![](../../Resources/Images/Druid%205.12/integer%20sample.png)

![](../../Resources/Images/Druid%205.12/date%20sample%20values.png)

> **NOTE:** This feature is backwards compatible, the training phrases with NER on flows and flow steps remain unchanged; however, we recommend you to update the training phrases with NER to provide sample values for entities.
>
> ![](../../Resources/Images/Druid%205.12/backwards%20compatible.png)

For more information, see [Using NER in Dialogs](../../Conversational%20AI/Using%20NER%20in%20Dialogs.md), [Using NER with Index Entities](../../Conversational%20AI/Using%20NER%20with%20Index%20Entities%20%28DRUID%20versions%20prior%20to%205.15%29.md), [Using NER with Intent Recognition](../../Conversational%20AI/Using%20NER%20with%20Intent%20Recognition.md) and [Improving the AI Agent NER](../../Conversational%20AI/Improving%20AI%20Agent%20NER.md).

- **Multiple dashboards available in workspaces**. You can put at business users disposal data from web views and charts by adding multiple dashboards to workspaces.

![](../../Resources/Images/CBA/show%20data.png)

For information on how to author dashboards and how to add them to workspaces, see [Create Dashboards](../../CBA/Create%20Dashboards.md).

- **Connector Designer**. Available in technology preview, the Connector Designer enables you to create complex automations: define the integration steps (for a connector action), add integration tasks, set conditions on integration tasks, link tasks, etc.
> **IMPORTANT!** If you define a complex automation using the Connector Designer, do any subsequent changes using the Connector Designer; otherwise, the automation will break.

![](../../Resources/Images/CNN%20Designer/designer%20overview.png)

For more information, see [Connector Designer](../../7_Integrations/Connector%20Designer/Connector_Designer.md).

- **NLU.NER.Utterance.KeepPunctuation** NLP parameter is now available and you can use it remove punctuation both at training and predict time, only if you set **NLU.NER.Classification.UseSemantic** to **false**, meaning that the default algorithm is used for classification. For more information, see [NLP Special Parameters](../../Conversational%20AI/NLP%20Special%20Parameters.md).

<a id="Improvements"></a>

## Improvements

- **Utterances used for soft trigger are now highlighted** - Utterances used for soft trigger (e.g., utterances used on hero card buttons) are highlighted in flow and flow step training phrases. Trying to delete them will raise a warning message.

![](../../Resources/Images/Druid%205.12/soft%20trigger.png)

- **Integrations grouped by category in the Flow Palette**. The Flow Palette now lists all integrations grouped by category.

![](../../Resources/Images/Druid%205.12/flow%20palette%20grouped%20by%20category.png)

When adding an integration from the Flow Palette to the Flow Diagram, a flow step of type Action is automatically created with that integration in the PostAction section.

- **Integrations created from web views and forms have the context entity set as request and response entity**. When you add a new integration in web views or forms (create, read, update or delete integration), the request and response entity is prefilled with the name of the entity from which you add the integration. The entity name is editable, so you can select another entity.
- **New function available in Code Editor and Custom Code**. The function `EntityUtils.Stringify(entity)` is now available and you can use it to get the JSON representation of an entity.
- **Flow diagram - preserve the link condition when inserting a step in between**. When you insert a step between two steps with link condition set, the previous condition is added to the link between the first step and new step.
- **Workspaces - select default form at entity level**. You can now personalize each workspace with a specific form for view records based on different business needs. After you define forms for an entity, configure your workspace entity links with the form, which addresses the specific needs of the business users who will use that workspace.

![](../../Resources/Images/Druid%205.12/default%20form%20on%20workspaces.png)

- **Quick search available in views on forms**. At run time, if a view is available on a form, business users can search through the view records.

![](../../Resources/Images/Druid%205.12/search%20in%20view.png)

- The DRUID package is no longer compatible with UiPath community Edition 2023 due to .NET 4.6.

<a id="BugFixes"></a>

## Bug Fixes

- Language Detection doesn't work when we have KB special flow.
- Fixed thresholds analysis on runtime on Neuralspace models.
