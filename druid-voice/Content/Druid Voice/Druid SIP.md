---
title: "Overview"
---


Druid SIP is the telephony voice gateway for Druid Voice. It enables organizations to seamlessly connect AI agents to SIP-based VoIP infrastructure, allowing callers to interact with AI Agents through existing telephony environments without requiring changes to their current voice architecture.

Acting as the core bridge between telephony systems and the Druid AI Platform, the gateway manages:

* **Call Control**. Streamlined call establishment and termination.
* **Audio Processing**. Real-time audio streaming and voice interaction management.
* **Security**. Robust security controls for voice data.

## Supported Telephony Environments

* Contact centers and PBXs
* SIP trunks and Session Border Controllers (SBCs)

Druid SIP allows organizations to embed conversational AI directly into their voice ecosystems, maximizing the value of current telephony investments.

## Prerequisites

Before configuring Druid Voice integrations or deploying voice capabilities across your environments, ensure that your firewall and network settings allow traffic to and from the Druid SIP Host application and the Media Server.

{% hint style="warning" %}
**IMPORTANT!** Whitelisting the Druid SIP Host IP addresses and ports is mandatory to establish proper SIP signaling and media stream connectivity.
{% endhint %}

### Druid SIP Host IP Addresses (SIP Signaling)

| Environment     | IP Address    | Ports     |
| --------------- | ------------- | --------- |
| Community       | 20.56.251.87  | 5060 5061 |
| PROD EU         | 20.50.55.224  | 5060 5061 |
| PROD US         | 20.83.136.183 | 5060 5061 |
| PROD US - HIPAA | 20.85.98.81   | 5060 5061 |
| PROD AU         | 4.147.95.8    | 5060 5061 |

### Druid SIP Media Server IP Addresses (Media Streams)

| Environment     | IP Address                  |
| --------------- | --------------------------- |
| Community       | 20.16.237.249 20.101.146.52 |
| PROD EU         | 20.56.27.59                 |
| PROD US         | 20.120.84.97                |
| PROD US - HIPAA | 172.206.63.183              |
| PROD AU         | 4.237.59.4                  |
| PROD UAE        | 20.233.248.10               |

## Core Capabilities

Druid SIP provides robust session, media, and security management:

### Session & Media Management

* **SIP Signaling & Session Management**. Handles call setup, teardown, and routing.
* **RTP Media Handling**. Ensures stable bidirectional Real-time Transport Protocol (RTP) audio stream delivery.
* **DTMF Processing**. Supports dual-tone multi-frequency (DTMF) key inputs.
* **Voice Activity Detection (VAD) & Barge-in**. Enables natural, fluid conversations by detecting when a user speaks or interrupts.
* **Call recording**. Supports the capturing and logging of voice sessions for compliance, quality assurance, and training purposes.

### Security & Authentication

Enforces zero-trust access boundaries using:

* **IP Allow-list Security**. Restricts access to trusted networks.
* **SIP Token Authentication**. Validates endpoint identity securely.
* **Mutual TLS (mTLS) Session Authentication**. Enforces two-way cryptographic verification for all traffic.

## Druid SIP Architecture

The Druid SIP gateway is deployed in the Druid Cloud and exposed through a public FQDN, which telephony platforms use as their primary SIP destination.

The following diagram illustrates how Druid SIP connects SIP-based voice infrastructure to the Druid AI Platform.

![](<../../.gitbook/assets/druid sip.png>)

### Telephony Infrastructure / Caller

Voice interactions originate from telephony systems such as contact centers, PBXs, IVRs, SIP trunks, or SBCs callers. These systems communicate with Druid SIP using standard SIP signaling and RTP audio streams.

### Druid SIP (VoIP Gateway)

Druid SIP acts as the entry point for all voice interactions.

### Druid AI Platform

After receiving the audio stream, Druid SIP routes the conversation to the Druid AI Platform, where:

* The Language Understanding Engine extracts intent and context.
* The Flow Engine executes business logic and conversation flows.
* The AI Agent generates responses.
* Conversation state is maintained throughout the interaction.

For all Druid SIP conversations, the platform automatically sets \[\[ChatUser]].ChannelId = "druid-sip". This allows AI Agents to apply channel-specific logic when required.

### Speech-to-Text Services

Incoming audio is sent to the configured Speech-to-Text provider, which converts spoken language into text before it is processed by the AI Agent. Supported providers are documented in the [TTS and STT Vendors](<TTS and STT Vendors.md>) topic.

### LLM Services (optional)

When generative AI capabilities are required, the AI Agent can call one or more configured Large Language Model (LLM) providers. LLM calls are optional and depend on the AI Agent setup. Supported providers are documented in the [LLM Resource Management and Governance](https://druidai.gitbook.io/druid-ai-docs/ai-platform/ai-governance-and-security/ai-evaluation-and-response-guardrails/llm-resource-management-and-governance) topic.

### Text-to-Speech Services

After the response is generated, the text is sent to the configured Text-to-Speech provider, which converts the response into audio and returns it to Druid SIP for playback to the caller. Supported providers are documented in the [TTS and STT Vendors](<TTS and STT Vendors.md>) topic.

## End-to-End Call Flow

The caller initiates a voice interaction through a SIP-enabled telephony platform.

1. A SIP session is established with Druid SIP.
2. RTP audio is streamed to Druid SIP.
3. Druid SIP processes voice activity and DTMF events.
4. Audio is sent to the configured Speech-to-Text provider.
5. The transcribed text is processed by the Flow Engine.
6. The AI Agent optionally invokes LLM services.
7. A response is generated and sent to the configured Text-to-Speech provider.
8. The synthesized audio is streamed back through Druid SIP.
9. The caller hears the AI Agent response.
