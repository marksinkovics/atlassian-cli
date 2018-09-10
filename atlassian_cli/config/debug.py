""" Debug configuration """

import argparse
import json
import os
import re
import sys

from .models import Debug

from .formatters import Simple

class DebugConfig:
    """ Debug configuration """

    def __init__(self):
        self.config = Debug()
        self.prepare_config_path()

    @property
    def name(self):
        """ Represent parser argument """
        return 'debug'

    @property
    def help(self):
        """ Represent parser help """
        return 'Debug configuration'

    @property
    def parser(self):
        """ Create argument parser """
        parser = argparse.ArgumentParser(add_help=False)
        subparsers = parser.add_subparsers()

        print_parser = subparsers.add_parser('print', help='Print settings')
        print_parser.set_defaults(debug_subcommand='print')

        log_parser = subparsers.add_parser('log', help='Set log level')
        log_parser.add_argument('log_level', type=int)
        log_parser.set_defaults(debug_subcommand='log')

        elapsed_time_parser = subparsers.add_parser('elapsed_time', help='Show elapsed time')
        elapsed_time_parser.add_argument('elapsed_time', type=self.str2bool)
        elapsed_time_parser.set_defaults(debug_subcommand='elapsed_time')

        received_bytes_parser = subparsers.add_parser('received_bytes', help='Show received bytes')
        received_bytes_parser.add_argument('received_bytes', type=self.str2bool)
        received_bytes_parser.set_defaults(debug_subcommand='received_bytes')

        show_arguments_parser = subparsers.add_parser('show_arguments', help='Show arguments')
        show_arguments_parser.add_argument('show_arguments', type=self.str2bool)
        show_arguments_parser.set_defaults(debug_subcommand='show_arguments')

        show_url_parser = subparsers.add_parser('show_url', help="Show the request url")
        show_url_parser.add_argument('show_url', type=self.str2bool)
        show_url_parser.set_defaults(debug_subcommand='show_url')

        return parser

    #
    # Helper methods
    #

    @property
    def config_folder_name(self):
        """ Default config folder name """
        return '.config-cli'

    @property
    def config_folder(self):
        """ Default config folder path """
        return os.path.join(os.path.expanduser('~'), self.config_folder_name)

    @property
    def config_file_name(self):
        """ Default config folder name """
        return 'debug.json'

    @property
    def config_file(self):
        """ Default config file path """
        return os.path.join(os.path.expanduser('~'),
                            self.config_folder_name,
                            self.config_file_name)

    #
    # Config file handlers
    #

    def prepare_config_path(self):
        """ Validate config folder existance """
        if not os.path.exists(self.config_folder):
            os.makedirs(self.config_folder)

    #
    # Read config file
    #

    def read(self):
        """ Read config file """
        if not os.path.exists(self.config_file):
            print('Config file ({}) is missing'.format(self.config_file), file=sys.stderr)
            return

        debug_data = {}

        with open(self.config_file, 'r', encoding='utf-8') as file:
            try:
                debug_data = json.load(file)
            except ValueError as error:
                print('Loading JSON has failed: {}'.format(error))

        if debug_data:
            self.config = Debug(debug_data)

    def write(self):
        """ Write config file """
        debug_data = self.config.to_json()
        with open(self.config_file, 'w') as file:
            json.dump(debug_data, file, sort_keys=True)
    #
    # Parse arguments
    #

    #
    # Parse command line arguments
    #

    @staticmethod
    def str2bool(value):
        """ Convert str to bool """
        if value.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif value.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    def parse(self, args):
        """ Parse arguments """

        subcommand = re.sub('-', '', args.debug_subcommand)
        method_name = 'parse_{}'.format(subcommand)
        try:
            method = getattr(self, method_name)
        except AttributeError:
            raise NotImplementedError("Class `{}` does not implement `{}`"
                                      .format(self.__class__.__name__, method_name))

        self.read()
        method(args)
        self.write()

    def parse_print(self, args):
        """ Parse print command """
        formatter = Simple()
        print(formatter.format_debug(self.config))

    def parse_log(self, args):
        """ Parse log command """
        self.config.log_level = int(args.log_level)

    def parse_elapsed_time(self, args):
        """ Parse elapsed_time command """
        self.config.show_elapsed_time = args.elapsed_time

    def parse_received_bytes(self, args):
        """ Parse received_bytes command """
        self.config.show_received_bytes = args.received_bytes

    def parse_show_arguments(self, args):
        """ Parse show_arguments command """
        self.config.show_arguments = args.show_arguments

    def parse_show_url(self, args):
        """ Parse show_url command """
        self.config.show_url = args.show_url
