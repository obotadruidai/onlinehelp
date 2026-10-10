---
title: Sending Email Links in the Chat
---

# Sending Email Links in the Chat

Email links are used for linking directly to an email address, which will automatically launch an email browser (or the user’s default email client) when the link is clicked.

Sending email hyperlinks in the chat are useful when you want to enable the users chatting with you AI Agent click a link the chat to send an email to a specific email address and with a specific subject.

This section provides you with the necessary steps to send an email link in the chat so that Druid automatically populates the email address and the email subject when the user clicks on the email link.

### Configure the email link on the flow step

On the desired flow step, General section, in the **Step message** field provide the desired text message and make sure that you enter the email link using markdown markup:

\[text]\(mailto:\[email address]?subject=\[email subject])

![](<../../.gitbook/assets/Sending Email Links in the.png>)

If you want to display an email address as the link text, remember that you have to use markdown markup:

\[email@company\&#64com]\(mailto:\[email address]?subject=\[email subject])

![](<../../.gitbook/assets/Sending Email Links in the_1.png>)

You can also get the email address and email subject from Druid variables. This is particularly useful when you want the client to send the email to multiple email addresses. To do so, in the Step message field provide the email link using the following format:

[email@company\&#64com](mailto:@email?subject=@subject)

![](<../../.gitbook/assets/Sending Email Links in the_2.png>)

In the Set variable, section enter the Druid variables where you store the two email and subject.

If you want the client to send the email to multiple recipients when clicking on the email link, set the value you used in the email link definition for the recipients in the following format: “email address 1;email address 2”. For example: “support@Druidai.com;admin@Druidai.com”

![](<../../.gitbook/assets/Sending Email Links in the_3.png>)

### How it works

The AI Agent sends the email link.

![](<../../.gitbook/assets/Sending Email Links in the_4.png>)

When the user clicks on the link in the chat, the user’s default email client is launched, on new email message. The To field and subject are automatically filled in with the values set by the AI Agent author when proving the email link in the Step message.

![](<../../.gitbook/assets/Sending Email Links in the_5.png>)
