---
title: "Enforce Login with Single Sign On (for Druid Portal admins)"
---

<a id="EnforceLoginwithSingleSignOnforDruidPortaladmins"></a>


By default, the login page allows users to sign in using either Single Sign On (SSO)—if enabled on the tenant—or standard user credentials (username and password).

![](../../Resources/Images/Enforce%20login%20with%20Single%20Sign%20On/Single%20Sign%20On%20Login%20Enforcement.png)

To mitigate the risk of DDoS attacks, credential theft, and unauthorized access from orphaned accounts, you can restrict login to SSO only, provided you have already enabled and configured login with an external provider (OpenID Connect, LDAP, Google, or WS-Federation). This ensures that all authentication follows your organization's centralized security policies and MFA requirements.

![](../../Resources/Images/Enforce%20login%20with%20Single%20Sign%20On/Single%20Sign%20On%20Login%20Enforcement_1.png)

> **NOTE:** This feature is available in Druid 9.18 and higher.

<a id="EnforceSSOLogin"></a>

## Enforce SSO Login

To enforce SSO login:

1. Go to **Administration** > **Settings**.
2. Click the **External Login Settings** tab.
3. Select **Enforce SSO login** and copy the **Login key**.

![](../../Resources/Images/Enforce%20login%20with%20Single%20Sign%20On/Single%20Sign%20On%20Login%20Enforcement_2.png)

4. Save this key in a secure vault for admin access only.
> **IMPORTANT!** If something goes wrong with the SSO login (downtime with the SSO provider, etc.) you want to provide the users with the option to login with user credentials. In order to do that, you will need the **Login key**.

5. Click the **Save all** button at the top right corner of the page.

<a id="RestoreMixedModeAuthentication"></a>

## Restore Mixed Mode Authentication

If you need to re-enable both SSO and credentials login (mixed mode), you must use the **Login key** to bypass the enforcement.

You can do this in two ways:

- Access your standard login page and, in the browser address bar, add **?login-key=<login key value>** to the end of the URL, replacing <login key value> with the key you previously saved in your secure vault.
- Access your tenant using the following URL format:

<tenancyName>.<subdomains>.druidplatform.com/account/login?login-key=<login key value>

Once the default login page appears:

1. Log in with your admin credentials (username and password).
2. Go to **Administration** > **Settings**.
3. Click the **External Login Settings** tab.
4. Disable **Enforce SSO login**.
5. Click the **Save all** button at the top right corner of the page to save the settings.
