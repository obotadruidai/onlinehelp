---
layout:
  title:
    visible: false
---

<a id="LanguageDetectionFlow"></a>

# Language Detection Flow

DRUID is capable of detecting any language change in the conversation prior triggering the **Intent not found** flow, covering the cases when the user types something in another language than the default language of the AI Agent. It does not include the cases when the user changes the conversation language using the snippet's Language option.

> **NOTE:** The user can change the current language in conversation in either the idle state, or inside a flow. In the second situation, the current flow gets canceled.

The Language Detection flow enables authors to address situations when DRUID detects a language change in the conversation.

<a id="LanguageDetectionFlowSolutionTemplate"></a>

## Language Detection Flow - Solution Template

To simply flow authoring when authors want to handle the situations when language change is detected within the conversation, DRUID provides you with a built-in solution template, **Language detection flow**, which addresses extensive use cases for language detection.

Go to the Solutions Library, search for the **Language detection flow** solution template, import it and enable language detection on the AI Agent, following the instructions described in [Enabling language detection on the AI Agent](#Enabling_language_detection_on_the_bot).

You can update the **Language detection flow** solution template or you can define your own flow for handling the cases when language change is detected in the conversation.

<a id="HowtheLanguagechangeflowisworking"></a>

### How the Language change flow is working

For each processing of a user says (not only for intent recognition, but also for input mapping), first the origin from where the language change is triggered is checked.

If condition **[[ChatUser]].DetectedLanguage == null** is met, then the user has changed the language from the chat snippet Language option. The AI Agent will continue the conversation in the new language (the Language Changed flow is not triggered).

![](../Resources/Images/Flows/language%20detection%20_%20lang%20from%20snippet.png)

If the user did not change the language from the chat snippet, then **automatic-language-detection** flow step will be executed.

If condition **![[ChatUser]].DetectedLanguage.IsAvailable** is met (that is, the detected language is not defined on the AI Agent), the AI Agent realizes that the user is typing in another language, captures this language in **[[ChatUser]].DetectedLanguage.FriendlyName** and tells the user that it doesn’t know that particular language, but to choose from one of the languages it knows, by presenting a hero card with all the available languages on the AI Agent.

![](../Resources/Images/Flows/hero%20step%20language%20change.png)

##### Example – AI Agent trained in Romanian and other languages, but NOT English

**Conversation Language**: Romanian

User types something in English

**AI Agent**: Observ că ai scris în limba Engleză. Din păcate nu cunosc această limbă în prezent. Pentru a continua, te rog să scrii ceea ce dorești în limba Română, sau alternativ, îmi poți scrie în… limba 1, limba 2 și limba 3.

The user receives a hero card with the languages available on the AI Agent.

User chooses language.

The AI Agent continues the conversation in the language chosen by the user and sets **[[ChatUser]].Language = [[ChatUser]].DetectedLanguage.Code**.

If the AI Agent realizes that the user is typing in another language, captures this language in **[[ChatUser]].DetectedLanguage.FriendlyName** and asks the user if he wants to continue in that language by either using an entity with a Boolean field or a local variable @yesno.

![](../Resources/Images/Flows/choose%20yes.png)

##### Example – AI Agent trained in Romanian and English

**Conversation Language**: Romanian

User types something in English

**AI Agent**: Observ că ai scris în limba Engleză. Dorești să continuam în această limbă?

**User**: yes/da

**AI Agent**: Sure, what can I do for you? (enters idle mode)

**User**: no/nu

If the user does not accept to change the language into the language detected by the model, then the user will not be prompted anymore for the following 15 minutes for that language. The user will, however, be asked if he/she wants to change into other languages, if detected by the model.

<a id="EnablinglanguagedetectionontheAIAgent"></a>

## <a id="Enabling_language_detection_on_the_bot"></a>Enabling language detection on the AI Agent

To enable language detection, on the AI Agent Details make the following settings:

1. Click the **Dialogue management** section header and select the **Language Changed flow** to be triggered when language change is detected in the conversation.
   If you imported the **Language detection flow** solution template, from the **Language Changed flow** field, select **Language change**.
2. Tap on **Language detection**. The **Threshold** field becomes editable.
3. In the **Threshold** field, enter a value (we recommend setting the threshold to 90). Whenever the threshold is reached, the selected **Language Changed Flow** will be triggered.
> **NOTE:** Only the texts that are detected in another language with a probability higher than the threshold will be taken into consideration.

![](../Resources/Images/Bot%20Advanced%20Settings/detect%20language.png)

4. Save the AI Agent.

> **IMPORTANT!**
> The Language Detected flow is triggered only if the following conditions are met simultaneously:
>
> - **[[ChatUser]].DetectedLanguage** is different than the **[[ChatUser]].Language**.
> - **[[ChatUser]].DetectedLanguage.Score** is higher than the value of the **NLP.Language.Detection.Threshold** parameter.
> - The last language change detection was more than 15 minutes ago. The last language change detection for the same new language identified, was more than 15 mins ago (E.g., the current language is German and AI Agent detects English; the user doesn’t want to switch to English because he/she only used a universal word like “laptop” or “mouse”; therefore, next time the AI Agent will identify a language change intent to English and current language is still German, it will not trigger the Language Changed special flow again).

<a id="DebuggingwhytheLanguagechangedflowwasnottriggered"></a>

## Debugging why the **Language changed flow** was not triggered

In DRUID 5.11 and higher you can test user says to see the **Predicted language** and the **Confidence** (the score of the predicted language). This is particularly useful for debugging purposes to check why language detection was not done on user says or why the **Language changed flow** was not triggered.

If the **Confidence** of the predicted language is below the language detection threshold (which by default is 90), the **Language Changed Flow** will not be triggered.

![](../Resources/Images/druid%205.11/test%20predict%20language.png)

## Related Topics

- [Configuring AI Agent Advanced Settings](../2_AI%20Agents/Configuring%20AI%20Agent%20Advanced%20Settings.md)
