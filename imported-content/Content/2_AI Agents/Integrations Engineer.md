---
layout:
  title:
    visible: false
---

<a id="IntegrationsEngineer"></a>

# Integrations Engineer

The Integration Agent manages connections between Druid AI Agents and external systems.

> **NOTE:** Currently available for Druid Data Service integrations, with third-party tools and enterprise systems planned for future releases.

<a id="KeyCapabilities"></a>

## Key Capabilities

- Audits existing integration endpoints to prevent duplicate connection setups.
- Confirms target integration outcomes in business logic terms before applying connections.
- Modifies active connections to correct mapping errors, parameter configurations, or query structures without requiring a full connection rebuild.
- Outputs change summaries detailing updated parameters after modifications finish.

<a id="OperationalRules"></a>

## Operational Rules

- Imports all available source fields during initial connection setup; narrowing field scope requires post-setup adjustment.
- Limits modification operations strictly to supported connection types.
- Restricts system changes exclusively to explicitly requested endpoints.
