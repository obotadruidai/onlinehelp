---
title: "eSignature Namirial"
---

<a id="eSignatureNamirial"></a>


eSignature Namirial is a solution that uses Namirial technology to provide your AI Agent with electronic signature capabilities. Use it if you want to showcase Druid-Namirial integration.

The solution template contains:

- Namirial setup for two signers. The type of signature is Click2Sign with authentication via PIN Code.
- Sample conversation available in EN-US to collect data for the first and second signer (first name, last name, email address).
- Sample document template to be signed. If you want to use another document template, you should generate it from your Namirial organisation.
- eSignAnywhere.Api V5 and full management of namirial-Druid integration services like: upload file to Namirial, generate file, get signature url, get envelope status or download documents.

<a id="WhychoosingeSignatureNamirial"></a>

## Why choosing eSignature Namirial?

By integrating with eSign, the electronic signature of a digital document can be done through any AI Agent, in any scenario, such as: at the point of sale, at the point of service, mobile sales, customer onboarding, KYC, contract management, remote signing (employees working remotely or working from home), or internal document signing.

The AI Agent will automatically apply to any document the electronic signature type specific to the internal flow, role and user rights (standard, advanced or qualified electronic signature). The digital documents are archived electronically, carrying advanced timestamps, in full compliance with Romanian, European and international laws.

You can read more about Namirial services [here](https://www.namirial.com/en/trust-services/).

<a id="HowtosetupeSignatureStarter"></a>

## How to set up eSignature Starter

**Prerequisites**:

- You need to have an [eSign](https://www.esignanywhere.net/) subscription with Namirial (either demo or production account).
- In Namirial Digital Transaction Management Platform, go to **Settings** > **Api Tokens and Apps** and generate a new ApiToken.

![](../Resources/Images/solution%20templates/esign%20namirial.png)

Copy this API token, you will need it in Druid to authenticate the requests.

- In order to use the Namirial eSignature, you need a DruidNamirialToken generated for your tenant. To get one, contact [Druid Tech Support](<mailto:support@druidai.com?subject=I need a DruidNamirialToken>).
  After Druid Tech Support confirms that a DruidNamirialToken was generated, you can see the token in the Druid Portal. From the main menu, click **Administration** > **Druid Services**.
  Copy the token as you will need it during the connector setup.

![](../Resources/Images/solution%20templates/namirial%20token.png)

To set up the REST connector used for electronic signature of documents:

1. From solution Apps, click **Namirial eSignature**. The Edit Connector page appears.
2. Depending on your Namirial setup, in the **URL** field, enter *https://saas.esignanywhere.net* for production environment or *https://demo.esignanywhere.net/Api* for demo environment.
3. From the **SecurityType** drop-down, select **Custom**.
4. From the **AuthorizeRequestConnectorAction** field, select **namirial-authorize**.
5. From the **CheckNotAuthenticatedConnectorAction** field, select **namirial-check-not-authenticated**.
6. In the Variables section, add the following:

- the **API token** you generated in Namirial.
- the **DruidNamirialToken** you copied from the **Administration** menu> **Druid Services**.
- the **StatusUpdateCallbackUrl**. When sending the file for signing (REST call), use the URL specific to the DRUID Cloud you're using:

- Druid Cloud Community: https://druidendpoints.comm.eu.druidplatform.com/api/Namirial/StartFlow
- Druid Cloud Australia: https://druidendpoints.au.druidplatform.com/api/Namirial/StartFlow
- Druid Cloud West-Europe: https://druidendpoints.druidplatform.com/api/Namirial/StartFlow

![](../Resources/Images/solution%20templates/esign%20setup.png)

7. Click **Save and Close**.

After you finish the setup, you need to train the AI Agent.

<a id="TraintheAIAgent"></a>

## Train the AI Agent

In the AI Agent configuration page, click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

![](../Resources/Images/solution%20templates/Cristina/train%20bot.png)

> **NOTE:**  It might take a few minutes for the NLP training to complete, so you might need to wait for Druid to finish training all AI Agent entities that have NLP enabled (NLP=true).

When **StatusUpdateCallbackURL** is filled in, via the Druid internal action **SaveNamirialCallBackContext** the information regarding the envelope signing is sent back to Druid via the status url and the appropriate flow is triggered.

If you want to change your status response flow, you can go to the flow **send-document-for-esignature**, and on the last step, **save-namirial-callback-context**, edit **[[NamirialEnvelope]].CallbackUtterance**.

Right now with the solution template, the call back is responding on the **eSignature-get-envelope-status** flow.

![](../Resources/Images/solution%20templates/namirial%20call%20back%20response%20utterance.png)

If you want to use the eSignature Namirial integration in anonymous conversations, go to the flow **send-document-for-esignature**, and on the last step, **save-namirial-callback-context**, set the **[[NamirialEnvelope]].TargetMasterUserId** to null.

> **IMPORTANT!** This feature is available for Druid version 1.47 or above.

![](../Resources/Images/Druid%201.47/namirial.png)

You can start chatting with the AI Agent by saying things like "send documents to sign" or " get signature".
