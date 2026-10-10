---
title: DRUID 8.1
---

# DRUID 8.1

Deployment Dates

The table below lists the deployment date of DRUID v8.1 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| October 10, 2024                                     | October 24, 2024                       | October 24, 2024                             | October 24, 2024                                    |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

* Custom Code improvements

### Improvements

* **Knowledge Base improvements**: This release introduces various improvements to the KB:
* **SharePoint Online data sources**: The crawler now identifies subsites and displays them as folders in the data source tree explorer.
* **Search feature**: With this release, you get efficient navigation and quick access to the information you need. You can perform exact match searches within a data source or across the entire Knowledge base. The search results will return all data source elements (node, leaf) and articles that exactly match your specified keywords.

When searching for specific keywords at the KB level, a maximum of 30 matching records (if available) will be displayed under the corresponding data source name.

![](<../../../.gitbook/assets/kb search (1).png>)

Similarly, when searching at the data source level, up to 30 results will be shown if they exist.

![](<../../../.gitbook/assets/saerch in DS.png>)

* **Website data sources - show error message for uncrawled links**: Website data sources now display error messages for uncrawled links, helping you quickly identify the reasons specific links were not crawled and are missing from the data source. To understand why specific links were not crawled, in the data source tree explorer, click the **Action**s icon, select **Page Info**, and then navigate to the **Extracted links** tab.

![](<../../../.gitbook/assets/page info (1).png>)

![](<../../../.gitbook/assets/error links (1).png>)

* **Live Chat - Send Timeout Warning to Agent**: You can now configure the system to send the **ConversationIdleWarningMessage** to agents when a live chat conversation becomes idle. The warning is triggered halfway through the configured **Live chat conversation idle timeout mins**, helping agents stay informed about inactive conversations.

![](<../../../.gitbook/assets/send agent warning.png>)

* **Reviewing and Validating LLM Responses – Store Timestamps in Conversation Context**: The \[\[HelpdeskClient]] system entity has been enhanced with new fields that capture timestamps for specific actions taken by agents while reviewing LLM responses. This improvement provides better tracking and auditing of agent interactions during the review process.

![](<../../../.gitbook/assets/helpdesk client timestamps.png>)

For more information on the new fields, see [Reviewing and Validating LLM Responses](<../../Live Chat/LLM Response Validation.md>).

* **Custom Code improvements**. This release introduces two improvements:
* **Parse XML to DRUID entity fields**: Introduced the ParseXMLToEntityFields feature, which allows parsing an XML array into a DRUID entity list. This enhancement simplifies the process of mapping XML data, such as currency rates, to entity fields using custom mappings, providing more flexibility and efficiency in handling XML-based datasets.
* **Add Delay with Wait() Method**: Introduced the `Wait()` method, allowing you to delay task execution by specifying a wait time in milliseconds, up to a maximum of 5000 ms (5 seconds). This method can be called up to 3 times per task, giving you greater control over the timing of integration tasks.

For more information, see [Custom Code](<../../7_Integrations/Custom Code.md>).

* **Document Builder**: With this release, you can now use the **Excel generator** integration task to create CSV files based on XLSX document templates.

![](<../../../.gitbook/assets/generate csv.png>)

* **Adaptive Cards**: Updated the system to support Adaptive Card 1.5, providing enhanced card design features and richer interactivity for improved user experiences.
* **DRUID Vision – Skip specific validations**: Introduced the ability to skip specific validation checks when extracting data from documents if extraction fails due to poor image quality. You can configure this per document type using the **skipValidations** request parameter.

Example: _Skipping validation checks for Romanian Identity Cards OCR_

![](<../../../.gitbook/assets/roid card valid.png>)

For more details, refer to the help section related to each document type, [DRUID Vision](<../../Druid AI Services/Druid Vision.md>).
