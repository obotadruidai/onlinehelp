---
title: "Release Lifecycle & Versioning"
---

<a id="ReleaseLifecycleVersioning"></a>


AI Agent versioning and release management across environments in the Druid AI Platform is based on the concept of solutions and environment separation. This approach enables teams to package, transport, and deploy configurations across environments in a controlled and repeatable way.

Instead of cloning entire tenants, Druid supports modular packaging of AI Agent configurations and lifecycle management through solutions, combined with dedicated environments for development, testing, and production.

A **solution** acts as a portable container that encompasses all necessary components—including flows, data entities, and system integrations—allowing movement between different environments and tenants.

<a id="Environments"></a>

## Environments

Dedicated environments ensure that changes are validated before impacting live systems:

- **Development**. Used for building AI Agent configurations (flows, integrations, informational model, etc.).
- **Testing**. Used for validation, QA, and pre-release checks.
- **Production**. Live environment used by end users.

<a id="SolutionVersioningandSnapshots"></a>

## Solution Versioning and Snapshots

To ensure AI quality, testing, and accuracy, Druid offers robust versioning tools within the solution. These tools allow you to manage the internal evolution of a solution separately from its movement between environments.

Snapshots act as localized recovery points within a specific environment.

- **Take Snapshot**. Save the current state of an AI agent solution before making significant logic changes. This serves as a critical recovery point and supports historical auditing.
- **Restore Snapshot**. Revert to a previous version of the solution if testing reveals performance regressions or logic errors in the latest build.
- **Download Snapshot**. Export a specific snapshot to a file for external backup, archival, or manual transfer to another system.
- **Delete Snapshot**. Remove outdated or unnecessary snapshots to manage storage and maintain a clean version history.

<a id="WhentoUseSnapshotsvsExports"></a>

## When to Use Snapshots vs. Exports

While both involve saving the state of a solution, they serve different purposes in the agent lifecycle:

| Feature | Use Case | Description |
| --- | --- | --- |
| Snapshots | Intra-environment iteration | Use these frequently during the development phase in Dev to create safety nets before changing complex flows. |
| Exports | Inter-environment promotion | Use these to package a stable, tested version of a solution for movement into Testing or Production. |

While Export/Import is used for moving between environments, Snapshots are used to manage versioning and recovery points within a single environment.

We recommended taking snapshots on all environments (Dev, Testing, and Production) to ensure the current configuration is saved, allowing you to revert to a stable version in the future if needed.

<a id="ReleaseLifecycle"></a>

## Release Lifecycle

A typical go-live follows these steps:

1. **Define the solution**. In the Development environment, define a solution within the AI Agent to logically group all development work.
2. **Configure the** AI Agent. Add all required components—such as flows, entities, and integrations—to the solution.
3. **Snapshot**. Take a snapshot in the current environment.
4. **Export the solution**. Package the solution into a deployable file.
5. **Import the solution**. Deploy the solution file into the corresponding AI Agent in the Testing environment.
6. **Validate the configuration**. Verify functionality and complete any required data setup, such as dictionary initialization.
7. **Go-live**. Once validated in Testing, import the solution into the Production environment.
8. **Secure Production State**. Before importing new solution versions, take a snapshot in Production to ensure you have a verified recovery point for the live environment.

<a id="KeyConsiderations"></a>

## Key Considerations

By design, solutions focus on configuration, not runtime data.

- **Data Exclusion**. Records and runtime data are not fully included in solution exports.
- **Dictionary Data**. These may require manual setup or initialization via setup flows.
- **Data Initialization and Migration Strategy**. Use setup flows to initialize required data (for example, dictionaries) as part of the deployment process. This reduces manual effort and helps ensure consistency across environments. If your scenario requires migrating existing data, additional configuration may be needed. For guidance, contact your Druid representative.
