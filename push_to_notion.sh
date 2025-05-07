#!/bin/bash

# Load environment variables from .env
source "$(dirname "$0")/.env"

# Push a test entry to Notion
curl -X POST https://api.notion.com/v1/pages \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{
    "parent": {
      "database_id": "'"$NOTION_DB_ID"'"
    },
    "properties": {
      "Name": {
        "title": [{
          "text": {
            "content": "Test Entry from Script"
          }
        }]
      },
      "Type": { "select": { "name": "Statement" }},
      "Entity": { "multi_select": [{ "name": "Nick Bianchi" }] },
      "Claim": {
        "rich_text": [{ "text": { "content": "This is a test pushed via shell script." }}]
      },
      "Weight": { "select": { "name": "Strong" }},
      "Status": { "select": { "name": "Draft" }},
      "Notes": {
        "rich_text": [{ "text": { "content": "Automated push from bash." }}]
      }
    }
  }'

