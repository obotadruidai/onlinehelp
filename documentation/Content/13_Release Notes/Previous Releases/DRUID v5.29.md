<a id="DRUID529"></a>

# DRUID 5.29

Deployment Dates

The table below lists the deployment date of DRUID v5.29 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| December 07, 2023 | December 21, 2023 | December 21, 2023 | December 21, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Active Directory - Password Reset integration
- Query-related entity functionality is now integrated into Get entity and Query entity
- Dynamic filtering and pagination in web views.

<a id="WhatsNew"></a>

## What's New

- **Active Directory - Password Reset integration**. With this release, authors have the capability to set the user state to "requires password reset" within the Active Directory. Upon the next login, users will be prompted to set a new password.
> **NOTE:**  To leverage this feature, an upgrade of the DRUID Connector Host is required.

For more information, see [Putting Users in the "Requires Password Reset" State in Active Directory](../../7_Integrations/Active%20Directory/PasswordReset.md).

- **ExtractEntities - new internal action**. The internal action **ExtractEntities** detects and extracts texts associated with non-deterministic entities: Boolean, Date, DateTime, Decimal, Email, Integer, Location, Organization, Percentage, and Person. The new internal action proves valuable in scenarios where identification, extraction, and removal/anonymization of sensitive data from user inputs, such as Personally Identifiable Information (PII), addresses, emails, and personal names, are crucial before advancing through subsequent stages of conversation processing, specifically preceding transmission to ChatGPT or to other external systems.

![](../../Resources/Images/druid%205.29/internal%20action.png)

With this internal action, a new system entity has been introduced, [[NamedEntity]] that stores the extracted sensitive data identified by the ML service function and a new field [[Intent]].Entities (an entity list/collection referencing [[NamedEntity]]).

<a id="Improvements"></a>

## Improvements

- **Query-related entity functionality is now integrated into Get entity and Query entity - DRUID Data Service integrations**. When disabling **Map All Fields** in the response, the entity fields list now includes 'Entity List' type fields. This optimizes performance by enabling the retrieval of data related to the root (response) entity within the Get entity / Query entity without the need for multiple Query related entity integration tasks. Users can select specific fields to bring, simplifying processes such as fetching all activities for a campaign and obtaining specific details for each activity.

![](../../Resources/Images/druid%205.29/query%20related%20integr.png)

![](../../Resources/Images/druid%205.29/getentity.png)

> **IMPORTANT!** Be careful of the payload size when manually mapping 'Entity List' type fields in Query entity, as it retrieves all records, including child records.

> **NOTE:**  To leverage this feature, an upgrade of the DRUID Connector Host is required.

For more information, see [Get Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Get_Entity.md) and [Query Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Query_Entity.md)

- **Druid Conductor and Knowledge base predict area optimization**. In this release, an enhancement has been made in the Predict area of the Knowledge Base when authors operate within the Druid Conductor. Authors can seamlessly test questions across all indexes linked to every connected child AI Agent associated with the respective Druid Conductor instance.

![](../../Resources/Images/druid%205.29/megabot%20kb%20predict.png)

- **Connector integrations UX improvements**. This release comes with a set of user experience enhancements that facilitates a more intuitive and efficient process when managing integration tasks.

- **Entity scope label**. This release comes with visuals for integrations shown in the flow diagram, connector list and diagram view, including web views - automations diagram view. A dedicated label on the request and response entity now clearly indicates the entity's scope, distinguishing between global and local scopes.

![](../../Resources/Images/druid%205.29/scope%20legend.png)

![](../../Resources/Images/druid%205.29/diagram%20ux%20scope.png)

- **Relevant integration details**. In the connector and flow diagram view, the name of the integration task and the request and response entities are shown as details for each integration. A specific icon indicates the integration type (the icon displayed at the top).

![](../../Resources/Images/druid%205.29/diagram%20ux%20scope.png)

![](../../Resources/Images/druid%205.29/flow%20integrations.png)

- **Dynamic filtering and pagination in web views - improved performance**. With this release, filtering and pagination are seamlessly handled server-side, harmonizing with any client-side settings. The user's applied filters and pagination on the web view synchronize with the Query entity integration (the server-side), ensuring a unified experience.
> **IMPORTANT!** You need to upgrade both the DRUID Connector Host and the entity associated with the web view; otherwise, loading the web view will fail.

For more information, see [Filtering records in a view](../../CBA/Filtering%20records%20in%20a%20view.md).

This features also introduces a new system entity field, PageInfo to the upgraded entity and three new system entities: [[PageInfo]], [[PageInfoFilter]] and [[PageInfoSorting]].  For more information, see [System Entities](../../5_Entities/System%20Entities.md).

> **Info:** While dynamic filtering and pagination in web views enhance your experience with DRUID Data Service in conversational business applications, you can also leverage this feature manually through SQL queries.

- **Enhanced Filtering for Flows, Entities, and Integrations**. You can now apply advanced filters to refine the list of flows, integrations, and entities. These filters are tailored to each list and designed for intuitive use.

![](../../Resources/Images/druid%205.29/filter%20integrations.png)

![](../../Resources/Images/druid%205.29/filter%20entities.png)

![](../../Resources/Images/druid%205.29/filter%20flows.png)

- **Code Extension Icon on Flow Step Cards**. In the Flow diagram, a dedicated icon is now displayed on step cards to indicate the use of Code extension.

![](../../Resources/Images/druid%205.29/code%20icon.png)

- **BotApp channel errors are visible in the Conversation History**. BotApp channel errors are now conveniently visible in the Conversation History. Authors can easily identify and troubleshoot errors encountered by the DRUID BotApp when sending messages to the WhatsApp (by Vonage) channel, streamlining the debugging process.
