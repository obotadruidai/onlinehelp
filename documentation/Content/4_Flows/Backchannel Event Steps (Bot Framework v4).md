<a id="BackchannelEventBotFrameworkv4"></a>

# Backchannel Event (Bot Framework v4)

Backchannel Event steps allow you to trigger events on the web page that hosts the AI Agent. These steps are useful for processes such as:

- Displaying additional information like Customer 360 views, Medical Records, etc.
- Loading iFrames directly in DRUID, which can include URLs, videos, images, UiPath Apps, or custom applications (e.g., CRM, Live ID).

This section explains how to use a Backchannel Event step to trigger a JavaScript function defined in the web page hosting the AI Agent.

<a id="Prerequisites"></a>

## Prerequisites

- Before adding and configuring the Backchannel Event step, ensure that your web page's source code includes the **webChatEventHandler** function. This function should define the actions and event handling logic you want to implement. For detailed guidance on configuring actions, events, and AI Agent layout, refer to [WebChat Common Styling and Behavior v4](../Channels/WebChat/WebChat_Common_Styling_and_Behavior_v4.md).

**webChatEventHandler function**

```
"webChatEventHandler": "(action, currentDruidState) => {
        if (action.type === 'DIRECT_LINE/INCOMING_ACTIVITY' && DruidWebchat_v2.isNewActivity(currentDruidState, action.payload.activity))
        {
            if(action.payload.activity.text == \"disable\") {DruidWebchat_v2.disableChat();}
        }
}"
```

![](../Resources/Images/Backchannel%20Event%20Steps/Backchannel%20Event%20Steps%20Bot.png)

- If you need the conversation in DRUID to continue after executing a backchannel event, ensure that a **sendMessage** function is in place to trigger an utterance that matches a corresponding flow in the AI Agent.

<a id="AddingandconfiguringBackchannelEventstepstotriggerJavaScriptfunctions"></a>

## Adding and configuring Backchannel Event steps to trigger JavaScript functions

To add and set up a Backchannel Event step that triggers a JavaScript function:

1. Open the desired flow in Flow Diagram view.
2. Expand the Flow Palette, then drag the **BC Event** step from the Dialog category into the main flow window and drop it onto the step you want to link it to.
3. Select the step on the diagram, then click the **Settings** icon from the Actions menu.
4. Set the General parameters:

- **Step name**: Enter the exact name of the JavaScript function defined in the web page's source code. The step will not trigger the function if the name is incorrect.
- **Step message**: Remove the default message and leave it empty. Backchannel Event steps are used to trigger functions, not display messages in the chat.

5. If you want to pass information to the backchannel event, select the relevant entity in the **Input mapping** field.
> **IMPORTANT!** This step is not related to receiving back information in the same entity.

> **NOTE:** This step is mandatory as the AI Agent requires this information to load the function. If no specific information needs to be passed, select any entity.

6. Click **Save** to save the settings.

<a id="UseCases"></a>

## Use Cases

<a id="FinancialUsecaseHandlingtheloanrequestcalculator"></a>

### Financial Use case: Handling the loan request calculator

In a financial scenario, a loan request calculator might need to trigger corresponding conversations in the background each time a user adjusts the sliders. This can be achieved using Backchannel Events linked with DRUID NLP.

<a id="AuthenticationFlowsUseCaseUpdatingUserNames"></a>

### Authentication Flows Use Case: Updating User Names

During authentication flows, after identifying a user, you may want to update their name in the AI Agent snippet. To do this, add a Backchannel Event step named **userAuthenticated** and in the **Input mapping** field, include **[[ChatUser]]**. The AI Agent will look for [[ChatUser]].FirstName to authenticate the user.

<a id="ChangingAIAgentandUserNamesinChat"></a>

### Changing AI Agent and User Names in Chat

You can also use Backchannel Events to change the AI Agent name or the user's name in the chat. For example, in an authentication flow, you could add a step named **ChangeDisplayName** and in the **Input mapping** field add the entity storing the AI Agent and user names (e.g., **BotDisplayName** and **UserDisplayName**). Depending on your needs, you can update either or both names.

Example:

![](../Resources/Images/Backchannel%20Event%20Steps/Backchannel%20Event%20Steps%20Bot_1.png)

![](../Resources/Images/Backchannel%20Event%20Steps/Backchannel%20Event%20Steps%20Bot_2.png)
