<a id="RetailAgenticSolution"></a>

# Retail Agentic Solution

The Retail Agentic Solution is a high-performance, end-to-end business application built on Druid technology. It transforms the traditional shopping experience from a static catalog into a natural, conversational, and visual journey. By orchestrating secure PII anonymization, real-time shop-aware inventory, and generative AI visualization, the solution automates complex retail administration while maintaining deep customer engagement and data privacy.

<a id="WhatsNewinVersion300"></a>

## What’s New in Version 3.0.0

- **Wishlist & Campaign Manager**. Authenticated users can now add products to a personal wishlist via natural conversation or hero card buttons. Admins can define Campaigns that automatically identify users with specific products in their wishlists and send them targeted email discount codes.
- **AI Image Preview**. While searching, users can request to preview a product in their own space (e.g., a book on a desk). The AI Agent uses Gemini to create a realistic composite image of the item in the user's defined context.
- **Restructured Workspaces**. Three dedicated environments — Admin, Retail Back-Office, and Retail Front-Office — for cleaner data segregation.
- **LLM Upgrade**. The solution is now fully optimized for GPT 4.1.

<a id="WhatsNewinVersion210"></a>

## What’s New in Version 2.1.0

- **Added Abandoned Cart**. Added functionality to track inactive users with items in their cart and capture potential lost sales. For more information, see [Configure Abandoned Cart](Set%20Up%20the%20Retail%20Solution%20%28for%20solution%20admins%29.md#Step).

<a id="KeyFeaturesandComponents"></a>

## Key Features and Components

This solution includes:

<a id="BusinessWorkflow"></a>

### Business Workflow

- **Complete Shopping Lifecycle**. Manages the full journey of a customer, including product discovery (text/image), adding items to a cart, secure checkout, and listing order history.
- **Intelligent Wish listing**. Authenticated users can save products for later by saying "Add this to my wishlist." Users can view, delete, or move these items directly to their cart from their account dashboard.
- **AI Image Preview**. Provides instant photo realistic visualization. A user can ask, "Show me how this book would look on my nightstand," and theAI Agent generates a composite image of the product in that setting.
- **Shop-Aware Inventory**. Searches for product availability across multiple physical stores simultaneously to offer the customer the quickest pickup or delivery option.
- **Automated Campaigns**. Admins can define marketing promotions. When triggered, the system automatically emails the target audience based on their wish list contents.
- **Secure Claims Management**. Allows users to file claims for damaged or missing items, with integrated support for uploading images stored securely in Azure Blob Service.

<a id="SettingsandConfigurationWorkflows"></a>

### Settings and Configuration Workflows

- **Setup and Provisioning**. An automated flow (triggered via the RetailHelper) that provisions the backend database with essential demo data, including Categories, Stores, Products, and Stock levels.
- **Data Anonymization**. An integrated security privacy layer that manages PII masking before data transmission to LLMs. This feature uses Becus 1.0 to redact user input during initial processing. By using this service, the system guarantees that no identifiable information reaches an external LLM context.
- **Visual Preview Configuration**. Enable the Gemini-powered image preview.
- **Abandoned Cart Automation**. Background tasks that handle inactivity timeouts and automatically convert abandoned carts into draft orders for reporting.

<a id="DataandAccess"></a>

### Data and Access

- **Data Model**: Contains all essential retail entities (Products, Stores, Stocks, and Transactions).
- **Operational Workspaces**. The solution contains three workspaces:

- **Admin Workspace**. Technical setup, global parameters (Anonymization/Preview), and the Data Provisioning engine.
- **Retail Back-Office Workspace**. Inventory, stock mapping, and campaign backend data (Audiences).
- **Retail Front-Office Workspace**. Customer-facing data, including order management, claims, returns, and marketing execution.

For a full reference of the entities available in each workspace, see [Data Model and Workspace References](Data%20Model%20and%20Workspace%20References.md).
