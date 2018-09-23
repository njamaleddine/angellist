
import os


config = {
    'API_URL': os.environ.get('ANGELLIST_API_URL', 'https://api.angel.co/1/'),
    'CLIENT_ID': os.environ.get('ANGELLIST_CLIENT_ID', None),
    'CLIENT_SECRET': os.environ.get('ANGELLIST_CLIENT_SECRET', None),
    'CONNECTION_TIMEOUT': os.environ.get('ANGELLIST_CONNECTION_TIMEOUT', 60),
    'OAUTH_API_URL': os.environ.get('ANGELLIST_OAUTH_API_URL', 'https://angel.co/api/'),
    'OAUTH_PATH': os.environ.get('ANGELLIST_OAUTH_API_URL', 'oauth/'),
}
