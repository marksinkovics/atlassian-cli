""" Test basic Service functionalities"""

from mock import patch
import httpretty
import pytest
from requests.auth import HTTPBasicAuth

from atlassian_cli.service import (
    Authentication,
    BasicAuthentication,
    Service
)

from atlassian_cli.config.models import (
    User
)

# pylint: disable=R0201, C0122, R0903

@pytest.mark.parametrize("model", [
    User({"username": "johndoe", "url": "https://example.com"})
])
class AuthenticationTestCase:
    """ Authentication testing class """

    def test_simple_auth(self, model):
        # pylint: disable=W0613
        """ Test Auth generation """
        auth = Authentication(model).auth()
        assert not auth

    @patch('keyring.get_password')
    def test_basic_auth(self, keyring_mock, model):
        # pylint: disable=W0613
        """ Test HTTP Basic auth generation """
        secret_pwd = 'secretpwd1234'
        keyring_mock.return_value = secret_pwd
        expected = HTTPBasicAuth(model.username, model.password)
        auth = BasicAuthentication(model).auth()
        assert expected == auth

@pytest.mark.parametrize("model", [
    User({"username": "johndoe", "url": "https://example.com"})
])
class ServiceTestCase:
    """ Service testing class """

    @patch('keyring.get_password')
    def test_service_creation(self, keyring_mock, model):
        """ Test service creation """
        secret_pwd = 'secretpwd1234'
        keyring_mock.return_value = secret_pwd
        basic_auth_obj = BasicAuthentication(model)
        basic_auth = basic_auth_obj.auth()
        service = Service(basic_auth_obj)
        assert service.auth == basic_auth

    @patch('keyring.get_password')
    @httpretty.activate
    def test_get_200(self, keyring_mock, model):
        """ Test GET request """
        secret_pwd = 'secretpwd1234'
        keyring_mock.return_value = secret_pwd
        httpretty.register_uri(httpretty.GET, model.url, body='', status=200)
        service = Service(BasicAuthentication(model))
        response = service.get(model.url)
        assert response.status_code == 200
        assert response.text == ''

    @patch('keyring.get_password')
    @httpretty.activate
    def test_get_301_redirect(self, keyring_mock, model):
        """ Test redirecting """
        secret_pwd = 'secretpwd1234'
        keyring_mock.return_value = secret_pwd        
        redirect_url = 'http://redirect.example.com'
        httpretty.register_uri(httpretty.GET,
                               model.url,
                               status=301,
                               adding_headers={'Location': redirect_url})
        httpretty.register_uri(httpretty.GET, redirect_url, body='', status=200)
        service = Service(BasicAuthentication(model))
        response = service.get(model.url)
        assert response.status_code == 200
        assert response.text == ''

    @patch('keyring.get_password')
    @httpretty.activate
    def test_get_error(self, keyring_mock, model):
        """ Test GET request """
        secret_pwd = 'secretpwd1234'
        keyring_mock.return_value = secret_pwd
        httpretty.register_uri(httpretty.GET, model.url, body='', status=404)
        service = Service(BasicAuthentication(model))
        with pytest.raises(SystemExit):
            _ = service.get(model.url)
