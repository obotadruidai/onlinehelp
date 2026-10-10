---
title: "Manipulating NER Candidates"
---

<a id="ManipulatingNERCandidates"></a>


You can manipulate entity candidates seamlessly, facilitating external database searches, and tailored flow authoring to meet specific contextual needs.

{% hint style="info" %}
**NOTE:** This feature is available in DRUID version 7.4 and higher.
{% endhint %}

The Flow Engine identifies all candidates from an utterance and stores information for each candidate in a dedicated system entity as follows:

- **[[Intent]].Entities[0].Text**: Stores the value of the candidate (the word identified as a candidate).
- **[[Intent]].Entities[0].Name**: Stores the name of the entity for the identified candidate value.

For example, from the training phrase: "What computer science Entity classes do you have in London Entity?" the Flow Engine identifies two possible candidates and stores their values as follows:

- [[Intent]].Entities[0].Text: "computer science"
- [[Intent]].Entities[0].Name: "CourseTopic"
- [[Intent]].Entities[1].Text: "London"
- [[Intent]].Entities[1].Name: "Location"

Where "CourseTopic" and "Location"are umbrella entities.

To determine the number of candidates found by the Flow Engine, use **[[Intent]].Entities.Count()**. Additionally, for each candidate, perform an extended NER using the internal action **LookupEntity** with the following parameters:

```
{
    “Index”: “<the value stored in [[Intent]].Entities[0].Name>”,
    “Value”: “[[Intent]].Entities[0].Text”,
    “MinScoreThreshold”: <integer>
}
```

For example:

```
{
    “Index”: “CourseTopic”,
    “Value”: “[[Intent]].Entities[0].Text”,
    “MinScoreThreshold”: 40
}
```

Based on your requirements, you can customize the flow by either adding an integration to search candidates in an external database, adding them to an external index or informing the user if it does not exist (if [[Intent]].Entities[0].Text==0).
