---
title: "Data Modeler"
---

<a id="DataModeler"></a>


The Data Modeler designs, reuses, and structures data entities required for agent operations.

<a id="KeyCapabilities"></a>

## Key Capabilities

- Matches requirements against a pre-built data template library covering eight industry areas like: healthcare appointments, insurance claims, retail orders, HR leave requests, support case management, marketing campaigns, academic advising, and outreach campaigns
- Identifies existing data structures to prevent duplicate entity creation.
- Flags terminology discrepancies between requested entity names and template schema definitions prior to import (for example, if you say “Building” but the matching template calls it “Facility”).
- Displays execution plans for user confirmation before applying schema updates.
- Executes a three-step confirmation sequence during template imports to verify complete configuration.
- Builds custom record types, fields, and relational mappings when templates do not match requirements (for example, “a Customer can have many Orders”).

<a id="OperationalRules"></a>

## Operational Rules

- Includes system baseline metadata fields (Name, ID, Creation Date) automatically on new record types.
- Enforces system naming conventions for record and field creation.
- Hands off non-data configuration requests to appropriate specialists automatically.
