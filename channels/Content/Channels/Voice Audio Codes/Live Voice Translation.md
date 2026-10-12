---
title: Live Voice Translation
---


Live Voice Translation, powered by AudioCodes Live Hub, enables real-time, bidirectional voice translation for your AI Agent. This feature allows your AI Agent to communicate seamlessly with users in multiple languages by automatically translating spoken conversations.

To activate and configure live voice translation, follow these steps:

1. Log into [AudioCodes LiveHub](https://livehub.audiocodes.io/).
2. In the main menu, click on **Hub+** menu and select **Voice translation**.

![](<../../../.gitbook/assets/voice translation menu.png>)

3. Click the **Add new voice translation** button to configure automatic voice translation.

![](<../../../.gitbook/assets/add translation.png>)

4. Enter the AI Agent name and from the **Region** drop-down, select the region associated with the AI Agent.
5. Select **Dynamic activation**. For more information on dynamic translation, see the [AudioCodes Live Hub documentation](https://techdocs.audiocodes.com/livehub/#LiveHub/Configure-dynamic-translation.htm?TocPath=Real-Time%2520voice%2520translation%257CCreate%2520a%2520new%2520voice%2520translation%257C_____2).

![](<../../../.gitbook/assets/dynamic activation.png>)

6. Click **Next**.
7. Add desired Languages and the activation triggers for each language pair. This defines which languages will be translated and under what conditions the translation will be activated.

![](<../../../.gitbook/assets/add languages.png>)

8. Click **Next**.
9. Adjust the original message volume and set the initiation message. This allows you to control the volume of the untranslated audio and set a message to be played when translation begins.

![](<../../../.gitbook/assets/message activation.png>)

10. Click **Create**. Now you need to enable voice translation for an inbound routing rule.
11. In the main menu, click **Routing**.
12. Search for the desired routing rule and click **Edit**.

![](<../../../.gitbook/assets/edit tule.png>)

13. Tap on **Voice translation** and select the newly created voice translation. This links your voice translation configuration to this specific inbound call route.

![](../../../.gitbook/assets/enable.png)

{% hint style="info" %}
**NOTE:** Following the Live Hub 2.19 upgrade, Voice Translation behavior after a call transfer is no longer carried over automatically from the initial call routing rule. The default setting is now disabled. If you want Voice Translation services to continue functioning after a call transfer, you must explicitly configure it on the relevant Transfer routing rule within the AudioCodes Live Hub.
{% endhint %}

14. Click **Update**.
15. In Druid, make sure you have configured the same voice codes on your Voice AudioCodes channel as you have set them within AudioCodes Live Hub (at [step 7](<Live Voice Translation.md#Step7>)). This ensures proper translation between Druid and AudioCodes.

![](../../../.gitbook/assets/languagemap.png)
