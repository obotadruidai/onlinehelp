<a id="DRUID712"></a>

# DRUID 7.12

Deployment Dates

The table below lists the deployment date of DRUID v7.12 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| July 04, 2024 | August 01, 2024 | August 01, 2024 | August 01, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="Improvements"></a>

## Improvements

- **Clone integrations**: You can now clone an integration directly from the Connector Diagram > integration > Info. This feature streamlines the authoring experience, eliminating the need to switch to the Connector list view to clone an integration.

![](../../Resources/Images/druid%207.12/clone%20integation.png)

- **REST Apps - Added support for SAML Assertion Authentication**. With this release, you can now integrate with REST APIs that require SAML assertion authentication.

![](../../Resources/Images/druid%207.12/security%20type.png)

For more information, see [SAML Assertion Authentication](../../7_Integrations/REST/SAML%20Assertion%20Authentication.md).

<a id="BugFixes"></a>

## Bug Fixes

- The GetIntentMatching internal action now recognizes the LanguageCode parameter.
- CNN tasks now include the missing parameter value from the request.
- The Help links on the AI Agent Summary page now redirect correctly.
- The 'Filter by' field in Webviews > Charts now resets properly when adding a new chart.

<a id="KnownIssueTeamsChannelIntegration"></a>

## Known Issue: Teams Channel Integration

The latest Teams mobile app update causes hero cards to not render properly.

**Workaround**

To view hero cards correctly, rotate your mobile device to a horizontal orientation.

**Status**

We will update you once Microsoft releases a new version of the Teams mobile app that resolves this issue.
