---
layout:
  title:
    visible: false
---

<a id="DRUID523"></a>

# DRUID 5.23

Deployment Dates

The table below lists the deployment date of DRUID v5.23 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| September 15, 2023 | September 28, 2023 | September 28, 2023 | September 28, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Global and Local scope available for REST and DRUID Data Services integrations (except for the GetEntity task)**. With this release, the connector action becomes a tool you can use to implement very complex automations. A new field, **Scope** is available on integration tasks (on both the Request and Response tabs) that allows you to set a local context that is different from the global context set on the connector action (the entity set as Request / Response entity on the connector action).

![](../../Resources/Images/druid%205.23/global%20scope.png)

Using the **Local** scope, you do all related queries directly inside the connector action instead of building a larger context outside the connector action via additional queries within the Flow Designer to put data inside the request entity and then send the data back to the connector action.

Use cases:

- do a validation to ensure that you do not add the same customer twice and the primary key is, for example, the personal ID.
  You get new account records and you do a query for a different account without overwriting the original data.

![](../../Resources/Images/druid%205.23/global%20and%20local.png)

- create an invoice from a contract.

![](../../Resources/Images/druid%205.23/generate%20invoice.png)

- **DRUID Data Services - Delete Entity integration task has been improved with filtering**. With this release, you can delete entity records that meet specific filtering conditions. E.g., from [[Account]].Cases delete all accounts that have the status "Active" and the account name contains the word "Jane".

![](../../Resources/Images/Druid%20Data%20Service%20Connector/delete%20filter%20example.png)

For more information, see [Delete Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Delete_Entity.md).
