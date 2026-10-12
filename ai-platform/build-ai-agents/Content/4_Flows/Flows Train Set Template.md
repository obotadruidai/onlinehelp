---
title: "Solution Train Set Format"
---

<a id="SolutionTrainSetFormat"></a>


The flows train set file has a specific format. In order for the upload to be successful you have to either fill in the flows train set template or update the existing flows train set file following the supported upload format.

This section provides description of all columns in the flows train set file.

| Column | Mandatory | Description |
| --- | --- | --- |
| Language | yes | The language code for which you are providing the line. Make sure to map it to one of the languages defined on your AI Agent. If there is no match, the line will be ignored. |
| Row Type | yes | Two possible values:  - **Intent** (or **0**) – the line provides information at the conversation flow level. The Phrase on the Intent line is usually the primary question of the intent. **NOTE:**    - You should use one single line for each pair Intent, Language and Row type = “Intent”.   - For row type **Intent**, you have to provide values for the columns Category, Description, Response and Security. - **Alternate question** (or **1**) – the line provides alternate question for the intent. **NOTE:** The lines which have the row type **Alternate question**, you have to include values just for Language, Row type, Utterance and Intent. Find and leave the other columns empty. If you provide value for the other columns, the values are ignored at import, just the Utterance value will be used. |
| Utterance | no | The train phrase for the intent. Format: Plain text. It is mandatory for alternate questions. **NOTE:** NER is not supported yet. |
| Intent | yes | The intent name. It is used to match the intent to update. |
| Category | no | The category of the intent. If provided, the existing intents will get the category updated. If missing, the new create flows will have category = “Import”, and existing flows will keep their existing category. |
| Description | no | The Description of the flow, in the respective language. If missing, the existing flow will keep the current Description, and the new created flows will have the Description set with the value in the **Intent**column. |
| Response | no | The value of the **Message** field on the first step in the flow. If value is provided in the **Response** field, at import, the value will overwrite the existing **Message** value. If the**Response**value is empty, no changes are applied to the flow step. Format: markdown language. |
| Security | no | If provided, at import it will overwrite the name(s) of the security roles set as “Used by” on the flow. If it is empty at import, no changes are applied on the security settings. If you to want to provide multiple roles, enter comma-separated roles names. Example: Admin,User. **NOTE:** This field is mandatory only for row type Intent. |
| Follow-up Flow Name | no | If provided, at import type, the first step of the intent will be created / updated into trigger “Flow” type, and the referenced flow is set based on the provided follow-up flow name. |

{% hint style="warning" %}
**IMPORTANT!** Providing values for "Response" column will **REPLACE** the Message in the first step of the flow. Providing values for the "Follow-up Flow Name" will set the first step as **TRIGGER FLOW**. If you don't want to update the Flow response, make sure that you clean the "Response" and "Follow-up Flow Name" columns in the Excel file before importing it.
{% endhint %}
