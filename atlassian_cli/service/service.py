""" Represent a basic form of Service module  """

import sys

import requests
from requests.auth import HTTPBasicAuth

# pylint: disable=too-few-public-methods
class Authentication:
    """ Base class of Authentication """
    def __init__(self, model):
        self.model = model

    def auth(self):
        # pylint: disable=R0201
        """ Create a requests module authentication """
        return None

class BasicAuthentication(Authentication): # pylint: disable=too-few-public-methods
    """
        Represent an authentication specialization
        for HTTP basic authentication
    """

    def auth(self):
        """ Create a requests module Basic authentication """
        return HTTPBasicAuth(self.model.username, self.model.password)

class Service(requests.Session):
    """
        Specialize requests.Session to be able to use
        own authentication class
    """
    def __init__(self, authentication, **kwargs):
        super().__init__(**kwargs)
        self.auth = authentication.auth()
        self.debug = None

    def get(self, url, **kwargs):
        try:
            response = super().get(url, **kwargs, allow_redirects=False)
            if response.status_code == 301: # Redirect in progress
                redirect_url = response.headers['Location']
                response = super().get(redirect_url, **kwargs, allow_redirects=False)
            response.raise_for_status()
        except requests.exceptions.RequestException as exp:
            print(exp)
            sys.exit(1)
        return response
