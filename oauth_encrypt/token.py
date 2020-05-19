from os import environ

class EncryptedToken:
    def __init__(self):
        # Read the reqired env variables
        self._set_config_variables()

        self._access_token = None
        pass

    def _set_config_variables(self):
        self._token_url = environ["TOKEN_URL"]
        self._client_id = environ["CLIENT_ID"]
        self._client_secret = environ["CLIENT_SECRET"]
        self._scope = environ["SCOPE"]

    def _get_fresh_token(self):
        """Get a new oauth token"""
        pass

    @staticmethod
    def _valid():
        """Check that the current token is valid"""
        return True

    @property
    def access_token(self):
        """Get the current access token"""
        return self._access_token
