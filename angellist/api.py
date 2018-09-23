import requests

from .auth import Authentication
from .classes import Startup, Comment, StartupRole, User
from .config import config
from .exceptions import AuthenticationError


class AngelList:
    """ Angellist API Object """

    def __init__(self, authentication=None, api_url=config.get('API_URL')):
        self.auth = self._authenticate(authentication)
        self.api_url = api_url

    def _authenticate(self, authentication=None):
        if isinstance(authentication, Authentication) and authentication.access_token:
            return authentication
        else:
            cliend_id = config.get('CLIENT_ID')
            client_secret = config.get('CLIENT_SECRET')

            if cliend_id and client_secret:
                authentication = Authentication(cliend_id, client_secret)
                authentication.get_access_token()
                return authentication
            raise AuthenticationError(
                'You must set both ANGELLIST_CLIENT_ID and ANGELLIST_CLIENT_SECRET '
                'in your environment variables if you want to authenticate without '
                'passing an Authentication object.'
            )

    def _access_tokenize(self, url):
        return '{url}?access_token={access_token}'.format(
            url=url,
            access_token=self.auth.access_token
        )

    @property
    def api_urls(self):
        return {
            'startups': '{api_url}startups/'.format(api_url=self.api_url),
            'users': '{api_url}users/'.format(api_url=self.api_url),
        }

    def _get_single_object(self, path, pk, params={}):
        """ Get a single object from the API """
        url = '{0}{1}'.format(path, pk)
        params = params
        response = requests.get(self._access_tokenize(url), params)
        return response

    def _get_multiple_objects(self, path, pk=None, list_route=None):
        url = path
        if pk and list_route:
            url = '{0}{1}/{2}'.format(path, pk, list_route)
        params = {}
        response = requests.get(self._access_tokenize(url), params)
        return response

    def _get_startup(self, pk):
        """
        Returns the response for getting a single startup from an pk
        """
        return self._get_single_object(path=self.api_urls['startups'], pk=pk)

    def get_startup(self, pk):
        """ Returns a Startup object with the given pk """
        return Startup(**self._get_startup(pk).json())

    def _get_startup_comments(self, pk):
        """ Get comments for a startup """
        list_route = 'comments'
        response = self._get_multiple_objects(
            path=self.api_urls['startups'], pk=pk, list_route=list_route
        )
        if response.status_code == 404:
            return None
        return response

    def get_startup_comments(self, pk):
        comments = []
        response = self._get_startup_comments(pk)
        if response:
            comments = [Comment(**comment) for comment in response.json()]
        return comments

    def _get_startup_roles(self, pk):
        """ Get roles in a startup """
        list_route = 'roles'
        response = self._get_multiple_objects(
            path=self.api_urls['startups'], pk=pk, list_route=list_route
        )
        if response.status_code == 404:
            return None
        return response

    def get_startup_roles(self, pk):
        roles = []
        response = self._get_startup_roles(pk)
        if response:
            roles = [StartupRole(**comment) for comment in response.json()]
        return roles

    def _get_user(self, pk, **kwargs):
        """
        Returns the response for getting a single startup from an pk
        """
        params = {}

        include_details = kwargs.get('include_details')
        if include_details:
            params['include_details'] = include_details
        return self._get_single_object(
            path=self.api_urls['users'], pk=pk, params=params
        )

    def get_user(self, pk):
        """ Returns a Startup object with the given pk """
        return User(**self._get_user(pk).json())

    def me(self):
        url = '{0}me'.format(self.api_url)
        params = {}
        response = requests.get(self._access_tokenize(url), params)
        return response
