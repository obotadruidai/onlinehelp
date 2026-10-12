---
title: Creating SMTP Connectors
---


Druid allows you to integrate with Simple Mail Transfer Protocol (SMTP) server to send emails.

{% hint style="info" %}
**NOTE:** For hybrid and on-premise Druid deployments, your network administrator needs to grant the SMTP connector access to your SMTP server.
{% endhint %}

This section describes the procedure for creating SMTP connectors.

## Step 1. Create App

Creating a SMTP app means defining your SMTP connection strings for the AI Agent within the selected solution.

To create a SMTP app:

1. From the main menu, click **Apps**. The Apps page appears listing the connection strings created for the selected solution.
2. Click **Create App** at the top-right corner of the page and select **Smtp** from the dropdown. The Edit Connector page appears.
3.  Provide the details listed in the table below.

    | Field                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | Code                   | Unique name to identify the App. You will reference in each Integration you call from this SMTP App. This is a mandatory field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
    | Execution Time         | The maximum number of seconds a request is allowed to execute. By default, the timeout for all connector integrations is 60 seconds. This setting will apply to all connector tasks which use this app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | Encryption Type        | Enables data encryption on the connector using the AES CGM encryption algorithm and allows authors to encrypt specific data before sending it to external SMTP apps, by using the Encrypt Data integration task as first task in the desired connector action. When you select AES CGM encryption algorithm (the only one currently available), two new options are available: - **Encryption Key** – click the **Generate** button to generate the key, which will be used by the Encrypt Data task to encrypt the data and by the client / 3rd party application to decrypt the data and use it further. - **Secure encryption with salt** – adds a random 64-bits salt to the data before encrypting it. Please note that using this feature requires the client to develop code for data decryption. For more information, see [Encrypt Data](<../Encrypt Data/EncryptData.md>). |
    | Host                   | The URL or IP address of your SMTP Server. This is a mandatory field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | Port                   | If your SMTP requires a specific port for the secure submission of email for delivery, provide the port number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
    | User name and Password | If your SMTP server requires authentication, provide the credentials (user name and password) of your SMTP Server account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

If your SMTP server sends emails using a secure SSL connection, click the **Use SSL** and select the SSL option specific to your SMTP server setup. If your SMTP server has a timeout mechanism set up, provide the timeout.

![](<../../../.gitbook/assets/Creating SMTP Connectors_2.png>)

4. Click the **Save & Close** button to save the app.

## Step 2. Create Integration Actions

Connector Action (Integration) only represents a host for a group of one or more integration tasks. The integration technology/type (SQL, REST, SOAP, SMTP, etc.) is defined at task level, not at action (integration) level.

**Example**: If, at a certain point in the conversation flow, you need to send an email to the client, but the necessary data for that email comes from 2 different sources, you can create a single action which always performs the three operations, sequentially (getting email address from an SQL Database, then getting some HR data via a REST API call, and then sending this data to that email address using a SMTP call). From the flow designing point of view, you only place one integration action on the flow step.

If a connector action (integration) has more tasks, the response data will be returned to the flow only after ALL tasks inside the action have run. Implicitly, data in the response entity might be altered by the execution of each task. Also, tasks within the same action can be of different types (SQL, REST, SOAP, SMTP, etc.).

Thus, at Connector Action (Integration) level, only the general information is saved, and used for describing and identifying the action.

Using the solution’s Connector Designer, you can define the integration actions and tasks:

1. From the main menu, click **Integrations**. The Connector Designer appears.
2. At the top-right corner of the page, click the **Create Connector Action** button The Edit Connector Action page appears by default on the **Connector general** tab.
3. Provide the connector action general details by setting up the parameters described in the table below.

| Parameter            | Description                                                                                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                 | The name of the action. The field is mandatory.                                                                                                                                             |
| Description          | A brief description of the action that might be useful for other tenant admins. The field is mandatory.                                                                                     |
| Category             | Define on the spot when creating the action. Useful when you want to find the actions in the Integrations list. The field is mandatory.                                                     |
| Icon                 | Select the icon that best describes the integration. It helps you easily identify the integration action in the list of integrations. If no icon is selected, Druid will show default icon. |
| Request Entity Name  | Select Email. The AI Agent uses the **\[\[Email]]** entity to send emails to the SMTP server via the current action.                                                                        |
| Response Entity Name | Select Email. The AI Agent uses the **\[\[Email]]** entity to receive notifications from the SMTP server via the current action.                                                            |
| Is Active            | Tick to activate the connector action. An inactive connector action will be ignored at runtime.                                                                                             |

4. Click **Save** to save the settings and stay on page to add tasks, or click **Save & Close** to save and exit the page. If you click **Save**, the **Connector steps** tab appears.

You can add as many connector actions as best suit your integration needs.

{% hint style="info" %}
**NOTE:** A Connector Action represents a set of one or more integration tasks, which run sequentially and use the same request and response entities.
{% endhint %}

## Step 3. Add Integration Tasks

1. At the top-right corner of the Edit Connector Action page (**Connector steps** tab), click on **Create task**, and then click **Email** > **Send SMTP**. The Edit Connector Task page appears by default on the **General** tab.
2. Set the general parameters:

| Parameter       | Description                                                      |
| --------------- | ---------------------------------------------------------------- |
| Description     | Provide a brief relevant description of the task.                |
| Connection Code | Select the SMTP app (for Connection Strings to your SMTP server) |

3. In the Headers section, define any custom SMTP headers you want to pass with the email request:
4. Click the Add (+) icon to create a new header row.
5. In the **Key** field, enter the header name (e.g., `X-KC-Customer-ID`).
6. In the **Value** field, enter the corresponding static text or dynamic variable (e.g., \[\[Csutomer]].Id).

![](<../../../.gitbook/assets/smtp headers.png>)

{% hint style="info" %}
**Info:** Sending custom headers is available starting with Druid 9.27.
{% endhint %}

4. Click the **Save** button.

## Step 4. Use Integration Action on Your Flow

On your flow, add a step for sending emails and configure it as follows:

1.  Click the **Set Variables** section header and add the following variables:

    ![](<../../../.gitbook/assets/Creating SMTP Connectors_5.png>)

    | Variable            | Description                                                                                                                                                                                                                       |
    | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | \[\[Email]].To      | The main recipient(s) of the email. If you want to send email to more than one person (email address), separate their email addresses using semicolon, no spaces. E.g., “person1@emailaddress.domain;person2@emailaddress.domain” |
    | \[\[Email]].From    | The email address from which emails are sent. It is the email address reserved by your system administrator for the AI Agent. E.g., [no-reply@Druidai.com](mailto:no-reply@druidai.com).                                          |
    | \[\[Emai]].Cc       | The email address(es) to which a copy of the email will be sent to other than the main recipient(s) of the email. The other recipients will see that someone else has been sent a copy of the email.                              |
    | \[\[Email]].Bcc     | The email address(es) to which a copy of the email will be sent to other than the main recipient(s) of the email. The other recipients won’t be able to see that someone else has been sent a copy of the email.                  |
    | \[\[Email]].Subject | A short description about the objective or primary topic of the email. It is the first text recipients see after the sender name when an email reaches their inbox (or simply the Email’s Subject).                               |
    | \[\[Email]].Body    | The email content. If you want to include HTML in the email body, you can do so by escaping the double quotation mark (“”) and replacing it with backslash (). For an example, see [Email Body](<Email Body.md#_Email_Body>).     |

    If you want to add attachment to the email and you uploaded the file to a previous step, you also need to add the variable **\[\[Email]].Attachment** and in the value field and type the name of the file to send as email attachment. E.g., \[\[Email]].Attachment1 = \[\[Employee]].File.

{% hint style="info" %}
**Info:** If you want to attach more than one email attachment, you can do so by adding more variable \[\[Email]].Attachment1, \[\[Email]].Attachment2, etc.
{% endhint %}

2.  Click the **PreActions**/**PostActions** section header and select the integration action you created for sending emails via the SMTP server.

    ![](<../../../.gitbook/assets/Creating SMTP Connectors_6.png>)
3. Click the **Save** button to save the flow step.
