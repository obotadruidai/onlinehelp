---
title: Generate Documents Using Dynamic Templates
---


DRUID offers authors with a simplified way to design conversational flows for generating documents by using dynamic templates. This is particularly useful when you want to generate documents using specific templates for departments in your company or for companies within a group of companies.

Using dynamic templates eliminates the need of creating one connector action and integration task for each document template. It also simplifies the conversational flow authoring; you design a single flow step that generates documents using multiple templates as set on the flow step; no need to add more steps with conditions in the conversational flow to address each document template.

## How to generate documents using dynamic templates

This section provides an example on how to generate documents specific to a company the user chooses in the chat, by using dynamic templates.

### Prerequisites

* Make sure that you properly built the AI Agent informational model (the entities and their relationships).

### Step 1. Create the document templates

Create the document templates following the procedures [Creating Word Document Templates](<Creating Word Document Templates.md>) and / or [Creating Excel Templates](<Creating Excel Templates.md>).

In this example, we created three document templates shown in figure below.

![](<../../../.gitbook/assets/doc templates 3.png>)

## Step 2. Design the flow

Create a flow that provides the user with the possibility to choose the company, capture user input and then based on it apply the specific template to generate the document:

1. Add a step of type Choice and in Input mapping enter the entity field that will store the user input.

![](<../../../.gitbook/assets/input mapping.png>)

2. Click the Metadata section and configure the step choices, then save the step. For more information, see [Choice Steps Configuration](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/flows/conversational-flows/flow-steps/choice-steps-configuration).

![](../../../.gitbook/assets/choices.png)

3. Add a step of type Message you will use to generate the document and send it to the user in the chat.
4. On the step General section, provide a **Step message**(e.g., , "Here is you document:") and on the Metadata section, in the Attachments field, provide the entity field that stores the generated document (e.g., \[\[Employee]].File).
5. Click the SetVariables section and set the entity field used for dynamic document template name. E.g., \[\[Employee]].TemplateName. You will use this on the integration task to generate documents. Use the code editor to set the variable and provide the JavaScript code that applies a specific document template for a specific company.

![](<../../../.gitbook/assets/set variables (2).png>)

![](../../../.gitbook/assets/js.png)

**Set variable for dynamic templates - JavaScript code example**

```
(function selectTemplate(companyId)
    {
        var templateName = "none";
        switch (companyId) 
            {
                case "Company A":
                    templateName = "Contract_Company_A.docx";
                    break;
                case "Company B":
                    templateName = "Contract_Company_B.docx";
                    break;
                case "Company C":
                    templateName = "Contract_Company_C.docx";
                    break;
            };
        return templateName;
    }
)([[Employee]].CompanyId)
```

6. Save the step.
7. On the step, in the PreActions section, add connector action and integration task for document generation.

![](<../../../.gitbook/assets/pre actions.png>)

When configuring the integration task, tap on **Use Dynamic Template Name** and in the **Dynamic Template Name** field, enter the entity field used for dynamic templates, the one you have set in the SetVariables section on the step.

![](<../../../.gitbook/assets/integration task example.png>)

In the **Dynamic File Name** field, specify the file name of the generated document either hard coded as string (e.g., "Invoice April") or as a value from the context: an entity field (e.g., \[\[Employee]].Name) or a local variable.

{% hint style="info" %}
**NOTE:** If the **Dynamic File Name** field is empty, DRUID will use the template file name as file name of the generated document. This field is available in DRUID 5.14 and higher.
{% endhint %}

Configure the integration task to store the generated document in a specific entity field (a field of type file created on the request entity) by providing the field name in the **ProjectResultToEntityPath** field on the integration task.

![](../../../.gitbook/assets/file.png)

8. Save the integration task.

If the user chooses Company A in the chat, then a document will be generated using the document template Contract\_Company\_A.docx, and so on.

![](../../../.gitbook/assets/chat.png)

## Related Topics

* [Creating Excel Templates](<Creating Excel Templates.md>)
* [Creating Word Document Templates](<Creating Word Document Templates.md>)
* [Step 3. Add Integration Tasks for Documents Generation](https://docs.druidai.com/docs/Content/7_Integrations/Document%20Builder/Step%203%20Create%20Action%20and%20Add.htm)
* [Step 4. Call action on the desired flow step](https://docs.druidai.com/docs/Content/7_Integrations/Document%20Builder/Step%204%20Call%20action%20on%20the.htm)
