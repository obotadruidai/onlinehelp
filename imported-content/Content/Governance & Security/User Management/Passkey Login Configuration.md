---
title: Passkey Login Configuration
---

# Passkey Login Configuration

Starting with Druid 9.23, administrators can enable user login using a passkey. Once activated, portal users can configure their user profile to log into the Druid Portalsecurely without typing their password every time.

### Admin Configuration: Enable Passkey Authentication

To allow your team to log in using passkeys, the tenant administrator must enable the option globally:

1. Navigate to **Administration** > **Settings** and click the **Security** tab.
2. Scroll down to the Passkey Login section.
3. Select **Enable login with passkey**.

![](<../../../.gitbook/assets/enable passkey login.png>)

4. Click **Save all** at the top right of the page.

### User Configuration: Set Up Your Passkey

If your tenant administrator has enabled this feature, you can configure your user profile to use a passkey for future logins.

{% hint style="info" %}
**NOTE:** You must have a passkey manager installed on your device before starting this setup.
{% endhint %}

To set up your passkey:

1. Log into the Druid Portal.
2. Click on your user profile icon located in the top-right corner of the page.

![](<../../../.gitbook/assets/user icon.png>)

3. Click **My Settings** from the right menu.
4. Click the **Passkeys** tab.
5. Click the **+** icon. If you have multiple passkey managers installed, select your preferred manager from the system prompt; otherwise, your default manager will launch automatically.
6. Choose the option to create a new passkey within your manager window. Depending on your specific passkey manager, enter your Druid Portal credentials to generate the passkey or authorize it via your device PIN.

![](<../../../.gitbook/assets/ENTER CREDENTIALS.png>)

7. Click **Save** inside your passkey manager interface.
8. Click the **+** icon on the Druid Portal again, and select the newly created passkey from your passkey manager modal.

![](<../../../.gitbook/assets/select passkey.png>)

9. A new device record will appear in your Passkeys tab list.

![](<../../../.gitbook/assets/passkey added.png>)

10. Click the **Save** button at the bottom of the My settings modal to finalize the process.

The next time you access the Druid Portal login page, you can choose to authenticate seamlessly using your passkey.

![](<../../../.gitbook/assets/log in.png>)
