---
layout:
  title:
    visible: false
---

<a id="TravelManagement"></a>

# Travel Management

Booking a travel can be a complex process when there are tens of options for flights, hundreds of available accommodations and many other criteria that you have to consider when deciding to book a trip in a certain destination. This solution comes with conversational flows that will assist the user in finding the perfect holiday destination, while saving them time and money. The AI Agent will act as a personal travel assistant, helping the user to get a travel quote, to complete the reservation or to receive travel tips for specific destinations.

<a id="SolutionSkills"></a>

## Solution Skills

This solution template provides a wide range of skills for customers:

| Skill | Description |
| --- | --- |
| Special offers & Complete the reservation | The users can type in requests about their destination and travel dates, giving the AI Agent criteria to browse options and to provide different travel offers.  When the users have decided upon a travel plan, the AI Agent can inquire about user information, asking them to provide an Identity Card. Druid OCR will be performed on the ID photo, the travel documents will be generated automatically and it can be electronically signed. The AI Agent also provides a channel to complete payments via credit cards, finalizes the reservations, and sends the booking confirmation via e-mail. |
| Travel tips | The AI Agent will recommend restaurants, shopping areas or places that could be visited during the trip in a specific destination. Also, it will generate cross-selling opportunities by providing coupons for restaurants or cafes which the travel agency has deals with. |
| My bookings | At any time, the client will have access to the “My Bookings” section, where he can view detailed related to the coming reservations. |
| FAQ | The travel solution comes with workflows that will assist the user in finding the right answer, 24/7, to questions related to travel conditions for different destinations, travel requirements, contact details for Embassies and many more. Now, more than ever, timely and correct responses are especially relevant because during the COVID-19 outbreak the travel guidelines between the countries can change daily and the user has to be informed. |

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../../2_AI%20Agents/Creating%20AI%20Agents.md).
- SQL server connection
- Namirial subscription (not mandatory, only if you want the travel documents to be electronically signed).
- SendGrid Subscription (not mandatory, only if you want to send the booking confirmation by email).
