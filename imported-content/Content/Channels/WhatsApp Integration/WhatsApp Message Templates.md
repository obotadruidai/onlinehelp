---
title: "WhatsApp Message Templates"
---

<a id="WhatsAppMessageTemplates"></a>


{% hint style="warning" %}
**IMPORTANT!** If a customer messages the AI Agent via the WhatsApp channel, the AI Agent has 24 hours to respond to the customer with a free-form message. After this period, the message sent by the AI Agent has to be a template type message.
{% endhint %}

**Prerequisites**:

- AI Agent should be [integrated with WhatsApp](WhatsApp%20Integration.md).
- In order to use WhatsApp message templates, you need a Facebook Developer account. You get one when you subscribe for a WhatsApp business account.
- A nexmo-whatsapp channel must already exist in the Druid AI Platform for that user. This means that a free-form message conversation must have existed at least once for that user.

<a id="DefineWhatsAppMessageTemplates"></a>

## Define WhatsApp Message Templates

Log in Facebook for developers using the account associated to your WhatsApp account and define the message templates.

If someone within your organization have already defined them, then you can start using them in Druid.

The table below provides some message template examples.

| Namespace | Name | Language | Message Template |
| --- | --- | --- | --- |
| 9b6b4fcb\_da19\_4a26\_8fe8\_78074a91b584 | sandbox\_doctors\_appointment | en\_US,  en\_GB | **Header**: APPOINTMENT CONFIRMATION  **Body**: Your appointment with Doctor {{1}} is now confirmed for the {{2}} at {{3}} and the {{4}}.Footer: none |
| 9b6b4fcb\_da19\_4a26\_8fe8\_78074a91b584 | sandbox\_shipping\_update | en\_US,  en\_GB | **Header**: Shipping Update  **Body**:Your parcel from {{1}} is due to arrive on {{2}} between {{3}} and {{4}}. Not going to be in? You can either change the date of your delivery or instruct us to leave your parcel in your designated safe place. Footer:none |
| 9b6b4fcb\_da19\_4a26\_8fe8\_78074a91b584 | verify | en-US, en-GB, ko, ja, it | **Header**: none  **Body**: {{1}} code: {{2}}. Valid for {{3}} minutes. Footer: none |

The Namespace and Name are unique identifiers for the WhatsApp message templates.

{% hint style="info" %}
**NOTE:** Only templates created in your own namespace will work. Using a template with a namespace outside of your own will return an error.
{% endhint %}

For information on how to create WhatsApp message templates, see [Facebook Developer Documentation](https://developers.facebook.com/docs/whatsapp/message-templates/creation).
