<a id="DRUID514"></a>

# DRUID 5.14

Deployment Dates

The table below lists the deployment date of DRUID v5.14 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| May 11, 2023 | June 08, 2023 | June 08, 2023 | June 08, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host to the latest version:

- Native scripts support in the Connector fields of the response mapping
- REST Connector - For custom authentication, added support for tokens returned as string
- Custom Code - added support to set and get connector local variables.

<a id="WhatsNew"></a>

## What's New

- **Knowledgebase - Unstructured Data sources (technology preview)**. You can now add unstructured data sources to the Knowledge base and crawl a website based on a specific crawling policy.

![](../../Resources/Images/KB/unstructured%20created.png)

![](../../Resources/Images/KB/extracted%20data%20source.png)

For more information, see [Knowledge base](../../Knowledgebase/Knowledgebase.md).

<a id="Improvements"></a>

## Improvements

- **AI Agent Summary Dashboard**. The Engagement KPIs metric Users now take into account the number of unique authenticated users providing authors with a more relevant view on the AI Agent usage.

![](../../Resources/Images/druid%205.14/engagement%20kpis%20overview.png)

![](../../Resources/Images/druid%205.14/engagement%20users%20kpis.png)

For more information on the Engagement KPIs, see [AI Agent Summary Dashboard](../../Usage/AI%20Agent%20Summary%20Dashboard.md).

- **Max number of sessions for automatic allocation**. When the maximum number of sessions for automatic allocation is set on a AI Agent level and on the queue level, DRUID takes into consideration the minimum value between the AI Agent level and queue level settings. If an agent is allocated to multiple queues with different maximum active sessions for automatic allocation set, DRUID takes into consideration the smallest value of them allocating clients to agents inth.

Example: Queue A has the **Max number of active sessions** set to 2 and Queue B has the **Max number of active sessions** set to 3. The **Max number of active sessions** on the AI Agent level is set to 4. If an agent is allocated to both Queue A and Queue B, the agent will be automatically allocated maximum 2 sessions in parallel for both queues; for Queue B the agent can manually take 2 more clients (to reach the maximum number of active sessions set on Queue B).

- **NLU.NER.IndexBasedEntityExtractorV2**. This is a new experimental NLP parameter set on the AI Agent level that acts as a fallback additional algorithm when the default extraction algorithm fails to extract. Set this parameter to **true** to extract complex data from indexed entities, values comprised of multiple words. E.g. "Carol Davila University of Medicine and Pharmacy".

![](../../Resources/Images/druid%205.14/experim%20param.png)

- **CNN Document Builder - support for dynamic file name**. You can now specify the file name of the generated document either hard coded as string (e.g., "Invoice April") or as a value from the context: an entity field (e.g., [[Employee]].Name) or a local variable.

![](../../Resources/Images/druid%205.14/dynamic%20file%20name.png)

> **NOTE:** If the **Dynamic File Name** field is empty, DRUID will use the template file name as file name of the generated document.

- **Native scripts support in the Connector fields of the response mapping**.
  To use the response from APIs that send data into language specific JSON properties (a key from a response task might be in a native script; e.g., Latin script: "téléphone"). You can now map in the response keys that are in the following native scripts: Latin, Greek, Hebrew, Simplified Chinese, Traditional Chinese, Japanese, Hindi and Arabic.

![](../../Resources/Images/druid%205.14/native%20scripts.png)

- **REST Connector - For custom authentication, added support for tokens returned as string**. If the Authenticate client returns the token in the response body as a simple string instead of a JSON object (e.g., "345b4hjbdjk5j234544"), when mapping the token in the **Authenticate Client Request** response, specify **text** in the **Connector field type** column.

![](../../Resources/Images/druid%205.14/authenticate.png)

- **Custom Code - added support to set and get connector local variables**. You can now set and use connector local variables from the integration context between integration tasks.
> **IMPORTANT!** You can use the connector local variables only within the integration context. You cannot use local variables set on flow steps within integrations and neither can you use connector local variables as local variables between flow steps.
>
> ![](../../Resources/Images/druid%205.17/nnn%20variables.png)

For more information, see [Using Connector Local Variables](../../7_Integrations/Use_connector_local_variables.md).

- **LiveChat UI improvement for helpdesk agents**. The conversation in which the agent is currently engaged with the client is marked with a gray bar displayed on the left and the other active live sessions are highlighted in orange.

![](../../Resources/Images/druid%205.14/live%20chat%20ui.png)

- Origin validation is included in **AuthoryzeAnonymousAsync**. You can now prevent AI Agents from being accessed from domains that are not yours by defining the **Allowed Origins** in the AI Agent details page, section General. This adds an extra layer of security to your AI Agent as the DRUID webchat will validate if the domain from where it is accessed corresponds to the Allowed Origins defined on the AI Agent.

![](../../Resources/Images/druid%205.14/allowed%20origins.png)

> **NOTE:** You need to specify the allowed origin in the following format: *https://domain.tld*. For example: *https://druidai.com*.

> **Info:** You can specify multiple allowed origins separated by comma.

- **Added security roles on solutions**. DRUID administrators can now grant authors access to specific solutions by grating the **Read Solution** security role permission and selecting the security role(s) on the solution (**Roles** tab).

Example:

![](../../Resources/Images/druid%205.14/read%20solution.png)

![](../../Resources/Images/druid%205.14/solution%20security%20role.png)

- **Read-only web forms**. You can now prevent users from editing records by setting the desired web forms as read-only.

![](../../Resources/Images/druid%205.14/set%20readonly%20form.png)

![](../../Resources/Images/druid%205.14/readonly%20form.png)

- **Right side editor - full screen option**. In the Druid Portal you can now expand the right side editor to the entire diagram area.

![](../../Resources/Images/druid%205.14/expand.png)

![](../../Resources/Images/druid%205.14/full%20screen.png)

<a id="BugFixes"></a>

## Bug Fixes

- NER: Sample values modal were not saved in some cases.
- OAuth - Import Solution - App didn't have the integrations set.
- Flows were not linked after uploading solution train set.
- FE: Intent Not Recognized was not triggered or single match below the target score (hotfix applied on 5.11).
- Is Response Collection was not enabled on DRUID Data Service Query Templates.
- Expansion level was not set to 2 on DRUID Data Service Query Templates.
- Adaptive Cards were not inactivated after the inactivity cancel conversation message was displayed.
- The newly created workspaces were displayed only after refresh.
- Solution content entries were not visible only on "read" permission.
