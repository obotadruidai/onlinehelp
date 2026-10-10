<a id="HTMLSettings"></a>

# HTML Settings

HTML Settings control how the Knowledge Base (KB) Engine crawls and extracts content from website data sources. Use them to exclude non-content page elements, skip unwanted links, and run scripts on dynamic pages before extraction.

These settings apply to website data sources. Configure defaults at the KB level on this page, or override them per data source when a site needs different selectors, link rules, or scripts.

Data source settings override KB defaults for that source only. For several websites with different layouts, set selectors and scripts per data source rather than only at the KB level.

To apply KB HTML settings defaults to all data sources and tree elements, use **Save to All** from the Knowledge Base advanced settings actions menu.

<a id="HTMLSelectorTagstoIgnore"></a>

## HTML Selector Tags to Ignore

Specify CSS selectors for HTML elements to exclude during extraction. Matching elements are not indexed, which keeps navigation, headers, footers, modals, and other structural UI out of the KB.

Enter one selector per line.

**Examples**

```
img
svg
script
style
noscript
iframe
nav
footer
header
[role="alert"]
[role="banner"]
[role="heading"]
[role="dialog"]
.hidden
.exclusive
div.sidemenu
div.topbar
div.search-content
div.navigations-container
[role="alertdialog"]
[class *= "breadcrumb"]
[role="region"][aria-label*="skip" i]
[aria-modal="true"]
```

<a id="LinkPatternstoIgnore"></a>

## Link Patterns to Ignore

Define regular expression (Regex) patterns for URLs the crawler should not follow or index. Use this to skip social profiles, media embeds, phone links, and mailto links that add noise without useful knowledge.

Enter one pattern per line.

**Examples:**

```
^\s*https?:\/\/(?:[a-zA-Z0-9-]+\.)*facebook\.com
^\s*https?:\/\/(?:[a-zA-Z0-9-]+\.)*instagram\.com
^\s*https?:\/\/(?:[a-zA-Z0-9-]+\.)*whatsapp\.com
^\s*https?:\/\/(?:[a-zA-Z0-9-]+\.)*twitter\.com
^\s*https?:\/\/(?:[a-zA-Z0-9-]+\.)*linkedin\.com
^\s*https?:\/\/(?:[a-zA-Z0-9-]+\.)*youtube\.com
^\s*https?:\/\/(?:[a-zA-Z0-9-]+\.)*x\.com
^\s*tel:
^\s*mailto:
```

<a id="HTMLPostRenderScript"></a>

## HTML Post Render Script

Enter Playwright-compatible JavaScript that runs after the page loads and before extraction. The script can change the DOM so dynamically rendered content is visible to the crawler—for example, expanding accordions or tabs, clicking Load more, closing cookie banners, or waiting for API-driven content.

> **NOTE:** This setting applies only to website data sources where **Crawl using HTTP** requests is disabled. If you have multiple website data sources, configure the script on each data source that needs it. For more information, see [Step 2. Configure Advanced Content Rendering (Optional)](../Website%20data%20sources.md#Step).

Leave the field empty when pages are fully static and no interaction is required before scrape.

**Script Example**

```
(async () => {
  const delay = ms =>
    new Promise(resolve => setTimeout(resolve, ms));

  await delay(500);
  document
    .querySelectorAll('[aria-expanded="false"]')
    .forEach(el => {
      if (el instanceof HTMLElement) {
        el.click();
      }
    });
  document
    .querySelectorAll('button, a')
    .forEach(el => {
      if (!(el instanceof HTMLElement)) return;

      const text = (el.textContent || '').toLowerCase();

      if (
        text.includes('more') ||
        text.includes('show') ||
        text.includes('open') ||
        text.includes('view')
      ) {
        el.click();
      }
    });

  await delay(500);
})();
```

What the script does:

1. **Waits for the page to settle**. The script waits 500 milliseconds, giving JavaScript-driven page components time to render.
2. **Expands collapsed elements**. It finds all elements whose aria-expanded attribute is set to false and clicks them. This commonly opens accordions, expandable menus, FAQ answers, and similar collapsed sections.
3. **Clicks common content-reveal controls**. It checks all buttons and links on the page. If their visible text contains more, show, open, or view, the script clicks them. This may activate controls such as:

- Show more
- View details
- Open section
- Load more

4. **Waits for newly revealed content**. If any elements are successfully clicked, the script waits another 500 milliseconds for new content to render before crawling continues.

> **IMPORTANT!** The matching rules are intentionally broad. Any button or link containing one of the specified words may be clicked, even if it is unrelated to revealing content. For a particular website, using more specific CSS selectors is safer and produces more predictable results.
