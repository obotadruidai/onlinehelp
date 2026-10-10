<a id="ExecutingConnectorActionsFromOutsidetheDRUIDPlatform"></a>

# Executing Connector Actions From Outside the DRUID Platform

You can update data in DRUID based on actions taken in a third-party system using the connector action as a webhook in the DRUID Platform. To execute a connector action from outside the DRUID platform, from within your third-party system, call DRUID's API endpoint `/PerformOperations`.

<a id="Prerequisites"></a>

## Prerequisites

- Reach out to [DRUID Support](<mailto:support@druidai.com?subject=Activate the Druid.WebView service for my tenant>) to activate the **Druid.WebView** service on your tenant and grant you the "read" and "write" claims for this service .
- You have a Druid Portal user account with access rights to the AI Agent and solution on which you want to execute the connector action.
- To execute a connector action from outside DRUID, you need to authorize the `PerformOperations` request using an access token. To get an access token, call the `ExternalAuthenticate` API. For information on how to get access token request, see [ExternalAuthenticate API](#ExternalAuthenticate_API).
> **NOTE:** For higher security, the access token will only be valid for 30 minutes.

<a id="ExternalAuthenticateAPI"></a>

## <a id="ExternalAuthenticate_API"></a>ExternalAuthenticate API

Returns an access token that allows you to access DRUID API endpoints. You should request access token for an active service account who has the privileges to manage AI Agents and solutions.

<a id="Syntax"></a>

### Syntax

`POST *.druidplatform.com/api/services/app/WebAPIService/ExternalAuthenticate`

**Request Body**

```
{
  "userNameOrEmailAddress": "username_or_email",
  "password": "password#",
  "tenant": "tenant_name"
}
```

| Parameter | Data Type | Mandatory | Description |
| --- | --- | --- | --- |
| userNameOrEmailAddress | String | Yes | The username or the email address associated to an existing DRUID service account who has the privileges to manage users. |
| password | String | Yes | Password of the above user account. |
| tenant | String | Yes | The name of your DRUID tenant. |

<a id="Response"></a>

### Response

```
{
  "result": {
    "accessToken": "access_token>",
    "encryptedAccessToken": "encrypted_access_token"
  },
  "targetUrl": null,
  "success": true,
  "error": <error message>,
  "unAuthorizedRequest": false,
  "__abp": true
}
```

| Parameter | Data Type | Description |
| --- | --- | --- |
| accesstoken | String | Access token required as a parameter when sending API requests. The access token is valid for 30 minutes (1800 seconds). When the access token expires, you need to get another one and use that in the next API calls. |
| encryptedAccessToken | String | The encrypted access token. |
| success | Boolean | True if the access token has been successfully generated. |
| error | String | - **Null** if error = “true”. The request was successful. - The error message providing the error reason - if error =”false”. E.g, the tenant name or username do not exist or the password is wrong. |

<a id="Errorcodes"></a>

### Error codes

- 400 – Bad request
- 500 — Internal server error

<a id="Example"></a>

### Example

- DRUID service account user requests an access token. The user has privileges to manage AI Agents and solutions on the tenant "Documentation".
- The user's account credentials are **test-oana** (username) and **Oana123!@#** (password).
- The request is successful and assigns the user an access token. This access token will be valid for 30 minutes (1800 seconds).

![](../Resources/Images/how%20to/execute%20auth%20response.png)

<a id="PerformOperationsAPI"></a>

## PerformOperations API

Executes the specified connector action. Calling this API requires authorization.

<a id="Syntax1"></a>

### Syntax

`POST *.druidplatform.com/druidwebview/api/{tenant_ID}/DataSource/{bot_ID}/PerformOperations`

To get the tenant ID, log into the Druid Portal and from the **Administration** menu, click **Druid Services**. The tenant ID is the number displayed in the **Tenant secret** before the hyphen.

![](../Resources/Images/how%20to/tenant%20id.png)

To get the AI Agent ID, select the desired AI Agent and from the browser get the AI Agent ID. It is placed between `edit/` and `/botdetails`.

![](../Resources/Images/how%20to/bot%20id.png)

<a id="Authorization"></a>

### Authorization

In the authorization section of the `PerformOperations` request, enter the access token you generated with the [ExternalAuthenticate API](#ExternalAuthenticate_API).

![](../Resources/Images/how%20to/auth%20token.png)

<a id="RequestBody"></a>

### Request Body

```
{
    “Type”: 0,
    “Operations”: [“<the ID of the connector action>”],
    “TimeoutInSeconds”: 60,
    “Payload”: {
        “$entityTypeName”: “<the name of the request entity>”,
        “Id”: “<the record ID>”,
        …
    }
}
```

| Parameter | Data Type | Mandatory | Description |
| --- | --- | --- | --- |
| Operations | String | Yes | The ID of the connector action you want to execute in DRUID. To get the connector action ID, in the Druid Portal, go to the connector action you want to execute from outside the DRUID Platform and in the **Connector General** tab, scroll down and copy the value from the **Connector action id** field.  ![](../Resources/Images/how%20to/cnn%20action%20id.png) |
| TimeoutInSeconds | String | Yes | The number of seconds after which the connector action execution times out. |
| Payload | String | Yes | The payload with the request entity contains the data you want to update in DRUID.  **IMPORTANT!** The Payload should contain the name of the request entity, the Id of the entity record and the entity field(s) you want to update.  **NOTE:** To get the Id of the entity record, you need to either have the **Id** field added on the web view or form or get it in your third party system via an integration with your system. |

<a id="Response1"></a>

### Response

If the connector action is successfully executed, the response depends on the action performed in DRUID.

<a id="Errorcodes1"></a>

### Error codes

- 400 – Bad request
- 401 - the access token has expired. You should get another access token then authorize the Perform Operations request.
- 404 - The syntax of the call is incorrect.
- 500 — Internal server error or a parameter in the payload does not exist in DRUID. The response provides you with the error details.

<a id="Example1"></a>

### Example

In this example:

- We have a web view that lists all cases existing in the DRUID Data Services.
- The tenant ID is **13** and the botId is **88c1ccb8-5c52-4b82-8383-08d9e267a599**.
- We will modify the Subject for the case number 1000 from "Access denied" to “User account permission denied”. The record Id of case 1000 is **a082515d-3a4a-41c4-87c0-39dae478fcda**.

![](../Resources/Images/how%20to/subject%20update.png)

- The connector action we will execute from outside the DRUID platform to update the case Subject is **Case-UpdateEntityDruidDataService** and its Id is **49b3a35b-a53d-4661-9ce3-1e88b9ea9f14**.

**Request**

```
{
    "Type": 0,
    "Operations": ["49b3a35b-a53d-4661-9ce3-1e88b9ea9f14"],
    "TimeoutInSeconds": 60,
    "Payload": {
        "$entityTypeName$": "Case",
        "Id": "a082515d-3a4a-41c4-87c0-39dae478fcda",
        "Subject": "User account permission denied"
    }
}
```

**Response**

```
{
    "DataSource": {
        "$entityTypeName$": "Case",
        "CreatedByUserId": "admin",
        "ModifiedByUserId": "test-oana",
        "OperatedByBotId": "00000000-0000-0000-0000-000000000000",
        "ModifiedOn": "2023-09-20T15:17:08.506Z",
        "Id": "a082515d-3a4a-41c4-87c0-39dae478fcda",
        "Subject": "User account permission denied",
        "CreatedOn": "2023-09-20T11:59:48.993Z"
    }
}
```

The case subject has been successfully updated in DRUID.

![](../Resources/Images/how%20to/SUBJECT%20UPDATED%20DRUID.png)
