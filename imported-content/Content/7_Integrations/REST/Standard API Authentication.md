---
title: "Standard API Authentication"
---

<a id="StandardAPIAuthentication"></a>


Use this guide if the target API uses a static, long-lived bearer token, API secret, username key, or organization header. For these services, you can skip complex login workflows and directly add permanent credentials to outbound requests.

{% hint style="info" %}
**Info:** If the target API tokens expire periodically and require a dedicated login endpoint call to refresh them, stop here and see the [Advanced Dynamic Authentication](Advanced%20Dynamic%20Authentication.md).
{% endhint %}

<a id="Definetheauthorizationtemplate"></a>

## Define the authorization template

The authorization template automatically attaches static credentials to every outbound integration request made through the connector.

<a id="Step1CreatetheAuthorizeRequesttask"></a>

### Step 1: Create the Authorize Request task

1. In the REST app configuration page, locate the **Authorize request connector action** field and click the **+** icon.
2. Complete the mandatory fields in the **Connector general** tab: **Name**, **Description**, **Category**, **Is Active**.

![](../../Resources/Images/Integrations/inegr%20general.png)

3. Click **Save**, and click the **Connector steps** tab.
4. Click **Create task** and choose **Authorize Request**.

![](../../Resources/Images/Integrations/author%20select.png)

<a id="Step2Configureintegrationtaskmetadata"></a>

### Step 2: Configure integration task metadata

1. In the **General** tab, enter a clear, descriptive name (for example, Authorize Action).
2. Select the matching **Connector Code** from the dropdown.
3. Select **Save**.

<a id="Step3Addcredentialstorequestheaders"></a>

### Step 3: Add credentials to request headers

1. Click the **Request** tab (this view defaults to the Headers sub-tab).
2. Add the authentication key and value required by the target provider.
3. Select **Save & Close** twice to exit the integration task editor.

#### Header formatting example: Bearer token

To pass a static token using a standard Bearer authorization header, apply the built-in string concatenation function inside the header value field:

Header Key: Authorization

Value: `concat('Bearer ', @StaticApiKey)`

![](../../Resources/Images/Integrations/CONCAT%20HEADER%20KEY%20VALUE.png)

<a id="Linktheauthorizeactiontotheconnectorapp"></a>

## Link the authorize action to the connector app

1. On the app configuration page, locate the **Authorize request connector action** dropdown.
2. Select the newly created authorization integration task.
3. Select **Save & Close** to apply the authentication format to all future calls.
