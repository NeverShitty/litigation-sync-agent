def list_files(service):
    results = service.files().list(
        pageSize=100,
        fields="files(id, name, mimeType, modifiedTime)").execute()
    items = results.get('files', [])
    return items

def evaluate_file(file):
    score = 0
    name = file['name'].lower()
    if "aribia" in name or "bianchi" in name:
        score += 2
    if file['mimeType'] == 'application/vnd.google-apps.document':
        score += 1
    return score

# Drive connection
service = get_drive_service()
files = list_files(service)

for f in files:
    score = evaluate_file(f)
    print(f"{f['name']} (Score: {score})")

