<a id="CustomerService"></a>

# Customer Service

This solution template provides a smart way to scale exceptional customer experiences. It includes conversation flows for submitting online complaints by asking the relevant details about the incident, automatically routing the customer to a human operator based on predefined rules, allowing the customers to easily fill in a service request or a product return form, etc.

This solution template provides a wide range of skills for customers:

| Skill | Description |
| --- | --- |
| [Complain Management](#Complain_Management) | Register online complaints by asking the user relevant details about the incident. |
| [Product Return](#Product_Return) | Guide and educate the customer on how to return an item purchased, how long the refund process takes and so on. |
| [Service Request](#Service_Request) | Guide the user to easily submit a service request. |
| [Product Warranty](#Service_Request) | Provide the warranty for the specified product. Enable customers to view and download their valid product warranties. |
| [Live Chat](#Live_chat) | Automatically route to human operator based on predefined rules or no intent recognition. |

<a id="Configurethetemplate"></a>

## Configure the template

After you import this solution, configure it following the procedure described in [Configuring Skill Templates](../General%20Settings/Configuring%20Solution%20Templates.md).

<a id="SolutionSkills"></a>

## Solution Skills

<a id="ComplainManagement"></a>

### <a id="Complain_Management"></a>Complain Management

The AI Agent can register online complaints by asking the relevant details about the incident. You can use the data and insights gathered through the AI Agent for oversight and policy development purposes.

The solution template includes high-speed response, 24x7 availability, real-time alerts, seamless integration into existing self-service systems and enterprise level security.

#### Key benefits

- 24/7 Availability
- Automated Notifications
- Easy Integration with existing ITSM tools
- Incident  Management
- Improved Employee Productivity.

#### See the skill in action

In the chat type: “I want to add a complain”.

Select a category related to the complain and provide the order number.

![](../../../Resources/Images/Retail/Customer%20Service.png)

Describe shortly the problem. You can also upload a photo/file to the complaint directly via the conversation with the AI Agent.

![](../../../Resources/Images/Retail/Customer%20Service_1.png)

Click **NO**.

The AI Agent will trigger a UiPath process and will retrieve the collected information into the ticketing system.

![](../../../Resources/Images/Retail/Customer%20Service_2.png)

Once the ticket is opened, the UiPath process will assign a new task to the Back-office Manager.

![](../../../Resources/Images/Retail/Customer%20Service_3.png)

<a id="ProductReturn"></a>

### <a id="Product_Return"></a>Product Return

This skill is designed to guide and educate the customer on how to return an item purchased, how long the refund process takes and so on.

#### See the skill in action

In the chat, type “I want to return a product”.

The AI Agent invites you to read the Return Policy.

![](../../../Resources/Images/Retail/Customer%20Service_4.png)

Choose the product to return and input the return reason.

![](../../../Resources/Images/Retail/Customer%20Service_5.png)

Select a refund option (either the money back, or a voucher that can be used for purchasing other products).

![](../../../Resources/Images/Retail/Customer%20Service_6.png)

Choose if you want to return the product directly in the showroom or via a courier.

![](../../../Resources/Images/Retail/Customer%20Service_7.png)

Select the “Showroom” option.

The AI Agent provides you with all available locations and allows you to check the coordinates of the locations on Google Maps.

![](../../../Resources/Images/Retail/Customer%20Service_8.png)![](../../../Resources/Images/Retail/Customer%20Service_9.png)

The AI Agent generates the return form and emails it to your email address or to the post mail company.

![](../../../Resources/Images/Retail/Customer%20Service_10.png)

<a id="ServiceRequest"></a>

### <a id="Service_Request"></a>Service Request

This skill provides the conversational flow to help customer easily submit service requests.

#### See the skill in action

In the chat, type “My laptop is broken, and I want to fill a service request”.

The AI Agent will search for the products that have a valid warranty and will ask you to choose.

![](../../../Resources/Images/Retail/Customer%20Service_11.png)

Provide a short description related to the defect and confirm the pick-up address and the pick-up date.

![](../../../Resources/Images/Retail/Customer%20Service_12.png)

![](../../../Resources/Images/Retail/Customer%20Service_13.png)

The AI Agent generates the service request form and it will send it via email to the courier company.

You can also download the service request form.

![](../../../Resources/Images/Retail/Customer%20Service_14.png)

<a id="ProductWarranty"></a>

### Product Warranty

This skill provides the customers with the option to view and download their valid product warranties.

#### See the skill in action

In the chat, type Please check if I have any valid warranties” or “Do I have any valid warranties?”

The AI Agent will provide you with the list of valid warranties and you can download the desired one.

![](../../../Resources/Images/Retail/Customer%20Service_15.png) ![](../../../Resources/Images/Retail/Customer%20Service_16.png)

<a id="Livechat"></a>

### <a id="Live_chat"></a>Live chat

Automatically route to human operator based on predefined rules or no intent recognition. While Druid can handle large volume of customer requests and respond instantly 24/7, unforeseen things can happen. Live agent transfer allows you to get the most value from your interactions with virtually zero impact on the customer with the conversation continuing in the same interface.

#### See the skill in action

In the chat, type “I want to talk with a human agent”

The AI Agent informs you that the conversation will be registered and asks for your consent. If you want to be transferred to an agent, click the “Agree” button.

![Graphical user interface, text, application, chat or text message Description automatically generated](../../../Resources/Images/Retail/Customer%20Service_17.png)

For information on how Live Chat Works, see [Live Chat](../../../Live%20Chat/Live%20Chat.md).
