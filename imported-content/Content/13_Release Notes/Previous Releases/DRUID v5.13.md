<a id="DRUID513"></a>

# DRUID 5.13

Deployment Dates

The table below lists the deployment date of DRUID v5.13 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| April 27, 2023 | May 11, 2023 | May 11, 2023 | May 11, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="Improvements"></a>

## Improvements

- **Voice Audio Codes channel**. Activating the VoiceAudio Codes channel has been improved to provide chat users with a flawless conversation. When mapping the language codes used by the Speech-To-Text (STT) service provider and DRUID-specific language codes, you have to provide the Text-to-speech voice DRUID will be using.

Use the following format for the language codes mapping:

"<STT Provider language code/locale>": "<DRUID-specific language code>|<Text-to-speech voice>"

For example:

```
{
  "ro-RO": "ro|ro-RO-AlinaNeural",
  "en-US": "en-US|en-US-AshleyNeural",
  "th-TH": "th-TH|th-TH-AcharaNeural"
}
```

A hotfix has been deployed to also include this improvement in DRUID 5.12.

- Other features are in technological preview and will be presented in future DRUID versions.

<a id="BugFixes"></a>

## Bug Fixes

- Modifications on elements inside the flows, integrations, entities, etc. (like flow steps, connector tasks, entity fields) will now update the last modification status on the parent element.
