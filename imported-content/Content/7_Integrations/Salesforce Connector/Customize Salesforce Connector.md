---
title: "Customize Salesforce Connector App"
---

<a id="CustomizeSalesforceConnectorApp"></a>


Select the Salesforce solution you imported and on the main menu, click **Apps** and click on the Salesforce app.

![](../../Resources/Images/Salesforce%20Connector/Customize%20Salesforce%20Connector.png)

The Salesforce app configuration page appears.

Configure the app by setting up the parameters described in the table below:

| Parameter | Description |
| --- | --- |
| Base URL | Base URL for all further method calls. It is the URL of the Salesforce instance you connect to.  For free trial versions, the base URL is [https://druid-dev-ed.my.salesforce.com](https://druid-dev-ed.my.salesforce.com).  For enterprise and licensed versions, enter the URL you get from the Salesforce team. |
| Security Type | Select **JWTBearer**. Each Salesforce user account has an associated security token that is commonly required when integrating with Salesforce.  DRUID built a native Salesforce Server-To-Server authentication, exactly as described in Salesforce documentation [here](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_jwt_flow.htm&type=5&language=en_US). |
| Consumer Key | The Consumer Key associated to your Salesforce app. To get this key, in Salesforce, go to your app,  To retrieve the Consumer key   1. Log in to Salesforce with the target user account. 2. From the **PLATFORM TOOLS** menu, click **Connected Apps**, then **Manage Connected Apps**. 3. Click the target Salesforce app and in the API (Enable OAuth Settings) section, click **Manage Consumer Detail**s. 4. Open the Connected App target and retrieve the Consumer Key (click Copy).   ![](../../Resources/Images/Salesforce%20Connector/Customize%20Salesforce%20Connector_1.png) |
| Authorization Server | The authorization server must verify that it is the intended audience for the token. Use the following authorization server URL: [https://login.salesforce.com](https://login.salesforce.com), [https://test.salesforce.com](https://test.salesforce.com), or [https://site.force.com/customers](https://site.force.com/customers) if implementing an Experience Cloud site. |
| User name | The username associated to the Salesforce account with privileges to access the Salesforce connected app. |
| Private Key | Upload private key.  The OAuth 2.0 JWTbearer authorization flow requires a digital certificate and the private key used to sign the certificate. For information on how to generate a private key, see [Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm). |
| Token Expires After | The time after which the JWT token expires. A new one will be automatically generated. |

![](../../Resources/Images/Salesforce%20Connector/Customize%20Salesforce%20Connector_2.png)

After customizing the Salesforce app, save it.
