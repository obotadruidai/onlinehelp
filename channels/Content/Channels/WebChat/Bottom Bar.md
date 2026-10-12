---
title: Bottom Bar
---


![](<../../../.gitbook/assets/bottom bar.png>)

{% hint style="info" %}
**NOTE:** In the HTML template below, make sure that your replace the following: , and .
{% endhint %}

**HTML Template**

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Your website html</title>
        <!-- Include the css file   -->
        <link defer href="<your Druid tenant>/Druid_webchat.css" rel="stylesheet">
    </head>
    <body>
        <!-- Include the script file   -->
        <script defer type="text/javascript" src="<your Druid tenant>/Druid_webchat.js"></script>
     <!-- Init the webchat component on document load -->
              <script type="text/javascript">
                 document.addEventListener("DOMContentLoaded", function(event) {
                    DruidWebchat.init({
                       <!-- Common settings  -->
                       botId: "<your <span class="mc-variable General.AI_Agent variable">AI Agent</span> id>",
                       baseUrl: "<your <span class="mc-variable General.AI_Agent variable">AI Agent</span>'s base URL>",
                       UI: {
                          containerElement: null, // [MANDATORY] example: document.getElementById('DruidContainerElement') -> specify the webchat expand DOM element
                       }
                    });
                 });
               </script>
      </body>
</html>
```
