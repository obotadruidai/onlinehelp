---
title: Create Solutions
---


A solution acts as a portable container that encompasses all necessary components—including flows, data entities, and system integrations—allowing for seamless movement between different environments and tenants.

When building a new AI Agent, you must define the solution. This ensures that all subsequent configuration is logically grouped and ready for lifecycle management.

To create a new solution:

1. Select the AI Agent.
2. On the Druid Portal header, select **Create new solution** from the **Solution** dropdown. The Create new solution modal appears.
3. Fill in the fields:

| Field          | Description                                                                                                                                                                                     | Mandatory |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Name           | Enter a unique identifier for the solution. This is used for internal tracking and Solution management.                                                                                         | Yes       |
| Description    | Provide a brief summary of the solution scope, such as the intended business use case or the specific department the AI Agent will serve.                                                       | No        |
| Category       | Use this field to group the solution within your internal library (e.g., HR, Sales, IT Support).                                                                                                | No        |
| Provider Name  | Enter the name of the organization or department responsible for developing and maintaining the AI Agent configuration.                                                                         | Yes       |
| Provider Icon  | Specify the URL or identifier for the solution author logo. This icon appears in the solutions library to help identify the source.                                                             | No        |
| Version Number | Assign a numerical value (e.g., 1.0.0) to track the solution lifecycle. Proper Solution versioning is critical for maintaining AI Quality, Testing, and Accuracy during environment migrations. | Yes       |

4. Save the form.

## Related Topics

* [Release Lifecycle & Versioning](https://druidai.gitbook.io/druid-ai-docs/release-lifecycle-and-versioning/release-lifecycle-and-versioning)
