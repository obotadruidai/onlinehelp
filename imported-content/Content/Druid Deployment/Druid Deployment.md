---
layout:
  title:
    visible: false
---

<a id="DruidDeployment"></a>

# Druid Deployment

In the era of digital transformation, organizations are challenged to innovate faster while keeping their network, systems and applications available, scalable and secure. But faster innovation while meeting the requirements in terms of availability, scalability and security can be hard to achieve especially due to the budget and resources constrains.

At Druid, we understand that every enterprise has unique needs and values the power of choice, so we offer flexible deployment options to meet your enterprise needs and resources. Choose the deployment option that best suits your enterprise needs.

The deployment models depend on where the infrastructure for the deployment resides and who has control over that infrastructure.

<a id="DruidDeploymentComparison"></a>

## Druid Deployment Comparison

| Category | Feature | Cloud | Hybrid | On premise | Edge\*\*\* |
| --- | --- | --- | --- | --- | --- |
| Platform | Requires installations | N | Y | Y | **Y** |
|  | Release cycle | Monthly (automatically applied) | Monthly (manually, at your choice) | Monthly (manually, at your choice) | Monthly (manually, at customer choice) |
| Infrastructure | Additional hardware / software required | N | Y | Y | **Y** |
|  | Auto scaling | Y | supported, requires on premise hardware infrastructure | supported, requires on premise hardware infrastructure | supported, requires on premise hardware infrastructure |
|  | High Availability | Y | supported, requires on premise hardware infrastructure | supported, requires on premise hardware infrastructure | supported, requires on premise hardware infrastructure |
|  | Connectivity with on premise apps | Internet calls to your on premise apps | No Internet calls to your on premise apps | No Internet calls to your on premise apps | Local / no Internet required |
|  | Conversation History - Data in transit | By Druid | By Druid | Hosted on premise | Customer-controlled |
|  | Conversation History - Data at rest | By Druid | Hosted on premise | Hosted on premise | Hosted on premise |
| Platform Security | Multi-Factor Authentication | Y | Y | Y | Y |
|  | User access management | Y | Y | Y | Y |
|  | Role based access control | Y | Y | Y | Y |
|  | Data at rest | SQL encryption |  |  | Customer-managed encryption |
|  | Data in transit | SSL, TLS1.2 |  | TLS 1.1, TLS1.2, as per your existing environment | TLS 1.2+, per customer environment |
| Support | Term | on-going | 2 years from release | 2 years from release | 2 years from release |
| Channels | Direct line (WebChat) | Y | Y | Y | Y\* |
|  | MS Teams | Y | Y | N | N |
|  | WhatsApp | Y | Y | Y\* | Y\* |
|  | Facebook Messenger | Y\*\* | Y\*\* | Y\*\* | Y\*\* |
|  | Slack | Y | Y | N | N |
|  | GoogleChat | Y | Y | Y | Y |
|  | WeChat | Y | Y | Y\* | Y\* |
|  | Telegram | Y | Y | N | N |
|  | Viber | Y | Y | Y\* | Y\* |
|  | Twilio | Y | Y | N | N |
|  | Instagram | Y | Y | Y | Y |
|  | LINE | Y | Y | N | N |
|  | WeCom | Y | Y | Y\* | Y\* |
|  | Webex | Y | Y | Y | Y |
|  | Office 365 Email | Y | Y | N | N |

\*Only available if specific Druid services have open connection to the Internet.

\*\*In Druid hybrid and cloud deployments Facebook channel uses the Microsoft Bot Framework, while in on premise deployments it uses direct DRUID Facebook integration.

#### \*\*\*Edge Deployment

Druid AI **fully supports edge deployment** through its containerized, **Kubernetes-based architecture**, enabling AI knowledge management and productivity applications to run **on-premises**, **in private cloud**, or **hybrid environments** with **full data sovereignty**, without reliance on public cloud inference.

Edge deployment refers to customer-managed, localized infrastructure deployments (including private data centers and regulated environments) using the same Druid AI Platform architecture as on-premises and hybrid deployments.

Edge deployments may operate in restricted or disconnected network environments, subject to customer security policies.

**Key capabilities**

- Fully on-premises deployment (including LLMs and knowledge base)
- Hybrid edge + cloud deployments
- Kubernetes-based portability across regions and infrastructures
- Data never leaves customer-controlled environments
- Supports regulated industries (finance, government, healthcare)
