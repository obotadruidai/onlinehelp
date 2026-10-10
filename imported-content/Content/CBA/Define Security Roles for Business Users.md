<a id="DefineSecurityRolesforBusinessUsers"></a>

# Define Security Roles for Business Users

Authors control business user access to workspaces using security roles, ensuring users only interact with the data and functionalities relevant to their role.

To grant workspace permissions:

1. Navigate to **Administration** > **Roles**.
2. Create a new role or edit an existing one.
3. Assign the necessary permissions:

- Create, Delete, Edit, Read Workspaces – Granular permissions for managing workspaces.
- Workspace Designer – Grants full permissions for workspace creation and management.

![](../Resources/Images/CBA/role%20permissions.png)

> **IMPORTANT!** Since workspaces operate within the context of AI Agents, assigned security roles must also have permission to read AI Agent information.

Ensure that business users are assigned roles with appropriate workspace privileges. For example:

- Service Managers – Full access to workspaces.
- Team Leads – Permissions to create, edit, and read workspaces.
- Helpdesk Agents – Read-only access to workspaces.

> **NOTE:**  Workspace privileges also apply to views and forms. A user with permissions to create and edit workspaces will also have the ability to create and edit views and forms.
