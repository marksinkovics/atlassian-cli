""" Bitbucket specified debug config """

from atlassian_cli.config import DebugConfig
from atlassian_cli.metadata import (
    BITBUCKET_CONFIG_FOLDER,
)

class BitbucketDebugConfig(DebugConfig):
    """ Bitbucket specified debug config """

    @property
    def config_folder_name(self):
        """ Default config folder name """
        return BITBUCKET_CONFIG_FOLDER
