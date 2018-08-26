""" Test jira-cli functionalities"""

from mock import patch
import pytest

from atlassian_cli.jira_cli import main as jira_main
from atlassian_cli import JIRA_CLI_PROG
from atlassian_cli.atlassian.jira.models import (
    User,
    Issue
)


# pylint: disable=R0201, C0122

class JiraCLITestCase:
    """ basic CLI testing class """

    @pytest.mark.skip(reason="User config file has to be mocked. Temporarily skipped.")
    @patch('sys.argv', [JIRA_CLI_PROG, 'myself'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.myself')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.formatUser')
    def test_arg_myself(self, mock_format, mock_myself):
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

    @pytest.mark.skip(reason="User config file has to be mocked. Temporarily skipped.")
    @patch('sys.argv', [JIRA_CLI_PROG, 'issue', 'ABC-12345'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.issue')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.formatIssue')
    def test_arg_issue(self, mock_format, mock_issue):
        """ Test issue argument """
        issue = Issue({
            'id': '1',
            'key:': 'ABC-12345'
        })
        mock_issue.return_value = issue
        jira_main()
        mock_format.assert_called_with(issue)
