""" Simple formatter class """

from termcolor import colored

from .formatter import Formatter

class Simple(Formatter):
    """ Simple config formatter """

    # pylint: disable=R0201

    def format_user_config(self, user_config):
        """ Format a certain user_config """
        if user_config.default:
            active_msg = colored('(Active)', 'green')
        else:
            active_msg = colored('(Deactive)', 'red')
        return '{} ({}) {}'.format(
            user_config.url,
            user_config.username,
            active_msg
        )

    def format_user_configs(self, user_configs):
        """ Format a list of user_config """
        results = list(map(self.format_user_config, user_configs))
        return "\n".join(results)
