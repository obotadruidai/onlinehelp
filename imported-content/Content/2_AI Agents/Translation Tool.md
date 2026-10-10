---
title: "Translation Tool"
---

<a id="TranslationTool"></a>


The Translation Tool enables translators and authors with the appropriate access permissions to easily translate AI Agent elements from a single, centralized space within the Druid Portal.

This tool is designed specifically for localization teams and professional translators to ensure an AI Agent is perfectly translated across all designated target languages without requiring deep technical knowledge of the Druid platform or flow configuration.

{% hint style="info" %}
**NOTE:** The Translation Tool is a tenant-level feature. To activate it for your tenant, please contact your Druid representative.
{% endhint %}

<a id="RequiredPermissions"></a>

## Required Permissions

- Grant your translators with a dedicated security role, which has following permissions:

- AI Agent **Designer** > **Read** AI Agent

![](../Resources/Images/Translation%20Tool/Translation%20Tool.png)

- **Solutions** > **Read Solution**.
- **Translation Tool**

![](../Resources/Images/Translation%20Tool/Translation%20Tool_1.png)

- If you want to allow advanced translators to jump directly from the Translation Tool to the Flow Diagram, they must also be granted read, create, and edit permissions for the Flow Designer.

![](../Resources/Images/Translation%20Tool/Translation%20Tool_2.png)

- If RBAC is enabled on the tenant, on the solution Author By section, select the **Translator** role and select the permissions **Read AI Agent Settings** and **Read Flow** .

![](../Resources/Images/Product%20recommendation%20with%20GPT/rbac%20solution%20permissions.png)

<a id="AccessingtheTranslationTool"></a>

## Accessing the Translation Tool

To access the Translation Tool for a specific AI Agent, select the AI Agent and the solution. From the main menu, click **Translations**.

![](../Resources/Images/Translation%20Tool/Translation%20Tool_3.png)

The Translations Overview page provides you with an overview of how many elements are translated from the default AI Agent language into additional AI Agent languages.

The translation overview is broken down per training phrases, flows description and responses.

The coloring of the percentages indicates how elements within a category are translated:

- Grey – all elements are translated.
- Orange – more than 50% elements are translated.
- Red – less than 50% elements are translated.

<a id="ViewingtranslatableelementsforaspecificAIAgentlanguage"></a>

## Viewing translatable elements for a specific AI Agent language

For the desired language, click on the percentage or label in the corresponding category column (e.g., Training Phrases).

![](../Resources/Images/Translation%20Tool/Translation%20Tool_4.png)

The Translation page appears which displays all flows within the current solution.

![](../Resources/Images/Translation%20Tool/Translation%20Tool_5.png)

Druid provides extensive filtering options:

- **Target language** – change the translation target language. By changing the language, the table will update to accommodate the selected language.
- **Category** – change the AI Agent component (AI Agent elements). The table will update to accommodate the selected category. It’s a multi-select filter; based on your needs, you can select one, more or all categories. Categories are: training phrases, flows description and responses (messages on steps).
- **Status** – Allows filtering elements within the selected category by translation status as follows:

- **Untranslated** – elements are not translated.
- **Human Translated** – elements translated by human when Machine Translation is active on the AI Agent.
- **Machine Translated** - elements automatically translated by Machine Translation, which is active on the AI Agent.
- **Translated** – elements manually translated by human.

- **Flow** – allows filtering elements for a specific flow. This is particularly useful for authors managing translations.
- Alphabetical order – all elements are grouped in alphabetical order.

The table provides the following details:

| Column | Description |
| --- | --- |
| Status | The translation status of the training phrases per flow. The status untranslated indicates that none or not all category elements have been translated. |
| Key | The flow name. |
| Base count | The number of elements within the specific category defined on the flow. |
| Target Count | The number of translated elements within the specific category on the flow. |

<a id="TranslatingAIAgentelements"></a>

## Translating AI Agent elements

To translate elements for a category record, click on the desired raw in the table. The translation pop-up appears, which contains all translatable elements on the selected record (all training phrases on selected flow, conditions set on specific flow steps (Link Expressions column) and set variables). The elements in default AI Agent language are non-editable. Enter translation in additional language and save.

Example:

![](../Resources/Images/Translation%20Tool/Translation%20Tool_6.png)

{% hint style="info" %}
**NOTE:** You need to translate all elements within the pop-up; otherwise, you are not able to save the translations.
{% endhint %}

After saving the translations, the status of the selected record will change to “Translated” and the **Target Count** will change to the number of translated elements on that record (Base Count equals Target Count).

When choosing to translate elements of a flow step, the pop-up will render translatable elements on the step based on the step type, including variables set in Set Variables section on the flow step (if any).

Example: message step

![](../Resources/Images/Translation%20Tool/Translation%20Tool_7.png)

Example: hero card step

![](../Resources/Images/Translation%20Tool/Translation%20Tool_8.png)

Example: choice step

![](../Resources/Images/Translation%20Tool/Translation%20Tool_9.png)

{% hint style="info" %}
**Info:**  For hero, choice, thumbnail steps, you can preview the step translation by clicking the **Preview** button at the top of the pop-up.

![](../Resources/Images/Translation%20Tool/Translation%20Tool_10.png)
{% endhint %}

Authors and translators with access permissions to the Translation Tool and Flow Designer (see prerequisites) can navigate from the Translation pop-up to the Flow Diagram by clicking the open flow icon (![](../Resources/Images/Translation%20Tool/Translation%20Tool_11.png)) at the top of the Translation pop-up. A new browser window will open the Flow Diagram and the translation elements will display in the Flow Diagram Editor per category.

![](../Resources/Images/Translation%20Tool/Translation%20Tool_12.png)

Authors can also access the Translation tool at a flow level in the Flow Diagram by clicking the Translation Tool icon (![](../Resources/Images/Translation%20Tool/Translation%20Tool_13.png)). They can edit translations using the Translation tool in the Flow Diagram Editor.

![](../Resources/Images/Translation%20Tool/Translation%20Tool_14.png)
