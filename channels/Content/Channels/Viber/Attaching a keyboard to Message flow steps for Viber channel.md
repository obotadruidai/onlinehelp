---
title: "Attaching a keyboard to Message Steps for Viber Channel"
---

<a id="AttachingakeyboardtoMessageStepsforViberChannel"></a>


{% hint style="info" %}
**NOTE:** This feature is available in DRUID 5.3 and higher.
{% endhint %}

Viber Chat Bot API allows sending a custom keyboard with each message, to supply the user with a set of predefined replies or actions.

In DRUID, you can only attach keyboards to flow steps of type Message. The keyboards are fully customizable and can be created and designed specifically for the AI Agent needs.

While [Viber documentation](https://developers.viber.com/docs/tools/keyboards/) provides you with detailed information on how to design keyboards and also provides you with extensive keyboard examples, this section describes how to attach a keyboard to a flow step of type Message in DRUID.

First, in Notepad++ or another text file tool, design the keyboard by defining the "keyboard" object.

{% hint style="info" %}
**NOTE:** Set keyboard parameters to static values as setting up keyboard parameters to values stored in DRUID entity fields is not working.
{% endhint %}

**"keyboard" object example**

```
"keyboard": {
    "Type": "keyboard",
    "Buttons": [
      {
        "Columns": 2,
        "Rows": 2,
        "ActionType": "reply",
        "ActionBody": "picture",
        "Text": "first picture",
        "TextVAlign": "bottom",
        "BgMediaType": "gif",
        "BgColor": "#e0e0e0",
        "BgMedia": "https://media.tenor.com/TmNWrln1uJAAAAAC/bongo-cat-cute.gif"
      },
      {
        "Columns": 2,
        "Rows": 2,
        "ActionType": "reply",
        "ActionBody": "cat2",
        "Text": "second picture",
        "BgColor": "#e0e0e0",
        "Image": "https://loremflickr.com/100/100"
      },
      {
        "Columns": 2,
        "Rows": 2,
        "ActionType": "reply",
        "ActionBody": "image",
        "Text": "third picture",
        "BgColor": "#e0e0e0",
        "Image": "https://cdn.wallpaperhub.app/cloudcache/b/d/7/6/4/b/bd764bb25d49a05105060185774ba14cd2c846f7.jpg"
      }
    ]
  },
```

In DRUID, go to the desired Message flow step and click to configure it. Click the Metadata section and tap on **Advanced Editing**.

In the JSON field paste the "Keyboard" object you defined previously.

**Attach keyboard to Message step example**

```
  "keyboard": {
    "Type": "keyboard",
    "Buttons": [
      {
        "Columns": 2,
        "Rows": 2,
        "ActionType": "reply",
        "ActionBody": "picture",
        "Text": "first picture",
        "TextVAlign": "bottom",
        "BgMediaType": "gif",
        "BgColor": "#e0e0e0",
        "BgMedia": "https://media.tenor.com/TmNWrln1uJAAAAAC/bongo-cat-cute.gif"
      },
      {
        "Columns": 2,
        "Rows": 2,
        "ActionType": "reply",
        "ActionBody": "cat2",
        "Text": "second picture",
        "BgColor": "#e0e0e0",
        "Image": "https://loremflickr.com/100/100"
      },
      {
        "Columns": 2,
        "Rows": 2,
        "ActionType": "reply",
        "ActionBody": "image",
        "Text": "third picture",
        "BgColor": "#e0e0e0",
        "Image": "https://cdn.wallpaperhub.app/cloudcache/b/d/7/6/4/b/bd764bb25d49a05105060185774ba14cd2c846f7.jpg"
      }
    ]
  },
  "message": {
    "pageSize": 10
  },
```

Save the flow step and you're done!
