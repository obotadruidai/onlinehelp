---
layout:
  title:
    visible: false
---

<a id="CommonFlowSettings"></a>

# Common Flow Settings

Some of the General and Metadata configuration settings vary based on the flow step type, while the following configuration settings apply to all flow steps regardless their type:

- [General](General.md)
- [Metadata](Metadata.md)
- [Set Variable](Set%20Variables.md)
- [Code Extension](Code%20Extension.md)
- [Pre Actions](Pre%20Actions.md)
- [Post Actions](Post%20Actions.md)
- [Voice](Voice.md)
- [Proactive AI Agent Messages](Proactive%20AI%20Agent%20messages.md)

For information on the step type specific settings, please refer to the respective step type configuration section.

<a id="FlowStepExecution"></a>

## Flow Step Execution

The diagram below describes the execution order on a flow step.

![](../Resources/Images/Flows/flow%20step%20execution.png)

> **IMPORTANT!** If you’re using same entities to capture data on all or some of the step sections, they will be overwritten during the step execution as described in the diagram above. For example, if you set an entity value in the Set Variable section and you use the same entity for input mapping in the General section, the value set in the Set Variable section will be overwritten by what the user says.
