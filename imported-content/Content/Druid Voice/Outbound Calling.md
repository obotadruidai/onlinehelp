---
title: Outbound Calling
---

# Outbound Calling

Outbound calling enables AI Agents to proactively contact users by phone to deliver information, collect responses, or automate business processes such as appointment reminders, payment notifications, surveys, or outreach campaigns.

Unlike traditional contact center platforms, Druid does not initiate outbound telephone calls directly. Instead, Druid integrates with external telephony or contact center platforms that are responsible for placing the call.

### How outbound calling works

In a typical deployment, an external telephony platform or contact center manages the outbound campaign and initiates the telephone call.

After the called party answers, the telephony platform establishes a SIP connection with Druid. From that point onward, the AI Agent manages the conversation, understands user input, executes business logic, accesses enterprise systems, and generates responses.

The overall call flow is illustrated below:

![](<../../.gitbook/assets/outbound calling.png>)

### Supported deployment model

Druid supports outbound voice scenarios when integrated with a SIP-compatible telephony platform or contact center solution capable of initiating outbound calls.

Common examples include:

* RingCentral
* Genesys Cloud
* Cisco Contact Center
* Amazon Connect
* Other SIP-enabled contact center or outbound dialing platforms

The exact integration depends on the telephony platform used in your deployment.

{% hint style="warning" %}
**IMPORTANT!** Druid does not function as an outbound dialer and cannot independently place telephone calls to users. An external telephony platform must first establish the telephone call. Druid joins the interaction only after the recipient answers and the SIP session is established.
{% endhint %}

### Typical use cases

Outbound calling with Druid is commonly used for:

* Appointment reminders and confirmations
* Patient engagement campaigns
* Student engagement campaigns
* Payment reminders
* Customer satisfaction surveys
* Service notifications
* Proactive customer outreach
* Follow-up calls after business events
