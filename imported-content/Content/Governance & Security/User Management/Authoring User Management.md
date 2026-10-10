---
title: Authoring User Management
---

# Authoring User Management

The User Management module allows you to manage authors and AI Agent users (also known as “Chat Users”) and their permissions within the Druid Portal.

**Author users** are the ones who create, modify or delete AI Agent and platform related configurations within Druid Portal (flows, integrations, security access, etc.).

**Chat Users** are the ones who only interact with the AI Agent through a messaging channel (also known as end users or client users); they don’t have ANY authoring permission in the Druid AI Platform.

Author users are always authenticated in the Druid AI Platform, while chat users may be authenticated or not, depending on the AI Agent configurations. By default, all chat users who initiate a conversation with a AI Agent are NOT authenticated (are Anonymous), until the conversation takes them to an authentication process.

This section covers two topics:

* [Authentication](<Authoring User Management.md#Authentication>)
* [Authorization](<Authoring User Management.md#Authorization>).

### Authentication <a href="#authentication" id="authentication"></a>

In Druid Portal, authors are authenticated via username and password. When creating a user directly in the Portal, we recommend you to make sure that password complexity meets the following requirements:

* The password minimum length is 8 characters.
* The password contains characters from all three of the following categories:
* At least one uppercase letter
* At least one lowercase letter
* At least one digit
* Non-alphanumeric characters (special characters): (\~!@#$%^&\*\_-+=\`|(){}\[]:;"'<>,.?/)

#### Password Management Policy

To set the password management policy, from the **Administration** menu, click **Settings** and in the Settings page, click the **User management** tab. Two options are available:

* Prevent the user's new password from being the same as any of the last x passwords. The default value is **3**.
* Set the password to expire after a specific number of days .The default value is **30 days**.

Select the desired option and set value, then click the **Save all** button at the top-right corner of the page.

![](<../../../.gitbook/assets/password policy.png>)

### Authorization <a href="#authorization" id="authorization"></a>

In Druid, authors are authorized based on security roles. They are granted access only based on the business area they need to know.

Security roles are groups of access privileges to specific elements which allow you to grand authors’ granular access rights within the Druid Portal.

The default security role, Admin grants the authors with access privileges to all Druid Portal features and all AI Agents.

{% hint style="info" %}
**NOTE:** Admin and User are default platform security roles and you cannot edit their permissions.
{% endhint %}

If you want to grant different access privileges to your authors (e.g. some authors can manage flows, while others can manage connector actions, document templates or solutions), add new security roles to accommodate your needs.

To create a new security role:

1. From the **Administration** menu, click **Roles**. The Roles page appears which lists all security roles existing in the platform.
2. At the top-right corner of the page, click the **Create new role** button. The Create new role page appears.
3. Enter **Role name**.

![](<../../../.gitbook/assets/create role.png>)

4. Click the **Permissions** tab.
5. Select the permission you want to group under this security role. The figure below provides an example.

![](<../../../.gitbook/assets/role permissions (1).png>)

6. Click the **Save** button to save the security role. You can now create AI Agent author users and assign the new security role, or assign it to existing authors.

### Portal Access Security

In addition to password policies, administrators can restrict access to the Druid Portal to authorized IPs or network locations. By enabling Portal Login IP Whitelisting, you can ensure that users (including those using SSO) can only log in from specific company IP addresses or VPN gateways.

For more information on configuring these restrictions, see [Enforce Druid Portal Access via IP Whitelisting](<Enforce Druid Portal Access via IP Whitelisting.md>).
