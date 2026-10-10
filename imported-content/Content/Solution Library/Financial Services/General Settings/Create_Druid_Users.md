---
title: Creating Druid Users For Financial Services
---

# Creating Druid Users For Financial Services

### Step 1: Create Service Account for UiPath Integration

In the Druid Portal, from the main menu, click **Administration**, and then click **Users**. Add a new user (or edit an existing one) and assign this user the **Service account** security role.

Write down the user credentials, you will use them later in the **config.json** file.

![](<../../../../.gitbook/assets/service account.png>)

### Step 2: Set Up Druid users

For either demo or production environments, you need to make sure that in the Druid Portal you assign the specific security roles to users, as follows:

* For all agents in your Contact center, create Druid users and assign them the **Helpdesk Agent** role:

![](<../../../../.gitbook/assets/helpdesk agents.png>)

* For all employees in the Back-Office department, create Druid users and assign them the designated role:

![](<../../../../.gitbook/assets/employees roles.png>)

To demo My Tasks, assign all three roles to your user.

{% hint style="info" %}
**NOTE:** To view all users created in Druid, tick the **ShowChatUsers** check box.

<img src="../../../../.gitbook/assets/view chatusers.png" alt="" data-size="original">
{% endhint %}
