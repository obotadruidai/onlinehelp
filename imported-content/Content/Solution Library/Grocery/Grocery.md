---
title: "Grocery"
---

<a id="Grocery"></a>


This solution provides conversational flows that will help any company to cross and up sell while inspiring the customers with amazing recipes that will help them save time by proposing just the perfect ingredients they can buy from the online store. The client can easily add or remove products to their shopping list and place the order in one moment. Once the product has been added to the cart, the customer will get a speedy and straightforward checkout.

Grocery is the AI AI Agent, which provides you with a wide range of skills:

| Skill | Description |
| --- | --- |
| Product search | Bring your products closer to the audience! The AI Agent understands the user`s intent and displays a range of product options based on the client’s preferences. |
| Recipes:   - selection of recipes - step-by-step recipe - shopping list based on selected recipe > place the order via the AI Agent | Cross and up sell while inspiring your customers with amazing recipes and help them save time by proposing just the perfect ingredients they can buy from your online store. |
| My shopping list:   - add / remove products to / from the shopping list - place an order based on your shopping list | Allows the client to easy add or remove products to their shopping list and easily place an order. |
| Find a store | Allows the client to check the opening hours / get directions to a specific store. |
| FAQ | No more headaches for your customers / visitors navigating through complex website structures or fuzzy materials to find the right piece of information. The AI Agent will assist them in finding the right answer 24/7. |
| Order again | Once the product has been added to the cart, the customer will get a speedy and straightforward checkout. The customer can also save time by easily placing the exact same order as last time. |

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../2_AI%20Agents/Creating%20AI%20Agents.md).
- SQL server connection.

<a id="ConfiguringSolutionTemplates"></a>

## Configuring Solution Templates

To configure the solution template, follow these steps:

<a id="Step1SetUptheAIAgent"></a>

### Step 1. Set Up the AI Agent

> **NOTE:** Grocery default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Grocery, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.

To configure the AI Agent for Grocery, in Druid Portal:

1. [Set AI Agent special flows](#Step_1%3A_Set_special_flows).
2. [Set the SQL connection strings](#Step_2%3A_Set_the_Connection_Strings_%28Apps%29_Details).
3. [Run Setup Flow](#Step_3%3A_Run_Setup_Flow).

#### <a id="Step_1:_Set_special_flows"></a>1.1. Set special flows

Click the Special Flows section header and select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome | first-welcome-flow-groceries-bot |
| IntentNotFound | Intent-not-recognized |
| Authentication | web-authentication-customer-groceries |

![](../../Resources/Images/grocery/set%20flows.png)

In production, you can configure these flows based on your needs.

#### <a id="Step_2:_Set_the_Connection_Strings_(Apps)_Details"></a>1.2. Set the Connection Strings (Apps) Details

**Prerequisite**

- You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your DB, from Grocery Apps, click **sql-db**. The Edit Connector page appears.

Make the following settings:

| Setting | Description |
| --- | --- |
| ClientType | Select SqlServer. |
| DataSource | Enter the name of the SQL server. |
| InitialCatalog | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account. |

Click **Save and Close**.

> **IMPORTANT!** In order for the AI Agent integration with the apps to be up and running, you need to publish the connector actions. To do so, from the main menu, click **Integrations** and click the **Publish** button.

#### <a id="Step_3:_Run_Setup_Flow"></a>1.3. Run Setup Flow

Open chat land AI Agent page and send the message “setup-groceries-bot”. This command sets up all the DB tables needed in Grocery.

Click **Done**. If the SQL connection strings are properly set, Grocery setup completes successfully.

You can now train the entities and the AI Agent.

<a id="Step2TraintheEntitiesandtheAIAgent"></a>

### Step 2. Train the Entities and the AI Agent

We created Druid for enterprises and unlike other AI Agent platforms; its entities are business objects with attributes and references.

#### Train the Entities

In the AI Agent configuration page, click the **Entities** tab. Train the entities [[Product]], [[SubComponent]] and [[Payment]] by clicking the **Edit Schedule** icon displayed in line with each entity.

![](../../Resources/Images/grocery/train%20entities.png)

In the pop-up that appears, click the **Train** button. After a few seconds, the following train status message should appear in the pop-up:

> **NOTE:**  If the train status message does not appear, you might want to check you have properly configured the corresponding Druid app.

After you successfully train the entities, click **Save** button.

Now you can train the AI Agent.

#### Train the AI Agent

Click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

![](../../Resources/Images/solution%20templates/Cristina/train%20bot.png)

> **NOTE:**  It might take a few minutes for the NLP training to complete, so you might need to wait for Druid to finish training all AI Agent entities that have NLP enabled (NLP=true).

<a id="SeeGroceryinAction"></a>

## See Grocery in Action

The list below provides you with the things you can say to the AI Agent in either English or Romanian to test the different solution skills.

| Skill | English | Romanian |
| --- | --- | --- |
| Product search | - Can you recommend me a chocolate - I am looking for some sugar - I need to buy some flour - Can I find butter in your catalogue? - Do you have any special offers? - What offers do you have in the catalogue? | - Vreau sa cumpar ciocolata - Ce tip de zahar imi pot recomanda - Am nevoie sa cumpar faina - Pot sa gasesc unt in catalogul vostru? - Ce oferte speciale aveti? - Ce oferte aveti in catalog? |
| Recipes | - I want to bake some cookies. do you have any special recipes? - I want to cook something for the weekend, can you recommend me a recipe? - Inspire me with some great recipes | - Vreau sa coc niste prajituri. aveti recomandari de retete? - Vreau sa gatesc ceva in weekend, poti sa imi recomanzi o reteta interesanta? |
| My shopping list | To add a product to shopping list, say "do you have any special offers", choose a product and add it to your shopping list.  To view the shopping list:   - what products do i have on my shopping list? - do i have any product on my shopping list? - please show my shopping list | - Ce produse am pe lista de cumparaturi? - Am produse adaugate pe lista de cumparaturi? - Te rog sa imi arati lista de cumparaturi |
| Find a store | - How can I check the opening hours for a store? - How can I locate a store - Can I get directions to a specific store? | - Cum pot sa verific programului unui magazin? - Cum pot sa localizez un magazin? - Poti sa imi localizezi pe harta un magazin? |
| FAQ | - Can I order from you via uber eats? - Do you deliver via uber eats? - One of your drivers was impolite. can i add a complain? - Want to post a complaint because one of the drivers had an inappropriate behaviour - I have an allergy to gluten - What happens if the courier doesn't find me home - I missed the delivery. What should I do now? - How do I get a refund? | - Pot sa comand de la voi prin uber eats? - Livrati prin uber eats? - Un sofer din echipa voastra a fost nepoliticos. - Pot sa adaug o plangere - Am alergie la gluten - Ce se intampla daca curierul nu ma gaseste acasa cand livreaza comanda? - Cum pot sa primesc rambursarea comenzii? |
| Order again | - Can you show me my last order - I want to order the same products as last time - I want to reuse my last order | - Poti sa imi arati te rog ultima mea comanda? - Vreau sa comand la fel ca data trecuta |
