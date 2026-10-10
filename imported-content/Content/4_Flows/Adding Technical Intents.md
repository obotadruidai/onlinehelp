---
title: "Adding Technical Intents"
---

<a id="AddingTechnicalIntents"></a>


The Commands section in Flow Details lets you define technical utterances as exact-match commands instead of using them as NLP training phrases. This helps you manage structured or system-level inputs — such as **\_\_update\_db\_parameters\_\_** or **#CreateNewFlowFromBot** — without affecting the language model’s performance.

Commands are matched exactly as typed, and they bypass natural language processing (NLP). By separating these phrases from NLP training data, you reduce noise and improve language understanding, especially when using LLM-supported models.

<a id="WhentousetheCommands"></a>

## When to use the Commands

Use the Commands section when you need to:

- Handle developer or system-facing phrases
- Avoid NLP interpretation of precise inputs
- Improve model clarity by reducing irrelevant training data
- Avoid using the Commands section for natural user language or open-ended intents.

<a id="AddaCommand"></a>

## Add a Command

To define a technical utterance as a command:

1. Open the AI Agent and go to your solution Flows.
2. Select the desired flow and click Flow Details.
3. Scroll to the Commands section.
4. Click **Add Command**.
5. Enter the exact phrase or command (e.g., **\_\_restart\_task\_\_** or **#RunReportNow**).
6. Click **Save**.

> **NOTE:** Commands are case-sensitive and must match user input exactly.

<a id="UpdateExistingFlows"></a>

## Update Existing Flows

If your current flows include technical phrases in the Training Phrases section:

1. Remove those phrases from the NLP training list.
2. Add them to the Commands section as described above.
3. Save and test your flow to ensure the commands trigger correctly.
