---
layout:
  title:
    visible: false
---

<a id="KYCPersona"></a>

# KYC Persona

The KYC Persona solution template enables your AI Agent to onboard customers by performing OCR of Romanian Identity Cards.

<a id="Howtosetupthesolution"></a>

## How to set up the solution

<a id="Step1GetToken"></a>

### Step 1. Get Token

The Druid API engine performs OCR and data extraction from Romanian Identity Cards. Get in touch with Contact [Druid Tech Support](mailto:support@druidai.com?subject=Request:%20Activate%20Druid%20Vision%20service%20IdentityCard) and provide your tenant information to receive the authorization token used in the OCR identity card process.

After Druid Tech Support confirms that Druid Vision is active on your tenant, you can see the endpoints and the token in the Druid Portal. To do so, from the main menu, click **Administration** > **Druid Services**.

Copy the endpoint URL by clicking the copy button (![](../../Resources/Images/KYC/KYC%20Persona.png)) in line with the desired endpoint and the generated token.

![](../../Resources/Images/KYC/KYC%20Persona_1.png)

<a id="Step2Configuretheintegrationapp"></a>

### Step 2. Configure the integration app

1. Go to Apps, search for the app with the name “OCR Identity Card” and click the edit icon.
2. From the **Security Type** drop-down, select **Custom**.
3. In the **Base URL**, enter the endpoint URL you copied from Druid Services.
4. From the **AuthorizeRequestConnectorAction** drop-down, select **Auth-OCR-ID-RO**.

![](../../Resources/Images/KYC/KYC%20Persona_2.png)

5. In the Variables table, add the token variable and in the **Value** column, paste the token you copied from Druid Services, then click the **Save** icon displayed inline.

![](../../Resources/Images/KYC/KYC%20Persona_3.png)

6. Save the app.

<a id="SeeKYCPersonainaction"></a>

## See KYC Persona in action

The table below provides you with things to say to the AI Agent to see the solution in action.

| English | Romanian |
| --- | --- |
| I want to start the kyc process | Vreau sa incep procesul kyc |
| Start KYC | Start KYC |

![](../../Resources/Images/KYC/KYC%20Persona_4.png)

![](../../Resources/Images/KYC/KYC%20Persona_5.png)

![](../../Resources/Images/KYC/KYC%20Persona_6.png)

![](../../Resources/Images/KYC/KYC%20Persona_7.png)

![](../../Resources/Images/KYC/KYC%20Persona_8.png)
