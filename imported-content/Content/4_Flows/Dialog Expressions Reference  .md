---
layout:
  title:
    visible: false
---

<a id="DialogExpressionsReference"></a>

# Dialog Expressions Reference

In the Druid AI Platform, you can utilize expressions in dialogs to perform various tasks, such as defining conditions for flow steps and crafting messages sent to users. Here's how you can use expressions effectively:

<a id="UsingExpressionsinCheckConditionsExamples"></a>

## Using Expressions in Check Conditions Examples

When setting up conditions for child steps, you can use expressions to trigger specific actions based on the conversation context. Here are some examples:

| Expression | Description |
| --- | --- |
| [[Product]] != null | Checks if the [[Product]] entity has a value. |
| [[Product]] == null | Checks if the [[Product]] entity is null. |
| [[Product]].Name != null && [[Product]].Name !=”” | Verifies if the Name field in the [[Product]] entity has a value. |
| [[Product]].Code.toLowerCase() == “abcd100” | Checks if the Code field in the [[Product]] entity matches the specified value. |
| [[ProductList]].Count >0 | Ensures the [[ProductList]] entity collection contains more than zero items. |
| @InternalActionResult == true.toString() | Verifies if the internal action of the previous step completed successfully. |
| [[Form]].YesNoAnswer | Checks the **YesNoAnswer** field (Boolean type) in the Form entity. |
| ([[Product]].Category != null ) && ([[ProductList]] ==null || [[ProductList]].Count ==0) | Checks if the Product Category is known and no products have been found in the [[ProductList]] entity collection. |
| [[ChatUser]].ChannelId == “directline” | Verifies if the ChannelId of the ChatUser is "directline". |
| [[ChatUser]].ChannelId == “nexmo-whatsapp” |  |
| [[ChatUser]].ChannelId == “facebook” |  |
| [[ChatUser]].ChannelId == “msteams” |  |
| [[ChatUser]].ChannelId == “slack” |  |

<a id="UsingExpressionsinMessagesExamples"></a>

## Using Expressions in Messages Examples

TWhen crafting messages for users, expressions can enhance the content dynamically. Here are some examples:

| Expression | Description |
| --- | --- |
| Monthly rate: \*\*{{FormatDecimal [[FinancialProduct]].InstallmentAmount format="#,#0.00"}} [[FinancialProduct]].Currency.Code\*\* | Format the **InstallementAmount** as Decimal. **format="#,#0.00"** is C# specification. |
| Request date: \*\*{{FormatDateTime [[FinancialProduct]].RequestDate format="dd-MM-yyyy"}}\*\* | Date time formats. The following date formats are available as per C# specification: "dd-MM-yyyy" "yyMMdd" "yyyy-dd-MM HH:mm:ss". |
| Including Insurance: \*\*{{FormatBoolean [[FinancialProduct]].hasInsurance format="yes/no"}}\*\* | Boolean formats: "yes/no", "y/n", "da/nu", "d/n", "true/false", "t/f", "adevarat/fals", "adevărat/fals", "a/f", "0/1" or "1/0". |
| Hello [[ChatUser]].FirstName |  |
| I found \*\*[[ProductList]].Count items\*\* with \*\*[[Product]].Category\*\* |  |
| I will submit the request with your comment: @CommentVariable |  |

By leveraging these expressions, you can create dynamic and engaging dialogs tailored to your users' needs and preferences.

## Related Topics

- [Common Flow Settings](Common%20Flow%20Settings.md)
- [Conversation Lifecycle](Conversation%20Lifecycle.md)
