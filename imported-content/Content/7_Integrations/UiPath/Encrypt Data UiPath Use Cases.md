---
title: "Encrypt Data - UiPath Use Cases"
---

<a id="EncryptDataUiPathUseCases"></a>


Druid version 1.61 and higher enables authors to send encrypted data from Druid connectors to the UiPath Orchestrator and RPA robots in integrations with UiPath Orchestrator Queues and UiPath unattended jobs. For the later, the UiPath processes executed by the jobs will have as input arguments the parameters encrypted.

<a id="Usecasesfordataencryptiononconnectors"></a>

## Use cases for data encryption on connectors

- Employees ask UiPath RPA robots to perform specific tasks in an external application/system on their behalf but they need to provide the robot with their account credentials (username and password) and password is sensitive data.
- authors would like to place specific elements in UiPath Queues and they want the information to be anonymized in the Orchestrator logs.

![](../../Resources/Images/UiPath%20Encrypt%20Data%20Use%20Case/Encrypt%20Data%20UiPath%20Use%20Cases.png)

![](../../Resources/Images/UiPath%20Encrypt%20Data%20Use%20Case/Encrypt%20Data%20UiPath%20Use%20Cases_1.png)

The example provided in this section address the first use case.

<a id="Step1EncryptDataontheUiPathconnectorapp"></a>

## Step 1. Encrypt Data on the UiPath connector app

Go to apps and select the desired UiPath app. If you don’t have one, create it following the instructions provided in section [Creating the UiPath Connection Strings](Creating%20the%20UiPath%20Connection%20Strings.md).

On the connector app, select the encryption type **AESCGM** and generate an encryption key.

![](../../Resources/Images/UiPath%20Encrypt%20Data%20Use%20Case/Encrypt%20Data%20UiPath%20Use%20Cases_2.png)

Select **Secure encryption with salt**. By doing so, Druid will alter the Druid fields with a random 64-bit salt and then will encrypt the data using the AES CGM algorithm and the encryption key from the connector app specified in the Encrypt Data integration task. For more information, see next section.

> **NOTE:**  This setting is mandatory for UiPath integration, so that the dedicated UiPath Studio activity in the UiPath processes decrypts the data.

<a id="Step2Encryptthedata"></a>

## Step 2. Encrypt the data

When defining the connector actions, you first encrypt the data based on your needs (in our example, the password) by using the Encrypt Data integration task, and then use that data on subsequent tasks.

If you want to add data encryption on existing UiPath connector actions, add the Encrypt Data task, configure it, and then use the drag and drop functionality to make it the first integration task to be executed in that connector action.

> **NOTE:** Use Encrypt Data as the first integration task on a connector action only if you are using the encrypted data on subsequent integration tasks within that action; otherwise, the encrypted data will be dropped at the end of the action execution.

To add an Encrypt Data integration task, go to the desired UiPath connector action, click the **Create Task** button, click **Security** and select **Encrypt data**.

![](../../Resources/Images/UiPath%20Encrypt%20Data%20Use%20Case/Encrypt%20Data%20UiPath%20Use%20Cases_3.png)

The Encrypt Data configuration page appears.

Provide a **Description** and from the **ConnectionCode** field, select the desired UiPath connector app.

> **Info:**  If the **ConnectionCode** field has no values that means you did not configure data encryption on any of the existing connector apps and you should configure it.

Provide the Druid entity field(s) you want to encrypt (fields from the request entity set on the connector action, e.g. [[UiPathUser]].Password). Druid automatically creates local variables that will store the encrypted values temporarily at runtime during the execution of the integration action. You can use these local variables in subsequent requests (tasks).

Druid uses the following naming rule for local connector variables: **@<entityName>\_<entityField>** corresponding to the Druid entity field selected in the left column, **[[<entityName>]].<entityField>**. For example, Druid automatically generates the local connector variable @UiPathUser\_Password for entity field [[UiPathUser]].Password.

![](../../Resources/Images/UiPath%20Encrypt%20Data%20Use%20Case/Encrypt%20Data%20UiPath%20Use%20Cases_4.png)

Save the integration task, by clicking the **Save & Close** button.

When Druid executes the connector action, it will use the AES CGM encryption algorithm and the encryption key from the connector app specified in the Encrypt Data integration task and will apply encryption on data from mapped input fields, into auto-generated local connector variables.

authors can take input data both from sensitive and non-sensitive entity fields.

The encrypted data will be visible is connector audit logs, for debugging purposes, but only in its encrypted state, so do sensitive data is stored in Druid AI Platform logs.

![](../../Resources/Images/UiPath%20Encrypt%20Data%20Use%20Case/Encrypt%20Data%20UiPath%20Use%20Cases_5.png)

In our example, the employee provides the account credentials (username and password) to the AI Agent, Druid encrypts the password on the connector and sends it to the UiPath RPA robot.

<a id="Step3DecryptthedatainUiPathStudio"></a>

### Step 3. Decrypt the data in UiPath Studio

For the RPA robot to use the encrypted data to perform tasks in external applications, you should decrypt encrypted data in UiPath Studio.

#### Prerequisite

- You have the **UiPath.Cryptography.Activities** package installed in UiPath Studio.

![](../../Resources/Images/UiPath%20Encrypt%20Data%20Use%20Case/Encrypt%20Data%20UiPath%20Use%20Cases_6.png)

Add the **Decrypt Text** activity to the process and configure the activity as follows:

1. Select the **AES CGM** algorithm.

![](../../Resources/Images/UiPath%20Encrypt%20Data%20Use%20Case/Encrypt%20Data%20UiPath%20Use%20Cases_7.png)

2. In the **Key** field, provide the decryption key (that is, the **Encryption Key** generated by Druid).
> **Info:** You can take the decryption key from an Orchestrator asset.

3. Provide the text to be decrypted from a local variable or argument.

![](../../Resources/Images/UiPath%20Encrypt%20Data%20Use%20Case/Encrypt%20Data%20UiPath%20Use%20Cases_8.png)
