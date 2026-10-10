---
title: "Loan Origination Workflow"
---

<a id="LoanOriginationWorkflow"></a>


Druid integrates with UiPath robots, UiPath AI Center, UiPath Data Service, UiPath Action Center and UiPath Automation Hub to provide you with a completely automated Loan Origination workflow.

*Figure*: Loan Origination Workflow

![](../../../Resources/Images/solution%20templates/Victor/Loan%20Origination%20workflow.png)

UiPath AI Center ensures that the files uploaded by the user in chat are processed by Document Understanding and the extracted information is used in the conversational context. For example, the AI Agent might ask the customers to upload the latest utilities bill and their identity card to check their address. Druid also uses AI Center to process document understanding (ID cards scan).

Druid supplies specialized models for AI Center. For instance, the ML model that does not require re-training and recognizes any ID document that complies with the MRZ standard.

Druid saves the conversation context in UiPath Data Service. It also reads information from Data Service and presents it in conversations to the chat users.

By integrating with the following types of UiPath Apps, Druid Victor solution provides great journeys for all loan origination stakeholders:

- **Informational UiPath App** (Customers & Call Center Agents only!). In chat conversations, users need detailed information such as a customer or supplier profile, a project file, a car specs file, etc. These kind of 360 views include dozens of fields, charts, lists and dashboards that require data from one or several systems. From within the chat, Druid automatically opens the correct UiPath application for the given context. Druid sends from the chat context the required parameters (such as client ID, contract ID, etc.). In this way, the user does not need to search through several dozen UiPath apps to identify the correct one. Thus, the UiPath apps become natural extensions of the chat conversation.
- **Form UiPath App**. When there is a need to capture a lot of information in chat (e.g., for creating a new contract), Druid opens the corresponding UiPath App: „Please fill in this form for me”. Thus, the UiPath App becomes again a natural extension of the chat conversation. The data captured in the UiPath App is saved in UiPath Data Service and from there, through native integration, Druid retrieves the information automatically and displays it in the conversation context.
- **Conversational UiPath App**. The AI Agent is embedded within the UiPath App. Therefore, the user can talk to the AI Agent in the context of the UiPath app. The UiPath app can address questions to the AI Agent and launch processes from the chat, or connect to a human agent through the Druid „Route to Human” functionality, all in the context of the UiPath app.
