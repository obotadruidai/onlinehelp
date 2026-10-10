<a id="AgenticFlows"></a>

# Agentic Flows

Agentic flows represent a fundamental shift from linear conversational design to autonomous problem-solving. Unlike standard flows that follow a fixed path, agentic flows use an agentic framework powered by Large Language Models (LLMs) to reason, plan, and execute tasks dynamically.

In this framework, the AI Agent acts as a digital worker capable of performing three core cognitive functions:

- **Reason**. Analyze complex or ambiguous user requests to identify the underlying intent.
- **Plan**. Determine the necessary sequence of steps and information required to reach a goal.
- **Act**. Execute specific tools (functions) to interact with enterprise systems and process data.

There are two primary methods for building an autonomous AI Agent within the Druid Portal, depending on the required level of automation and granular control:

- **Using AI Authoring Agents**. By launching the Conversational from the **New Agentic Flow** button, you can describe your business requirements in natural language to automatically create the complete skill package: the conversational flows, entity data models, and orchestrated Druid Data Service integrations. For more information, see the [AI Authoring Agents](../2_AI%20Agents/AI%20Authoring%20Agents.md).
- **Manual Creation (Agent Step)**. For authors who require granular control over the logic and decision-making process, the **Agent** step allows manual creation. You can add the Agent step to an existing flow or a dedicated new flow to define an autonomous AI Agent. Adding this step to a flow diagram automatically generates the four-part architectural structure required for the autonomous loop:

- Agentic Step. Where the persona, instructions, and tool inventory are defined.
- Run Agent Step. The engine that manages the reasoning and execution cycles.
- Conversational Branch. Handles dialogue for clarification and data gathering.
- Function Call Branch. The action path where specific function handlers execute authorized tools.
