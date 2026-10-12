---
title: "Trigger Events from the Web Page Hosting the AI Agent"
---

<a id="TriggerEventsfromtheWebPageHostingtheAIAgent"></a>


{% hint style="info" %}
**NOTE:** Events are sent only if the AI Agent is initialized—meaning the AI Agent is open and the connection is established.
{% endhint %}

<a id="Triggeraconversationalflow"></a>

## Trigger a conversational flow

You can programmatically trigger a specific conversational flow from the web page hosting the AI Agent, with or without context data (entity data set in the web page), using the `sendEvent()` function.

{% hint style="info" %}
**NOTE:**

- Triggering a conversational flow from the web page interrupts the current flow execution. If you only want to update the conversation context, see [Update the Conversation Context](#Update_the_Conversation_Context) instead.
- When triggering a flow with context data, the entity values from the web page will overwrite the current conversation context.
{% endhint %}

<a id="EventSyntaxTriggeraflowwithoutupdatingtheconversationcontext"></a>

### Event Syntax – Trigger a flow without updating the conversation context

**Event syntax**

```
DruidWebchat_v2.sendEvent({
    name: "flow_utterance"
})
```

Where:

- `flow_utterance` is the training phrase (utterance) defined in Druid that triggers the flow.

<a id="EventSyntaxTriggeraflowandupdatetheconversationcontext"></a>

### Event Syntax – Trigger a flow and update the conversation context

**Event syntax**

```
DruidWebchat_v2.sendEvent({
    name: "<flow_utterance>", /* This is the training phrase that triggers the flow */
    value: {
        "$entityTypeName$": "entity_type", /* Corresponds to the entity type. Must be the first field in the payload */
        "EntityField": "entity_value"
    }
})
```

Example:

The following JavaScript code defines a function named 'example1' and assigns it to ;window.example1', making it globally accessible in the browser. When this function is executed, it triggers a Druid conversational flow by sending an event (sendEvent) to the Druid Webchat with specific entity data:

- If the AI Agent is open and connection established, it will trigger the "test sendEvent" conversational flow in DRUID.
- The AI Agent will receive the [[Address]] entity with "City": "Bucharest" and "PostalCode": "050171", updating the conversation context.
- If the flow is designed to use this entity, the AI Agent can process or respond accordingly.

**Example – Trigger a flow with context data**

```
window.example1 = () => {
    /*  
        Example data:  
        [[Address]].City = Bucharest  
        [[Address]].PostalCode = 050171  
    */

    DruidWebchat_v2.sendEvent({
        name: "test sendEvent",
        value: {
            "$entityTypeName$": "Address",
            "City": "Bucharest",
            "PostalCode": "050171"
        }
    })
}
```

<a id="UpdatetheConversationContext"></a>

## <a id="Update_the_Conversation_Context"></a>Update the Conversation Context

You can update the conversation context without interrupting the current flow execution by using the `sendEvent()` function with a special utterance: **"UpdateConversationContext"**.

{% hint style="info" %}
**NOTE:** The entity data sent from the web page will overwrite the existing conversation context.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** Ensure that no flow in Druid has the training phrase "UpdateConversationContext" to avoid conflicts.
{% endhint %}

**Syntax - Update conversation context**

```
DruidWebchat_v2.sendEvent({
    name: "UpdateConversationContext",
    value: {
        "$entityTypeName$": "entity_type", /* Corresponds to the entity type. Must be the first field in the payload */
        "EntityField": "entity_value"
    }
})
```

<a id="Sendausermessageinthechat"></a>

## Send a user message in the chat

You can send a specific message in the chat on behalf of the chat user when they perform an action on the web page hosting the AI Agent.

For example, this can be triggered when a user:

- Clicks a button
- Submits a form
- Completes an interaction.

**Syntax**

```
DruidWebchat_v2.sendMessage("Your text message here");
```

Where:

- "Your text message here" is the message that will appear in the chat as if the user typed it.

**Example – Send a message when a user clicks a button**

```
document.getElementById("sendMessageButton").addEventListener("click", function() {
    DruidWebchat_v2.sendMessage("I submitted my order.");
})
```

When the user clicks the button with the ID "sendMessageButton", the AI Agent receives the message "I submitted my order" as if the user manually entered it.

The AI Agent can then respond based on its configured flows.
