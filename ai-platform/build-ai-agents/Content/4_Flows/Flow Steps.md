---
title: Flow Steps
---


Flow steps are the essential building blocks for creating flows and defining the logic of AI Agents. They enable you to design complex conversational experiences. Each flow step represents a specific action, decision point, or interaction within the flow, shaping how the conversation unfolds.

Druid offers common dialog flow steps and predefined integration steps in the Flow Palette to streamline the flow authoring process. You can use these predefined dialog flow steps or integration steps to quickly build and customize your AI Agent.

* Each step features a set of intuitive icons that highlight active settings and integrations, reducing the need to click into each step to verify configurations.

![](<../../.gitbook/assets/flow step icons.png>)

Below is a brief description of the dialog flow steps available in the platform.

| Type              | Description                                                                                                                                                                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Action            | Triggers an integration action or an internal AI Agent action.                                                                                                                                                                                 |
| Adaptive Cards    | Displays rich content in the chat, including text, graphics, buttons, and interactive forms. **NOTE:** This flow step is available only if you have bot framework version 4 activated on your tenant and the AI Agent is configured to use it. |
| Choice            | Provides users with multiple-choice options. Capture the user's selection in an entity or variable defined in the **Input Mapping** field.                                                                                                     |
| Flow              | Triggers the execution of another flow specified in the Metadata section.                                                                                                                                                                      |
| Hero              | Displays Hero cards, allowing you to present a compact menu, render files with data, or display a list of files. Capture user input using the **Input Mapping** field.                                                                         |
| Message           | Sends a text response to the user, as specified in the **Message** field.                                                                                                                                                                      |
| Prompt            | Waits for user input and captures the information in **Input Mapping**, either as an entity or a variable.                                                                                                                                     |
| Thumbnail         | Similar to Hero steps, but displays the image as a thumbnail.                                                                                                                                                                                  |
| File Upload       | Prompts the user to upload a file.                                                                                                                                                                                                             |
| Backchannel Event | Triggers events on the web page that hosts the AI Agent.                                                                                                                                                                                       |
| UiPath            | Integrates with UiPath to start a UiPath process from DRUID. For configuration details, see [Starting UiPath Unattended Processes](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/rpa/uipath-connector/starting-uipath-unattended).                                                  |

## Related Topics

* [Defining the Dialog](<Defining the Dialog.md>)
