---
layout:
  title:
    visible: false
---

<a id="CreatingDruidUsersForFinancialServices"></a>

# Creating Druid Users For Financial Services

<a id="Step1CreateServiceAccountforUiPathIntegration"></a>

## Step 1: Create Service Account for UiPath Integration

In the Druid Portal, from the main menu, click **Administration**, and then click **Users**. Add a new user (or edit an existing one) and assign this user the **Service account** security role.

Write down the user credentials, you will use them later in the **config.json** file.

![](../../../Resources/Images/solution%20templates/Victor/service%20account.png)

<a id="Step2SetUpDruidusers"></a>

## Step 2: Set Up Druid users

For either demo or production environments, you need to make sure that in the Druid Portal you assign the specific security roles to users, as follows:

- For all agents in your Contact center, create Druid users and assign them the **Helpdesk Agent** role:

![](../../../Resources/Images/solution%20templates/Victor/helpdesk%20agents.png)

- For all employees in the Back-Office department, create Druid users and assign them the designated role:

![](../../../Resources/Images/solution%20templates/Victor/employees%20roles.png)

To demo My Tasks, assign all three roles to your user.

> **NOTE:** To view all users created in Druid, tick the **ShowChatUsers** check box.
>
> ![](../../../Resources/Images/solution%20templates/Victor/view%20chatusers.png)
