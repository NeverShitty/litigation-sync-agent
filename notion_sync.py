
import os
import json
import requests

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DB_ID = os.getenv("NOTION_DB_ID")
NOTION_VERSION = "2022-06-28"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": NOTION_VERSION
}

def push_to_notion(data):
    payload = {
        "parent": { "database_id": NOTION_DB_ID },
        "properties": {
            "Title": { "title": [ { "text": { "content": data["title"] } } ] },
            "Document Type": { "select": { "name": "Statement" }},
            "Entity": { "multi_select": [ { "name": "Nick Bianchi" } ] },
            "Linked Case": { "select": { "name": "ARIBIA v. Bianchi - Cook County" }},
            "Evidentiary Weight": { "select": { "name": data.get("weight", "Moderate") }},
            "Status": { "status": { "name": data.get("status", "Draft") }},
            "Notes": {
                "rich_text": [ { "text": { "content": data.get("claim", "") } } ]
            }
        }
    }

    res = requests.post("https://api.notion.com/v1/pages", headers=HEADERS, data=json.dumps(payload))
    print("→", res.status_code, res.text)

if __name__ == "__main__":
    bundle_dir = "litigation-sync-gpt-bundle"
    for file in Path(bundle_dir).glob("*.json"):
        with open(file) as f:
            try:
                data = json.load(f)
                print(f"Processing: {file}")
                push_to_notion(data)
            except Exception as e:
                print(f"Error processing {file}: {e}")
