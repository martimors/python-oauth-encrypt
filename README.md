Class abstraction of an application oauth flow, where the access token is persisted as a file. The token is encrypted using a custom encryption key to avoid persisting the key itself.

# How to use

```python
from oauth_encrypt.token import EncryptedOauth2Client
from os import environ
import yaml

config = {
    "token_url": environ["TOKEN_URL"],
    "client_id": environ["CLIENT_ID"],
    "client_secret": environ["CLIENT_SECRET"],
    "scope": environ["SCOPE"],
    "encryptionkey": environ["ENCRYPTION_KEY"],
}

client = EncryptedOauth2Client(config)


def main():
    """Example using Encrypted Reusable Oauth Client"""
    # Read YAML file with arguments
    with open("args.yaml", "r") as stream:
        args = yaml.safe_load(stream)

    r = client.get(
        environ["REQUEST_URL"], params=args
    )

    print(f"Retrieved {len(r['elements'])} entries")


if __name__ == "__main__":
    main()
```
