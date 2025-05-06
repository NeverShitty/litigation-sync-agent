# 🧠 Litigation Sync GPT Bundle

This repository contains all the components required to deploy a Custom GPT agent that syncs structured litigation data into Notion databases.

## 📦 Components

- `manifest.json` – Describes the GPT agent's name, capabilities, OpenAPI spec, and secrets.
- `actions_validated_customgpt.json` – OpenAPI schema for the Notion API POST /pages endpoint.
- `function_full_customgpt.json` – GPT function definition to map fields like Name, Claim, Entity, etc.
- `gpt_module_litigation_sync.json` – Optional module with extended capabilities: contradiction resolution, timeline generation, etc.

## 🔑 Required GPT Secrets

- `NOTION_TOKEN` – Your Notion integration token.
- `NOTION_DB_ID` – The target Notion database ID.

## 🚀 Installation

1. In your [OpenAI Custom GPT builder](https://chat.openai.com/gpts/editor), upload:

   - `manifest.json`
   - `actions_validated_customgpt.json` under the "Actions" tab
   - `function_full_customgpt.json` under the "Functions" tab

2. Paste your Notion secrets into the GPT’s "Secrets" section.

3. Tag your content with `#notion-sync` to automatically trigger Notion updates.

## 🛠 Example Payload (for `createNotionCaseEntry`)

```json
{
  "parent": { "database_id": "{{secrets.NOTION_DB_ID}}" },
  "properties": {
    "Name": { "title": [{ "text": { "content": "Motion to Compel Arbitration" } }] },
    "Type": { "select": { "name": "Motion" } },
    "Entity": { "multi_select": [{ "name": "ARIBIA LLC" }] },
    "Claim": { "rich_text": [{ "text": { "content": "Enforce clause in LLC agreement" } }] },
    "Weight": { "select": { "name": "Strong" } },
    "Status": { "select": { "name": "Draft" } },
    "Notes": { "rich_text": [{ "text": { "content": "References Section 8.5 of the agreement" } }] }
  }
}
```

## 🙋‍♂️ Contact

Built by [Nick Bianchi](https://github.com/NeverShitty)

Use responsibly. Sync ruthlessly.