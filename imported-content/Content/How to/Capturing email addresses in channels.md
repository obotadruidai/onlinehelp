---
layout:
  title:
    visible: false
---

<a id="CapturingEmailAddresses"></a>

# Capturing Email Addresses

An email address identifies an email mailbox to which messages are delivered. An email address is comprised of local-part, the symbol @ and a domain. The classic validation rules on the email address format and transmission as per RFC 5322 and RFC 6854 are restrictive.

In conversational flows, email addresses are conversational input and users might use additional characters and words when providing their email address. E.g., “my email is: john.doe@domain”.

Although you can manage this through Input Mapping Training Phrases, DRUID might still capture accidental words / characters alongside the actual email address.

Applying the classic rules for email validation might prevent DRUID from extracting email addresses from user input.

> **IMPORTANT!** DRUID applies less restrictive validation rules on email format, which might lead to capturing non-existent / broken emails. To ensure that the email format complies with the email format supported by your organization, we recommend you do an extra JavaScript validation in the flow(s) to apply your specific format rules by including a regular expression (regex) on a step after the one that captures user email.

<a id="DRUIDvalidationrulesforemails"></a>

## DRUID validation rules for emails

- Email address can contain upper case for domain (both domain name and extension (e.g., john.doe@Domain.Ext).
- The local-part of the email address can be unquoted and might use any of these ASCII characters:

- uppercase and lowercase Latin letters **A** to **Z** and **a** to **z**
- digits **0** to **9**
- printable character: grave accent **`**
- dot **.**, if it is not the first or last character and if it does not appear consecutively (e.g., John..Doe@example.com).

- The maximum total length of the local-part of an email address is 64 octets.

> **NOTE:**  These email validation rules apply in DRUID version 5.8 and higher.
