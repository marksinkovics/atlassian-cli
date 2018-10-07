""" Test jira-cli functionalities"""

from mock import patch, PropertyMock

from atlassian_cli import JIRA_CLI_PROG

from atlassian_cli.jira_cli import main as jira_main
from tests.mock.jira.models import (
    USERS,
    MYSELF,
    ISSUES, ISSUE,
    BOARDS, BOARD,
    SPRINTS, SPRINT,
    EPICS, EPIC
)

# pylint: disable=R0201, C0122

@patch('keyring.get_password')
@patch('atlassian_cli.config.UserConfig.users',
       create=True,
       new_callable=PropertyMock,
       return_value=USERS)
class JiraCLITestCase:
    # pylint: disable=C0301
    """ basic CLI testing class """

    #
    #   Myself
    #

    @patch('sys.argv', [JIRA_CLI_PROG, 'myself'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.myself')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_user')
    def test_arg_myself(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613
        """ test myself argument """
        mock_service.return_value = MYSELF
        jira_main()
        mock_format.assert_called_with(MYSELF)

    #
    #   Issue
    #

    @patch('sys.argv', [JIRA_CLI_PROG, 'issue', 'ABC-1'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.issue')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_issue')
    def test_arg_issue(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613
        """ Test issue argument """
        mock_service.return_value = ISSUE
        jira_main()
        mock_format.assert_called_with(ISSUE)

    #
    #   JQL
    #

    @patch('sys.argv', [JIRA_CLI_PROG, 'jql', 'a'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.jql')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_issues')
    def test_arg_jql(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613
        """ Test jql argument """
        mock_service.return_value = iter([ISSUES])
        jira_main()
        mock_format.assert_called_with(ISSUES)

    #
    #   Board
    #

    @patch('sys.argv', [JIRA_CLI_PROG, 'boards'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.boards')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_boards')
    def test_arg_boards(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613,R0913
        """ Test board argument """
        mock_service.return_value = iter([BOARDS])
        jira_main()
        mock_format.assert_called_with(BOARDS)

    @patch('sys.argv', [JIRA_CLI_PROG, 'board', '1'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.board')
    @patch('atlassian_cli.atlassian.jira.service.JiraService.sprints')
    @patch('atlassian_cli.atlassian.jira.service.JiraService.epics')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_board')
    def test_arg_board(self, mock_format, mock_epics, mock_sprints, mock_board, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613,R0913
        """ Test board argument """
        mock_board.return_value = BOARD
        mock_epics.return_value = iter([])
        mock_sprints.return_value = iter([])
        jira_main()
        mock_format.assert_called_with(BOARD)
        mock_sprints.assert_called_with('{}'.format(BOARD.id_))
        mock_epics.assert_called_with('{}'.format(BOARD.id_))

    #
    #   Sprint
    #

    @patch('sys.argv', [JIRA_CLI_PROG, 'sprints', '1'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.sprints')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_sprints')
    def test_arg_sprints(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613,R0913
        """ Test board argument """
        mock_service.return_value = iter([SPRINTS])
        jira_main()
        mock_format.assert_called_with(SPRINTS)


    @patch('sys.argv', [JIRA_CLI_PROG, 'sprint', '12345'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.sprint')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_sprint')
    def test_arg_sprint(self, mock_format, mock_sprint, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613
        """ Test sprint argument """
        mock_sprint.return_value = SPRINT
        jira_main()
        mock_format.assert_called_with(SPRINT)

    @patch('sys.argv', [JIRA_CLI_PROG, 'sprint', '12345', 'issues'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.sprint_issues')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_issues')
    def test_arg_sprint_issues(self, mock_format, mock_sprint, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613
        """ Test sprint argument """
        mock_sprint.return_value = iter([ISSUES])
        jira_main()
        mock_format.assert_called_with(ISSUES)


    #
    # Epic
    #

    @patch('sys.argv', [JIRA_CLI_PROG, 'epics', '1'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.epics')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_epics')
    def test_arg_epics(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613,R0913
        """ Test board argument """
        mock_service.return_value = iter([EPICS])
        jira_main()
        mock_format.assert_called_with(EPICS)



    @patch('sys.argv', [JIRA_CLI_PROG, 'epic', '12345'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.epic')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_epic')
    def test_arg_epic(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613
        """ Test epic argument """
        mock_service.return_value = EPIC
        jira_main()
        mock_format.assert_called_with(EPIC)

    @patch('sys.argv', [JIRA_CLI_PROG, 'epic', '12345', 'issues'])
    @patch('atlassian_cli.atlassian.jira.service.JiraService.epic_issues')
    @patch('atlassian_cli.atlassian.jira.formatters.Simple.format_issues')
    def test_arg_epic_issues(self, mock_format, mock_service, mock_userconfig_users, mock_keyring):
        # pylint: disable=W0613
        """ Test epic argument """
        mock_service.return_value = iter([ISSUES])
        jira_main()
        mock_format.assert_called_with(ISSUES)
