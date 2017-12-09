""" Bitbucket command line interface """

import re

from atlassian_cli.cli import CLI
from atlassian_cli.atlassian.bitbucket.service import BitbucketService
from atlassian_cli.atlassian.bitbucket.formatters import Simple

from atlassian_cli.config import ConfigCLI
from atlassian_cli.atlassian.bitbucket.config import (
    BitbucketUserConfig,
    BitbucketDebugConfig
)

class BitbucketCLI(CLI):
    """ Bitbucket command line interface controller class """

    def __init__(self,
                 add_help=True,
                 add_version=True,
                 prog=None):
        self.config_cli = ConfigCLI()
        self.config_cli.add_custom_subparser(BitbucketUserConfig())
        self.config_cli.add_custom_subparser(BitbucketDebugConfig())
        super().__init__(add_help=add_help, add_version=add_version, prog=prog)
        self.debug = BitbucketDebugConfig()
        self.debug.read()

    def create_subparser_config(self):
        """ Create config subparser """
        config_parser = self.subparsers.add_parser('config',
                                                   help='Config',
                                                   parents=[self.config_cli.parser])
        config_parser.set_defaults(subcommand='config')

    def create_subparser_projects(self):
        """ Create subparser projects command """
        projects_parser = self.subparsers.add_parser('projects',
                                                     help='projects',
                                                     parents=[self.output_parent_parser])
        projects_parser.set_defaults(subcommand='projects')

    def create_subparser_project(self):
        """ Create subparser project command """
        project_parser = self.subparsers.add_parser('project',
                                                    help='project',
                                                    parents=[self.output_parent_parser])
        project_parser.set_defaults(subcommand='project')
        project_parser.add_argument('projectId')

        repo_group = project_parser.add_mutually_exclusive_group()
        repo_group.add_argument('--repos',
                                action='store_true',
                                help="Show repositories for a specific project")
        repo_group.add_argument('--repo',
                                action='store',
                                metavar='slug',
                                help='Show detail of repository')

    def create_subparser_mypr(self):
        """ Create subparser pull-requests command """
        my_pull_requests = self.subparsers.add_parser('my-pull-requests',
                                                      help='my-pull-requests',
                                                      parents=[self.output_parent_parser])
        my_pull_requests.set_defaults(subcommand='my-pull-requests')

    def create_subparser_myprcount(self):
        """ Create subparser pull-requests-count command """
        my_pull_requests_count = self.subparsers.add_parser('my-pull-requests-count',
                                                            help='my-pull-requests-count')
        my_pull_requests_count.set_defaults(subcommand='my-pull-requests-count')

    def create_subparser(self):
        super().create_subparser()
        self.create_subparser_config()
        self.create_subparser_projects()
        self.create_subparser_project()
        self.create_subparser_mypr()
        self.create_subparser_myprcount()

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
            user_config = BitbucketUserConfig()
            user_config.read()
            if not user_config.users:
                print('There is not any valid user account.')
                return
            default_user = user_config.default_user()
            service = BitbucketService(default_user)
        else:
            service = None
        subcommand = re.sub('-', '', args.subcommand)
        method_name = 'parse_{}'.format(subcommand)
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

    def parse_projects(self, service, args):
        """ Parse projects command """
        formatter = Simple(oneline=args.oneline)
        for projects in service.projects():
            print(formatter.formatProjects(projects))

    def parse_project(self, service, args):
        """ Parse project command """
        formatter = Simple(oneline=args.oneline)
        if args.repos:
            for repos in service.project_repos(args.projectId):
                print(formatter.formatRepositories(repos))
        elif args.repo:
            repo = service.project_repo(args.projectId, args.repo)
            print(formatter.formatRepository(repo))
        else:
            project = service.project(args.projectId)
            print(formatter.formatProject(project))

    def parse_mypullrequests(self, service, args):
        """ Parse my-pull-requests command """
        formatter = Simple(oneline=args.oneline)
        for pull_requests in service.pull_requests():
            print(formatter.formatpull_requests(pull_requests))

    def parse_mypullrequestscount(self, service, args):
        # pylint: disable=W0613
        """ Parse my-pull-requests-count command """
        formatter = Simple()
        count = service.pull_requests_count()
        print(formatter.formatPullRequestCount(count))
