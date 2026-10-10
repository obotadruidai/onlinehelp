---
title: "Dynamic Search Priority at Conversation Time"
---

<a id="DynamicSearchPriorityatConversationTime"></a>


While you can configure default search priorities at the data source level, you can also override these priorities dynamically at runtime during a live conversation.

> **Info:** This feature is available starting with Druid 10.1.

To adjust search priorities dynamically:

1. Navigate to the desired flow step where you want to apply the priority change.
2. In the step configuration editor, click on **Set variables**.
3. Set **[[Intent]].KBWeights** using a JavaScript function that maps your data source names to the desired priority levels (low, medium, or high).

**Example**

```
(function(){
    return {DataSource1: "low", DataSource2: "high", DataSource3: "high"};
})()
```

4. Save the step.

> **IMPORTANT!**
>
> - **Case Sensitivity**. While search priorities (e.g., "low", "high") are case-insensitive, data source names are case-sensitive. Ensure you match the exact capitalization of your data source names.
> - **Conversation Reset**. Runtime weight overrides apply only to the active session. Upon conversation reset, the system automatically reverts to the default priorities configured at the data source level.
