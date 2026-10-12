---
title: "Druid Voice"
---


Druid Voice enables organizations to deploy AI-powered voice Agents across telephony systems and digital voice channels. By combining speech recognition, conversational AI, large language models, and speech synthesis, Druid Voice allows users to interact naturally with AI Agents using their voice.

Built on the Druid AI Platform, Druid Voice provides a provider-agnostic architecture that enables organizations to independently configure speech services while maintaining a consistent conversational experience.

Whether deployed in contact centers, enterprise telephony environments, or digital channels, Druid Voice allows organizations to automate customer interactions, improve service availability, and deliver natural voice experiences at scale.

## Supported Voice Channels

Druid Voice currently supports the following voice channels:

* **Druid SIP (VoIP Gateway)**– Enables AI-powered voice interactions through SIP-based telephony infrastructure, including contact centers, PBXs, SBCs, and SIP trunk providers.
* **webRTC** – Enables browser-based voice interactions through the Druid WebChat channel. This channel is available starting with Druid 10.1.

Both channels leverage the same Druid AI Platform and can use the same conversational flows, integrations, and AI capabilities.

## Architecture Overview

The following diagram illustrates the core components of Druid Voice:

![](<../../.gitbook/assets/DRUID VOICE.png>)

### Voice Channels

Voice interactions originate through supported channels such as Druid SIP and webRTC.

### Speech-to-Text Services

Incoming audio is converted into text using the configured Speech-to-Text provider. Supported providers are documented in the [TTS and STT Vendors](<TTS and STT Vendors.md>) topic.

### Druid AI Platform

The Druid AI Platform is the central intelligence layer responsible for processing user requests and generating responses.

The platform includes:

* **Language Understanding Engine** – Extracts intents, entities, and contextual information from user input.
* **Flow Engine** – Executes conversation logic, orchestrates integrations, and manages dialogue flow.
* **Audio and Voice Orchestration** – Audio Orchestration and Voice Orchestration are logical platform components that abstract communication between Druid Voice and external or proprietary speech providers. These orchestration layers provide:
* Provider abstraction
* Service failover
* Language-specific configuration
* Runtime routing of speech requests

### LLM Services

For use cases requiring generative AI capabilities, the platform can invoke configured Large Language Model providers through the LLM Resources Manager. LLM providers are configured and governed at the tenant level through the Druid Portal. Supported providers are documented in the [LLM Resource Management and Governance](https://druidai.gitbook.io/druid-ai-docs/ai-governance-and-security/ai-evaluation-and-response-guardrails/llm-resource-management-and-governance) topic.

### Text-to-Speech Services

Generated responses are converted into natural-sounding speech using the configured Text-to-Speech provider. Supported providers are documented in the [TTS and STT Vendors](<TTS and STT Vendors.md>) topic.

## End-to-End Core Voice Flow

The platform processes real-time voice interactions across five lifecycle stages:

1. **Voice Input**. Capture of the incoming audio stream via telephony (SIP) or voice web chat channel.
2. **Speech-to-Text Processing**. Audio transcription via abstracted speech provider integrations.
3. **AI Agent Orchestration**. Context analysis, intent extraction, and conversational state tracking within the Druid AI Platform.
4. **Response Generation**. Dynamic text generation using enterprise LLM resources.
5. **Speech Synthesis (TTS)**. Conversion of text responses back into natural audio streams for caller delivery.

## Prerequisites

Before using Druid Voice:

* The Druid Voice feature must be enabled for your tenant.
* You must have at least one published AI Agent.
* Appropriate STT, TTS, and optional LLM providers must be configured.
