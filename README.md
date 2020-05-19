Class abstraction of an application oauth flow, where the access token is persisted as a file. The token is encrypted using a custom encryption key to avoid persisting the key itself.

# How to use

```python
from oauth_encrypt.token import EncryptedOauth2Client
from os import environ
import yaml

config = {
    "token_url": "provider.com/token",
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "scope": "your.scope",
    "encryptionkey": "long-and-complicated-encryption-key",
}

client = EncryptedOauth2Client(config)


def main():
    """Example using Encrypted Reusable Oauth Client"""
    args = {"foo": "bar}
    r = client.get(
        environ["REQUEST_URL"], params=args
    )


if __name__ == "__main__":
    main()
```
