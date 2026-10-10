---
layout:
  title:
    visible: false
---

<a id="Step1CreateADApp"></a>

# Step 1. Create AD App

Creating an AD app means defining your AD connection string for the AI Agent within the selected solution.

The connection string is a list of key/value pairs that the Connection object will parse; it will use the information to find the domain root and domain address, authenticate, and establish a connection.

To create an AD app:

1. From the solution menu, click **Apps**. The Apps page appears listing the connection strings created for the selected solution.
2. From the **Create App** dropdown, select **Active Directory**. The app configuration page appears.
3. Provide the details listed in the table below.

| Field | Description |
| --- | --- |
| Code | Unique name to identify the App. You will reference in each Integration you call from this AD App. The field is mandatory. |
| Type | The field automatically filled in with **Active Directory**. It is non-editable. |
| Icon | Select the icon that best describes the app. It helps you easily identify the app in the list of apps. If no icon is selected, Druid default icon per selected app type will be shown in the apps list. |
| AI Agent | The field is automatically filled in with the name of the AI Agent on which you’re creating the AD app. It is non-editable. |
| Execution Timeout | The maximum number of seconds a request is allowed to execute. By default, the timeout for all connector integrations is 60 seconds. This setting will apply to all connector tasks which use this app.  **IMPORTANT!** To avoid long execution time for an integration with many tasks, the maximum sum of all timeouts configured on an integration is 250 seconds. Whenever this maximum is reached, the execution of the currently running integration task is interrupted and any subsequent integration tasks are no longer executed. |
| Encryption Type | Enables data encryption on the connector using the AES CGM encryption algorithm and allows authors to encrypt specific data before sending it to external AD apps, by using the Encrypt Data integration task as first task in the desired connector action.  When you select AES CGM encryption algorithm (the only one currently available), two new options are available:   - **Encryption Key** – click the **Generate** button to generate the key, which will be used by the Encrypt Data task to encrypt the data and by the client / 3rd party application to decrypt the data and use it further. - **Secure encryption with salt** – adds a random 64-bits salt to the data before encrypting it. Please note that using this feature requires the client to develop code for data decryption.   For more information, see [Encrypt Data](../Encrypt%20Data/EncryptData.md). |
| Domain Root (Search base) | The root domain in your company’s AD domain namespace hierarchy.  Example: `DC=Druidad,DC=local` |
| Client type | Specifies the authentication method used for the LDAP connection. **Simple** uses basic DN (Distinguished Name) and password authentication, while **Digest** (SASL) provides a more secure MD5-based challenge-response mechanism. |
| LDAP Schema | Defines the connection protocol and security layer:   - **LDAP**: Standard unencrypted connection (typically port 389). - **LDAPS**: LDAP over SSL/TLS, encrypting the communication from the start (typically port 636). - **STARTTLS**: Initiates a plain LDAP connection and then upgrades it to a secure TLS connection on the same port. |
| Domain Address | The IP address or the DN of the DNS host name. |
| Port | The network port used for the connection. Common defaults are 389 for LDAP/STARTTLS and 636 for LDAPS. |
| User name | The credential used to authenticate the Active Directory connection. The required format depends on the selected Client type:   - **Simple authentication**: Requires the full LDAP Distinguished Name (DN). This identifies the specific user object within the directory hierarchy.  *Example: CN=oanabota,OU=Product,DC=domain,DC=com*  For a complete list of Relative Distinguished Name (RDN) attribute types, refer to the [Microsoft documentation](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ldap/distinguished-names). - **Digest authentication**: Typically uses the Simple User Name (sAMAccountName) or the User Principal Name (UPN) rather than a full DN.  *Example: oanabota or oanabota@domain.com* |
| Password | The password of your AD domain admin account. |
| Domain | The FQDN of the Active Directory domain (e.g., corp.contoso.com). |

4. Save the app.
