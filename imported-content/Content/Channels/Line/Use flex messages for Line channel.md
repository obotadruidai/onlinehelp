<a id="UsingFlexMessagesforLINEChannel"></a>

# Using Flex Messages for LINE Channel

LINE Chat Bot API allows sending flex message, to provide the user with a set of predefined actions.

In Druid, you can customize Flex messages only in flow steps of type Message. The Flex messages are fully customizable and can be created and designed specifically for the AI Agent needs.

While [LINE documentation](https://developers.viber.com/docs/tools/keyboards/) provides you with detailed information on how to design Flex and also provides you with a simulator to help you customize the messages, this section describes how to customize the flow steps in Druid to send flex messages.

If you have a LINE account, use the [Flex Message Simulator](https://developers.line.biz/flex-simulator/) to customize the layout of your message. After you finish designing the layout of the Flex message, click the **View as JSON** button at the right-top side of the Simulator.

![](../../Resources/Images/Line/view%20json.png)

Copy the JSON content.

**Flex message example from the Flex Message Simulator**

```
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.druidai.com/hubfs/druid-logo-dark.svg",
    "aspectMode": "fit",
    "action": {
      "type": "uri",
      "uri": "https://www.druidai.com/"
    },
    "position": "relative",
    "animated": true,
    "size": "xxl"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "DruidAI Flex Message",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "text",
            "text": "5.0",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "Call",
          "uri": "https://www.druidai.com/druid-<span class="mc-variable General.AI_Agent variable">AI Agent</span>-platform-about-us"
        },
        "color": "#70b244"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "Web site",
          "uri": "https://www.druidai.com/"
        },
        "color": "#808184"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
}
```

> **NOTE:** Set the flex message parameters to static values as setting them up to values stored in Druid entity fields is not working.

In Druid, go to the desired Message flow step and click to configure it. Click the Metadata section and tap on **Advanced Editing**.

In the JSON field add the following object:

**Add the lineFlexMessages object**

```
{
  "lineFlexMessages": {
    "type": "flex",
    "altText": "DruidAI Notification",
    "contents": <the flex message layout goes here>
},
```

In the "contents" property paste the flex message layout, that is the JSON you copied from the Flex Message Simulator.

**Example - Adding flex message layout to Message step**

```
{
  "lineFlexMessages": {
    "type": "flex",
    "altText": "DruidAI Notification",
    "contents": {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://www.druidai.com/hubfs/druid-logo-dark.svg",
        "aspectMode": "fit",
        "action": {
          "type": "uri",
          "uri": "https://www.druidai.com/"
        },
        "position": "relative",
        "animated": true,
        "size": "xxl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "DruidAI Flex Message",
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "margin": "md",
            "contents": [
              {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "sm",
                "color": "#999999",
                "margin": "md",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "height": "sm",
            "action": {
              "type": "uri",
              "label": "Call",
              "uri": "https://www.druidai.com/druid-<span class="mc-variable General.AI_Agent variable">AI Agent</span>-platform-about-us"
            },
            "color": "#70b244"
          },
          {
            "type": "button",
            "style": "primary",
            "height": "sm",
            "action": {
              "type": "uri",
              "label": "Web site",
              "uri": "https://www.druidai.com/"
            },
            "color": "#808184"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "margin": "sm"
          }
        ],
        "flex": 0
      }
    }
  },
  "message": {
    "pageSize": 10
  },
  "choice": {
    "attachmentLayout": "carousel",
    "pageSize": 10,
    "moreItemsValue": "More Items",
    "noMoreItemsValue": "No More Items",
    "options": {
      "actions": [
        {
          "text": "caption",
          "value": "value"
        }
      ]
    }
  },
  "hero": {
    "attachmentLayout": "carousel",
    "pageSize": 10,
    "moreItemsValue": "More Items",
    "noMoreItemsValue": "No More Items",
    "cards": [
      {
        "images": [
          {
            "url": "/assets/common/images/286x180.jpg"
          }
        ],
        "title": "Title",
        "subtitle": "Subtitle",
        "text": "Description",
        "buttons": [
          {
            "title": "",
            "type": "imBack",
            "value": ""
          }
        ]
      }
    ]
  },
  "thumbnail": {
    "attachmentLayout": "carousel",
    "pageSize": 10,
    "moreItemsValue": "More Items",
    "noMoreItemsValue": "No More Items",
    "cards": [
      {
        "images": [
          {
            "url": "/assets/common/images/286x180.jpg"
          }
        ],
        "title": "Title",
        "subtitle": "Subtitle",
        "text": "Description",
        "buttons": [
          {
            "title": "",
            "type": "imBack",
            "value": ""
          }
        ]
      }
    ]
  },
  "uiPath": {
    "technologyId": 0,
    "unattended": {
      "useCurrentUser": true
    },
    "attended": {}
  },
  "adaptiveCard": {
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3"
  },
  "delay": ""
}
```

Save the flow step and you're done!
