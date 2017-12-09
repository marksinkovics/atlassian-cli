""" Basic formatter class """

class Formatter:
    """ basic config formatter """

    def __init__(self, oneline=False):
        self._oneline = oneline

    # pylint: disable=R0201
    def format_user_config(self, user_config):
        """ Format a certain user_config """
        return user_config

    def format_user_configs(self, user_configs):
        """ Format a list of user_config """
        return user_configs
