""" Debug configuration """

import argparse
import json
import os

from .models import Debug

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
        parser.add_argument('--set-loglevel', help='Set level of logging')
        parser.add_argument('--show-elapsed-time', help='Show elapsed time of a request')
        parser.add_argument('--show-received-bytes', help='Show the size of the received bytes')
        parser.add_argument('--show-arguments', help='Show the given command line arguments')
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
            print('Config file ({}) is missing'.format(self.config_file))
            return

        debug_data = {}

        with open(self.config_file, 'r', encoding='utf-8') as file:
            try:
                debug_data = json.load(file)
            except json.JSONDecodeError as error:
                print('Loading JSON has failed: {}'.format(error.msg))

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
        return value.lower() in ("yes", "true", "t", "1")

    def parse(self, args):
        """ Parse arguments """
        self.read()

        if args.show_elapsed_time:
            self.config.show_elapsed_time = self.str2bool(args.show_elapsed_time)

        if args.show_received_bytes:
            self.config.show_received_bytes = self.str2bool(args.show_received_bytes)

        if args.set_loglevel:
            self.config.log_level = int(args.set_loglevel)

        if args.show_arguments:
            self.config.show_arguments = self.str2bool(args.show_arguments)

        self.write()
