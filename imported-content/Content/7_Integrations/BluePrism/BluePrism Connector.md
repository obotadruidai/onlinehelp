---
title: BluePrism Connector
---

# BluePrism Connector

{% hint style="info" %}
**NOTE:** The Blue Prism Connector is available in DRUID 1.58 and higher.
{% endhint %}

DRUID provides you with the full power of native Robotic Process Automation (RPA) integration, enabling you to automate complicated, end-to-end procedures. Integrating with RPA from BluePrism you can streamline the customer and employee experience and help them fulfill their needs across the entire journey.

In Blue Prism the workqueue is the central hub of all automations.

### How it works

In BluePrism the RabbitMQ queue is the central hub of all automations.

![](<../../../.gitbook/assets/diagram (3).png>)

1. DRUID sends items to RabbitMQ queue.
2. RabbitMQ direct exchange delivers messages to queues based on the message routing key. A queue binds to the exchange with a specific routing key.
3. The trigger configured on the RabbitMQ queue automatically starts the BluePrism process.
4. The BluePrism process automatically calls back DRUID and sends the output.
