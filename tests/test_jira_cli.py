""" Test jira-cli functionalities"""

from mock import patch, PropertyMock

from atlassian_cli import JIRA_CLI_PROG
from atlassian_cli.atlassian.jira.models import (User, Issue)

from atlassian_cli.jira_cli import main as jira_main
from atlassian_cli.config.models import User as ConfigUser

# pylint: disable=R0201, C0122

@patch('keyring.get_password')
class JiraCLITestCase:
    """ basic CLI testing class """

    USERS = [
        ConfigUser({
            "createdAt": "2018-02-19T20:01:54Z",
            "default": True,
            "url": "https://foobarbaz.com",
            "username": "johndoe"
        })
    ]

    @patch('sys.argv', [JIRA_CLI_PROG, 'myself'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.myself')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_user')
    @patch('atlassian_cli.config.UserConfig.users',
           create=True,
           new_callable=PropertyMock,
           return_value=USERS)
    def test_arg_myself(self, mock_userconfig_users, mock_format, mock_myself, mock_keyring):
        # pylint: disable=W0613
        """ test myself argument """
        user = User({
            'active': True,
            'emailAddress': 'johndoe@example.com',
            'name': 'johndoe',
            'displayName': 'John Doe'
        })
        mock_myself.return_value = user
        jira_main()
        mock_format.assert_called_with(user)

    @patch('sys.argv', [JIRA_CLI_PROG, 'issue', 'ABC-12345'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.issue')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_issue')
    @patch('atlassian_cli.config.UserConfig.users',
           create=True,
           new_callable=PropertyMock,
           return_value=USERS)
    def test_arg_issue(self, mock_userconfig_users, mock_format, mock_issue, mock_keyring):
        # pylint: disable=W0613
        """ Test issue argument """
        issue = Issue({
            'id': '1',
            'key:': 'ABC-12345'
        })
        mock_issue.return_value = issue
        jira_main()
        mock_format.assert_called_with(issue)
