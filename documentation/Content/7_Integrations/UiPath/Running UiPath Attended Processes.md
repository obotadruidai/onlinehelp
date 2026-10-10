<a id="RunningUiPathAttendedProcesses"></a>

# Running UiPath Attended Processes

Druid offers a simplified way to interact with your personal, locally installed UiPath robot.

The integration of Robot.JS framework in Druid webchat resources allows authors to configure execution of either manually created attended processes or processes stored in Orchestrator. The communication is done via the UiPath Assistant, while the Orchestrator serves as a repository for processes that allows Druid to take the input and output arguments of the process.

The processes are taken from the Orchestrator and synced on the local machine where they run.

Check out Lesson 8 of the Technical Intermediate Course on DRUID Academy for a detailed video tutorial on how to set up UiPath integration to run attended processes.

[Watch video](https://academy.druidai.com/mod/resource/view.php?id=57)

<a id="Prerequisites"></a>

## Prerequisites

- Robot.JS resources are built-in for Druid Portal landing page and for Druid web chat widget (using the snipped code from AI Agent Designer menu)
- If the AI Agent is hosted directly in an external custom web page, then the following Robot.JS resources must be included in the web page script:

**Robot.JS resources**

```
<script src="https://download.uipath.com/js/1.1.1/UiPathRobot.js"></script>
```

- The UiPath Assistant must be installed on the same machine where the AI Agent is accessed.
- The UiPath Process(es) must be published in the UiPath Assistant.
