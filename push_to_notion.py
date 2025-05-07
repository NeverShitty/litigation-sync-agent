def push_to_notion(title, claim, status="Draft", weight="Moderate"):
    payload = {
        "parent": { "database_id": NOTION_DB_ID },
        "properties": {
            "Title": { "title": [ { "text": { "content": title } } ] },
            "Document Type": { "select": { "name": "Statement" } },
            "Entities": { "multi_select": [ { "name": "Nick Bianchi" } ] },
            "Case Reference": { "rich_text": [ { "text": { "content": "ARIBIA v. Bianchi" } } ] },
            "Evidentiary Weight": { "select": { "name": weight } },
            "Status": { "status": { "name": status } },
            "Notes": { "rich_text": [ { "text": { "content": claim } } ] }
        }
    }

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=headers, data=json.dumps(payload))
    print(f"→ Sync result: {response.status_code} - {response.text}")

