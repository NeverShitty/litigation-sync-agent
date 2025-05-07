from dotenv import load_dotenv
load_dotenv()

import os
import requests
import json

NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_DB_ID = os.environ.get("NOTION_DB_ID")
NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
NOTION_VERSION = "2022-06-28"

def push_to_notion(title, claim, status="Draft", weight="Moderate"):
    payload = {
        "parent": { "database_id": NOTION_DB_ID },
        "properties": {
            "Name": { "title": [ { "text": { "content": title } } ] },
            "Type": { "select": { "name": "Claim" } },
            "Entity": { "multi_select": [ { "name": "System Sync" } ] },
            "Claim": { "rich_text": [ { "text": { "content": claim } } ] },
            "Weight": { "select": { "name": weight } },
            "Status": { "select": { "name": status } },
            "Notes": { "rich_text": [ { "text": { "content": "Auto-pulled from GitHub repo sync." } } ] }
        }
    }

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION
    }

    response = requests.post(NOTION_API_URL, headers=headers, data=json.dumps(payload))
    print(f"→ Sync result: {response.status_code} - {response.text}")

# Example sync from a schema file
with open("../litigation-sync-gpt-bundle/actions_validated_customgpt.json") as f:
    title = "Validated Actions Schema"
    claim = f.read()[:4000]  # Trim if needed
    push_to_n

