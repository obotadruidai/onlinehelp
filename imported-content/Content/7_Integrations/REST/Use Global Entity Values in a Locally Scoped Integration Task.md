---
layout:
  title:
    visible: false
---

<a id="UseGlobalEntityValuesinaLocallyScopedIntegrationTask"></a>

# Use Global Entity Values in a Locally Scoped Integration Task

There may be scenarios where the response entity is both local and global, and it possesses distinct memory slots. You have the capability to retrieve values from a globally scoped entity at the integration (connector action) level within an integration task that has local scope.

For instance, consider a campaign scenario where an integration task with local scope is employed to create a new campaign sharing the same category as the campaign from the global entity. In the add/create integration task, referencing the [[Campaign]] with local scope, you can assign a new name and date while maintaining the category from the global entity's Campaign. To achieve this, map the relevant DRUID entity fields on the Response, assuming they exist: [[Campaign]].Name, [[Campaign]].CreationOn, and [[Campaign]]\_Global.Category.

![](../../Resources/Images/druid%205.31/object%20explorer%20global.png)

![](../../Resources/Images/druid%205.31/global%20example.png)
