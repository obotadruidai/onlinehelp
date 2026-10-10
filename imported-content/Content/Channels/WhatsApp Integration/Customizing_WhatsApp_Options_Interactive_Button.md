---
title: "Customizing the WhatsApp \"Options\" Interactive Button"
---

<a id="CustomizingtheWhatsAppOptionsInteractiveButton"></a>


For hero, choice and thumbnail steps, in DRUID 5.5 and higher you can customize the label of the **Options** button shown in WhatsApp. To do so, on the flow step, in the Metadata section, tap on **AdvancedEditing** and in the code editor and under your specific step type object, add the following object:

**"Custom button text" - example**

```
  "channelData": {
    "whatsappOptionsButtonName": "custom button text"
  },
```

> **Info:** Replace "custom button text" with the desired text to be shown on the button (put the text between " ").

> **NOTE:** The character limit for each button text is **20** for choice steps and **24** for hero and thumbnail steps.

![](../../Resources/Images/WhatsAppMeta/advanced%20editing.png)
