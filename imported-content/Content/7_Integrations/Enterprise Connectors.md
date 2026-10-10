<a id="EnterpriseConnectors"></a>

# Enterprise Connectors

Enterprise Connectors are the primary mechanism for enabling Druid AI Agents to communicate with external business applications, automation platforms, and databases. These connectors translate conversational inputs into structured data queries that your backend systems can understand, allowing agents to perform high-value business operations.

<a id="SupportedConnectionTypes"></a>

## Supported Connection Types

Druid supports a wide array of industry-standard protocols and platform-specific integrations, categorized by their technical architecture:

- **Web Services**: Full support for REST and SOAP APIs, allowing for seamless synchronous communication with modern web-based applications.
- **Data & Storage**: Direct connectivity to Relational Databases (SQL) and cloud storage like Azure Blob Storage. This category also includes the Druid Data Service Connector and UiPath Data Service, providing high-level abstraction for structured data layers.
- **Enterprise Resource Planning (ERP)**: Dedicated integration capabilities for SAP, ensuring secure and optimized data exchange with core business modules.
- **Robotic Process Automation (RPA)**: Deep integration with UiPath and BluePrism, allowing AI Agents to trigger attended or unattended robots to complete complex tasks across legacy systems.
- **Identity & Productivity**: Specialized connectors for Active Directory (authentication), Salesforce (CRM data), and eSign services (digital signatures).

<a id="Configuration"></a>

## Configuration

To establish and manage a connection using an Enterprise Connector, follow these primary phases in the Druid Portal:

1. **Define the connection**. Configure the Connection String, including the base URL and authentication headers (OAuth 2.0, SAML, Basic, or API Key).
2. **Map the integration actions**. Create specific requests (Integration Actions) for the operations your AI Agent needs (e.g., GET customer details, POST a new ticket, or Trigger RPA Robot).
3. **Refine with developer tools**. Utilize the Connector Designer to map data variables and use connector local variables for temporary data processing during the flow.
4. **Test & Debug**. Use the built-in Debugging Integrations tool to verify that the external system returns the expected payload and to review changes before deployment.
