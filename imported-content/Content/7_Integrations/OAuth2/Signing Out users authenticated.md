---
layout:
  title:
    visible: false
---

<a id="SigningOutusersauthenticatedusingOAuthv2"></a>

# Signing Out users authenticated using OAuth v2

For users authenticated within the conversation using OAuth v2, you can log them out by making a custom configuration based on the Log out endpoint of the API service.

<a id="Step1DefinetheSignOutaction"></a>

## Step 1. Define the Sign Out action

To create the Sign out action, follow these steps:

1. Go to the OAuth2 app configuration page, click the add icon next to the **Sign Out Connector Action** field. The Connector Action page appears on the **Connector general** tab.
2. Provide a **Name**, **Description** and **Category** and select **Is Active**.

![](../../Resources/Images/Oauth%202_FINAL/Signing%20Out%20users%20authenticated.png)

3. Click **Save**. The page refreshes and displays on the **ConnectorSteps** tab.
4. At the top-right corner of the page, click the **Create Task** button and select **Sign Out**.
   The Edit Connector Action page appears on the **General** tab.

<a id="Step2DefinetheSignoutintegrationtask"></a>

## Step 2. Define the Sign out integration task

Enter a **Description** and from the **Connection Code** drop-down, select the action you created at Step 1.

![](../../Resources/Images/Oauth%202_FINAL/Signing%20Out%20users%20authenticated_2.png)

Click the **Request** tab and provide the API endpoint of the web application for logging the user out.

Based on the information (parameters, body) expected by the API service set the request (parameters, etc.). Usually, a log out endpoint expects user metadata which has been previously obtained by the **Get user identity** action.

Example: Log out user from Google

![](../../Resources/Images/Oauth%202_FINAL/Authenticating%20user%20within_3.png)

Click **Save & Close** twice to go to the Integrations page. Publish the integration by clicking the **Publish** button (![](../../Resources/Images/Oauth%202_FINAL/Configuring%20OAuth%20v2%20Authorization_14.png)) at the top-right corner of the page.

<a id="Step3SelectSignOutactionontheOAuth2app"></a>

## Step 3. Select Sign Out action on the OAuth2 app

Go to the OAuth2 app configuration page and from the **Sign Out Connector Action** field, select the integration you defined at Step 2.

![](../../Resources/Images/Oauth%202_FINAL/Signing%20Out%20users%20authenticated_3.png)

Save the app.

<a id="Step4UpdatetheflowforsigninginuserswithOAuthv2"></a>

## Step 4. Update the flow for signing in users with OAuth v2

Go to the conversational flow designed for OAuth v2 authorization. On the flow where you authenticate users using OAuth v2, from the Flow Palette, Dialog section, drag and drop the **Oauth 2.0 Sign out** step. The step requires no further configuration.
