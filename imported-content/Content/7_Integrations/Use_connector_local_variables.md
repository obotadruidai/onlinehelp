---
title: "Using Connector Local Variables"
---

<a id="UsingConnectorLocalVariables"></a>


Connector local variables are variables you can use from the integration context between the integration tasks.
These variables are of type string.

{% hint style="warning" %}
**IMPORTANT!** You can use the connector local variables only within the integration context. You cannot use local variables set on flow steps within integrations and neither can you use connector local variables as local variables between flow steps.

![](../Resources/Images/druid%205.17/nnn%20variables.png)
{% endhint %}

To set a connector local variable, on the response of an integration task use the format **@variable**.

![](../Resources/Images/druid%205.17/set%20cnn%20variable.png)

To use a connector local variable within the integration context on integrations tasks of type other than Custom Code, use the following format: `@variable`.

To use a connector local variable within the integration context on integrations tasks of type Custom Code, use the following format: `var` `<variable name>``= Context.GetContextVariable("``<variable name>``");`

**Example - using connector variables inside the Custom Code tasks**

```
//This is the default snippet for CustomCode
(function main(){

   var text = Context.GetContextVariable("text");
   var conditions = Context.GetContextVariable("conditions");
   var employee = Context.GetResponseEntity();
   var angajat = EntityUtils.Stringify(employee);

   Context.LogResponseTask("text = "+text + " \n conditions = " + conditions + " \n employee stingified = " + angajat);

})()
```
