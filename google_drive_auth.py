from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def get_drive_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret_1_187458330646-nffgjrk5db0bb5qnpuc5oe832h4f14ns.apps.googleusercontent.com.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('drive', 'v3', credentials=creds)
    return service

