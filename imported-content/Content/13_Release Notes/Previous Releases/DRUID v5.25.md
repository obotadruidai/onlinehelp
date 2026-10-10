---
layout:
  title:
    visible: false
---

<a id="DRUID525"></a>

# DRUID 5.25

Deployment Dates

The table below lists the deployment date of DRUID v5.25 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| October 12, 2023 | October 26, 2023 | October 26, 2023 | October 26, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Technology preview!Custom Code integration - CodeTrace**. This release introduces code tracing, an effective tool in debugging efforts at authoring time as it traces the execution of all the lines in the code. Use it to validate your code by testing the execution of your code and manually verifying in the CodeTrace that the code works correctly or if there are any logic errors.

![](../../Resources/Images/Custom%20Code/codetrace.png)

- **MultiChat - include views and forms as tabs to the agents' page**. With this release, you can allow your helpdesk agents to access web views and forms and manage records stored in [conversational business applications](../../CBA/Conversational%20AI%20Applications.md) while talking to the users (e.g., update user account details). Putting the power of the DRUID CRM in the hands of your helpdesk agents, you ensure that you provide better assistance to your clients and employees.

![](../../Resources/Images/Live%20Chat/web%20form%20tab.png)

For more information, see [Handling live chat on agent side](../../Live%20Chat/Handling%20live%20chat%20on%20Agent%20side.md).

- **Technology preview! DRUID Data Services - DRUID custom query in the Query Entity task**. The DRUID Data Services query integration tasks now offer you with the option to interrogate other entities (than the request entity) by performing a DRUID custom query instead of doing Query related. The DRUID custom query supports a set of TSQL transactions (statements, functions, operators and clauses). For more information, see [Query Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Query_Entity.md).
- **DRUID Vision - Promissory Notes**. The DRUID API engine now performs OCR and data extraction from Promissory notes. For more information, see [Promissory Notes OCR](../../Druid%20AI%20Services/Promissory%20Notes%20OCR.md).

<a id="Improvements"></a>

## Improvements

- **Document Builder - Merging PDF**. The Document\_Generator connector now provides you with the option to merge PDF files addressing the following two scenarios:
  - Generate a PDF file from a document template (Word or Excel) and merge it with other PDF files uploaded to the DRUID Storage. For more information, see [Generate a PDF document and merge it with PDFs stored in DRUID Storage](../../7_Integrations/Document%20Builder/Generate%20a%20PDF%20Document%20and%20Merge%20With%20Other%20PDFs.md).
  - Merge PDF files stored in an entity list of files. For more information, see [Merge PDF Files Stored in an Entity List](../../7_Integrations/Document%20Builder/Merge%20PDF%20Files%20Stored%20in%20an%20Entity%20List.md).
- **Conversation History - log the flow name that rises security violation message**. When a user accesses a flow that is restricted (the user does not have the appropriate security roles assigned to access the flow), the following message is logged into the Conversation History "Sorry, I cannot disclose that information" together with the name of the flow that triggered the alert.
- **Channels - triggering the "Welcome flow" on Conversation/channel creation**. For GDPR and cookie policy compliance, when the user creates the first chat with the AI Agent in any of the following persisted channels: Twilio SMS, Telegram, Viber, Whatsapp Nexmo and Whatsapp Meta, the predict with the initial "user says" is dropped and the AI Agent responds with the Welcome flow.

<a id="BugFixes"></a>

## Bug Fixes

- Exception handler on flows is no longer ignored when the user uploads a file with an unsupported file type.
- **Custom Code integration task** fix. Saving a Custom Code that has been edited in expanded view now saves the integration task.
- **Conversation History v2 fix**. Returning from a conversation details will keep the initial filters applied before viewing conversation details.
