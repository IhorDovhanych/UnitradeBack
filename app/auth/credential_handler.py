import os.path
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport import Request
import json

SCOPES = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

def request_creds():
    creds = None
    if os.path.exists("auth/creds.json"):
        flow = InstalledAppFlow.from_client_secrets_file("auth/creds.json", SCOPES)
        creds = flow.run_local_server(port=0)
        return Credentials.from_authorized_user_info(json.loads(creds.to_json()), SCOPES)
    else:
        print("Credentials not present")
        sys.exit(1)

def get_creds(token=None):
    if token:
        creds = Credentials.from_authorized_user_info(token, SCOPES)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        return creds
    return request_creds()