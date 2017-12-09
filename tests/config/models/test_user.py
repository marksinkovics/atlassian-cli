""" Test for user model """

import pytest
from mock import patch

from atlassian_cli.config.models import User
from atlassian_cli.metadata import SERVICE_IDENTIFIER

# pylint: disable=R0201

@pytest.mark.parametrize("user", [
    User({
        'username': 'johndoe',
        'url': 'https://example.com'
    })
])

class UserModelTestCase:
    """" Test case for model testing """

    def test_init(self, user):
        """ Test model creation """
        assert user.url == 'https://example.com'
        assert user.username == 'johndoe'

    def test_model_id(self, user):
        #pylint: disable=unused-argument
        """ Test model id generation """
        assert user.model_id == 'johndoe@https://example.com'

    @patch('keyring.get_password')
    def test_password_getter(self, keyring_mock, user):
        #pylint: disable=unused-argument
        """ Test pwd reading """
        secret_pwd = 'secretpwd1234'
        keyring_mock.return_value = secret_pwd
        assert user.password == secret_pwd

    @patch('keyring.set_password')
    def test_password_setter(self, keyring_mock, user):
        #pylint: disable=unused-argument
        """ Test pwd seting """
        secret_pwd = 'secretpwd1234'
        user.password = secret_pwd
        keyring_mock.assert_called_with(SERVICE_IDENTIFIER, user.model_id, secret_pwd)

    @patch('keyring.delete_password')
    @patch('keyring.get_password')
    def test_password_del(self, keyring_get_mock, keyring_del_mock, user):
        #pylint: disable=unused-argument
        """ Test pwd deleting """
        keyring_get_mock.return_value = True
        user.password = None
        keyring_get_mock.assert_called_with(SERVICE_IDENTIFIER, user.model_id)
        keyring_del_mock.assert_called_with(SERVICE_IDENTIFIER, user.model_id)

    @patch('keyring.delete_password')
    @patch('keyring.get_password')
    def test_password_del_failed(self, keyring_get_mock, keyring_del_mock, user):
        #pylint: disable=unused-argument
        """ Test pwd delete failing """
        keyring_get_mock.return_value = False
        user.password = None
        keyring_get_mock.assert_called_with(SERVICE_IDENTIFIER, user.model_id)
        assert not keyring_del_mock.called

    def test_equality(self, user):
        #pylint: disable=unused-argument
        """ Test equality """
        assert user == user

    def test_stringify(self, user):
        """ Test stringify """
        expected = '{}@{}'.format(user.username, user.url)
        assert expected == str(user)
