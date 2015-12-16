from __future__ import print_function, unicode_literals

import requests

from errors import AngellistError


class Authentication(object):
    OAUTH_API_URL = 'https://angel.co/api/'
    OAUTH_PATH = 'oauth/'

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
        url = '{0}{1}'.format(self.oauth_url, 'authorize')
        params = {
            'client_id': self.client_id,
            'response_type': 'code'
        }
        if state_variable:
            params['state'] = state_variable

        response = requests.get(url, params)

        try:
            data = response.json()
            code = data['code']
            return response
        except Exception as e:
            print(response.json())
            raise AngellistError(e.message)

    def get_access_token(self):
        url = '{0}{1}'.format(self.get_oauth_url(), 'token')
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': self.code,
            'grant_type': 'authorization_code'
        }

        response = requests.get(url, params)

        try:
            data = response.json()
            access_token = data['access_token']
            return access_token
        except Exception as e:
            print(response.json())
            raise AngellistError(e)
