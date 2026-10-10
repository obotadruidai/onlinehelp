---
title: "Ellucian Banner"
---

<a id="EllucianBanner"></a>


Ellucian Banner is a comprehensive enterprise resource planning (ERP) platform designed specifically for higher education institutions. Integrating your AI agent with Banner allows students to interact with their academic and administrative data through a conversational interface.

This integration focuses on Student Self-Service capabilities. By connecting to the Banner API via the Ellucian Ethos Integration Hub, the AI agent can provide students with real-time access to:

- **Course Management**. Retrieval of course lists and schedules.
- **Academic Progress**. Viewing total credits earned, GPA details, and learning curricula.
- **Admissions**. Checking the status of current applications.
- **Advising**. Accessing academic advice and degree progress.

<a id="Prerequisites"></a>

## Prerequisites

Before configuring the integration in the platform, ensure the following requirements are met by your IT administrator:

- **Ethos Application Creation**. An application must be registered within the Ellucian Ethos Integration Hub for the AI Agent integration. This application defines which Banner resources (e.g., students, grades) the AI Agent is authorized to access.
- **API Key**. A unique API Key (UUID) must be generated for the registered application. This key is used to authenticate the AI Agent requests to your Banner data.
- **Tenant URL (Base URL)**. You must obtain the specific Base URL for your institution's Ethos instance. Common formats include:

- **Production**: https://integrate.elluciancloud.com/
- **Sandbox/Dev**: https://integrateapi.elluciancloud.com/

You also have a published AI Agent.

<a id="ConfigurationSteps"></a>

## Configuration Steps

This section explains how to integrate with Ellucian Banner.

<a id="Step1ConfigureUserAuthentication"></a>

### Step 1: Configure User Authentication

Because the AI Agent retrieves personalized student data, you must first establish a secure connection between Druid and your institution's identity provider.

Set up an Identity Provider (IdP) in Druid (e.g., Azure AD, Okta) to authenticate students. To ensure the student's identity is correctly mapped to their profile, refer to the help topic specific to your institution's authentication method:

- [Active Directory](../../../../7_Integrations/Active%20Directory/Active%20Directory%20Connector.md)
- [SSO Authentication and Authorization with OAuth2](../../../../7_Integrations/OAuth2/SSO%20Authentication%20and%20authorization.md)
- [SSO Authentication with SAML](../../../../7_Integrations/SamlAuth/SSO%20Authentication%20with%20SAML.md)

<a id="Step2ConfiguretheBannerAppinDruid"></a>

### Step 2: Configure the Banner App in Druid

To set up the Banner app within the Druid Portal, follow these steps:

1. Navigate to **Solution Contents** > **Apps**.
2. Click the **Create App** button to create a new app and select **REST**. The New App page opens.
3. In the **Code** field, enter a unique app identifier (e.g., Ethos\_API).
4. In the **Base URL** field, enter the URL of your institution's Ethos instance.

![](../../../../Resources/Images/Banner/app%20general.png)

5. From the **Security type** dropdown, select **Custom**. The Custom security type requires specific connector actions to manage the secure handshake between the Druid AI Platform and Banner. For detailed instructions on how these actions work, refer to [Custom Authentication](../../../../7_Integrations/REST/Custom%20Authentication.md).
6. In the Variables table, add a variable named **apikey** and paste the Ethos API Key in the Value column. Check the Encrypted box to secure the key.

![](../../../../Resources/Images/Banner/custom%20security.png)

7. Save and publish the app.
