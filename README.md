Class abstraction of an application oauth flow, where the access token is persisted as a file. The token is encrypted using a custom encryption key to avoid persisting the key itself.

The reason I made this is because OAuth2 tokens cost money, thus it is a good idea to use the token until it expires. The token is persisted (encrypted) between runs of the parent code such that the token is completely reusable.

# How to use

```python
from oauth_encrypt.client import EncryptedOauth2Client

# Example credentials and encryption
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
    # Get and print an access token
    r = client.access_token
    print(r)

    # Make a get request
    print(client.get("protected.com"))

if __name__ == "__main__":
    # This can be run as many times as you want, it will only get a new
    # token when the previous one has expired
    main()

```
