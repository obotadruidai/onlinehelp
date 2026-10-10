---
title: "Import Solutions"
---

<a id="ImportSolutions"></a>


{% hint style="warning" %}
**IMPORTANT!** When you import a solution, please be aware that the elements in the solution will overwrite the AI Agent elements with the same name and SourceId.
{% endhint %}

To import a solution, follow these steps:

1. In the Druid Portal, click the **Solutions** drop-down and select **Import solution**. The [Solutions Library](../Solution%20Library/Solutions%20Library.md) appears.
2. At the top-right corner of the page, click the **Import from file** button.

![](../Resources/Images/Solutions%20Library/import%20from%20file.png)

The Import Solution pop-up appears.

3. Click the **Choose file** button, browse for your solution zip file and click **Open**. The solution details appear by default on the **Description** tab which provides you with the solution language(s).

![](../Resources/Images/Working%20with%20solutions/import%20sol.png)

4. If not all language(s) defined on the destination AI Agent exist in the solution package, a warning icon (![](../Resources/Images/Working%20with%20solutions/attention.png)) displays next to the **Language Settings** tab. In this case, click the **Language Settings** tab. The languages from the solution package that exist on the destination AI Agent display as read-only. Select which language from the solution to import for the non-matching language(s) of the destination AI Agent.

If none of the languages on the destination AI Agent exist in the solution package, you have to select which language from the solution to import on each language of the destination AI Agent.

{% hint style="info" %}
**Info:** On import, Druid will write the messages in the selected languages making it easy for you to translate in the specific languages later.
{% endhint %}

5. Check the content of the solution template by clicking the **Components** tab.

The orange label indicates the number of elements which will be updated by the solution template installation.

The blue label indicates the number of new elements which will be added on the AI Agent.

To see details about a specific element, click on it (e.g., Flows). The list of flows appears including new and existing flow which will be updated on solution import.

{% hint style="warning" %}
**IMPORTANT!** All elements which will be overwritten by solution import are marked with the **Warning** label. Solution import (elements overwriting) cannot be reverted, so we strongly recommend you to install solutions on a dev/sandbox environment.
{% endhint %}

6. Click the **Import** button.
7. Click the **Refresh** button to view the import status (completed / success or pending) and update the counters in the **Solution Contents** menu.

After importing a solution, a snapshot is automatically created and marked as a backup snapshot. You can view this snapshot under the solution details in the Solution Snapshots section.
