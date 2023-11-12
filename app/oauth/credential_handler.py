import os.path
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport import Request

SCOPES = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]


def request_creds():
    creds = None
    if os.path.exists("core/creds.json"):
        flow = InstalledAppFlow.from_client_secrets_file("core/creds.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("core/token.json", "w") as token:
            token.write(creds.to_json())
        return Credentials.from_authorized_user_file("core/token.json", SCOPES)
    else:
        print("Credentials not present")
        sys.exit(1)


def get_creds():
    if os.path.exists("core/token.json"):
        creds = Credentials.from_authorized_user_file("core/token.json", SCOPES)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        return creds
    return request_creds()
