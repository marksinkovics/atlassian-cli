""" User configuration """

import argparse
import datetime
import json
import re
import os

from .helpers.action import NonEmptyStringAction
from .helpers.dialog import Dialog

from .models import User
from .formatters import Simple

class UserConfig:
    """ User configuration """

    def __init__(self):
        self.users = []
        self.prepare_config_path()

    @property
    def name(self):
        """ Represent parser argument """
        return 'user'

    @property
    def help(self):
        """ Represent parser help """
        return 'User configuration'

    @property
    def parser(self):
        """ Create argument parser """
        parser = argparse.ArgumentParser(add_help=False)
        subparsers = parser.add_subparsers()

        user_set_parser = subparsers.add_parser('set', help='Set user')
        self.__add_default_arguments(user_set_parser)
        user_set_parser.add_argument('--password', '-p',
                                     required=False,
                                     action=NonEmptyStringAction)
        user_set_parser.set_defaults(user_subcommand='set')

        user_rm_parser = subparsers.add_parser('remove', help='Remove user')
        self.__add_default_arguments(user_rm_parser)
        user_rm_parser.set_defaults(user_subcommand='remove')

        user_default_parser = subparsers.add_parser('set-default',
                                                    help='Set user as default')
        self.__add_default_arguments(user_default_parser)
        user_default_parser.set_defaults(user_subcommand='set-default')

        user_list_parser = subparsers.add_parser('list',
                                                 help='List users')
        user_list_parser.set_defaults(user_subcommand='list')
        return parser

    #
    # Helper methods
    #

    @classmethod
    def __add_default_arguments(cls, parser):
        parser.add_argument('--username', '-u',
                            required=True,
                            action=NonEmptyStringAction)
        parser.add_argument('--url',
                            required=True,
                            action=NonEmptyStringAction)

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
        return 'users.json'

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

        users_data = None

        with open(self.config_file, 'r', encoding='utf-8') as file:
            try:
                users_data = json.load(file)
            except json.JSONDecodeError as error:
                print('Loading JSON has failed: {}'.format(error.msg))

        if users_data:
            self.users = list(map(User, users_data))

    def write(self):
        """ Write config file """
        users_data = list(map(lambda user: user.to_json(), self.users))
        with open(self.config_file, 'w') as file:
            json.dump(users_data, file, sort_keys=True)

    #
    # Parse arguments
    #

    #
    # Parse command line arguments
    #

    def parse(self, args):
        """ Parse arguments """
        subcommand = re.sub('-', '', args.user_subcommand)
        method_name = 'parse_{}'.format(subcommand)
        try:
            method = getattr(self, method_name)
        except AttributeError:
            raise NotImplementedError("Class `{}` does not implement `{}`"
                                      .format(self.__class__.__name__, method_name))
        method(args)

    def parse_set(self, args):
        """ Parse user setting """
        # Before write anything reload the whole config
        self.read()
        filtered_users = list(filter(lambda user:
                                     user.username == args.username and
                                     user.url == args.url,
                                     self.users))
        if filtered_users:
            user = filtered_users[0]
            user.updatedAt = datetime.datetime.utcnow()
        else:
            user = User(
                username=args.username,
                url=args.url,
                createdAt=datetime.datetime.utcnow(),
                updatedAt=datetime.datetime.utcnow()
            )
            self.users.append(user)

        if args.password:
            user.password = args.password
        else:
            user.password = Dialog.ask_secure_question('Password: ')

        self.write()

    def parse_remove(self, args):
        """ Parse user removing """
        self.read()
        filtered_users = list(filter(lambda user:
                                     user.username == args.username and
                                     user.url == args.url,
                                     self.users))
        if not filtered_users:
            print('The given user is not exist. Skip.')
        user = filtered_users[0]
        self.users.remove(user)
        self.write()

    def parse_setdefault(self, args):
        """ Parse user setting to default """
        self.read()
        filtered_users = list(filter(lambda user:
                                     user.username == args.username and
                                     user.url == args.url,
                                     self.users))
        if not filtered_users:
            print('The given user is not exist. Skip.')
        current_default_user = list(filter(lambda user: user.default, self.users))
        if current_default_user:
            current_default_user[0].default = False
        user = filtered_users[0]
        user.default = True
        self.write()

    def parse_list(self, args):
        # pylint: disable=W0613
        """ List users """
        self.read()
        formatter = Simple()
        print(formatter.format_user_configs(self.users))

    #
    # Extra methods
    #

    def default_user(self):
        """ Return default user """
        self.read()
        current_default_user = list(filter(lambda user: user.default, self.users))
        if current_default_user:
            return current_default_user[0]
        elif self.users:
            return self.users[0]
        return None
