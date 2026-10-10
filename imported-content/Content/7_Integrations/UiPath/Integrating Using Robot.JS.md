---
title: "Integrating Using Robot.JS"
---

<a id="IntegratingUsingRobotJS"></a>


> **IMPORTANT!** This integration is available only for backward compatibility. We recommend you to use [Running UiPath Attended Processes.](Running%20UiPath%20Attended%20Processes.md)

Interacting with your personal, locally installed UiPath robot is now easier than ever, thanks to the integration of Robot.JS framework in Druid webchat resources.

> **NOTE:** This functionality is available only for web-hosted AI Agents. It is not available from MS Teams, Slack, WhatsApp, Facebook, etc.

<a id="Prerequisites"></a>

## Prerequisites

- Robot.JS resources are built-in for Druid Portal landing page and for Druid web chat widget (using the snipped code from AI Agent Designer menu)
- If the AI Agent is hosted directly in an external custom web page, then the following Robot.JS resources must be included in the web page script:

```
<script src="https://download.uipath.com/js/1.1.1/UiPathRobot.js"></script>
```

- The UiPath Assistant must be installed on the same machine where the AI Agent is accessed.
- The UiPath Process(es) must be published in the UiPath Assistant.
- The Druid entity **[[RobotJsInput]]** must be defined and must include the following mandatory fields, with fixed names:

  - ProcessName
  - CallbackUtterance

- You need to have a Callback Flow created.

<a id="Howtriggeringanattendedprocessworks"></a>

## How triggering an attended process works

![](../../Resources/Images/Integrations/attended%20robot.png)

<a id="Configuration"></a>

## Configuration

Triggering a local process and transferring structured data between the AI Agent and the UiPath robot can simply be managed by a dedicated Back Channel (BC) type flow step – RobotJsStartProcess.

No connector actions or internal actions are needed in order to trigger the UiPath process. All configurations are made within the Flow Designer.

<a id="FlowConfiguration"></a>

## Flow Configuration

The Back Channel flow step **RobotJsStartProcess** is the element which will trigger the UiPath Process via the UiPath Assistant. To do that, the UiPath Process Name and any utterance of the Druid flow used for callback must be provided to the Back Channel flow step, using the **[[RobotJsInput]]** entity.

A simple flow configuration might look like this:

![https://www.druidai.com/wiki/wp-content/uploads/2020/07/Flow-Step-Configuration.jpg](../../Resources/Images/UiPath%20Robot/UiPath%20Robot%20JS%20integration.jpg)

When the conversation reaches the Back Channel step, the UiPath Assistant will be called (using built-in Robot.JS functionality) to start the Process <ProcessName>.

<a id="UiPathAssistantAuthorization"></a>

## UiPath Assistant Authorization

The first interaction between the browser and the UiPath Assistant will trigger an authorization process:

![https://www.druidai.com/wiki/wp-content/uploads/2020/07/Pop-up.jpg](../../Resources/Images/UiPath%20Robot/UiPath%20Robot%20JS%20integration_1.jpg)

Click **Open UiPath Assistant**. The UiPath Assistant access request pop-up appears.

![https://www.druidai.com/wiki/wp-content/uploads/2020/07/Authorization-2.jpg](../../Resources/Images/UiPath%20Robot/UiPath%20Robot%20JS%20integration_2.jpg)

Click **Allow**. After the authorization process is complete, the robot will start the UiPath process.

> **NOTE:** The UiPath authorization process happens is valid for 30 days, unless the browser is used in incognito mode.

<a id="DruidCallback"></a>

## Druid Callback

When the UiPath process ends, Robot.JS notifies the AI Agent hosting web page and will automatically send to the AI Agent the utterance defined in the **[[RobotJsInput]].CallbackUtterance** entity field.

The flow which is trained to respond to the respective utterance is the triggered in the AI Agent conversation.

<a id="TransferringdatabetweentheAIAgentandUiPathrobot"></a>

## Transferring data between the AI Agent and UiPath robot

<a id="FromAIAgenttorobot"></a>

### From AI Agent to robot

**[[RobotJsInput]]** is the data transporter from the AI Agent to the UiPath process. All the fields defined in the entity will be fed as input arguments to the UiPath process. Apart from the two mandatory fields, **ProcessName** and **CallbackUtterance**,  you can define as many fields as you need, of any data type available in the Druid Platform.

For example, you can add three more fields to the entity, as below:

```
[[RobotJsInput]]
    .ProcessName
    .CallbackUtterance
    .FirstName
    .LastName
    .City
```

or use the **Entity** or the **Entity List** field type to send the whole data structure already used in the AI Agent process configuration:

```
[[RobotJsInput]]
    .ProcessName
    .CallbackUtterance
    .AccountData
    .ContractList
```

Where:

- **AccountData** is an Entity type field, referred to the **[[Account]]** entity.
- **ContractList** is an Entity List type field, referred to [[Contract]] entity.

The two fields will be sent as Jobject type arguments (not variables) to the UiPath process, where they can be deserialized and mapped to the UiPath data structure accordingly.

> **IMPORTANT!** The **[[RobotJsInput]]** field names must be identical with the UiPath Process input arguments.

<a id="FromrobottoAIAgent"></a>

### From robot to AI Agent

Data that needs to be transferred back to the AI Agent must be placed in the output argument with fixed name – Payload.

The Payload argument (type string) must contain the serialized string of a Druid Entity, having the following definition:

```
{
     "$entityTypeName$":"<Druid Response Entity Name>",
     "<Field 1>":"value",
     "<Field 2>":"value",
     .....
     "<Field n>":"value"
}
```

The entity used for response data mapping can be any existing Druid Entity

The entity fields defined in the UiPath process must exist and have the same names as of the entity defined in Druid Platform.

Collection type data can also be sent back to the AI Agent. The definition of the Druid Entity Json, in this case, is the one presented below:

```
{
     "$entityTypeName$": "Account",
     "ManagerName":"John Doe",
     "ContractList": {
                    "$entityTypeName$": "Contract_Collection",
                    "items": [
                        {
                            "$entityTypeName$": "Contract",
                            "Number": "100",
                            "Date":"2020-07-01",
                            "Object":"Personal Loan"    
                        },
                        {
                            "$entityTypeName$": "Contract",
                            "Number": "105",
                            "Date":"2020-05-21",
                            "Object":"Investment Loan"    
                        },
                        {
                            "$entityTypeName$": "Contract",
                            "Number": "230",
                            "Date":"2015-02-03",
                            "Object":"Morgage"    
                        }
                    ]
	}
 }
```

The structure of the **[[Account]]** entity is as follows:

```
[[Account]]
.ManagerName    -- string
.ContractList   -- Entity List, referred to [[Contract]] entity
```

When the callback flow is triggered, the **[[Account]]** entity will be populated with data from the example above.

## Related Topics

- [Accessing Druid Endpoints in Druid Hybrid Deployments](../../Druid%20Deployment/Accessing%20Druid%20Endpoints%20in%20Druid%20Hybrid%20Deployments.md)
