""" Basic configuration """

import argparse

class ConfigCLI:
    """ Basic configuration """
    def __init__(self):
        self.parser = argparse.ArgumentParser(add_help=False)
        self.subparsers = self.parser.add_subparsers()
        self.custom_subparsers = []

    def add_custom_subparser(self, subparser):
        """ Add custom subparser """
        custom_subparser = self.subparsers.add_parser(subparser.name,
                                                      help=subparser.help,
                                                      parents=[subparser.parser])
        custom_subparser.set_defaults(config_subcommand=subparser.name)
        self.custom_subparsers.append(subparser)

    def parse(self, args):
        """ Parse arguemnts """
        if not hasattr(args, 'config_subcommand'):
            return
        subcommand = args.config_subcommand
        subparser = list(filter(lambda s: s.name == subcommand, self.custom_subparsers))
        if not subparser:
            print('Custom subparser is missing!')
        subparser[0].parse(args)
