---
layout:
  title:
    visible: false
---

<a id="DRUID531"></a>

# DRUID 5.31

Deployment Dates

The table below lists the deployment date of DRUID v5.31 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| December 21, 2023 | January 18, 2024 | January 18, 2024 | January 18, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Connector integration task with local scope – Request entity\_Global available in the object explorer
- Druid Data Services Connector - Disable Connector audit logging

<a id="Improvements"></a>

## Improvements

- **Predicting "User says" in the knowledge base enhancement**. In this release, there is a refinement in the testing process for "user says" within the knowledge base. When conducting tests at the knowledge base level, DRUID now performs predictions across ALL trained data sources. Alternatively, if you test the user says within a specific data source, the intent is predicted exclusively within that particular data source. This enhancement allows for a more granular approach to testing against the knowledge base.

*Predict on the knowledge base level*

![](../../Resources/Images/druid%205.31/predict%20in%20kb.png)

*Predict within a data source*

![](../../Resources/Images/druid%205.31/predict%20in%20data%20source.png)

- **Live Chat - disable conversation timeout when the last message is from the client**. Introducing the "Apply only on client silence" feature in this release enhances live chat session management by disabling conversation timeout when the last message is from the client. This improvement effectively mitigates the auto-disconnect mechanism triggered by the **Live Chat Conversation Idle Timeout**, aligning with scenarios where auto-disconnect exclusively occurs during client unresponsiveness, excluding agent activity.

![](../../Resources/Images/druid%205.31/client%20silence.png)

When in operation, it alleviates the necessity for the agent to pause the conversation when undertaking tasks outside of the chat, particularly those requiring a significant amount of time.

> **NOTE:** By default, this feature is set to be active on new AI Agents, maintaining compatibility with existing configurations.

- **Connector integration task with local scope – Request entity\_Global available in the object explorer**. There may be scenarios where the response entity is both local and global, and it possesses distinct memory slots. In this release, you now have the capability to retrieve values from a globally scoped entity at the integration (connector action) level within an integration task that has local scope.

For instance, consider a campaign scenario where an integration task with local scope is employed to create a new campaign sharing the same category as the campaign from the global entity. In the add/create integration task, referencing the [[Campaign]] with local scope, you can assign a new name and date while maintaining the category from the global entity's Campaign. To achieve this, map the relevant DRUID entity fields on the Response, assuming they exist: [[Campaign]].Name, [[Campaign]].CreationOn, and [[Campaign]]\_Global.Category.

![](../../Resources/Images/druid%205.31/object%20explorer%20global.png)

![](../../Resources/Images/druid%205.31/global%20example.png)

> **NOTE:** This feature requires DRUID Connector Host upgrade.

- **Druid Data Services Connector - Disable Connector audit logging**. In this release, we've introduced a valuable enhancement for Druid Data Services Connector integration tasks – the "Disable Connector Audit Logging" option. This feature empowers users to optimize execution time and conserve database resources, particularly when dealing with significant payloads during integration tasks.

*Example: Add entity integration task*

![](../../Resources/Images/Druid%20Data%20Service%20Connector/add%20brief%20description%20add%20entity.png)

> **NOTE:** This feature requires DRUID Connector Host upgrade.
