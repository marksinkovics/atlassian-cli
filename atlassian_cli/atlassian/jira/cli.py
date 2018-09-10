""" Command line interface for Jira """

import atlassian_cli.metadata as jira_metadata
import atlassian_cli.config.metadata as config_metadata

from atlassian_cli.cli import CLI
from atlassian_cli.atlassian.jira.service import JiraService
from atlassian_cli.atlassian.jira.formatters import Simple

from atlassian_cli.config import ConfigCLI
from atlassian_cli.atlassian.jira.config import (
    JiraUserConfig,
    JiraDebugConfig
)

class JiraCLI(CLI):
    """ Jira command line interface controller class """

    def __init__(self,
                 add_help=True,
                 add_version=True,
                 prog=None):
        config_metadata.SERVICE_IDENTIFIER = jira_metadata.SERVICE_IDENTIFIER
        self.config_cli = ConfigCLI()
        self.config_cli.add_custom_subparser(JiraUserConfig())
        self.config_cli.add_custom_subparser(JiraDebugConfig())
        super().__init__(add_help=add_help, add_version=add_version, prog=prog)
        self.debug = JiraDebugConfig()
        self.debug.read()

    def create_subparser_config(self):
        """ Create config subparser """
        config_parser = self.subparsers.add_parser('config',
                                                   help='Config',
                                                   parents=[self.config_cli.parser])
        config_parser.set_defaults(subcommand='config')

    def create_subparser_myself(self):
        """ Create subparser for myself command """
        myself_help = 'Show information about current user (myself)'
        myself_parser = self.subparsers.add_parser('myself', help=myself_help)
        myself_parser.set_defaults(subcommand='myself')

    def create_subparser_issue(self):
        """ Create subparser for issue command """
        issue_help = 'Show issue by id'
        issue_parser = self.subparsers.add_parser('issue',
                                                  help=issue_help,
                                                  parents=[self.output_parent_parser])
        issue_parser.set_defaults(subcommand='issue')
        issue_parser.add_argument('issueId', help='issueId')

    def create_subparser_boards(self):
        """ Create subparser for boards command """
        boards_help = "Show available boards"
        boards_parser = self.subparsers.add_parser('boards',
                                                   help=boards_help,
                                                   parents=[self.output_parent_parser])
        boards_parser.set_defaults(subcommand='boards')

    def create_subparser_board(self):
        """ Create subparser for board command """
        board_help = 'Show a specific board by id'
        board_parser = self.subparsers.add_parser('board', 
                                                  help=board_help, 
                                                  parents=[self.output_parent_parser])
        board_parser.add_argument('boardId', action='store', help='boardId')
        board_parser.set_defaults(subcommand='board')

    def create_subparser_sprint(self):
        """ Create subparser for sprint command """
        sprints_help = 'Show sprints for a specific board'
        sprints_parser = self.subparsers.add_parser('sprints',
                                                    help=sprints_help,
                                                    parents=[self.output_parent_parser])
        sprints_parser.add_argument('boardId', help='boardId')
        sprints_parser.set_defaults(subcommand='sprints')

        sprint_help = 'Show details of a specific sprint'
        sprint_parser = self.subparsers.add_parser('sprint', help=sprint_help)
        sprint_parser.add_argument('sprintId', help='sprintId')
        sprint_parser.set_defaults(subcommand='sprint')
        sprint_subparsers = sprint_parser.add_subparsers()
        sprint_issue_parser = sprint_subparsers.add_parser('issues',
                                                           help='Issues for a specific sprint',
                                                           parents=[self.output_parent_parser])
        sprint_issue_parser.set_defaults(sprint_subcommand='issues')

    def create_subparser_epic(self):
        """ Create subparser for epic command """
        epics_help = "Show epics for a specific board"
        epics_parser = self.subparsers.add_parser('epics',
                                                  help=epics_help,
                                                  parents=[self.output_parent_parser])
        epics_parser.add_argument('boardId', help='boardId')
        epics_parser.set_defaults(subcommand='epics')

        epic_help = 'Show details of a specific epic'
        epic_parser = self.subparsers.add_parser('epic', help=epic_help)
        epic_parser.add_argument('epicId', help='epicId')
        epic_parser.set_defaults(subcommand='epic')
        epic_subparsers = epic_parser.add_subparsers()
        epic_issue_parser = epic_subparsers.add_parser('issues',
                                                       help='Issues for a specific epic',
                                                       parents=[self.output_parent_parser])
        epic_issue_parser.set_defaults(epic_subcommand='issues')

    def create_subparser_jql(self):
        """ Create subparser for sprint command """
        jql_parser = self.subparsers.add_parser('jql',
                                                help='Jira Query Language',
                                                parents=[self.output_parent_parser])
        jql_parser.set_defaults(subcommand='jql')
        jql_parser.add_argument('jql', help='jql')

    def create_subparser(self):
        """ Create subparsers """
        super().create_subparser()
        self.create_subparser_config()
        self.create_subparser_myself()
        self.create_subparser_issue()
        self.create_subparser_boards()
        self.create_subparser_board()
        self.create_subparser_sprint()
        self.create_subparser_epic()
        self.create_subparser_jql()

    def create_parser(self):
        super().create_parser()
        self.parser.set_defaults(command='jira')


    def parse_command(self, args):
        if super().parse_command(args):
            return

        if not hasattr(args, 'subcommand'):
            self.parser.print_help()
            return

        if args.subcommand != 'config':
            user_config = JiraUserConfig()
            user_config.read()
            if not user_config.users:
                print('There is not any valid user account.')
                return

            default_user = user_config.default_user()
            service = JiraService(default_user)
        else:
            service = None
        method_name = 'parse_{}'.format(args.subcommand)
        try:
            method = getattr(self, method_name)
        except AttributeError:
            raise NotImplementedError("Class `{}` does not implement `{}`"
                                      .format(self.__class__.__name__, method_name))
        method(service, args)

#
#   parse commands
#

    # pylint: disable=R0201

    def parse_config(self, service, args):
        """ Parse config command """
        # pylint: disable=W0613
        self.config_cli.parse(args)

    def parse_myself(self, service, args):
        # pylint: disable=W0613
        """ Parse myself command """
        formatter = Simple()
        user = service.myself()
        print(formatter.format_user(user))

    def parse_issue(self, service, args):
        """ Parse issue command """
        formatter = Simple()
        issue = service.issue(args.issueId)
        print(formatter.format_issue(issue))

    def parse_jql(self, service, args):
        """ Parse jql command """
        formatter = Simple(oneline=args.oneline)
        for issues in service.jql(args.jql):
            print(formatter.format_issues(issues))

    def parse_boards(self, service, args):
        """ Parse boards command """
        formatter = Simple(oneline=args.oneline)
        for boards in service.boards():
            print(formatter.format_boards(boards))

    def parse_board(self, service, args):
        """ Parse board command """
        formatter = Simple()
        board = service.board(args.boardId)
        print(formatter.format_board(board))
        if not args.oneline:
            print("=> Sprints: ")
            for sprints in service.sprints(args.boardId):
                print(formatter.format_sprints(sprints))
            print("=> Epics: ")
            for epics in service.epics(args.boardId):
                print(formatter.format_epics(epics))

    def parse_sprints(self, service, args):
        """ Parse sprints command """
        formatter = Simple(oneline=args.oneline)
        for sprints in service.sprints(args.boardId):
            print(formatter.format_sprints(sprints))

    def parse_sprint(self, service, args):
        """ Parse sprint command """
        if hasattr(args, 'sprint_subcommand'):
            if args.sprint_subcommand == 'issues':
                formatter = Simple(oneline=args.oneline)
                for issues in service.sprint_issues(args.sprintId):
                    print(formatter.format_issues(issues))
        else:
            formatter = Simple()
            sprint = service.sprint(args.sprintId)
            print(formatter.format_sprint(sprint))

    def parse_epics(self, service, args):
        """ Parse epics command """
        formatter = Simple(oneline=args.oneline)
        for epics in service.epics(args.boardId):
            print(formatter.format_epics(epics))

    def parse_epic(self, service, args):
        """ Parse epic command """
        if hasattr(args, 'epic_subcommand'):
            if args.epic_subcommand == 'issues':
                formatter = Simple(oneline=args.oneline)
                for issues in service.epic_issues(args.epicId):
                    print(formatter.format_issues(issues))
        else:
            formatter = Simple()
            epic = service.epic(args.epicId)
            print(formatter.format_epic(epic))
