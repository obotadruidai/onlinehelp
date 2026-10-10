<a id="SAMLAssertionAuthentication"></a>

# SAML Assertion Authentication

A SAML assertion is an XML document that verifies the user's authentication to the OAuth provider. If you integrate with an API that requires SAML assertion authentication, you need to create a DRUID app with the security type 'SamlAssertion'.

Setting up an app with SAML assertion authentication is similar to setting up custom authentication. This section outlines the steps that are different:

1. Select **SamlAssertion** from the **Security Type** field.
2. Enter the **Public Key** and the **Private Key** you received from your OAuth authentication provider.
3. The **Saml Assertion Xml** field contains a template. Enter values for the parameters in the Variables table, except for **SamlAssertion**, which does not require a value. You will refer to it in the Authenticate Client integration task.

![](../../Resources/Images/druid%207.12/saml%20xml%20values.png)

4. Save the app.
5. When defining the Authenticate Client integration task, make a request to your authentication endpoint as required by the API. Set the Parameters, Headers, or Body with the values appropriate to your authentication API. Use the **@SamlAssertion** variable to securely refer to the SAML assertion XML from the app.

![](../../Resources/Images/druid%207.12/set%20variable.png)

6. On the app, select the authentication integration you defined previously.

## Related Topics

- [Custom Authentication](Custom%20Authentication.md)
