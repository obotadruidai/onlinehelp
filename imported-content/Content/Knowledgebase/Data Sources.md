---
layout:
  title:
    visible: false
---

<a id="DataSources"></a>

# Data Sources

Druid allows you to aggregate knowledge from multiple enterprise silos to enable Retrieval-Augmented Generation (RAG). Depending on your data architecture and format, you can configure three types of data sources:

<a id="UnstructureddatasourcesFilesWebContent"></a>

## Unstructured data sources (Files & Web Content)

Connecting local document repositories and web assets allows the AI Agent to parse and search free-form text. This setup supports direct uploads of unstructured PDF, DOCX, and TXT files (ideal for policy documents, manuals, and standard operating procedures) alongside web crawling for public-facing websites, help centers, or blogs. The system automatically processes, splits, and extracts raw text from these files and web pages to index them for semantic search.

<a id="Nativedatasourceconnectors"></a>

## Native data source connectors

Integrating native application connectors links the Knowledge Base directly to external enterprise platforms, database systems, and cloud environments without requiring custom code or development. This setup supports built-in integrations with platforms like ServiceNow (to ingest CMDB, Incidents, and KB articles) alongside native connectors to cloud file repositories—specifically SharePoint Site Libraries, OneDrive, Google Drive, and Network Shared Drives. It automatically synchronizes folder structures, securely ingests data using built-in credential fields, and extracts text from files to index them for semantic search.

<a id="Customdatasources"></a>

## Custom data sources

Designed for unique business requirements or proprietary internal platforms that do not fit standard connectors, custom data sources support proprietary business systems, internal middleware, and custom-built APIs. These sources allow ingestion mapping of both structured payloads and unstructured text via tailored API integrations, giving you complete control over data formatting and vectorization.
