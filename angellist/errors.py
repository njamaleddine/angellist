
from __future__ import print_function


class AngellistError(Exception):

    def __init__(self, error_description, response=None):
        # self.error = error
        self.error_description = error_description
        Exception.__init__(self, error_description)

    def __str__(self):
        return self.error_description
