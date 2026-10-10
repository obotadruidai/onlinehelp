<a id="SettingUptheWebChatinHTMLPage"></a>

# Setting Up the Web Chat in HTML Page

This section provides you with a HTML page template (a .txt. file) that contains web chat. You can download it and easily configure it to include your AI Agent. You can use this HTML page to run the test scripts.

Download the HTML website page template (**Chatbot-Victor.txt** file).

[!\[\](../../../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/Victor/Chatbot-Victor.txt?st=2021-02-14T15%3A45%3A42Z&se=2021-12-31T15%3A45%3A00Z&sp=rl&sv=2018-03-28&sr=f&sig=sog3T0rdKQ2Pxod2yOmibrPYIoDbMkN7Q%2BQyucKPTms%3D)

For more information on how to integrate the AI Agent in your website and access more HTML templates, see [WebChat](../../../Channels/WebChat/WebChat.md).

<a id="SetcustompageforUiPathOrchApi"></a>

## Set custom page for UiPathOrchApi

In Druid Portal, go to solution Flows, search for the **my-tasks-complete-uipath-form-task** flow and click on it. The flow steps appear.

Search for the **add-email** step and in the Set Variables section, modify the **[[Email]].Body** variable. By default it contains the hardcoded link https://demo-Druid-web01.azurewebsites.net/demo/Standard2/Victor/. Replace it with the link of your custom page hosting the webchat.
