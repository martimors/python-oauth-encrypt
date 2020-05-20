from oauth_encrypt.client import EncryptedOauth2Client

# Example credentials and encryption, do not use in production environments
config = {
    "token_url": "lol.com/token",
    "client_id": "something",
    "client_secret": "something_else",
    "scope": "my.scope",
    "encryptionkey": "nDtagLlBTMJBilyIgYTYELAUmZD39hnGa6XaLwlhRVQ=",
}

client = EncryptedOauth2Client(config)


def main():
    """Example using Encrypted Reusable Oauth Client"""
    # Make a get request
    print(client.get("protected.com"))

if __name__ == "__main__":
    main()
