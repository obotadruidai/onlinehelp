---
layout:
  title:
    visible: false
---

<a id="Step2CreateIntegrationActions"></a>

# Step 2. Create Integration Actions

A Connector Action (Integration) only represents a host for a group of one or more integration tasks. The integration technology / type (SQL, REST, SOAP, SMTP, AD, etc.) is defined at task level, not at action (integration) level.

If a connector action (integration) has more tasks, the response data will be returned to the flow only after ALL tasks inside the action have run. Implicitly, data in the response entity might be altered by the execution of each task. Also, tasks within the same action can be of different types (SQL, REST, SOAP, SMTP, etc.).

Thus, at Connector Action (Integration) level, only the general information is saved and used for describing and identifying the action.

Using the Connector Designer, you can define the integration actions and tasks:

1. From the main menu, click **Integrations**. The Connector Designer appears.
2. At the top-right corner of the page, click the **Create Connector Action** button. The Edit Connector Action page appears by default on the **Connector general** tab.
3. Provide the connector action general details by setting up the parameters described in the table below.

| Parameter | Description |
| --- | --- |
| Name | The name of the action. The field is mandatory. |
| Description | A brief description of the action that might be useful for other tenant admins. The field is mandatory. |
| Category | Define on the spot when creating the action. Useful when you want to find the actions in the Integrations list. The field is mandatory. |
| Icon | Select the icon that best describes the integration. It helps you easily identify the integration action in the list of integrations. If no icon is selected, Druid will show default icon. |
| Request Entity Name | The entity used by the AI Agent to send data to the external app via the current action. |
| Response Entity Name | The entity used by the AI Agent to receive data from the external app via the current action. |
| Is Response Collection | Tick only if the expected response is a list of records.  E.g., search for the list of AD users with a specific First Name or get the list of all AD users.. |
| Is Active | Tick to activate the connector action. An inactive connector action will be ignored at runtime. |
| Reduce Connector Audit Logging | Disables the logging of Request Entity and Response Entity data within the Connector Audit Log. Use this option to optimize performance and storage when the entity payload is expected to be significantly large. |
| Disable Connector Audit Full Database Logging | Prevents the storage of the full entity payload in the database. This is recommended when handling a high request volume that does not require detailed tracking or when payloads are large. While this reduces tracking overhead, system errors are still logged for monitoring and debugging purposes. |

4. Click **Save** to save the settings and stay on page to add tasks, or click **Save & Close** to save and exit the page. If you click **Save**, the **Connector steps** tab appears.

You can add as many SQL connector actions as best suit your integration needs.

> **NOTE:**  A Connector Action represents a set of one or more integration tasks, which run sequentially and use the same request and response entities.

You will define the AD query in the dedicated AD Integration task.
