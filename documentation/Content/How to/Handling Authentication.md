<a id="HandlingAuthentication"></a>

# Handling Authentication

<a id="microcontent1"></a>

When you have the AI Agent available in your public website, each conversation starts as anonymous. You don’t know the actual user chatting with your AI Agent.

You can authenticate the users chatting with your AI Agent asking specific questions and checking the provided information with the Druid back-end systems.

Using the Flow Designer, create and configure an authentication flow, following this sequence of actions:

![](../Resources/Images/Use%20Cases/auth%20flow.png)

You can also use authentication for other channels like: Teams, Facebook or WhatsApp when the user is chatting with the AI Agent for the first time.

<a id="Step1Askauthenticationquestions"></a>

## Step 1: Ask authentication questions

Ask the user to provide authentication information. It can be: VAT Code, Client ID, Email address, Date of birth, Phone number, Badge (for employees) etc.

<a id="Step2Verifyusercredentials"></a>

## Step 2: Verify user credentials

Based on the information provided by the user, search for the user in linked apps like CRM, ERP etc. For higher security, you might want to use two-factor authentication, sending SMS code, typing DNA, asking security questions from the user profile etc. To verify user credentials, you can use external actions on the authentication flow (step).

<a id="Step3Savetheuserprofile"></a>

## Step 3: Save the user profile

Call the internal action **SaveIdentifiedUser** to match existing profile or provision the user as authenticated user in the Druid AI Platform.

> **IMPORTANT!**  **DO NOT** use the internal action **SaveIdentifiedUser** to change an authenticated user to another one (e.g., switch the current conversation from Jane to John).

![](../Resources/Images/Use%20Cases/save%20identified%20user.png)

The table below lists the ChatUser attributes expected as input by the SaveIdentifiedUser action. In the Set Variables section of the step where you call the internal action SaveIdentifiedUser, provide the variables listed in the table below. While the DomainUserName which is optional, you need to provide it as well if you integrate with AD or other user management systems.

| ChatUser Attribute | Description |
| --- | --- |
| ChatUser.MasterId | Holds the business unique key for the user. It is the Badge for an HR AI Agent, the Client Id or VAT No or CNP for a Customer Support AI Agent. This is a **mandatory** attribute. |
| ChatUser.DomainUserName | Used in AI Agents for employees, like the HR AI Agent or the Help Desk AI Agent. It is used in Active Directory integrated AI Agents (intranet web page) or MS teams AI Agents. |
| ChatUser.Email | The Email should be unique across users on your tenant. If an existing user has the same email address as the new one, the SaveIdentifiedUser action will raise an error and will not create the new user profile. This is a **mandatory** attribute. |
| ChatUser.FirstName | The user's first name. This is a **mandatory** attribute. |
| ChatUser.LastName | The user's last name. This is a **mandatory** attribute. |

The **SaveIdentifiedUser** system action searches the list of users on the tenant for an existing user profile by the **MasterId** field. If found, the current user is linked to the respective profile. If not found, a new profile is created.

If a match is found, than the AI Agent impersonates the user and from that moment, the user is no longer anonymous but identified.

If DomainUserName exists as well, the pair MasterID –DomainUserName is used to identify the user.

The system applies the following criteria for matching the user profile:

- Searches for the **MasterId**. If found, then checks the **DomainUserName**. If there is match, it links it with the existing profile.
- If the **MasterId** exists and the **DomaninUserName** does not match, it updates the existing profile with the new **DomainUserName** and links it with the existing profile. The existing profile is updated with the FirstName, LastName, Email and DomainUserName.
- If the **MasterId** is not found, it creates a new user profile.

<a id="Step4Authenticateconversation"></a>

## Step 4: Authenticate conversation

Call the internal action **SaveAuthenticatedUser** to set the current conversation as authenticated.

> **NOTE:** For DRUID version 1.71 and higher, the messages in chat will be sent by the new [[ChatUser]].FirstName of the recently authenticated user. If you want to change the user's name in the AI Agent snippet to a specific name, you can further use a backchannel step and configure it based on your use case. For more information about backchannel event steps and the two use cases available, see [Backchannel Event Steps (Bot Framework v4)](../4_Flows/Backchannel%20Event%20Steps%20%28Bot%20Framework%20v4%29.md).

For the web channels using the Druid webchat snippet, you can also add a second step of type Back Channel to change the user name listed in the conversation.

![](../Resources/Images/Use%20Cases/auth%20flow%20steps.png)

After the authentication flow completes, you might want to return the user to the initial flow from where the authentication flow was triggered.

To do so, you can configure the user-authenticated step in a step of type trigger flow as follows: from the **Type** field, select **Flow** and in the **Input mapping** field, enter **@AuthOriginalFlow**.

Once the user is authenticated in the conversation context, the AI Agent will return to the flow from which the authentication was triggered.

<a id="ChangingtheAIAgentnameandtheusersname"></a>

## Changing the AI Agent name and the user’s name

You can use backchannel events to change the AI Agent and the user’s name in the chat. You can do so by adding a step of type Backchannel Event on the authentication flow. Name the step **ChangeDisplayName** and in the **Input mapping** field, add the entity that stores the AI Agent and user name (the entity has these two entity fields: **BotDisplayName** and the **UserDisplayName**). You can either change both the AI Agent and the user’s name or only one of them based on your needs.

Example:

![](../Resources/Images/Backchannel%20Event%20Steps/Backchannel%20Event%20Steps%20Bot_1.png)

![](../Resources/Images/Backchannel%20Event%20Steps/Backchannel%20Event%20Steps%20Bot_2.png)

<a id="Step5Assignrolestoauthenticateduser"></a>

## Step 5: Assign roles to authenticated user

Assign specific roles to the authenticated user by calling the **AddUserRoles** internal action and entering the target roles in the text field. Specify the roles between brackets, separated by commas. Example: ["User","Admin"]

> **IMPORTANT!** Even if no custom roles are needed, you must still assign the default "User" role. If this step is omitted, the user profile will be created with no roles assigned.

<a id="Step6SelecttheAIAgentauthenticationflow"></a>

## Step 6: Select the AI Agent authentication flow

This authentication flow can be set up as special flow on the AI Agent. Click the AI Agent, go to **Special flows** and select the your autehntication flow as **Authentication special flow**. This means that when an unauthenticated user reaches a flow that requires authentication, the special authentication flow will be triggered.

There are various ways in which the user can be sent to the authentication flow.

- You can redirect users in the welcome flow and the welcome flow does not require authentication. This means that you trigger the authentication flow from the welcome flow.
- Or on the welcome flow you trigger a menu flow and the menu flow requires authentication. This means that when the user reaches the menu flow, authentication is triggered.
- Or the welcome flow requires authentication.

<a id="ChatUserinformationautomaticallyavailableintheconversationcontext"></a>

## ChatUser information automatically available in the conversation context

The AI Agent automatically provisions a set of ChatUser parameters in the conversation context. The ChatUser information available within the conversation context is specific per channel, as follows:

<a id="MSTeams"></a>

### MS Teams

- [[ChatUser].Email
- [[ChatUser].FirstName
- [[ChatUser].Lastname
- [[ChatUser].DomainUserName
- [[ChatUser].UserId – the MS Teams user id.

<a id="Facebook"></a>

### Facebook

- [[ChatUser].UserId – the Facebook user id.
- [[ChatUser].FirstName
- [[ChatUser]].Lastname

[[ChatUser]].FirstName and [[ChatUser]].Lastname are stored only if you configured Facebook to transmit the client information. To do so, log into Meta for Developers and go to your app (the one you created for AI Agent integration). On the **Webhooks** menu, click **Messenger**. In the Webhook subscriptions, add the following subscription: **messaging\_customer\_information**.

![](../Resources/Images/FB%20integration/chatuser%20name.png)

<a id="WhatsAppNexmo"></a>

### WhatsApp (Nexmo)

- [[ChatUser]].UserId – holds the incoming phone number

<a id="GoogleChatavailableforDruidv155orhigher"></a>

### Google Chat (available for Druid v1.55 or higher)

- [[ChatUser]].Email - holds the Google user's email.
- [[Chatuser]].FirstName - holds the Google user's display name.

<a id="AuthenticateuserinTelephony"></a>

### Authenticate user in Telephony

- [[ChatUser].UserId – holds the incoming phone number.

<a id="Telegram"></a>

### Telegram

- [[ChatUser].UserId – holds the incoming phone number.

<a id="Viber"></a>

### Viber

- [[ChatUser].UserId – holds the incoming phone number.
