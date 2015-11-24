import requests


class API(object):
    """ Angellist API Object """
    API_HOST = 'https://api.angel.co/'
    API_ROOT = '/1/'

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

    def get_startup(self, id):
        """
        Get a startup given an id
        """
        url = '{0}{1}'.format(self.startups_root_url, id)
        params = {}
        response = requests.get(self.access_tokenize(url), params)
        return response
