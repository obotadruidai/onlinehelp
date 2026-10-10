---
layout:
  title:
    visible: false
---

<a id="EmailBody"></a>

# <a id="_Email_Body"></a>Email Body

This section provides an example of how an HTML email body looks like for a Druid Email connector versus the normal HTML email body.

<a id="NormalHTMLEmailBody"></a>

## Normal HTML Email Body

```
<!DOCTYPE HTML>
<html lang="en">
     <head>
        <meta charset="UTF-8">
            <title></title>
                <link rel="stylesheet" type="text/css" href="">
     </head>
     <body>
        <table border="0" cellspacing="0" cellpadding="0" style="width:100%; background-color:#EFF3F8;">
            <tr><td style="padding: 80px 30px 80px 30px;">
                <center>
                <div style="background-color: white; font-family:Calibri,sans-serif; text-align:center; width: 500px; padding: 40px; font-size: 14pt; color: #57697E;">
                     <span style="font-size: 30pt;">Welcome to DruidPortal!</span><br><br>
                    <span style="color: #ccc;">This email is sent to provide the access credentials to the <span class="mc-variable General.AI_Agent variable">AI Agent</span> platform.</span>
                    <br><br>
                    <strong>User name:</strong> [[User]].UserName<br>
                    <strong>Access Code:</strong> [[User]].AccessCode<br><br><br>
                    Access the <span class="mc-variable General.AI_Agent variable">AI Agent</span> here: <a href="https:// Druid.Druidplatform.com" style="font-weight: bold; color: #57697E;"> Druid.Druidplatform.com</a>
                 </div>
                </center>
            </td></tr>
        </table>
     </body>
 </html>
```

<a id="HTMLEmailBodyforDruidEmailConnector"></a>

## HTML Email Body for Druid Email Connector

As the [[Email]].Body field is of type String, in order to use HTML code in the email body, you will have to escape the code. Below is an example of how to use HTML code in the email body.

```
<!DOCTYPE HTML>
 <html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\">
        <title></title>
        <link rel=\"stylesheet\" type=\"text/css\" href=\"\">
    </head>
    <body>
        <table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" style=\"width:100%; background-color:#EFF3F8;\">
            <tr><td style=\"padding: 80px 30px 80px 30px;\">
                <center>
                    <div style=\"background-color: white; font-family:Calibri,sans-serif; text-align:center; width: 500px; padding: 40px; font-size: 14pt; color: #57697E;\">
                    <span style=\"font-size: 30pt;\">Welcome to DruidPortal!</span><br><br>
                    <span style=\"color: #ccc;\">This email is sent to provide the access credentials to the <span class="mc-variable General.AI_Agent variable">AI Agent</span> platform.</span>
                    <br><br>
                    <strong>User name: </strong>"+[[User]].UserName+"<br>
                    <strong>Password: </strong>"+[[User]].Pass+"<br><br><br>
                    Access the <span class="mc-variable General.AI_Agent variable">AI Agent</span> here: <a href=\"https://Druid.Druidplatform.com\" style=\"font-weight: bold; color: #57697E;\">Druid.Druidplatform.com</a>
                    </div>
                </center>
            </td></tr>
        </table>
     </body>
 </html>
```
