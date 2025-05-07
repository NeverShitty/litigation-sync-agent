from pathlib import Path

# Create the contents of the notion-puller.py script
notion_puller_py = """
import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DB_ID = os.getenv("NOTION_DB_ID")
NOTION_VERSION = "2022-06-28"
NOTION_API_URL = "https://api.notion.com/v1/pages"

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
            "Notes": { "rich_text": [ { "text": { "content": "Auto-synced from GitHub repo." } } ] }
        }
    }

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION
    }

    response = requests.post(NOTION_API_URL, headers=headers, data=json.dumps(payload))
    print(f"→ Sync result: {response.status_code} - {response.text}")

if __name__ == "__main__":
    with open("../litigation-sync-gpt-bundle/actions_validated_customgpt.json") as f:
        title = "Validated Actions Schema"
        claim = f.read()[:4000]  # Trim to avoid payload overflow
        push_to_notion(title, claim)
"""

# Create the contents of the .env file
dotenv_content = """
NOTION_TOKEN=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
NOTION_DB_ID=1eb94de435798054bd2fea10db2bc34c
"""

# Define file paths
script_path = Path("/mnt/data/notion-puller.py")
env_path = Path("/mnt/data/.env")

# Write the files
script_path.write_text(notion_puller_py)
env_path.write_text(dotenv_content)

# Return the paths for download
script_path, env_path

