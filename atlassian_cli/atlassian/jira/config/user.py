""" Jira specified user config """
from atlassian_cli.config import UserConfig
from atlassian_cli.metadata import (
    JIRA_CONFIG_FOLDER,
)

class JiraUserConfig(UserConfig):
    """ Jira specified user config """

    @property
    def config_folder_name(self):
        """ Default config folder name """
        return JIRA_CONFIG_FOLDER
