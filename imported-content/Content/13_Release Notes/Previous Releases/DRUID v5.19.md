---
title: "DRUID 5.19"
---

<a id="DRUID519"></a>


Deployment Dates

The table below lists the deployment date of DRUID v5.19 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| July 20, 2023 | August 03, 2023 | August 03, 2023 | August 03, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Provisioning Portal Users with Active Directory via LDAP**. By using LDAP authentication on your DRUID tenant you ensure that all your Active Directory (AD) users logging into the Druid Portal with their AD account credentials (Windows credentials) are automatically provisioned in DRUID at their first login and are being granted with the default security roles.

![](../../Resources/Images/LDAP/DIAGRAM.png)

For more information, see [Provisioning Portal Users with Active Directory via LDAP](../../Governance%20%26%20Security/User%20Management/Provisioning%20Portal%20Users%20with%20LDAP.md).

- **Custom Code task - added support for request body /data encryption / decryption using the AES256CBC algorithm**. Using the Custom Code integration task, you can do pre-request or post-request scripts in a DRUID integration. You can use the Custom Code task to encrypt or decrypt (AES Encrypt / AES Decrypt) elements sent or received through REST integration tasks.  For more information about the integration, see [Custom Code](../../7_Integrations/Custom%20Code.md).
- **Multi-language context menu**. When the user changes the language in the chat, the **Context menu** options display in the selected language.

![](../../Resources/Images/druid%205.19/context%20menu.png)

<a id="Improvements"></a>

## Improvements

- **Knowledge Base Settings**. With this release, the Knowledge Base settings are centralized in a single page, which is accessible by clicking the **Settings** button on the Knowledge Base page.

![](../../Resources/Images/KB/kb%20settings%20button.png)

![](../../Resources/Images/druid%205.19/kb%20settings.png)

- **Flow Diagram default view for flows**. When viewing a flow, it appears by default in the Flow Diagram view.

![](../../Resources/Images/druid%205.19/flow%20diagramview.png)

- **Knowledge Base - invalid URL error**. Trying to add an unstructured data source from an invalid URL raises an error message.

![](../../Resources/Images/druid%205.19/invalid%20url.png)

- **Limit intent switch details**. The flows to be executed on intent switch (if any selected) are shown on the flow step in the Flow Diagram.

![](../../Resources/Images/druid%205.19/intent%20switch.png)

- New default value for three NLP parameters, as follows:

- NLU.NER.CrfAlgorithmImplementation: Crf++V2
- NLU.NER.CrfFlowStepInputMappingAlgorithmImplementation: Crf++V2
> **NOTE:** If you are already using the two parameters mentioned above, we recommend you to set their value to Crf++V2 for higher performance and train the AI Agent.

- NLU.NER.IndexBasedEntityExtractorV2: true.

<a id="BugFixes"></a>

## Bug Fixes

- LiveChat. Agent who inherited working hours from the queue (Inherit Queue hours) can now connect to clients.
- Decryption issue in CNN audit log. Encrypted data can now be seen in the connector audit log if the data was marked as being sensitive and only the **Encrypt In Conversation History** was enabled.
- Evaluation Tool – Train Set. Utterances with entities that have sample values are now displayed in the Train Set list.
