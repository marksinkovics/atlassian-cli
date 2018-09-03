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

    def format_debug(self, debug):
        """ Format debug commands """
        result = "Log level: {}".format(debug.log_level)
        result += "\nShow elapsed time: {}".format(debug.show_elapsed_time)
        result += "\nShow received bytes: {}".format(debug.show_received_bytes)
        result += "\nShow arguments: {}".format(debug.show_arguments)
        return result
