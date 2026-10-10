---
title: "Disable Portal Users"
---

<a id="DisablePortalUsers"></a>


To enhance security and maintain an audit trail, Portal users cannot be permanently deleted. Instead, you can disable (inactivate) users. Inactive users cannot access the Portal, but their history and activity remain available for auditing and reporting purposes.

{% hint style="info" %}
**Info:** In DRUID versions prior to 9.5, you can permanently delete Portal users, but we recommend disabling them instead to preserve user history and associated data.
{% endhint %}

To disable a Portal user, follow these steps:

1. Go to **Administration** > **Users**.
2. In the Users list, locate the user you want to disable.
3. Click **Actions** next to the user and select **Inactivate**.

![](../../Resources/Images/Authoring%20User%20Management/inactivate%20user.png)

In Druid prior to version 9.6, click **Actions** next to the user and select **Edit**.
In the user details, clear the **Active** checkbox.

4. Click **Save**.

To inactivate multiple users at once, select them from the list and click the **Inactivate** button above the list.

![](../../Resources/Images/Authoring%20User%20Management/inactivate%20multiple%20users.png)

{% hint style="info" %}
**NOTE:**

- Inactive users remain listed in the Portal but cannot log in or perform any actions.
- All data and activity associated with inactive users are preserved for compliance and auditing.
{% endhint %}
