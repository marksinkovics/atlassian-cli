""" Represent a base class handling command line arguments """

import argparse

from atlassian_cli.metadata import APPLICATION_VERSION

class CLI:
    """ Abstract implementation of CLI class """

    def __init__(self,
                 add_help=True,
                 add_version=True,
                 prog=None):
        self.parser = None
        self.subparsers = None
        self.add_help = add_help
        self.add_version = add_version
        self.prog = prog

        self.output_parent_parser = argparse.ArgumentParser(add_help=False)
        self.output_parent_parser.add_argument('--oneline',
                                               action='store_true',
                                               help='Show output only in one line')
        self.create_parser()
        self.create_subparser()

        self.debug = None

    def create_subparser(self):
        """ Create subparsers """
        self.subparsers = self.parser.add_subparsers(help='commands')

    def create_parser(self):
        """ Create argument parser """
        self.parser = argparse.ArgumentParser(add_help=self.add_help)
        self.parser.prog = self.prog
        if self.add_version:
            self.parser.add_argument(
                '--version',
                action='version',
                version='%(prog)s (version {version})'.format(version=APPLICATION_VERSION))

    def parse(self):
        """ Parse command line arguments """
        return self.parser.parse_args()

    def parse_command(self, args):
        # pylint: disable=W0613,R0201
        """ Handle input arguemnts """
        return False

    def parser_arguments(self):
        """ Parse imput arguments """
        args = self.parse()
        if self.debug.config.show_arguments:
            print('Args: {}'.format(vars(args)))
        if not vars(args):
            self.parser.print_help()
            return
        self.parse_command(args)
