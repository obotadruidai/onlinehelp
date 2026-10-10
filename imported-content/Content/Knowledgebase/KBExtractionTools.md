---
title: "KB Extraction Tools"
---

<a id="KBExtractionTools"></a>


DRUID provides you with two extraction tools that operate as content extraction tools during conversations, particularly valuable for document analysis using Large Language Models (LLMs).

The KB extraction tools during conversations use the content extraction functionality found in the DRUID KB Engine but operate in isolation from the KB processing pipeline, focused on content extraction without introducing changes to the underlying KB infrastructure.

<a id="Extractcontentfromdocuments"></a>

## Extract content from documents

Extract content from a document (structured or unstructured) using the internal action **KBExtractDocumentContent**. This action accepts a document from a [[File]] entity field and provides output in the following format:

- For unstructured documents: content is returned in **[[KBOperation]].ExtractedDocument[i].Content**.
- For structured documents: content is divided into **[[KBOperation]].ExtractedDocument[i].Question** and **[[KBOperation]].ExtractedDocument[i].Answer**.

| Parameter | Description |
| --- | --- |
| SourceFile | The file property of the [[Entity]] from which the document content is extracted. This parameter is mandatory.  **NOTE:**   - The internal action imposes a source file size limit of 5 MB. - Extracted content is limited to 1 MB.   If the document exceeds 5 MB or the extracted content surpasses 1 MB, the internal action returns an error and does not proceed with the extraction. |
| DocumentType | Indicates if the document is structured or not. Default value is "unstructured". This parameter is optional. |

**Syntax**

```
{
  "SourceFile": "[[Entity]].FileProperty",
  "DocumentType": "structured" //optional, default value = unstructured
}
```

**Example**

```
{
  "SourceFile": "[[Employee]].Resume",
  "DocumentType": "structured" 
}
```

When extracting data from EML documents, the response JSON includes dedicated fields for email metadata, making the extracted data easier to process and use in business applications:

- **To** - The recipient email address(es).
- **From** - The sender email address.
- **Subject** - The email subject line.
- **Date** - The email timestamp (ISO 8601 format).

> **NOTE:** The response JSON includes dedicated fields for email metadata.

> **IMPORTANT!** The Antimalware Check treats .eml files as archives to prevent unnecessary data loss. If an email contains a restricted or infected attachment, the system isolates and discards only that specific file while successfully extracting the email body and all other safe attachments. Every excluded element triggers a system warning message detailing the reason for exclusion. This replaces the behavior in previous releases, which resulted in EML document rejection for the entire file if a single attachment failed the scan.

The full email content, including all metadata and the complete message body, is also saved in both the answer and content fields within the paragraphs array.

```
{
  "to": "recipient@example.com",
  "from": "sender@example.com",
  "subject": "Email subject line",
  "date": "2024-01-15T10:30:00Z",
  "paragraphs": [
    {
      "question": "string",
      "answer": "Complete email body content including To: recipient@example.com, From: sender@example.com, Subject: Email subject line, Date: 2024-01-15T10:30:00Z, and the full message body text",
      "content": "Complete email body content including To: recipient@example.com, From: sender@example.com, Subject: Email subject line, Date: 2024-01-15T10:30:00Z, and the full message body text"
    }
  ],
  "error": "string"
}
```

This structured response allows you to easily access specific email fields for filtering, sorting, or display purposes, while maintaining the complete email content for comprehensive processing.

<a id="Extractcontentfromwebsites"></a>

## Extract content from websites

Crawl a specific website and extract paragraphs (unstructured data) using the internal action **KBExtractUrlContent**. internal action crawls a specified website and extracts unstructured content as paragraphs. The extracted content is returned as a collection of strings in **[[KBOperation]].ExtractedDocument[i].Question** and **[[KBOperation]].ExtractedDocument[i].Answer**.

**Syntax**

```
{
  "Url": "",
  "CrawlHttpRequests": "true|false"
}
```

| Parameter | Description |
| --- | --- |
| Url | The URL of the website starting with 'https://'. E.g. https://druidai.com. |
| CrawlHttpRequests | Set to 'true' if the website is static HTML site; otherwise, set to 'false'. |
