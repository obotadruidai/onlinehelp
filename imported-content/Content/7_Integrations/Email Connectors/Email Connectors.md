---
title: "Email Connectors"
---

<a id="EmailConnectors"></a>


Druid allows authors to integrate AI Agents with SMTP and Twilio SendGrid service, enabling the AI Agents to send emails.

![](../../Resources/Images/Email%20Connectors/Email%20Connectors.png)

Email connectors always send emails from the system entity [[Email]]. This entity has the following fields:

| Field | Type | Description |
| --- | --- | --- |
| [[Email]].To | String | The main recipient(s) of the email. |
| [[Email]].From | String | The email address from which emails are sent. While for SendGrid, it can be any email address, for SMTP, it is the email address reserved by your system administrator for the AI Agent.  According to RFC.5321 is the email address to which bounce messages are delivered. |
| [[Email]].Subject | String | A short description about the objective or primary topic of the email. It is the first text recipients see after the sender name when an email reaches their inbox. |
| [[Email]].Body | String | The email content. If you want to include HTML in the email body, you can do so by escaping the double quotation mark (“”) and replacing it with backslash (\). For an example, see [Email Body](Email%20Body.md#_Email_Body). |

To include email attachments, you need to create as many fields of type File as attachments you want to send in your email. The [[Email]] entity supports up to 10 fields of type File.

![](../../Resources/Images/Email%20Connectors/Email%20Connectors_1.png)
