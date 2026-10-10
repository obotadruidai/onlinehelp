---
layout:
  title:
    visible: false
---

<a id="DRUID710"></a>

# DRUID 7.10

Deployment Dates

The table below lists the deployment date of DRUID v7.10 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| June 06, 2024 | July 04, 2024 | July 04, 2024 | July 04, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="Improvements"></a>

## Improvements

- **Knowledge Base improvements**. This release introduces various improvements to the Knowledge Base:

- **Unstructured data sources: Enhanced prediction capabilities for the KB Engine**. This release introduces a new parameter in the Knowledge Base advanced settings, "trainableColumns", leveraging comprehensive article information to improve the accuracy and relevance of predictions. This parameter allows you to specify which parts of an article — question / title / short description and / or answer — the KB Engine should use during prediction. To fully leverage this feature, review and transform unstructured data into a question-and-answer format.
> **NOTE:**  For new AI Agents created in DRUID 7.10, the engine will predict against both the question and answer by default. For existing AI Agents, the engine will only predict against the answer ("trainableColumns": null) until you update the setting.

![](../../Resources/Images/druid%207.10/edit%20article.png)

![](../../Resources/Images/druid%207.10/trainable%20columns.png)

- **Unstructured data sources: improved user experience and bulk actions**. This release enhances the user experience for unstructured data sources by streamlining data source management based on type and status. You can now perform bulk actions tailored to the data source type and status, making management more efficient. For more information, see [Data Source Status and Bulk Actions](../../Knowledgebase/Data%20source%20status.md).
- You can now access the extraction order of articles in a data source within the Flow Engine. The order number is stored in **[[Intent]].KBQnAItems[i].OrderNumber**. This feature allows you to manipulate the articles provided to GPT.
- **Safeguard for Large Language Model (LLM) usage**. A new parameter is now available in the KB Advanced settings area, **maxTokensPerSessionLimit** that serves as a safeguard for LLM usage, defining the maximum number of tokens to be utilized per extraction session (i.e., for each extraction action).

![](../../Resources/Images/druid%207.10/limit%20chunking.png)

> **NOTE:** For new AI Agents, the default value is set at 400,000. However, for AI Agents created in previous DRUID versions, the parameter defaults to null. To efficiently manage high volumes of data extraction, we recommend configuring this parameter accordingly.

- **Actions icon in the tree explorer**.The actions icon is now available in the tree explorer when you hover your mouse over an element.

![](../../Resources/Images/druid%207.10/action%20in%20explorer.png)

- **Start DRUID Conversations via API improvement**. A new optional parameter is available in the request body of the StartFlow API that allows you to set the initial language for a conversation when starting a flow. It ensures that the conversation context is properly initialized with the desired language.
> **NOTE:** If the language is not one of the AI Agent languages, the language code is incorrect, or not specified, the conversation will begin in the language the user used to interact with the AI Agent on that channel.

For more information, see [Start DRUID Conversations via API](../../How%20to/Start%20Druid%20conversations%20by%20API.md).

- **Druid Conductor: NLU Testing Improvement**. Testing user inputs in the **NLU** > **Configurations** > **Intents** > **Thresholds and parameters** area on a Druid Conductor now also returns results from child AI Agents.

![](../../Resources/Images/druid%207.10/test%20nlu%20megabot.png)

- **AI Agent settings update**. Conversational AI settings have been removed from the AI Agent settings.

![](../../Resources/Images/druid%207.10/previous%20version.png)

These settings are now only available in **NLU** > **Configurations**. For more information, see [Setting Up the AI Agent Conversational AI](../../Conversational%20AI/Setting%20Up%20the%20Conversational%20AI.md).

- **Custom Code: CryptoJS Library Improvement**. The CryptoJS library now supports the HMAC SHA1 encryption algorithm.

**Example: HMAC SHA1 algorithm**

```
(function main(){

var message = "Hello, World!";
var key = "secretkey";
var hash = CryptoJS.HmacSHA1(message, key);

var hashString = hash.toString(CryptoJS.enc.Hex);

Context.LogRequestTask(hashString);
})()
```

- **Connector Diagram improvement**. The Connector Diagram now displays the integration task type on the left. This enhancement makes it easier to identify and manage different integration tasks at a glance.

![](../../Resources/Images/druid%207.10/cnn%20diagram.png)

- **Custom dashboards: filtering data in dynamic charts**: You can now filter data in dynamic charts on the custom dashboards by selecting **Filter By** in the chart configuration.  For more information, see [Custom dashboards](../../Data%20Analytics%20%26%20Insights/Track%20Business%20KPIs.md).

![](../../Resources/Images/druid%207.10/filter%20by.png)

![](../../Resources/Images/Custom%20Dashboards/Filtering%20table%20records%20on_1.png)

![](../../Resources/Images/Custom%20Dashboards/Custom%20Dashboards_10.png)
