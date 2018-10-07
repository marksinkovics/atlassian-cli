""" Test bitbucket-cli functionalities"""

from mock import patch, PropertyMock

from atlassian_cli.bitbucket_cli import main as bitbucket_main
from atlassian_cli import BITBUCKET_CLI_PROG
from tests.mock.bitbucket.models import (
    USERS,
    PROJECTS, PROJECT,
    PULLREQUESTS, PULLREQUEST
)

# pylint: disable=R0201, C0122

@patch('keyring.get_password')
@patch('atlassian_cli.config.UserConfig.users',
       create=True,
       new_callable=PropertyMock,
       return_value=USERS)
class BitbucketCLITestCase:
    """ basic CLI testing class """

    #
    #   Projects
    #

    @patch('sys.argv', [BITBUCKET_CLI_PROG, 'projects'])
    @patch('atlassian_cli.atlassian.bitbucket.service.BitbucketService.projects')
    @patch('atlassian_cli.atlassian.bitbucket.formatters.Simple.format_projects')
    def test_arg_projects(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613,R0913
        """ Test board argument """
        mock_service.return_value = iter([PROJECTS])
        bitbucket_main()
        mock_format.assert_called_with(PROJECTS)

    @patch('sys.argv', [BITBUCKET_CLI_PROG, 'project', '1'])
    @patch('atlassian_cli.atlassian.bitbucket.service.BitbucketService.project')
    @patch('atlassian_cli.atlassian.bitbucket.formatters.Simple.format_project')
    def test_arg_project(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613,R0913
        """ Test board argument """
        mock_service.return_value = PROJECT
        bitbucket_main()
        mock_format.assert_called_with(PROJECT)

    #
    #   My pull-requests
    #

    @patch('sys.argv', [BITBUCKET_CLI_PROG, 'my-pull-requests'])
    @patch('atlassian_cli.atlassian.bitbucket.service.BitbucketService.pull_requests')
    @patch('atlassian_cli.atlassian.bitbucket.formatters.Simple.format_pull_requests')
    def test_arg_my_prs(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613,R0913
        """ Test board argument """
        mock_service.return_value = iter([PULLREQUESTS])
        bitbucket_main()
        mock_format.assert_called_with(PULLREQUESTS)
