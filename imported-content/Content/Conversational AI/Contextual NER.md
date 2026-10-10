---
title: "Contextual NER"
---

<a id="ContextualNER"></a>


The Druid AI Platform allows authors to configure AI Agents so that they also perform entity recognition by taking into consideration a specific context.

Contextual NER means that the value found in the indexed train set also needs to be part of a certain context (an entity list).

{% hint style="info" %}
**NOTE:** Contextual NER is available only for non-deterministic entity recognition.
{% endhint %}

<a id="Example"></a>

### Example:

Let’s assume that we need to extract the cities from a specific country. For example, Melbourne exists both in Australia and in USA (Florida). If we have defined a trained entity (AI Agent entity) with all cities in the world, asking for Melbourne in an intent will return 2 values: the one in Australia and the one in USA.

If we prepare a second entity list (e.g., using a connector action,) with cities from USA only, then we can use that list to further filter the values from the main indexed entity, directly at extraction / input mapping stage.

In the example below, the [[City]] entity is the indexed entity with all the cities in the world. We want to capture the destination city for a client’s holiday in **[[Holiday]].City** (field of type Entity, referred to [[City]]), in the Input mapping of a Prompt flow step).

From the previous flow steps, we already know that our client wants to visit the USA, so we used a connector action to load all cities in USA in [**[Country]].Cities** (a field of type Entity List field, referred to [[City]] as well).

By mentioning **[[Country]].Cities** in the **Contextual NER** field of the same prompt step, then all values extracted with NER from the [[City]] index will be further filtered with values from [[Country]].Cities, and then set in **[[Holiday]].City**.

![](../Resources/Images/NLU/contextual%20NER.png)

In our example, as Melbourne has two records in the main indexed entity ([[City]]), the two values will not be shown to users. The values will be instead, it will be filtered by [[Country]].Cities where there is only one record for Melbourne, and therefore, Melbourne from the USA will be set in [[Holiday]].City.

{% hint style="info" %}
**NOTE:**

- Contextual NER can be used either in an Input mapping field (within a flow), or directly from the intent (when setting up a flow utterance). In the second case, the value(s) extracted from the intent will be filtered with the list set in the first flow step where that entity is set in the Input mapping and **Contextual NER** is activated.
- The entities mentioned in the Input Mapping and Contextual NER fields MUST refer the same base entity. In the example above, both [[Holiday]].City and [[County]].Cities refer to the [[City]] entity.
- Intersection of the two collections is performed on all common fields which are not null. [[City]] can be trained as indexed entity with values in the [[City]].Name, [[City]].Country and [[City]].State fields, whereas [[Country]].Cities can only have values in the State field ([[Country]].Cities.State). Therefore, the filtering will be performed only on values from the State field of each entity.
{% endhint %}

## Related Topics

- [Named Entity Recognition (NER)](Named%20Entity%20Recognition%20NER.md)
- [Using NER with Index Entities (DRUID versions prior to 5.15)](Using%20NER%20with%20Index%20Entities%20%28DRUID%20versions%20prior%20to%205.15%29.md)
- [Using NER with Intent Recognition](Using%20NER%20with%20Intent%20Recognition.md)
