from os import environ
from pathlib import Path
import json
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
from cryptography.fernet import Fernet


class EncryptedOauth2Client:
    def __init__(self, config):
        # Read the reqired env variables
        self._set_config_variables(config)

        # Read the credentials if they exist, otherwise get new token
        if Path("access_key.credential").exists():
            self._read_token()
        else:
            self._get_fresh_token()

    def _set_config_variables(self, config):
        """This unpacks the config object to class attributes"""
        self._token_url = config["token_url"]
        self._client_id = config["client_id"]
        self._client_secret = config["client_secret"]
        self._scope = config["scope"]
        self._encryptionkey = Fernet(config["encryptionkey"])

    def _get_fresh_token(self):
        """Get a new oauth token"""
        # Set up the oauth2.0 session
        _client = BackendApplicationClient(client_id=self._client_id)
        _session = OAuth2Session(client=_client)
        self._access_token = _session.fetch_token(
            token_url=self._token_url,
            client_id=self._client_id,
            client_secret=self._client_secret,
        )
        self._save_token()

    def _save_token(self):
        encrypted_token = self._encryptionkey.encrypt(
            json.dumps(self._access_token).encode("UTF-8")
        )
        # write the encrypted file
        with open(Path("access_key.credential"), "wb") as file:
            file.write(encrypted_token)

    def _read_token(self):
        with open(Path("access_key.credential"), "rb") as file:
            # read all file data
            file_data = file.read()
        self._access_token = json.loads(
            self._encryptionkey.decrypt(file_data).decode("UTF-8")
        )

    def get(self, url, params):
        """Send a get-request to a url"""
        try:
            client = OAuth2Session(self._client_id, token=self._access_token)
            r = client.get(url, params=params)
        except TokenExpiredError:
            self._get_fresh_token()
            client = OAuth2Session(self._client_id, token=self._access_token)
            r = client.get(url, params=params)

        # Raise errors if any
        r.raise_for_status()

        # Return payload as dictionary
        return r.json()

    @property
    def access_token(self):
        """Get the current access token"""
        return self._access_token
