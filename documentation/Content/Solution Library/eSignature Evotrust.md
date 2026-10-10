<a id="ElectronicSignaturewithEvrotrust"></a>

# Electronic Signature with Evrotrust

This solution enables electronic signing of documents by integrating Evrotrust and DigiTech Consult's REST API services. These services handle different aspects of the process:

- **Evrotrust**

- Sending documents
- User authentication
- User identification
- Downloading documents
- Document encryption

- **DigiTech Consult (DCS)**

- Generating RSA encryption keys
- Extracting metadata from documents
- Document decryption
- Generating and returning dynamic, temporary URLs for the decrypted signed documents
- Automatically and periodically deleting signed documents shortly after creation.

<a id="KeyBenefits"></a>

## Key Benefits

- Secure Encryption: RSA encryption ensures document confidentiality at every step.
- Streamlined Workflow: Automated metadata extraction and temporary URLs simplify document handling.
- User-Friendly Process: Integration with Evrotrust’s provides a seamless signing experience.

<a id="Howitworks"></a>

## How it works

#### Step 1: Initiating the Process

1. The user provides their phone number to the AI Agent.
2. After validation, an integration call is made to DigiTech Consult’s server (DCS) to generate a new RSA key pair:

- The public key is sent to Druid.
- The private key is securely stored in DCS for use during decryption steps.

#### Step 2: Authentication

1. An integration call is triggered to Evrotrust’s authentication service with the phone number and public key.
2. Evrotrust returns a transaction ID, completing the authentication process.

#### Step 3: Identification

1. When the user clicks the **Identify** button, Druid sends another integration call to Evrotrust’s identification service with the phone number and public key.
2. Evrotrust:

- Sends a document containing the user's personal data to their mobile app.
- Returns a transaction ID to Druid.

#### Step 4: Signing the Document

1. After signing the document in the Evrotrust mobile app, the user confirms in Druid by clicking a button.
2. An integration call is made to DCS with:

- The transaction ID
- A unique conversation token generated for the chat session

3. DCS requests the signed document from Evrotrust:

- The encrypted document is downloaded and decrypted by DCS.
- DCS extracts metadata from the document (e.g., personal data fields) and generates a temporary URL pointing to the signed document.

4. The metadata and the temporary URL are returned to Druid.

#### Step 5: Sending the Signed Document for Final Approval

1. The user clicks the Sign button to proceed, triggering another integration call to Evrotrust with the phone number and public key.
2. Evrotrust sends the prepared document to the user’s mobile app and provides a transaction ID.
3. Druid waits for the user to sign the document in the app.

#### Step 6: Finalizing and Downloading the Signed Document

1. Once the user confirms the signed document in the chat:

- Druid triggers a call to DCS with the transaction ID and conversation token.
- DCS downloads the encrypted signed document from Evrotrust, decrypts it, and stores it temporarily.
- DCS generates a temporary URL pointing to the signed document.

2. Druid presents this URL to the user, allowing them to download the signed document.

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../2_AI%20Agents/Creating%20AI%20Agents.md).
- To integrate Evrotrust and DigiTech Consult services for electronic document signing, obtaining specific API keys and completing contractual steps is essential. These measures ensure secure communication and proper usage of the services. To obtain the required API keys, contact [DigiTech Consult Ltd Sales](<mailto:plamena@digitechconsult.com?subject=DRUID Esignature with Evotrust solution>).

<a id="Configuringthesolution"></a>

## Configuring the solution

To configure the solution, follow these steps:

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

### Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution 'Electronic Signature with Evrotrust' and import it following the instructions provided in section [Installing Solution Templates](Installing%20Solution%20Templates.md).

Wait until the import status shows as “Success.”

Once the import is successful, click **Save & Close**.

<a id="Step2SetuptheAIAgentspecialflows"></a>

### Step 2. Set up the AI Agent special flows

Make sure that the **Intent not found flow** is selected on the AI Agent (AI Agent details > Dialogue Management).

<a id="Step3ConfigureEvotrustAPIkey"></a>

### Step 3. Configure Evotrust API key

On the **Solution Contents** menu, click **Integrations**, then click on the **Hash Request** integration. The integration contains only a custom code task.

![](../Resources/Images/evotrust/custom%20code.png)

Click on it and enter the API key you got from DigiTech Consult Ltd.

Save the integration task.

<a id="Step4Uploadyourdocumenttemplateandconfiguretheintegration"></a>

### Step 4. Upload your document template and configure the integration

On the **Solution Contents** menu, click **Documents** and upload the document template that the AI Agent will send to the user in the chat for signing. Use the 'Create new template' feature to upload a new document template.

![](../Resources/Images/evotrust/add%20template%20doc.png)

On the **Solution Contents** menu, click **Integrations**. Click on **Document\_Generator** integration, then click on the integration task.

From the **Document Template Name** field, select your document template.

![](../Resources/Images/evotrust/tempalte%20name.png)

Click **Save & Close**, then click **Save**.

Publish the integrations.

<a id="Step5Additionalconfigurationfornewfieldsinthedocumenttemplate"></a>

### Step 5. Additional configuration for new fields in the document template

If additional fields need to be included in the document template, to ensure seamless integration between the AI Agent data and the document template, allowing the user’s information to populate dynamically during the signing process, follow these steps:

1. Add the desired fields to the **[[User]]** entity. These fields will serve as placeholders for dynamic values in the document template.
2. Add Placeholders in the Contract Signing flow:

- Go to the 'Add Placeholders And Set Parameters' step and under Set Variables, add the new placeholders.
- Ensure each placeholder corresponds to the field you want to display in the document when it is initially shown to the user.

![](../Resources/Images/evotrust/set%20variables.png)

3. Map the additional fields to the corresponding entity fields.

*Example*:

If the AI Agent has an entity field such as [[UserInfo]].Occupation, and you want its value to appear in the document template, in the 'Collect Info From Document' step of the **Contract Signing 2** flow, set the value as a variable: [[User]].Occupation = [[UserInfo]].Occupation

This mapping ensures the data from the AI Agent field ([[UserInfo]].Occupation) is correctly transferred to the corresponding field ([[User]].Occupation) in the document template.
