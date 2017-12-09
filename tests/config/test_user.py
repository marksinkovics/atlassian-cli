""" Test user config  """

from datetime import datetime, date
import json
import pytest
from mock import patch, PropertyMock, mock_open

from atlassian_cli.config.models import User
from atlassian_cli.config import UserConfig
from atlassian_cli.metadata import (
    CONFIG_FOLDER,
)

# pylint: disable=R0201

class UserConfigTestCase:
    """ Test UserConfig """

    USER_CONFIG_DATA = [
        {
            "createdAt": "2018-02-18T20:12:05Z",
            "default": False,
            # "updatedAt": datetime(2018, 2, 18, 20, 12, 5),
            "url": "https://example.com",
            "username": "user1"
        },
        {
            "createdAt": "2018-02-19T20:01:54Z",
            "default": True,
            # "updatedAt": datetime(2018, 2, 19, 20, 1, 54),
            "url": "https://foobarbaz.com",
            "username": "user2"
        }
    ]
    USER_CONFIG_JSON = json.dumps(USER_CONFIG_DATA, ensure_ascii=False)
    INVALID_USER_CONFIG_JSON = '{[INVALID_JSON'
    USERS = list(map(User, USER_CONFIG_DATA))

    @patch('atlassian_cli.config.UserConfig.name', new_callable=PropertyMock)
    def test_name(self, mock_name):
        """ Test config name function """
        mock_name.return_value = 'name'
        config = UserConfig()
        assert config.name == 'name'

    @patch('atlassian_cli.config.UserConfig.help', new_callable=PropertyMock)
    def test_help(self, mock_help):
        """ Test config help function """
        mock_help.return_value = 'help'
        config = UserConfig()
        assert config.help == 'help'

    def test_parser(self):
        """ test parser creation """
        pass

    @patch('atlassian_cli.config.UserConfig.config_folder_name', 'config')
    @patch('os.path.expanduser', return_value='/home/test')
    @patch('atlassian_cli.config.UserConfig.prepare_config_path')
    def test_config_folder(self, mock_prepare, mock_expanduser):
        # pylint: disable=W0613
        """ test default config folder path """
        expected_value = '/home/test/config'
        config = UserConfig()
        assert config.config_folder == expected_value

    @patch('atlassian_cli.config.UserConfig.config_folder_name', 'config')
    @patch('atlassian_cli.config.UserConfig.config_file_name', 'file.json')
    @patch('os.path.expanduser', return_value='/home/test')
    @patch('atlassian_cli.config.UserConfig.prepare_config_path')
    def test_config_file(self, mock_prepare, mock_expanduser):
        # pylint: disable=W0613
        """ test default config file path """
        expected_value = '/home/test/config/file.json'
        config = UserConfig()
        assert config.config_file == expected_value

    @patch('atlassian_cli.config.UserConfig.config_file', new_callable=PropertyMock)
    @patch('os.path.exists')
    @patch('atlassian_cli.config.UserConfig.prepare_config_path')
    def test_read_missing_file(self, mock_prepare, mock_exists, mock_config_file, capsys):
        # pylint: disable=W0613
        """ test missing config file """
        mock_exists.return_value = False
        mock_config_file.return_value = 'file.json'
        config = UserConfig()
        config.read()
        out, _ = capsys.readouterr()
        assert out == 'Config file (file.json) is missing\n'

    @patch('os.path.exists')
    @patch('builtins.open')
    @patch('atlassian_cli.config.UserConfig.prepare_config_path')
    def test_read(self, mock_prepare, mock_builtins_open, mock_exists):
        # pylint: disable=W0613
        """ test config file reading """
        mock_builtins_open.return_value = mock_open(read_data=self.USER_CONFIG_JSON).return_value
        mock_exists.return_value = True
        config = UserConfig()
        config.read()
        assert len(config.users) == 2

    @patch('os.path.exists')
    @patch('builtins.open', mock_open(read_data=INVALID_USER_CONFIG_JSON))
    @patch('atlassian_cli.config.UserConfig.prepare_config_path')
    def test_read_invalid_data(self, mock_prepare, mock_exists, capsys):
        # pylint: disable=W0613
        """ test invalid config data """
        mock_exists.return_value = True
        config = UserConfig()
        config.read()
        out, _ = capsys.readouterr()
        assert not config.users
        assert out.startswith('Loading JSON has failed: ')

    @patch('json.dump')
    @patch('builtins.open')
    @patch('atlassian_cli.config.UserConfig.prepare_config_path')
    def test_write(self, mock_prepare, mock_builtins_open, mock_json_dump):
        # pylint: disable=W0613
        """ test config file writing """
        config = UserConfig()
        config.users = self.USERS
        config.write()
        assert mock_json_dump.called

    def test_parse(self):
        """ test parsing """
        pass

    def test_parse_set(self):
        """ test set command parsing """
        pass

    def test_parse_remove(self):
        """ test remove command parsing """
        pass

    def test_parse_setdefault(self):
        """ test setdefault command parsing """
        pass

    def test_parse_list(self):
        """ test list command parsing """
        pass

    def test_default_user(self):
        """ test default_user"""
        pass
