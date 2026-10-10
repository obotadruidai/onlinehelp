---
title: "JWT Assertion Authentication"
---

<a id="JWTAssertionAuthentication"></a>


This section explains how to configure Druid to authenticate API calls using a JSON Web Token (JWT) assertion with Microsoft Identity Platform. This method is particularly useful when integrating with APIs that require JWT assertion authentication.

<a id="WhatisJWTAssertionAuthentication"></a>

## What is JWT Assertion Authentication?

JWT assertion authentication allows your application to prove its identity to an API by presenting a digitally signed JWT. This JWT is signed using a certificate owned by your application and trusted by the Microsoft Identity Platform.

<a id="Prerequisites"></a>

## Prerequisites

Before you begin, ensure you have completed the following steps within the Microsoft Entra admin center:

- Associate a certificate credential with your client application: This involves uploading your certificate to the application registration.

![](../../Resources/Images/JWT%20AUTH%20WITH%20MS/CERT.png)

- Grant Druid API access permissions to your application. Ensure your application has the necessary permissions to interact with the Druid API.

<a id="SetupJWTAssertionAuthenticationinDruid"></a>

## Set up JWT Assertion Authentication in Druid

Configuring an app in Druid for JWT assertion authentication shares similarities with setting up custom authentication. This section highlights the specific steps for this method:

1. Create a new REST app.
2. Provide a name and description for your application.
3. In the **Security Type field**, select **MicrosoftIdentityPlatform**.
4. In the **Authorization Server** field, replace {TenantID} with your Microsoft Entra ID.

![](../../Resources/Images/JWT%20AUTH%20WITH%20MS/TENANT%20ID.png)

5. In the **Token Expires After** field, enter the expiration time on or after which the JWT must not be accepted for processing, and select the time in hours, minutes, days.
> **NOTE:** The value you enter here must not exceed the certificate expiration time.

6. Upload the **Private Key** file associated with the certificate you configured in the Microsoft Identity Platform. This key is crucial for signing the JWT assertion.
7. In the **Audience** field, enter the intended recipient of the JWT. In this scenario, it is the Microsoft login server. You can directly copy and paste the URL from the **Authorization Server** field.
8. In the **Issuer** field, provide the identifier of the principal that issued the JWT. This is your client application's ID.

![](../../Resources/Images/JWT%20AUTH%20WITH%20MS/CLIENT%20APP%20ID.png)

9. In the **Subject** field, specify the claim that identifies the subject of the JWT. This is also the ID of your client application.
10. In the **Client ID** field, enter the ID of your application registered in Microsoft Entra.

![](../../Resources/Images/JWT%20AUTH%20WITH%20MS/CLIENT%20APP%20ID.png)

11. In the **Tenant ID**, enter your Microsoft Entra tenant ID (the same ID used in the Authorization Server field).
> **IMPORTANT!** When authenticating with a third-party application that uses Microsoft Identity Platform (Microsoft Entra ID) solely for authorization—and does not use Microsoft Graph endpoints—you must define the **Scope** variable to target that specific application's API; otherwise, the authorization will fail. In the Variables table, add variable **Scope** (case-sensitive) and set value to: **api://**<Application-ID>**/.default**.
>
> To get the Application (client) ID, follow these steps:
>
> 1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
> 2. In the left navigation pane, expand Identity and select **Applications** > **App registrations**.
> 3. Click the **All applications** tab.
> 4. Search for and select the target third-party application you are authorizing.
> 5. On the Overview page, locate the **Application (client) ID** field.
> 6. Copy to clipboard the GUID value (e.g., 11111111-2222-3333-4444-555555555555).
> 7. Paste this ID in place of <Application-ID> in your Scope value.

12. Save the app.

> **Info:** The JWT assertion is automatically included in all REST calls to external API endpoints (when using the app as Connection Code).
