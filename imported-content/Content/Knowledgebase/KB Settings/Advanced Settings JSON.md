---
layout:
  title:
    visible: false
---

<a id="AdvancedSettingsJSON"></a>

# Advanced Settings JSON

The Advanced Settings JSON allows you to configure advanced Knowledge Base (KB) settings.

> **IMPORTANT!**  Incorrectly modifying the JSON structure may cause extraction failures during runtime. To prevent issues, avoid making structural changes.

This field is particularly useful for adding new elements to collections, making them available in the Advanced Settings UI. You can use it to:

- Add new generative endpoints
- Configure content chunkers
- Define score calculator strategies, etc.

For experienced users, additional parameters can be adjusted to fine-tune KB behavior. However, changes should be made carefully to avoid disrupting functionality.

> **NOTE:** This action is irreversible and will impact all customized generative endpoints settings and credentials.
