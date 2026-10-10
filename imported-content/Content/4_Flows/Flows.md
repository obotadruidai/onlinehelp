---
layout:
  title:
    visible: false
---

<a id="Flows"></a>

# Flows

In the Druid AI Platform, a flow is a structured sequence of interactions that defines how the AI Agent handles specific user requests. Depending on your automation goals and the complexity of the task, you can build two types of flows:

- **Conversational Flows** – These define traditional dialog configurations between the end-user and the AI Agent based on a specific intent. A conversational flow consists of an intent (what the user says) and a dialog (a series of predefined steps). They are ideal for structured processes where you want to control the exact sequence of the conversation and the actions executed on third-party systems. For more information, see [Creating Conversational Flows](Conversational%20Flows.md).
- **Agentic Flows** – These leverage the Druid agentic framework to create AI agents capable of reasoning, planning, and acting based on natural language instructions. Unlike conversational flows, agentic flows use generative AI to dynamically manage the conversation, determine which tools to use, and validate user data without manual step-by-step configuration. For more information, see Create Agentic Flows.

The Druid Portal provides a Flow Designer that allows you to create and manage both flow types within your solutions, ensuring you can handle everything from simple inquiries to complex, autonomous AI Agent tasks.
