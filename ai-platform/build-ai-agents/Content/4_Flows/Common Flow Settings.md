---
title: Common Flow Settings
---


Some of the General and Metadata configuration settings vary based on the flow step type, while the following configuration settings apply to all flow steps regardless their type:

* [General](General.md)
* [Metadata](Metadata.md)
* [Set Variable](<Set Variables.md>)
* [Code Extension](<Code Extension.md>)
* [Pre Actions](<Pre Actions.md>)
* [Post Actions](<Post Actions.md>)
* [Voice](Voice.md)
* [Proactive AI Agent Messages](<Proactive AI Agent messages.md>)

For information on the step type specific settings, please refer to the respective step type configuration section.

## Flow Step Execution

The diagram below describes the execution order on a flow step.

![](<../../.gitbook/assets/flow step execution.png>)

{% hint style="warning" %}
**IMPORTANT!** If you’re using same entities to capture data on all or some of the step sections, they will be overwritten during the step execution as described in the diagram above. For example, if you set an entity value in the Set Variable section and you use the same entity for input mapping in the General section, the value set in the Set Variable section will be overwritten by what the user says.
{% endhint %}
