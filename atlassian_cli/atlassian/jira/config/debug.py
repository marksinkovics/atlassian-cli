""" Jira specified debug config """
from atlassian_cli.config import DebugConfig
from atlassian_cli.metadata import (
    JIRA_CONFIG_FOLDER,
)

class JiraDebugConfig(DebugConfig):
    """ Jira specified debug config """

    @property
    def config_folder_name(self):
        """ Default config folder name """
        return JIRA_CONFIG_FOLDER
