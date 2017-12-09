""" Bitbucket specified user config """

from atlassian_cli.config import UserConfig
from atlassian_cli.metadata import (
    BITBUCKET_CONFIG_FOLDER,
)

class BitbucketUserConfig(UserConfig):
    """ Bitbucket specified user config """

    @property
    def config_folder_name(self):
        """ Default config folder name """
        return BITBUCKET_CONFIG_FOLDER
