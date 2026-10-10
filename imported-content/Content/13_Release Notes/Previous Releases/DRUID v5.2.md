---
layout:
  title:
    visible: false
---

<a id="DRUID52"></a>

# DRUID 5.2

Deployment Dates

The table below lists the deployment date of DRUID v5.2 across Druid Clouds. To view the Druid Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| November 24, 2022 | January 05, 2023 | January 05, 2023 | January 05, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Technological preview**: A new app, **Oauth2** and two flow steps, **Oauth 2.0 Sign in** and **Oauth 2.0 Sign out** and are now available to provide authors with the option to authenticate users during chat conversations using the OAuth 2.0 protocol.

Documentation will be available in DRUID 5.3.

- A new entity NER-specific parameter, **NLU.NER.EntityIndex.AlternativeCalculationForProbability** provides an alternative method for computing the probability of an entity, which favors exact matches within the index. For information about entity parameters that you can set for NER, see [Entity NER specific Parameters](../../Conversational%20AI/Entity%20NER%20specific%20Parameters.md).

<a id="BugFixes"></a>

## Bug Fixes

- Improved behavior for snippet on unpublished AI Agents.
- Detection fields improvements in the Romanian Car Registration Certificates OCR (NrInmatriculare, confusing 0 with O, NumeProprietar).
