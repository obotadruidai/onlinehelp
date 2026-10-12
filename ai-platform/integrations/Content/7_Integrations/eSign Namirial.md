---
title: eSign Namirial
---


You can use [Namirial technology](https://www.namirial.com/en/trust-services/) to provide your AI Agents with electronic signature capabilities, enabling users to apply electronic signatures on documents through AI Agents, in both office and work-from-home environments.

By integrating with eSign, the electronic signature of a digital document can be done through any AI Agent, in any scenario, such as: at the point of sale, at the point of service, mobile sales, customer onboarding, KYC, contract management, remote signing (employees working remotely or working from home), or internal document signing.

The AI Agent will automatically apply to any document the electronic signature type specific to the internal flow, role and user rights (standard, advanced or qualified electronic signature). The digital documents are archived electronically, carrying advanced timestamps, in full compliance with Romanian, European and international laws.

To provide your AI Agent with electronic signature capabilities, you need to set up a REST connector, which you will use for electronic signature of documents.

The figure below provides an overview on how you can use the eSign Namirial integration.

![](<../../.gitbook/assets/eSign Namirial.png>)

## Prerequisites

* You need to have an [eSign](https://www.esignanywhere.net/) subscription with Namirial (either demo or production account).
* In Namirial Digital Transaction Management Platform, go to **Settings > Api Tokens and Apps** and generate a new ApiToken.

![](<../../.gitbook/assets/eSign Namirial_1.png>)

Copy this **API token**, you will need it in Druid to authenticate the requests.

* In order to use the Namirial eSignature, you need a DruidNamirialToken generated for your tenant. To get one, contact [Druid Tech Support](mailto:support@druidai.com?subject=I%20need%20a%20DruidNamirialToken). After Druid Tech Support confirms that a DruidNamirialToken was generated, you can see the token in the Druid Portal. From the main menu, click **Administration > Druid Services**. Copy the token as you will need it during the connector setup.

![](<../../.gitbook/assets/eSign Namirial_2.png>)

## Step 1. Set the REST connection strings

Create connection strings following the generic procedure with the following particularities:

1. Depending on your Namirial setup, in the URL field, enter https://saas.esignanywhere.net for production environment or https://demo.esignanywhere.net/Api for demo environment.
2. In the Variables section, add the following:

* the **API token** you generated in Namirial.
* the **DruidNamirialToken**. Copy it from the **Administration** menu> **Druid Services**.
* the **StatusUpdateCallbackUrl**. When sending the file for signing (REST call), use the URL specific to the Druid Cloud you're using:
* Druid Cloud Community: https://comm-Druid-endpoints.azurewebsites.net/api/Namirial/StartFlow
* Druid Cloud Australia: https://prod-au-Druid-endpoints.azurewebsites.net/api/Namirial/StartFlow
* Druid Cloud West-Europe: https://prod-Druid-endpoints.azurewebsites.net/api/Namirial/StartFlow

## Step 2. Add integration task to send document for signature

Make a POST request to **/v5/envelope/send**.

From the **RequestType** field, select **UseBodyTemplate**.

In the **Body** field, enter your request. This section provides useful information for making the request to send document for e-signature.

In the eSign Namirial integration, Druid supports three callback types:

* **Envelope callback** - The basic callback (“CallbackUrl”: “\{{DruidBaseURL\}}?Token=\{{DruidToken\}}\&envelope=##EnvelopeId##”), which is fired if the envelope reaches a final state (completed, rejected).
* **Envelope status callback** - Envelopes status callbacks (“StatusUpdateCallbackUrl”: “\{{DruidBaseURL\}}?Token=\{{DruidToken\}}\&envelope=##EnvelopeId##\&action=##Action##”,) are fired, based on envelope events/actions:
* workstepFinished: when the workstep was finished
* workstepRejected: when the workstep was rejected
* workstepDelegated: when the workstep was delegated
* workstepOpened: when the workstep was opened
* sendSignNotification: when the sign notification was sent
* envelopeExpired: when the envelope was expired
* workstepDelegatedSenderActionRequired: when an action from the sender is required because of the delegation.
* **Workstep Event callback** - specific event callbacks ("StatusUpdateCallbackUrl": “\{{DruidBaseURL\}}?Token=\{{DruidToken\}}\&envelope=##EnvelopeId##\&event=##EventType##”) fired on events caused by the underlying "SIGNificant Server Platform" component, but also routed through the notification system of eSignAnyWhere. These callbacks inform in a more detailed way about the workstep events - but note that those events are not necessarily time-synced to the envelope events. To trigger activities on the eSignAnyWhere API, always consider the envelope or envelope status callbacks.

{% hint style="info" %}
**NOTE:** This callback type is available in Druid 1.67 and higher.
{% endhint %}

Based on the type of callback you want to make, in the request body, provide the URL for the appropriate callback type in the following format:

```
“CallbackUrl”: “{{DruidBaseURL}}?Token={{DruidToken}}&envelope=##EnvelopeId##”,
“StatusUpdateCallbackUrl”: “{{DruidBaseURL}}?Token={{DruidToken}}&envelope=##EnvelopeId##&action=##Action##”
"WorkstepEventCallback": { "Url": “{{DruidBaseURL}}?Token={{DruidToken}}&envelope=##EnvelopeId##recipientEmail=##RecipientEmail##&recipientOrder=##RecipientOrder##",
	"WhiteList":
		["string"]
	},
```

{% hint style="warning" %}
**IMPORTANT!** Make sure that the callback URLs have a length of maximum 500 characters to comply with Namirial URL length restriction.
{% endhint %}

You can use additional information provided by the Workstep event callback in the main conversation or start a secondary conversation, as best suits your needs.

Use cases for triggering a secondary conversation:

* Another user (service account, usually) will update the same envelope ID information (returned by the callback) in a database or in a third-party system, without interfering with the main conversation.
* You want to inform a manager that the user has signed off a document, without interfering with the main conversation.

Click the **Body** tab and map DruidBaseURL and DruidToken to Druid local variables @DruidBaseURL and @DruidToken (which have been set on the app).

Save the integration task. Call it on the desired step of the flow where you send the document for signature.

## Step 3. Save Namirial callback context

On the flow you created to send the document for signature, add as last step a step of type action on which you set the following variables:

* \[\[NamirialEnvelope]].EnvelopeId = \[\[eSignature]].EnvelopeId
* \[\[NamirialEnvelope]].TargetUserMasterId = \[\[ChatUser]].MasterId
* \[\[NamirialEnvelope]].CallbackUtterance = \<the utterance of the flow you want to be trigger at callback, assuming you created that flow>

![](<../../.gitbook/assets/eSign Namirial_3.png>)

For Druid 1.67 or higher, if you want to trigger a second conversation to process information returned by the Workstep event callback, use secondary parameters available in the \[\[NamirialEnvelope]] system entity. For more information on the available entity fields, see [System Entities](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/ai-agent-informational-model/system-entities).

In order for the callback to initiate a secondary conversation, you need to add the parameter “**secondary=true**” to the corresponding callback URL (to any of the 3 URLs which can be specified in the request: Callback URL, Status Callback URL or Workstep event callback URL).

For example: “\{{DruidBaseURL\}}?Token=\{{DruidToken\}}\&envelope=##EnvelopeId##recipientEmail=##RecipientEmail##\&recipientOrder=##RecipientOrder##&**secondary=true**".

Additionally, all following metadata sent by Namirial callback can now pe mapped to Druid conversation context:

* workstepId=##WorkstepId## – workstep of current action
* eventType=##EventType## – type of event (see list of types below)
* source=##Source## – internal (eSAW)  or external (Viewer)
* time=##Time## – time when the action occurred
* description=##Description## – textual description of the event
* recipientEmail=##RecipientEmail## – emailadress of current recipient
* recipientOrder=##RecipientOrder## – index of current recipient

{% hint style="info" %}
**NOTE:** Make sure to type the name of the parameter with first character in lower case, as they are described above.
{% endhint %}

In order to shorten the length of the URL when sending multiple callback parameters, you can replace the **Token** parameter with a much shorter authentication key : “secret”.

For example: “\{{DruidBaseURL\}}?secret=\{{DruidTenantSecret\}}\&envelope=##EnvelopeId##recipientEmail=##RecipientEmail##\&recipientOrder=##RecipientOrder##\&secondary=true"

The value for Druid Tenant Secret can be found in Druid Portal -> Administration / Druid Services:

![Graphical user interface, application Description automatically generated](<../../.gitbook/assets/eSign Namirial_4.png>)

On this last step, in the Post actions section, call Druid Internal action **SaveNamirialCallbackContext**.

## eSignature Namirial Solution Template

To simplify the AI Agent authoring experience, go to Solutions Library and import the eSignature Namirial solution template. It contains:

* Namirial setup for two signers. The type of signature is Click2Sign with authentication via PIN Code.
* Sample conversation available in EN-US to collect data for the first and second signer (first name, last name, email address).
* Sample document template to be signed. If you want to use another document template, you should generate it from your Namirial organization.
* eSignAnywhere.Api V5 and full management of namirial-Druid integration services like: upload file to Namirial, generate file, get signature url, get envelope status or download documents.

For information on how to configure the solution template, see [eSignature Namirial solution template](https://druidai.gitbook.io/druid-ai-docs/solution-library/solution-templates/esignature_namirial).
