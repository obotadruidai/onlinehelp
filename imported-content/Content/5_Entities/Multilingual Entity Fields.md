---
layout:
  title:
    visible: false
---

<a id="MultilingualEntityFields"></a>

# Multilingual Entity Fields

Druid simplifies the authoring process for NER management in multi-language AI Agents. Multilingual entity fields and NER enable AI Agents to align entity records (e.g., healthcare specialties, product names, city names, etc.) with the current chat user's language. These multilingual entity fields can be regarded as aliases for language-specific field clones.

> **NOTE:** This feature is available for entity fields of type **String.**

<a id="Setmultilingualentityfields"></a>

## Set multilingual entity fields

To designate an entity field as multilingual, simply enable the **Holds multilanguage records** option in the field configuration page.

![](../Resources/Images/Entities/hols%20multi%20records.png)

> **IMPORTANT!** You cannot set an entity field to be multilingual if it holds sensitive data (where **Holds Sensitive Data** is enabled).

Upon saving the entity field, Druid automatically generates associated field clones to store language-specific values for all tenant AI Agent languages. These clones follow a naming convention of <fieldname>\_<LanguageCode>  and are not visible in Entity Designer. Druid utilizes these clone fields to match entity records aligned with the current chat user's language.

<a id="MultilingualentityfieldsandNER"></a>

## Multilingual entity fields and NER

In the context of multlingual AI Agents, multilingual entity fields play a crucial role in NER. They facilitate the validation of user input against a list of predefined values specific to the current user's language ([[ChatUser]].Language). Druid NLP seamlessly identifies multilingual entity fields, creating language-specific NER indexes and utilizing the corresponding language-specific clone fields.

<a id="Managemultilingualentityfields"></a>

## Manage multilingual entity fields

Should you decide to revert an entity field from being multilingual, simply disable the **Holds multilanguage records** option. You have the choice to either automatically delete the auto-generated field clones or handle their deletion manually. Disabling this option may impact conversational flows, especially if clone fields are utilized in flow or integration tasks. For streamlined management, Druid provides the flexibility to review conversational flows and manually remove field clones accordingly.

![](../Resources/Images/Entities/diable%20multilanguage.png)

Choosing **Handle Manually** will make the auto-generated language specific field(s) visible in Entity Designer and you can review the conversational flows and remove the field clones afterwords.

To automatically delete the field clones, click **Delete**. All auto-generated language specific field(s) will be deleted on entity field save.

<a id="LanguagespecificfieldclonesinAIAgentlanguagechanges"></a>

## Language-specific field clones in AI Agent language changes

When adding additional languages to an AI Agent, Druid automatically creates language-specific entity fields (field clones) for all existing multilingual entity fields. Similarly, when introducing a new language, Druid generates entity fields for that language, including field clones for multilingual entity fields. Deleting a language unique to your tenant enables the removal of language-specific entity fields, allowing for a thorough review of conversational flows without impacting dialogs.

<a id="Usingmultilingualentityfieldsonflowsandintegrations"></a>

## Using multilingual entity fields on flows and integrations

In flow settings and integration tasks, leverage multilingual entity fields to enhance functionality. The Flow Engine seamlessly integrates language-specific clone fields, utilizing them if populated. However, use language-specific clone fields in flows only when explicitly necessary. For NER in multilingual AI Agents with expected language-specific values from external databases, ensure proper mapping of language-specific values to Druid language-specific field clones in the database response.

## Related Topics

- [Managing Entity Fields](Managing%20Entity%20Fields.md)
- [Set Variables](../4_Flows/Set%20Variables.md)
- [Using NER with Index Entities (DRUID versions prior to 5.15)](../Conversational%20AI/Using%20NER%20with%20Index%20Entities%20%28DRUID%20versions%20prior%20to%205.15%29.md)
