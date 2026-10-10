---
title: "Full Page Chat"
---

<a id="FullPageChat"></a>


![](../../Resources/Images/WebChat/full%20page%20chat.png)

> **NOTE:** In the HTML template below, make sure that your replace the following: <your Druid tenant>, <your AI Agent ID> and <your AI Agent base URL>.

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
                       botId: "<your <span class="mc-variable General.AI_Agent variable">AI Agent</span> ID>",
                       baseUrl: "<your <span class="mc-variable General.AI_Agent variable">AI Agent</span>'s base URL>",
                        
                       UI: {
                          "autoExpandEnabled": true,
                          "fullScreenMode": true,
                          "fullScreenMode_leftRightClass": "",
                          "fullScreenMode_mainChatClass": "col-md-12",
                          containerElement: null // [MANDATORY] example: document.getElementById('DruidContainerElement') -> specify the webchat expand DOM element
                       }
                  });
             });
       </script>
     </body>
</html>
```

```
<!DOCTYPE html>
<html>
   <head>
        <meta charset="UTF-8">
        <title>Your website html</title>

        <!-- Include the css file   -->
        <link defer href="<your Druid tenant>/Druid_webchat.css" rel="stylesheet">
   </head>
   <body>
       <!-- Include the script file   -->
       <script defer type="text/javascript" src="<your Druid tenant>/Druid_webchat.js"></script>

	<!-- Init the webchat component on document load -->
       <script type="text/javascript">
            document.addEventListener("DOMContentLoaded", function(event) {
                 DruidWebchat.init({
                       <!-- Common settings  -->
                       botId: "<your AI Agent ID>",
                       baseUrl: "<your AI Agent's base URL>",
                        
                       UI: {
                          "autoExpandEnabled": true,
                          "fullScreenMode": true,
                          "fullScreenMode_leftRightClass": "",
                          "fullScreenMode_mainChatClass": "col-md-12",
                          containerElement: null // [MANDATORY] example: document.getElementById('DruidContainerElement') -> specify the webchat expand DOM element
                       }
                  });
             });
       </script>
     </body>
</html>
```
