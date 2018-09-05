""" Test basic CLI functionalities"""

import json
import pytest
from mock import patch, mock_open

from atlassian_cli.bitbucket_cli import main as bitbucket_main
from atlassian_cli.jira_cli import main as jira_main

from atlassian_cli import (
    BITBUCKET_CLI_PROG,
    JIRA_CLI_PROG
)
from atlassian_cli.metadata import APPLICATION_VERSION

# pylint: disable=R0201, C0122, W0108

@pytest.mark.parametrize("prog,main", [
    (BITBUCKET_CLI_PROG, (lambda: bitbucket_main())),
    (JIRA_CLI_PROG, (lambda: jira_main())),
])
class CLITestCase:
    """ basic CLI testing class """

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', mock_open(read_data=b'    '))
    def test_with_empty_args(self, mock_builtins_open, capsys, prog, main):
        """ test with empty arguments """
        with pytest.raises(SystemExit):
            main()
        _, err = capsys.readouterr()
        assert err.startswith('usage: {}'.format(prog))

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', mock_open(read_data=b'    '))
    def test_invalid_args(self, mock_builtins_open, prog, main, capsys):
        "test with invalid command"
        with pytest.raises(SystemExit):
            with patch('sys.argv', [prog, 'hello']):
                main()
        _, err = capsys.readouterr()
        assert err.startswith('usage: {}'.format(prog))

    def test_arg_version(self, prog, main, capsys):
        "test with --version argument"
        with pytest.raises(SystemExit):
            with patch('sys.argv', [prog, '--version']):
                main()
        out, _ = capsys.readouterr()
        assert out == '{} (version {})\n'.format(prog, APPLICATION_VERSION)

    def test_arg_help(self, prog, main, capsys):
        "test with --help argument"
        with pytest.raises(SystemExit):
            with patch('sys.argv', [prog, '--help']):
                main()
        out, _ = capsys.readouterr()
        assert out.startswith('usage: {}'.format(prog))
