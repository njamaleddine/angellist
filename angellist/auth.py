from urllib.parse import urlencode

import requests

from .config import config
from .exceptions import AngellistError


class Authentication:
    OAUTH_API_URL = config.get('OAUTH_API_URL')
    OAUTH_PATH = config.get('OAUTH_PATH')

    def __init__(self, client_id, client_secret, access_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.code = None

    @property
    def oauth_url(self):
        return '{0}{1}'.format(self.OAUTH_API_URL, self.OAUTH_PATH)

    def get_authorization_code(self, state_variable=None):
        """
        Get the authorization code

        state_variable (str): is used to maintain state between requests. (Not required).
        """
        url = '{oauth_url}{path}'.format(oauth_url=self.oauth_url, path='authorize')
        params = {
            'client_id': self.client_id,
            'response_type': 'code'
        }
        if state_variable:
            params['state'] = state_variable

        try:
            response = requests.get(url, params)
            return response.json().get('code')
        except Exception as e:
            raise AngellistError(e.message)

    def get_access_token(self):
        url = '{oauth_url}{path}'.format(oauth_url=self.oauth_url, path='token')
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': self.code,
            'grant_type': 'authorization_code'
        }

        parameterized_url = '{url}?{params}'.format(
            url=url, params=urlencode(params)
        )

        try:
            response = requests.post(parameterized_url)
            return response.json().get('access_token')
        except Exception as e:
            raise AngellistError(e)
