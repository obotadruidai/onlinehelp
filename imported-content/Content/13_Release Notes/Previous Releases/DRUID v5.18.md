---
title: "DRUID 5.18"
---

<a id="DRUID518"></a>


Deployment Dates

The table below lists the deployment date of DRUID v5.18 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| July 06, 2023 | August 03, 2023 (part of 5.19) | August 03, 2023 (part of 5.19) | August 03, 2023 (part of 5.19) |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host to the latest version:

- BluePrism Connector.

<a id="WhatsNew"></a>

## What's New

- **Megabots**. With this release you can leverage the multi-AI Agent architecture to easily add more AI Agent skills and expand the range of use cases to address multiple business purposes. The megabots provide you with the following benefits:

- Unified user experience
- Better authoring governance
- Higher efficiency and streamlined authoring experience
- AI Agent content segregation based on role based access
- Higher AI performance.

![](../../Resources/Images/druid%205.18/megabot.png)

> **NOTE:** Megabots is a tenant feature available in DRUID 5.18 and higher. If you want to activate it on your tenant, get in touch with [DRUID Support](<mailto:support@druidai.com?subject=Activate Megabots on my tenant>).

For more information, see [Megabots](../../AI%20Agent%20Orhestration/Druid%20Conductor.md).

- **BluePrism Connector**. You can now integrate AI Agents with RPA from BluePrism to streamline the customer and employee experience and help them fulfill their needs across the entire journey.  For more information about the integration, see [BluePrism Connector](../../7_Integrations/BluePrism/BluePrism%20Connector.md).

<a id="Improvements"></a>

## Improvements

- **Extended the AI Agent languages set** to include those covered by the selected NLP provider.
- **Difference allowed in file extension vs file signature for pictures only**. For mobile channels (e.g., MS Teams on mobile), when uploading an image in the chat, the image extension is automatically changed to .png. DRUID's antimalware check allows a mismatch between the file extension .png and the following file signatures: jpg, png, jpeg, tif, tiff and bmp.
- **Intent rephrase flow**. With this release, you can define a flow to rephrase / improve user intent by using an external service (e.g., GPT) to a user intent that is optimal for your AI Agent model. On the AI Agent details page, click the **Dialogue management** section and from the Intent rephrase flow drop-down, select the flow you designed for intent rephrasing.

![](../../Resources/Images/druid%205.18/REPHRASE%20FLOW.png)

After the user sends the intent, the AI Agent first executes the "Intent rephrase flow" that rephrases the utterance and then the AI Agent uses the result (the rephrased intent stored in [[Intent]].Text) to predict in the model.

> **IMPORTANT!** The "Intent rephrase flow" is executed only when the user input is sent while the conversation is in idle mode. Once in a flow, the flow no longer executes (the user intent is not altered).

- **Knowledge Base - unstructured data source logs**. With this release, you can see the status of the crawled URLs within an unstructured data source by opening the data source and clicking the **Logs** tab.

![](../../Resources/Images/druid%205.18/crawling%20logs.png)

- **Knowledge Base - add new articles to structured data sources**. You can now manually add articles to structured data sources by clicking the **Add new** button, providing the questions and answer pair and clicking **Save**.

![](../../Resources/Images/druid%205.18/new%20article.png)

> **NOTE:**  After manually adding articles to structured data sources, you need to train the Knowledge Base.

- **NLU.NER.EntityIndex.RescaleProbs**. An experimental entity parameter that you can set to **true** to increase the extraction score which ensures that NER identifies more entity candidates.

For more information, see [Entity NER specific Parameters](../../Conversational%20AI/Entity%20NER%20specific%20Parameters.md).

<a id="BugFixes"></a>

## Bug Fixes

- When restoring a solution snapshot no longer erases everything from additional languages if the snapshot was made on a solution that contains flows flow with data for the additional languages (e.g. message, conditions, variables, description, utterances).
- ML no longer brings dates from the past. “I want holiday until Sunday” sets in the conversation context the date of the last Sunday.
- Importing solutions with OAuth configurations actions no longer keeps the API URL from the source in the OAuth actions.
- In the Conversation History, authors can now copy text from the "Message" column in the Conversation transcript.

![](../../Resources/Images/druid%205.18/copy%20text.png)
