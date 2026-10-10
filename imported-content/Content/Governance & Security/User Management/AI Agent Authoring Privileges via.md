---
layout:
  title:
    visible: false
---

<a id="AIAgentAuthoringPrivilegesviaRBACPolicy"></a>

# AI Agent Authoring Privileges via RBAC Policy

> **NOTE:** RBAC functionality is not available by default, we activate it on request. To activate it, get in touch with [Druid Tech Support](<mailto:support@druidai.com?subject=Activate RBAC for my tenant>).

Using Role-based Access Control (RBAC) policies you can grant authors access privileges to specific elements on AI Agent level: AI Agent Security, AI Agent Settings, Connector Action, Connector List, Conversation History, Document Template, Entity, Flow or Live Chat Settings.

To grant authors specific privileges for a specific AI Agent:

1. Go to **All Settings** > **AI Agents**.
2. Select your AI Agent.
3. Click the **Security** tab.

![](../../Resources/Images/Authoring%20User%20Management/security%20tab.png)

4. Click the **AuthorBy** section header. The section expands.
5. Click the **Create new policy** button.
6. From the dropdown, select the security role.
7. Set the access privileges to different elements based on your use case.

![](../../Resources/Images/Authoring%20User%20Management/create%20policy.png)

> **Info:**  You can create multiple RBAC policies on the same AI Agent to accommodate different access permissions for different authors based on your needs. To do so, click the **Create new policy** button. A new policy section appears below the policy(es) you created. You can set different permissions for another security role.

To remove an RBAC policy, click the delete icon below the security role dropdown.

![](../../Resources/Images/Authoring%20User%20Management/remove%20policy.png)

After you finish creating all needed RBAC policies, click the **Save & Close** button. At next login, the authors who have been assigned with the security role specified in the RBAC policy, will have access permissions on the AI Agent as specified in the RBAC policy.
