---
title: Product recommendation with GPT-Azure
---

# Product recommendation with GPT-Azure

Combining the DRUID technology and GPT technology, you provide users with an amazing human-like multi-turn conversation based on form completion. DRUID orchestrates the entire conversation and asks expertise from GPT in the context of your data and business domain.

To learn how to work with the ChatGPT, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/chatgpt?pivots=programming-language-chat-completions).

### How it works?

DRUID orchestrates the entire conversation and offers GPT the possibility to ask additional questions. When GPT has all the required information, it recommends products in the context of your data and business domain.

### Setting up the solution

The solution comes with Azure OpenAI integration and a flow that has three flow steps.

![](<../../../.gitbook/assets/Product recommendation with.png>)

### Step 1. Import the solution

Go to the **Solutions Library**, search for solution **Product recommendation with GPT-Azure** and import it.

### Step 2. Set up your OpenAI API URL and key

{% hint style="info" %}
**NOTE:** DRUID provides Open AI features from own Azure subscriptions. The Open AI consumption is charged in addition to your AI Agents subscriptions. Contact your DRUID Sales representative for details. You can also bring your own Microsoft Azure OpenAI service subscription. For more information, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview).
{% endhint %}

To set up the Azure OpenAI URL and key:

1. In Druid Portal, on your AI Agent, select solution **Product recommendation with GPT-Azure** and on the main menu, click **Apps**.
2. Click on the GPT app.

![A screenshot of a computer Description automatically generated with medium confidence](<../../../.gitbook/assets/Product recommendation with_1.png>)

The app configuration page opens.

3. In the **Base URL** field, enter the URL of your Azure OpenAI.

![A screenshot of a computer Description automatically generated with medium confidence](<../../../.gitbook/assets/Product recommendation with_2.png>)

4. Scroll down to the Variables table and as value for the key variable, enter the secret key of your Azure OpenAI.

![A screenshot of a computer Description automatically generated with medium confidence](<../../../.gitbook/assets/Product recommendation with_3.png>)

5. Publish the changes.

### Step 3: Set the System role (message)

The system role also known as the system message is included at the beginning of the conversational flow. It provides the initial instructions to the model. To learn more about the system role, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/chatgpt#system-role?pivots=programming-language-chat-completions).

To customize the system role, click the **Settings** icon on the first step and in the step editor, click on the Set Variables section, then click the **Code Editor** icon.

![](<../../../.gitbook/assets/Product recommendation with_4.png>)

In the Code Editor, customize the system role for your use case or just include basic instructions.

![A screenshot of a computer Description automatically generated with medium confidence](<../../../.gitbook/assets/Product recommendation with_5.png>)

The system role that comes with the solution template provides GPT with the following instructions:

1. Set up the context.
2. Set the parameters of the search.
3. Instruct GPT to send the response in a JSON format and provide the GPT model with the format of the response.
4. Set the search context aligned with the business domain to instruct the GPT model to provide an answer within a restricted business context.
5. Instruct GPT what to answer when the response is outside of the specified business context.

### Step 4: Run the first call to OpenAI

The solution uses the REST Connector to call the OpenAI service. Make the request to the generative AI model completions API endpoint.

![Screens screenshot of a chat Description automatically generated with medium confidence](<../../../.gitbook/assets/multiturn azure api call.png>)

In the request body, control the hallucination. Set the “temperature” to zero if you want to disable the usage of OpenAI open knowledge, in correlation with the instructions you provided in the prompt. You can also limit the tokens consumption by setting up the “max\_tokens”.

![](<../../../.gitbook/assets/Product recommendation with_7.png>)

The prompt comes with a predefined Custom Code task that adds the OpenAI response into the Messages collection. DRUID sends the collection to the OpenAI with the next calls to keep the conversation flow.

![](<../../../.gitbook/assets/Product recommendation with_8.png>)

You can use the Code Extension task to add additional operations on the response (if required).

#### Step 5: Present the response in the chat

Present the Open AI response in the chat and capture the user input.

![A screenshot of a computer Description automatically generated](<../../../.gitbook/assets/Product recommendation with_9.png>)

#### Step 6: Prompt Open AI again and loop

Add the user response to the Messages collection and ask the Open AI again. Loop until conversation completes.

Use the same integration action you used on the first OpenAI call.

![](<../../../.gitbook/assets/Product recommendation with_10.png>)

To add user messages to the Messages collection that is sent to OpenAI, in the Set variables section enter the name of the request entity you used in the REST integration for GPT, and then click the **Code Editor** icon and set the user role by using the code format below.

**Set the User role**

```
(
    function () {
        let objMessage = EntityFactory.CreateEntityByName("<the entity that stores the messages>");
        objMessage.Role = "user";
        objMessage.Content = <the entity field that stores user input provided in input mapping on a prompt step>;
 
        [[<GPT integration request entity>]].Messages.Add(objMessage);
 
        return [[<GPT integration request entity>]];
 
    }
)();
```

![](<../../../.gitbook/assets/Product recommendation with_11.png>)

You have successfully customized a multi-turn conversation using GPT technology.
