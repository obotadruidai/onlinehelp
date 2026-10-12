---
title: "Real-time Machine Translation"
---

<a id="RealtimeMachineTranslationinLiveChat"></a>


Use real-time machine translation to enable seamless multilingual communication between clients and agents during live chat sessions.

When real-time machine translation is enabled on the AI Agent, clients and agents can interact in different languages, and the AI Agent will automatically translate messages in both directions.

For example, a French-speaking client chatting with an English-speaking agent can type in French, while the agent responds in English. The AI Agent handles translating messages to the appropriate language so both parties understand each other without needing a common language.

<a id="Howitworks"></a>

## How it works

The Live Chat component integrates with real-time machine translation services such as SDL Machine Translation Cloud, Azure Translator (Cognitive Services) and LLM. This integration supports over 100 language combinations, allowing human agents and AI Agents to provide support in multiple languages simultaneously—without manually authoring responses in each language.

When a message is received in a language different from the recipient’s configured language, the AI Agent translates it before displaying it in the Live Chat interface.

<a id="Requirements"></a>

## Requirements

To use real-time machine translation in Live Chat:

- You must have an active SDL, Azure Translator or LLM account.
- Machine translation must be enabled and the desired machine language service must be configured for Conversation time translation on your AI Agent.
- Enable and configure language change detection on the AI Agent.

For information on how to enable and configure machine translation, see [Using Machine Translation](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/localization/multilingual-ai-agents/using-machine-translation).
