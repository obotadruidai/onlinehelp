<a id="DataSecurityandPrivacy"></a>

# Data Security and Privacy

Druid protects data, identity, and access across the full platform runtime—from user authentication and role assignment through to data storage, system communication, and operational monitoring. Security controls are built into the platform architecture and apply consistently across all deployment topologies. They do not require additional configuration for regulated or sensitive deployments.

<a id="PlatformDataEncryption"></a>

## Platform Data Encryption

Data protection is enforced at every layer of the architecture to ensure enterprise-grade security:

- **Data in Transit**: All communication is protected using TLS 1.2 or higher.
- **Data at Rest**: Databases and storage are encrypted using AES-256.
- **Key Management**: Customer-managed key options are available for regulated deployments requiring additional control over key custody.

<a id="IdentityandAccessManagement"></a>

## Identity and Access Management

Druid uses Role-Based Access Control (RBAC) to govern which users can access specific AI Agents, flows, data, and platform features.

- **Granular Control**: RBAC policies are applied at the tenant, AI Agent, and flow level, allowing fine-grained control over authoring privileges, user access, and knowledge segmentation across teams and geographies.
- **Authentication Methods**: Druid supports industry-standard methods including:

  - **Single Sign-On (SSO**): Integration via Active Directory, Okta, and Google using OAuth 2.0 and SAML protocols.
  - **Multi-Factor Authentication (MFA)**: Enforced across all deployment models.
  - **Access Rules**: Attribute-based and time-bound rules for granular session and resource control.

For detailed configuration steps, see Authoring User Management.

<a id="PIIandPHIProtection"></a>

## PII and PHI Protection

Druid secures sensitive data by decoupling personal information from the AI Agent execution layer.

- **Real-time Anonymization**: The platform applies automatic PII anonymization during conversation processing. Sensitive data—including personal identifiers, account numbers, and health information—can be masked, anonymized, or tokenized before it is stored or passed to connected systems.
- **Compliance Workflows**: Consent management, data deletion workflows, and residency rules ensure that protected data does not surface outside the boundaries defined by your deployment policy.

<a id="IntegrationSecurity"></a>

## Integration Security

To maintain security when communicating with external systems, Druid provides field-level protection for integration payloads.

- **Sensitive Data Manipulation**: Administrators can configure specific fields and entities to be masked, ensuring sensitive information is never exposed in the UI or plain-text logs.
- **Encrypt Data Connector**: Use this tool to secure data payloads exchanged with third-party systems, ensuring end-to-end encryption.
