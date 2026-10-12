---
title: Customizing Hero Card Buttons for Viber Channel
---


{% hint style="info" %}
**NOTE:** This feature is available in DRUID 5.3 and higher.
{% endhint %}

While Viber provides advanced options for customizing messages and buttons, DRUID provides you with a set of options to customize Hero card buttons.

To customize hero step buttons, go to the desired hero step configuration and click **Metadata** and tap on **Advanced Editing**.

In the JSON field search for "hero" and for each hero card, under the "buttons" array , add the **channelData** property and in it the desired button parameter(s).

{% hint style="info" %}
**Info:** The **channelData** property is automatically generated if you fill-in the **buttonClass** field on the hero card; otherwise, you have to add it in the JSON field.
{% endhint %}

![](<../../../.gitbook/assets/ADVANCED EDITING HERO CARD.png>)

{% hint style="info" %}
**Info:** To easily customize hero card buttons, you might want to copy the code from the JSON field and paste it in Notepad++ or another text file program, customize the buttons there and then copy the code and paste it in DRUID.
{% endhint %}

For each hero card button, you can define the parameters described in the table below.

{% hint style="info" %}
**NOTE:** Set button parameters to static (string) values as setting up parameters to values stored in DRUID entity fields is not working.
{% endhint %}

| Parameter Name | Description                                                                                                                                                                                                                                                                                                                            | Possible values                                                           | Default value              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------- |
| bgColor        | Background color of button                                                                                                                                                                                                                                                                                                             | Valid color HEX value                                                     | Default Viber button color |
| image          | URL of image to place on top of background (if any). Can be a partially transparent image that will allow showing some of the background. Will be placed with aspect to fill logic.                                                                                                                                                    | Valid URL. JPEG and PNG files are supported. Max size: 500 kb             |                            |
| textVAlign     | Vertical alignment of the text                                                                                                                                                                                                                                                                                                         | top, middle, bottom                                                       | middle                     |
| textHAlign     | Horizontal align of the text                                                                                                                                                                                                                                                                                                           | left, center, right                                                       | center                     |
| actionType     | Type of action pressing the button will perform: - **Reply** - will send a reply to the AI Agent. - **open-url** - will open the specified URL and send the URL as reply to the AI Agent. **NOTE:** **location-picker** and **share-phon**e are not supported on desktop, and require adding any text in the **ActionBody** parameter. | reply, open-url, location-picker, share-phone, none                       | reply                      |
| actionBody     | Text for **reply** and **none**. ActionType or URL for **open-url**. This parameter is mandatory.                                                                                                                                                                                                                                      | For ActionType **reply** - text. For ActionType **open-url** - Valid URL. |                            |
| openURLType    | Determine the **open-url** action result, in app or external browser.                                                                                                                                                                                                                                                                  | internal, external                                                        | internal                   |

**Hero cards customization example**

```
{
  "hero": {
    "attachmentLayout": "carousel",
    "pageSize": 10,
    "moreItemsValue": "More Items",
    "noMoreItemsValue": "No More Items",
    "cards": [
      {
        "images": [
          {
            "url": "https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/7642fb7f-8c3b-4423-a3a7-dddb47be03b0/icon-design-22-opt.png"
          }
        ],
        "title": "Title",
        "subtitle": "Subtitle",
        "text": "Description",
        "buttons": [
          {
            "title": "BUTON",
            "type": "imBack",
            "value": "button",
            "channelData": {
              "bgColor": "#FFB90F",
              "image": "https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/cat-icon.png",
              "textVAlign": "top",
              "TextHAlign": "right",
              "actionType": "open-url",
              "actionBody": "https://www.youtube.com/",
              "OpenURLType": "external",
              "rows": "3",
              "columns": "4",
              "buttonClass": "button"
            }
          }
        ]
      }
    ]
  },
```

Save the hero card step and you're done!
