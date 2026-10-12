---
title: Accessing Druid Endpoints in Druid Hybrid Deployments
---


{% hint style="info" %}
**NOTE:** Druid Endpoints are available in Druid Connector Host version 1.52 or above. If you want to integrate Druid with third party applications that are installed on premise, you need to install Druid Connector Host version 1.52 or above on premise so that your application can communicate with Druid.
{% endhint %}

This configuration should be used in the hybrid scenario only, when both the Druid Connector Host AND the integrating services (e.g., UiPath Orchestrator) are installed in on-premise infrastructure and can only communicate INSIDE the intranet.

The Druid Connector Host will forward the calls received in its endpoint service towards the Druid AI Platform cloud infrastructure.

To access Druid endpoints in Druid hybrid deployments, you need to configure the endpoint parameters (Base URL and Local port number) as follows:

* For Druid version 1.57 or higher, configure the Druid Endpoints parameters in the installation wizard ([Druid Connector Host installer](https://druidai.gitbook.io/druid-ai-docs/hybrid/druid-connector-host/install-druid-connector-host)).
* From Druid version 1.52 to 1.56, add the **Base URL** and **Local port number** parameters in the Druid Connector Host configuration file.

## Use Case: UiPath

If the on-premise UiPath Orchestrator webhook cannot make calls outside the internal network, then its calls can be directed towards the Druid Connector Host, which in this scenario acts as an endpoint.

When setting up the third-party application webhook, you need to provide a specific URL in the following format:

_http://localhost:5008/Druidendpoints/_{\*\*catchAll}

Where:

* Localhost is the address of the machine where the Druid Connector Host is installed and can be accessed from another machine within the intranet.
* {\*\*catchAll} is the Druid endpoint. To take this endpoint, in the Druid Portal, go to your UiPath connector app and from the Druid Endpoint URL copy only the endpoint.

![](<../../.gitbook/assets/endpoint druid.png>)

Example: _http://192.168.0.10:5008/Druidendpoints/api/UiPath/Events/Job/899839..._,

Where:

* _http://192.168.0.10_ is the address of the Druid Connector Host.
* _/api/UiPath/Events/Job/899839…_ is the dedicated AI Agent endpoint for UiPath integration.

For the complete list of Druid Endpoints, access the following link: {Druid Endpoint Base URL}_/swagger/index.html_

The {Druid Endpoint Base URL} is unique to each environment and it is available in the connector app details, **Druid Endpoint URL** field.

![](<../../.gitbook/assets/DRUID ENDPOITN BASE URL.png>)
