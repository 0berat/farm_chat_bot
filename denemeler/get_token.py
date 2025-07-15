from google_auth_oauthlib.flow import InstalledAppFlow

# Google Cloud’dan indirdiğin JSON dosyasının adı
CLIENT_SECRETS_FILE = "client_secret.json"

SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]

def main():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    print("Access Token:", creds.token)

if __name__ == "__main__":
    main()
