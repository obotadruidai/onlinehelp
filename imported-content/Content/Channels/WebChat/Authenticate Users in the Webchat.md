---
title: "Authenticate Users in the Druid Webchat"
---

<a id="AuthenticateUsersintheDruidWebchat"></a>


When you want to seamlessly authenticate users in the Webchat hosted on your web page, it's crucial to follow the proper procedures to ensure security and efficiency. This section provides detailed options for transferring authentication context from your web page to the Druid Webchat snippet, enabling automatic authentication of conversations.

> **NOTE:** Data transfer through **queryParams** must occur prior to the initial Druid Webchat initialization. Avoid transferring sensitive data in clear through queryParams to prevent security risks.

<a id="Transferusermetadatausinganaccesstoken"></a>

## Transfer user metadata using an access token

Authenticate users on your web hosting page using OAuth mechanisms like Google or Facebook SSO.

Retrieve the session's access token from the OAuth system on the server hosting the web page. The server will use it to interrogate the authentication system and retrieve the user metadata backend-side.

From the web hosting page send the access token to Druid through queryParams. Druid backend will use the connector to fetch user metadata and authenticate the user based on known Druid mechanisms (e.g., **SaveIdentifiedUser**).

![](../../Resources/Images/WebChat/varanta%201.png)

<a id="Transferusermetadatabackendsideonly"></a>

## Transfer user metadata backend-side only

To securely transfer user metadata backend-side, employ robust systems such as SQL or API-based services designed to store data securely. These systems ensure the protection and integrity of user information during transmission to the backend. As a best practice, the backend-side process should include the transmission of a unique identifier for user metadata, enhancing the overall security and traceability of the data.

In scenarios where the use of SQL or dedicated API-based services is not feasible, Druid offers a secure alternative: the Druid temporary storage. This serves as a reliable solution, guaranteeing the safe transfer and storage of user metadata on the backend. Consider adopting this alternative to maintain the confidentiality and integrity of user information in situations where conventional secure systems are not available.

![](../../Resources/Images/WebChat/varianta%202.png)

<a id="TransferusermetadatabackendsideusingDruidtemporarystorage"></a>

## Transfer user metadata backend-side using Druid temporary storage

Securely transfer user metadata backend-side by leveraging Druid temporary storage within the Druid API service.

Follow these steps to transfer user metadata using the Druid temporary storage:

![](../../Resources/Images/WebChat/VARIANTA%203.png)

<a id="Step1GenerateClientAPIKeyinDruidPortal"></a>

### Step 1. Generate Client API Key in Druid Portal

> **NOTE:** To generate a Client API Key, you must have one of the following:
>
> - A Druid admin security role.
> - A security role with permission to Edit AI Agent.

In the Druid Portal, navigate to your AI Agent details, expand the General section, and generate the Client API Key.

![](../../Resources/Images/WebChat/client%20api%20key.png)

> **IMPORTANT!** Ensure the secure storage of this key in the backend server of the hosting page.

<a id="Step2Configurewebhostingpage"></a>

### Step 2. Configure web hosting page

Configure the web hosting page to notify the hosting server (backend) when a user authenticates. Prior to displaying the web chat, prompt the server to transmit authenticated user metadata to Druid.

<a id="Step3MakeauthenticatedAPIcalltoDruidtemporarystorage"></a>

### Step 3. Make authenticated API call to Druid temporary storage

From the hosting server, perform an authenticated backend-wise API call to Druid temporary storage. Use a POST request to the Druid API `/SetAuthorizationContext`.

Use the API endpoint specific to your DRruid Cloud (community or production):

- **Druid Cloud Community**: https://druidapi.comm.eu.druidplatform.com/
- **Druid Cloud West-Europe**: https://druidapi.druidplatform.com/
- **Druid Cloud US**: https://druidapi.us.druidplatform.com
- **Druid Cloud Australia**: https://druidapi.au.druidplatform.com

##### Request Headers

Add the following properties in teh request header:

- **Content-Type**: set the value to **application/json**
- **x-api-key**: set the value to the Client API Key generated in the Druid Portal.

![](../../Resources/Images/WebChat/property%20in%20header.png)

##### Request Body

In the request body send the following user metadata:

**Request Body - user metadata**

```
{
    "domainUserName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "masterId": "string"
}
```

##### Response

Druid API responds synchronously to the server hosting the web page with a short-lived, single-use token (valid for 30 minutes). Once consumed by a `GetAuthorizationContextByToken` call, the token is immediately invalidated and cannot be reused.

**Response - token**

```
{
"token": "string"
}
```

<a id="Step4DeliverDruidtokentowebpage"></a>

### Step 4. Deliver Druid token to web page

Transmit the token generated by Druid from the hosting server to the web page (client-side).

<a id="Step5IncludetokeninDruidwebchatsnippet"></a>

### Step 5. Include token in Druid webchat snippet

Before initializing the web chat, embed the generated token in the Druid Webchat snippet in queryParams.

```
<script type="text/javascript">
            document.addEventListener("DOMContentLoaded", function(event) {
                DruidWebchat_v2.init({
                    <!-- Common settings  -->
                    botId: "88c1ccb8-5c52-4b82-8383-08d9e267a599",
                    baseUrl: "https://druidapi.testing.druidplatform.com",
                    queryParams: "DruidToken="+token, // pass queryParams to AuthorizeAsync method
                });
            });
        </script>
```

When the user initiates the Druid webchat, the conversation automatically receives the token in the [[QueryParam]] entity, as specified in the code snippet (e.g., DruidToken).

<a id="Step6RetrieveusermetadatafromDruidAPI"></a>

### Step 6. Retrieve user metadata from Druid API

Use that token in Druid (the token received in the [[QueryParams]] entity) on the authentication flow to retrieve user metadata from Druid API. Send an authenticated POST request to `/GetAuthorizationContextByToken`.

##### Request Headers

Add the "x-api-key" property in the request header, setting its value to the Client API Key generated in the Druid Portal.

![](../../Resources/Images/WebChat/property%20in%20header%20get.png)

##### Request Body

In the request body send the token:

**Request Body - send token**

```
{
  "token": “string"
}
```

##### Response

Druid API sends the user metadata based on the token sent.

**Response - user metadata**

```
{
  "botId": "string",
  "domainUserName": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "masterId": "string"
}
```

<a id="Step7Authenticateuserinconversations"></a>

### Step 7. Authenticate user in conversations

Use the retrieved user metadata to authenticate the user in the Druid conversation using classic methods (e.g., **SaveIdentifiedUser**). This ensures a secure and seamless user authentication process within the Druid Webchat environment.

By following these steps, you can seamlessly authenticate users in the Druid Webchat while ensuring data security and integrity.
