<a id="TestingSettings"></a>

# Testing Settings

The Druid AI Platform provides the possibility to test the configurations of the REST Task directly from authoring portal (without the need to place your newly created connector action in a flow and test it within a chat conversation).

To test a request, click the **Test** tab. Click the **RequestEntity** tab. The JSON field contains by default the name of the entity the AI Agent uses to send data to the REST app via the current action.

For example:

![](../../Resources/Images/Integrations/esign%20test%20request%20entity.png)

In case you need to map data from the **[[ChatUser]]** entity, as well, click the **ChatUser** tab and in the JSON field, replace the values of the chat user details:

![](../../Resources/Images/Integrations/esign%20send%20envelope%20chatuser.png)

**Replace the values of the chat user details**

```
{
  "$entityTypeName$": "ChatUser",
  "Id": "00000000-0000-0000-0000-000000000000",
  "TenantId": 0,
  "TenantUserId": "00000000-0000-0000-0000-000000000000",
  "IsAnonymous": false,
  "IsAuthenticated": false,
  "BotId": "00000000-0000-0000-0000-000000000000",
  "IsConnectedAsHelpdeskAgent": false,
  "IsAwaitingHelpdeskAgent": false,
  "IsConnectedToHelpdeskAgent": false,
  "ConversationStatus": "None",
  "LanguageChangedSuccess": false,
  "WasAuthenticated": false,
  "ClientTimeStamp": "0001-01-01T00:00:00Z",
  "ServerTimeStamp": "0001-01-01T00:00:00Z",
  "IsCommandChannel": false,
  "IsVoiceChannel": false,
  "ReturningFromFacebookHandover": false
}
```

At the top-right corner of the page, click the **Test** button (![](../../Resources/Images/Integrations/test%20button.png)).

For REST connectors with custom authentication, after running a test, two test results sections are available: one for the authentication connector action that is run first and gets the authentication token and the other one for the main connector action that you test.

![](../../Resources/Images/Integrations/rest%20test%20results.jpg)

If the test is successful, you can save the action.

If the test fails, you can navigate through the **Test Result** tabs to troubleshoot misconfiguration.

## Related Topics

- [REST request settings](Request%20Settings.md)
- [REST Response General Settings](Response%20Settings.md)
