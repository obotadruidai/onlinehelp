---
title: Routing Intelligence & Context Preservation
---


Druid Conductor is the primary AI Agent the user always talks to — it knows when to call in a specialist and when to handle things itself.

## Routing Intelligence

It uses its own NLU model in combination with the models of all orchestrated AI Agents to predict the best match for every user utterance. The Ranking and Resolver engine weighs these predictions and selects the specialized AI Agent. When multiple AI Agents score above the confidence threshold, Druid Conductor initiates a brief sub-dialog to confirm the user's intent before proceeding — avoiding misrouting without frustrating the user.

If no orchestrated AI Agent matches, Druid Conductor falls back to its own intents, acting as a catch-all that ensures no user message goes unanswered.

![](../../.gitbook/assets/Drawing1.jpg)

Users never know which AI Agent is handling their request. They just talk to Druid Conductor — Mary, in the healthcare example — and the right AI Agent is silently engaged behind the scenes.

## Context Preservation Across Agent Handoffs

One of the most powerful aspects of Druid Conductor is its ability to maintain conversation context across agent transitions. It tracks which AI Agent last engaged the user, and when the next utterance arrives, it first predicts against that agent before broadening the search. This means a user can move naturally from booking an appointment to asking a billing question — without feeling transferred or having to repeat themselves.
