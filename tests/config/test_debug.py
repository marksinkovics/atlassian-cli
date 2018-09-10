""" Test debug config  """

from datetime import datetime, date
import json
import pytest
from mock import patch, PropertyMock, mock_open

from atlassian_cli.config.models import Debug
from atlassian_cli.config import DebugConfig
from atlassian_cli.metadata import (
    CONFIG_FOLDER,
)

# pylint: disable=R0201

class DebugConfigTestCase:
    """ Test DebugConfig """

    DEBUG_CONFIG_DATA = {
        "log_level": 1,
        "show_arguments": True,
        "show_elapsed_time": True,
        "show_received_bytes": True
    }

    DEBUG_CONFIG_JSON = json.dumps(DEBUG_CONFIG_DATA, ensure_ascii=False)
    INVALID_DEBUG_CONFIG_JSON = '{[INVALID_JSON'
    CONFIG = Debug(DEBUG_CONFIG_DATA)

    @patch('atlassian_cli.config.DebugConfig.name', new_callable=PropertyMock)
    def test_name(self, mock_name):
        """ Test config name function """
        mock_name.return_value = 'debug'
        config = DebugConfig()
        assert config.name == 'debug'

    @patch('atlassian_cli.config.DebugConfig.help', new_callable=PropertyMock)
    def test_help(self, mock_help):
        """ Test config help function """
        mock_help.return_value = 'help'
        config = DebugConfig()
        assert config.help == 'help'

    def test_parser(self):
        """ test parser creation """
        pass

    @patch('atlassian_cli.config.DebugConfig.config_folder_name', 'config')
    @patch('os.path.expanduser', return_value='/home/test')
    @patch('atlassian_cli.config.DebugConfig.prepare_config_path')
    def test_config_folder(self, mock_prepare, mock_expanduser):
        # pylint: disable=W0613
        """ test default config folder path """
        expected_value = '/home/test/config'
        config = DebugConfig()
        assert config.config_folder == expected_value

    @patch('atlassian_cli.config.DebugConfig.config_folder_name', 'config')
    @patch('atlassian_cli.config.DebugConfig.config_file_name', 'file.json')
    @patch('os.path.expanduser', return_value='/home/test')
    @patch('atlassian_cli.config.DebugConfig.prepare_config_path')
    def test_config_file(self, mock_prepare, mock_expanduser):
        # pylint: disable=W0613
        """ test default config file path """
        expected_value = '/home/test/config/file.json'
        config = DebugConfig()
        assert config.config_file == expected_value

    @patch('atlassian_cli.config.DebugConfig.config_folder_name', 'config')
    @patch('atlassian_cli.config.DebugConfig.config_file_name', 'file.json')
    @patch('os.path.expanduser', return_value='/home/test')
    @patch('os.path.exists', return_value=False)
    @patch('atlassian_cli.config.DebugConfig.prepare_config_path')
    @patch('os.makedirs')
    def test_read_missing_file(self, mock_makedirs, mock_prepare, mock_exists, mock_expanduser, capsys):
        # pylint: disable=W0613
        """ test missing config file """
        config = DebugConfig()
        config.read()
        _, err = capsys.readouterr()
        assert err == 'Config file (/home/test/config/file.json) is missing\n'

    @patch('os.path.exists')
    @patch('builtins.open')
    @patch('atlassian_cli.config.DebugConfig.prepare_config_path')
    def test_read(self, mock_prepare, mock_builtins_open, mock_exists):
        # pylint: disable=W0613
        """ test config file reading """
        mock_builtins_open.return_value = mock_open(read_data=self.DEBUG_CONFIG_JSON).return_value
        mock_exists.return_value = True
        config = DebugConfig()
        config.read()
        assert config.config.show_arguments
        assert config.config.show_received_bytes
        assert config.config.show_elapsed_time
        assert config.config.log_level == 1

    @patch('os.path.exists')
    @patch('builtins.open', mock_open(read_data=INVALID_DEBUG_CONFIG_JSON))
    @patch('atlassian_cli.config.DebugConfig.prepare_config_path')
    def test_read_invalid_data(self, mock_prepare, mock_exists, capsys):
        # pylint: disable=W0613
        """ test invalid config data """
        mock_exists.return_value = True
        config = DebugConfig()
        config.read()
        out, _ = capsys.readouterr()
        assert config.config
        assert not config.config.show_arguments
        assert not config.config.show_received_bytes
        assert not config.config.show_elapsed_time
        assert config.config.log_level == 0
        assert out.startswith('Loading JSON has failed: ')

    @patch('json.dump')
    @patch('builtins.open')
    @patch('atlassian_cli.config.DebugConfig.prepare_config_path')
    def test_write(self, mock_prepare, mock_builtins_open, mock_json_dump):
        # pylint: disable=W0613
        """ test config file writing """
        config = DebugConfig()
        config.config = self.CONFIG
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
