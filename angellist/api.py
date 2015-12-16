import requests

from .classes import Startup, Comment, StartupRole, User


class API(object):
    """ Angellist API Object """
    API_HOST = 'https://api.angel.co/'
    API_ROOT = '1/'

    def __init__(self, authentication=None, host=API_HOST, api_root=API_ROOT):
        self.auth = authentication
        self.host = host
        self.api_root = api_root

    @property
    def api_url(self):
        return '{0}{1}'.format(self.host, self.api_root)

    def access_tokenize(self, url):
        if self.auth and self.auth.access_token:
            return '{0}?access_token={1}'.format(url, self.auth.access_token)

    @property
    def startups_root_url(self):
        return '{0}{1}{2}'.format(self.host, self.api_root, 'startups/')

    @property
    def users_root_url(self):
        return '{0}{1}{2}'.format(self.host, self.api_root, 'users/')

    def _get_single_object(self, path, pk, params={}):
        """ Get a single object from the API """
        url = '{0}{1}'.format(path, pk)
        params = params
        response = requests.get(self.access_tokenize(url), params)
        return response

    def _get_multiple_objects(self, path, pk=None, list_route=None):
        url = path
        if pk and list_route:
            url = '{0}{1}/{2}'.format(path, pk, list_route)
        params = {}
        response = requests.get(self.access_tokenize(url), params)
        return response

    def _get_startup(self, pk):
        """
        Returns the response for getting a single startup from an pk
        """
        return self._get_single_object(path=self.startups_root_url, pk=pk)

    def get_startup(self, pk):
        """ Returns a Startup object with the given pk """
        return Startup(**self._get_startup(pk).json())

    def _get_startup_comments(self, pk):
        """ Get comments for a startup """
        list_route = 'comments'
        response = self._get_multiple_objects(
            path=self.startups_root_url, pk=pk, list_route=list_route
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
            path=self.startups_root_url, pk=pk, list_route=list_route
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
            path=self.users_root_url, pk=pk, params=params
        )

    def get_user(self, pk):
        """ Returns a Startup object with the given pk """
        return User(**self._get_user(pk).json())

    def me(self):
        url = '{0}me'.format(self.api_url)
        params = {}
        response = requests.get(self.access_tokenize(url), params)
        return response
