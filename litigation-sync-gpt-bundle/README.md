# 🧠 Litigation Sync GPT Bundle

This repository directory contains a plug-and-play Custom GPT bundle for syncing litigation events, filings, and contradictions into Notion.

## 📦 Contents

| File                               | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| `actions_validated_customgpt.json` | Full OpenAPI schema for Custom GPT Action (`createNotionCaseEntry`)         |
| `function_full_customgpt.json`     | GPT function definitions using the Notion-compatible nested format          |
| `gpt_module_litigation_sync.json`  | Bundle of GPT-callable functions including contradiction and timeline tools |

## 🚀 How to Use

1. **OpenAI Custom GPT Setup**
   - Paste the contents of `actions_validated_customgpt.json` into the **Actions** tab
   - Paste the contents of `function_full_customgpt.json` into the **Functions** tab
   - Add secrets:
     - `NOTION_TOKEN` — your Notion integration token (starts with `secret_`)
     - `NOTION_DB_ID` — the database ID from your Notion tracker

2. **Instructions for GPT**
   Paste this in your Instructions:

   ```text
   When a message includes #notion-sync or references litigation filings:
   - Format the entry with Name, Type, Entity, Claim, Weight, Status, and Notes.
   - Trigger `createNotionCaseEntry` with the formatted Notion API payload.
   ```

3. **Triggers**
   - `#notion-sync` — Push any filing/motion/statement into Notion
   - `#check-contradiction` — Run logic comparison on past statements
   - `#summarize-timeline` — Generate an event timeline

## 🔐 API Integration Notes

- Endpoint: `https://api.notion.com/v1/pages`
- Auth Header: `Authorization: Bearer {{secrets.NOTION_TOKEN}}`
- Pass the DB ID via: `{{secrets.NOTION_DB_ID}}`

## 🧠 Future Extensions

- OCR + Email evidence parsing (in progress)
- Clause contradiction detector
- Entity-based timeline builder

---

© 2025 NeverShitty Systems. Licensed for personal or internal legal research.