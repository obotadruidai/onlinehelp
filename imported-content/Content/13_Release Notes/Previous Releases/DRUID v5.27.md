---
layout:
  title:
    visible: false
---

<a id="DRUID527"></a>

# DRUID 5.27

Deployment Dates

The table below lists the deployment date of DRUID v5.27 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| November 09, 2023 | November 23, 2023 | November 23, 2023 | November 23, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Web views – bulk delete on multiple records selection. It also requires DRUID Data Service upgrade to the latest version.
- Custom Code integration - CodeTrace improvements.

<a id="WhatsNew"></a>

## What's New

- **RingCentral channel**. RingCentral is a multi-channel integrator, which also offers live chat capabilities. With this release, you can create AI Agents and deploy them in your preferred channels via RingCentral. You can also use RingCentral's live chat capabilities.

*User talking to the AI Agent*

![](../../Resources/Images/RingCentral/bot%20conv.png)

*User talking to a helpdesk agent*

![](../../Resources/Images/RingCentral/mesg%20routed%20to%20agent.png)

For more information, see [RingCentral Channel](../../Channels/RingCentral/RingCentral_channel.md).

<a id="Improvements"></a>

## Improvements

- **File Upload steps: Store files in dedicated entity fields**. With this release, you can author the File upload steps to store the files users upload in the chat in dedicated entity fields of type [[File]] by providing the specific entity field in **Input mapping** on the File upload step.

For more information on , see [File Upload Steps Configuration](../../4_Flows/File%20Upload%20Steps%20Configuration.md).

- **Technology preview! Custom Code integration - CodeTrace improvements**. This release comes with CodeTrace improvements, which simplify the debugging efforts at authoring time:

- Highlights in red the points of failure in code tracing.
- Shows in gray the lines of code which were not executed and marks with a green line on the left the lines that were successfully executed.

![](../../Resources/Images/druid%205.27/CodeTrace_failure.png)

- Allows you to compare entity data throughout code execution and see what has changed.

![](../../Resources/Images/druid%205.27/entity%20comparison.png)

- Allows you to view an entity as JSON (useful for big entities).

![](../../Resources/Images/druid%205.27/see%20entity%20json.png)

- Allows you to view the audit log for **Context.ExecuteTask** and see the values returned from the executed task if the task was executed successfully, or the error otherwise.

![](../../Resources/Images/druid%205.27/task%20successful.png)

![](../../Resources/Images/druid%205.27/task%20failed.png)

> **NOTE:** This feature requires DRUID Connector Host upgrade to version 5.27.

For more information, see [Custom Code](../../7_Integrations/Custom%20Code.md).

- **Default Security Roles are read-only**. The default platform security roles Admin and User are now read-only, you cannot edit their permissions.
- **Web views – bulk delete on multiple records selection**. In the views that display records from DRUID Data Service **ONLY**, you can delete multiple records in bulk by selecting the records you want to delete and then clicking the **Delete** button at the top-right corner of the page.
> **NOTE:** This feature requires DRUID Connector Host upgrade to version 5.27 or higher and DRUID Data Service upgrade to the latest version.

![](../../Resources/Images/druid%205.27/view_delete%20bulk.png)

- **Knowledge base - set the search balance for the KB engine**. You can now set the search balance between the two algorithms the KB engine uses to search within the knowledge base: the keyword (Text) search algorithm and the semantic (Vector) search algorithm.

![](../../Resources/Images/druid%205.27/kb%20search.png)

For more information see [Knowledge Base](../../Knowledgebase/Knowledgebase.md), section Knowledge Base Settings.

<a id="BugFixes"></a>

## Bug Fixes

- **Fix on OAuth integrations (OAUths step) defined in a functional AI Agent**: When the conversation with a Druid Conductor reaches an orchestrated AI Agent that has OAuth set, the authentication is now working.
- **Code Extension - secondary language code**. The Code Extension on the secondary language is now working even if there is no code on the default language.
- **UI: Search in the code editor**. Opening the code editor from Variables (Flow Designer), Code Extension (Flow Designer), Custom Code (Integrations) and searching using the CTRL+F features is now working.
