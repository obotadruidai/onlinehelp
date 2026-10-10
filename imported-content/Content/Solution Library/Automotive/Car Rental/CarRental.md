---
layout:
  title:
    visible: false
---

<a id="CarRental"></a>

# Car Rental

This solution template provides a wide range of skills for prospects and clients:

| Skill | Description |
| --- | --- |
| Car search | People have lots of questions when renting a vehicle, but finding the perfect car can be an easy process if you have a concierge to assist you during the process. Even if we are talking about a small car or a 4X4 SUV, a car with manual transmission or with an automatic one, the AI Agent is trained with all the information related to these vehicles and it will help the customer to choose just the car he needs. |
| Rent a car- Booking Section | Once the car was selected, the AI Agent will guide the customer through the booking process. At the end of the process, the client will receive the booking confirmation via e-mail. |
| - My bookings - Cancel a booking - Generate invoice | At any time, the client will have access to the “My Booking” section, where he can view detailed related to the coming reservation, cancel a reservation or generate an invoice. |
| FAQ | Waiting on hold to get an answer or navigating through complex website structures or fuzzy materials to find the right piece of information is not making a good customer experience for anybody. The car rental solution comes with workflows that will assist the customer in finding the right answer, 24/7, to questions related to prices, rental conditions, payments and many more. |

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../../2_AI%20Agents/Creating%20AI%20Agents.md).
- SQL server connection.

<a id="Downloadsolution"></a>

## Download solution

In the Druid Portal, go to the Solution Library and from the "Automotive" category, download the **Car Rental** solution.

<a id="Configuringthesolutiontemplate"></a>

## Configuring the solution template

1. [Set up the AI Agent](#Step_1._Set_Up_the_Bot).
2. [Train the entities and the AI Agent](#Step_2._Train_the_Entities_and_the_Bot).

<a id="Step1SetUptheAIAgent"></a>

### <a id="Step_1._Set_Up_the_Bot"></a>Step 1. Set Up the AI Agent

In Druid Portal:

##### 1.1. Configure the AI Agent

> **NOTE:** Car Rental default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Healthcare, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.

To configure the AI Agent for Car Rental, you need to set special flows and configure the connection strings.

###### Set special flows

Click the Special Flows section header and select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome | welcome-flow-car-rental |
| IntentNotFound | Intent-not-recognized |

![](../../../Resources/Images/Automotive/car%20rental%20special%20flows.png)

In production, you can configure these flows based on your needs.

##### 1.2. Set the Connection Strings (App) Details

> **NOTE:** To run the Car Rental setup flow, you need to set up the SQL app.

###### Prerequisite

- You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your DB, from Car Rental Apps, click **Cars Data Base**. The Edit Connector page appears.

Set up the credentials for your SQL database connection:

| Setting | Description |
| --- | --- |
| ClientType | Select SqlServer. |
| DataSource | Enter the name of the SQL server. |
| InitialCatalog | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account. |

Click **Save and Close**.

##### 1.3. Run Setup Flow

Open chat land AI Agent page and send the message “setup-bot”. This command sets up all the DB tables needed in Car Rental.

Click **Done**. If the SQL connection strings are properly set, the Healthcare setup completes successfully.

You can now train the entities and the AI Agent.

<a id="Step2TraintheEntitiesandtheAIAgent"></a>

### <a id="Step_2._Train_the_Entities_and_the_Bot"></a>Step 2. Train the Entities and the AI Agent

##### Train the Entities

In the AI Agent configuration page, click the **Entities** tab. Train the entity "BrandSubcomponent" by clicking the **Edit Schedule** icon displayed in line with each entity.

![](../../../Resources/Images/Automotive/train%20entity.png)

In the pop-up that appears, click the **Train** button.

After a few seconds, the Status **Trained** should appear in the pop-up:

> **NOTE:**  If the train status message does not appear, you might want to check you have properly configured the corresponding Druid app.

After you successfully train the entities, click **Save** button.

Now you can train the AI Agent.

##### Train the AI Agent

Click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

![](../../../Resources/Images/solution%20templates/Cristina/train%20bot.png)

> **NOTE:**  It might take a few minutes for the NLP training to complete, so you might need to wait for Druid to finish training all AI Agent entities that have NLP enabled (NLP=true).

<a id="SeeCarRentalinAction"></a>

## See Car Rental in Action

> **NOTE:** The AI Agent is trained in two languages: RO and EN. If you want to switch between languages, just type the following commends in the chat:
>
> - “Romana te rog” if you want to switch from EN to RO.
> - “English please” if you want to switch from RO to EN.

The list below provides you with an extensive list of things you can say to the AI Agent in either English or Romanian.

|  |  |  |
| --- | --- | --- |
| Feature | Intents |  |
|  | English (EN) | Romanian (RO) |
| Car search  Rent a car- Booking Section | I am traveling next week and I need to rent a car How can I book a car?  I need to rent a car  Can you help me to rent a car?  Do you have available <car brand> cars for renting?  I am looking for a <car brand>  **NOTE:**  The AI Agent is trained with the following car brands: Skoda, Dacia, Renault, Fiat, Volkswagen | Calatoresc saptamana viitoare si am nevoie sa inchiriez o masina Cum pot sa rezerv o masina?  Vreau sa inchiriez o masina  Ma poti ajuta sa inchiriez o masina?  Ajuta-ma sa gasesc o masina <car brand> disponibila pentru inchiriere  Caut sa inchiriez o <car brand>  **NOTE:**  Chatbotul este antrenat cu urmatoarele brand-uri de masini: Skoda, Dacia, Renault, Fiat, Volkswagen |
| My Bookings | I want to see my coming reservations  When is my next booking? | Ce rezervari am?  Cand este urmatoarea mea rezervare? |
| Cancel a reservation | How can I cancel a reservation?  My flight was canceled. How can I cancel my car reservation?  Please help me to cancel a booking | Cum pot sa anulez o rezervare?  Zborul meu a fost anulat. Cum pot anula rezervarea masinii?  Te rog ajuta-ma sa anulez o rezervare |
| Generate invoice | I made the payment for my car reservation but I did not receive the bill | Am facut plata pentru rezervarea masinii, dar nu am primit factura |
| FAQ | Will I need my passport to pick up a car?  What is the maximum period of rental?  Can I rent a car if I do not have a credit card?  Do I get a refund if I return my car early?  What is Theft Protection (TP)?  What happens if I get a speeding ticket or other fines during my rental period? | Am nevoie de pasaport cand vin sa preiau masina?  Care este perioada maxima pentru care pot inchiria o masina?  Pot inchiria o masina daca nu am un card de credit?  O sa imi rambursati diferenta de bani daca returnez masina mai devreme?  Ce este protectia impotriva furtului (TP)?  Ce se intampla daca iau o amenda de viteza in timp ce merg cu masina inchiriata? |
