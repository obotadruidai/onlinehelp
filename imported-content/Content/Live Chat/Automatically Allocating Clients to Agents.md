---
title: Automatically Allocating Clients to Agents
---

# Automatically Allocating Clients to Agents

Live Chat allows your helpdesk agents to accept client live chat requests automatically. Once a client initiates a live chat request, DRUID automatically connects them to an available helpdesk agent. Available agents are logged-in agents who did not reach the concurrent chat limit and did not request a break.

### Benefits

* Maximizes the call center productivity by spreading the work evenly across your call center team, ensuring equal workload for all your agents
* Reduces the clients wait time, which helps reduce queue abandonment.

### Concurrent Chat Limit

To configure the maximum number of chat conversations above which DRUID platform will not automatically connect waiting clients to agents, you should take into consideration the following aspects:

* You have only the generic queue, there are no queues defined. To configure the maximum number of chat conversations above which DRUID platform will not automatically connect waiting clients to agents, go to the AI Agent details, click the Live Chat section header and in the to **Max number of sessions for automatic allocation** field, type the desired value. The default value is 0, which means that automatic allocation is disabled.

![](<../../.gitbook/assets/set limit.png>)

* You have queues defined. In this case, the **Max number of sessions for automatic allocation** settings no longer appears on the AI Agent details page; the **Has automatic allocation** setting appears in the Live Chat section and it is disabled and non-editable.

![](<../../.gitbook/assets/disbled max alloc.png>)

{% hint style="info" %}
**NOTE:** Setting the maximum number of sessions for automatic allocation on a queue level is available in DRUID 5.17 and higher. For backwards compatibility, if you have AI Agents with multiple queues defined and automatic allocation was set on the AI Agent, the **Has automatic allocation** setting displays in the AI Agent details and it is disabled and non-editable. You have to set up the **Max number of sessions for automatic allocation** per queue.
{% endhint %}

Set the **Max number of sessions for automatic allocation** per queue.

![](<../../.gitbook/assets/automatic all on queue level.png>)

After you set the **Max number of sessions for automatic allocation** for a queue / more queues, the **Has automatic allocation** setting in the AI Agent details page is automatically enabled.

![](<../../.gitbook/assets/auto alloc enabled.png>)

If the **Max number of sessions for automatic allocation** is set on queues, DRUID takes into consideration the minimum value of the setting on queue level when automatically allocating clients to agents.

{% hint style="info" %}
**NOTE:** The maximum concurrent chat supported for one agent is 5. You can modify this limit only in external agent pages.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** If **Max number of active sessions** is set on both AI Agent level and queue level, DRUID takes into consideration the minimum value when automatically allocating clients to agents. If an agent is allocated to multiple queues with different maximum active sessions set, DRUID takes into consideration the smallest value of them. E.g., Queue A has the **Max number of active sessions** set to 2 and Queue B has the **Max number of active sessions** set to 3. The **Max number of active sessions** on the AI Agent level is set to 4. If an agent is allocated to both Queue A and Queue 2, the agent will be automatically allocated maximum 2 sessions in parallel for both queues; for Queue B having the possibility to manually take 2 more clients (to reach the maximum number of active sessions set on Queue B).
{% endhint %}

If you want to place live chat calls to a specific waiting queue and automatically allocate clients to agents, you can do so by editing the **live-chat-connect-to-agent** flow. Add an action step and in the Pre / PostActions section, add the internal action **ConnectToHelpdeskAgent**, enter the queue code (not the queue name) and add the following additional parameter: `"AutomaticAllocation" : true` (in JSON format).

For example:

**Example - Automatic allocation to \[\[MyEntity]].CodeOfTheQueue**

```
{
    "QueueCode" : "[[MyEntity]].CodeOfTheQueue",
    "AutomaticAllocation" : true
}
```

![](<../../.gitbook/assets/concurrent limit auto.png>)

{% hint style="info" %}
**NOTE:** For backwards compatibility, you can put clients in a specific waiting queue by specifying the queue code either from a DRUID entity field ( \[\[]].), or a DRUID local variable (@queue\_code) or directly as a string (e.g., "Loans").
{% endhint %}

When transferring clients to another queue, you can automatically allocate clients to agents. To do so, add the following additional parameter to internal action **TransferHelpdeskCall**: `"AutomaticAllocation" : true` (in JSON format)

For example:

**Example - Automatic allocation to \[\[MyEntity]].CodeOfTheQueue**

```
{
    "QueueCode" : "[[MyEntity]].CodeOfTheQueue",
    "AutomaticAllocation" : true
}
```

![](<../../.gitbook/assets/transfer allocation.png>)

{% hint style="info" %}
**NOTE:** For backwards compatibility, you can transfer clients to a queue by specifying the queue code either from a DRUID entity field ( \[\[]].), or a DRUID local variable (@queue\_code) or directly as a string (e.g., "Loans").
{% endhint %}

### Chat Allocation Rules

DRUID will automatically allocate clients entering in a waiting queue to an agent, following these rules:

* Allocate client to an agent who is free (has zero ongoing live conversations).
* If no agent is free, allocate the client to an agent who has not reach out the concurrent chat limit following these criteria:
  * Allocate client to the agent who has the least number of connected clients.
  * Allocate client to an agent based on the time of the last connection with a client in ascending order.
* If all agents are busy (have reach out the concurrent chat limit), during break or have requested a break, the client remains in the waiting queue and will be allocated to the first available agent.

{% hint style="warning" %}
**IMPORTANT!** If there are clients waiting in the queue and the working hours of that queue is reached out (clients waiting in the queue outside working hours), DRUID will stop automatically allocating clients to agents in that queue giving the agents the option to choose if they want to take further live chat calls outside the working hours.
{% endhint %}

{% hint style="info" %}
**NOTE:** For Multichat, DRUID searches available agents defined on the specific queue where the client was initially placed. DRUID will not automatically transfer the client to another queue.
{% endhint %}

![](<../../.gitbook/assets/allocating agents.png>)

For information on how to enable the Break functionality, see [Live Chat With Multiple Queues](<Live Chat Multiple Queues.md>), Step 6.

### Related Topics

* [Automatically Logging Out Helpdesk Agents](<Automatically Logging Out.md>)
* [Live Chat With Multiple Queues](<Live Chat Multiple Queues.md>)
* [Multichat for Helpdesk Agents](<Multichat v2 for Helpdesk.md>)
