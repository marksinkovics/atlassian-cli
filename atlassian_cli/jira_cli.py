#!/usr/bin/env python3

""" Entry file for jira-cli """

from atlassian_cli.atlassian.jira.cli import JiraCLI
from atlassian_cli import JIRA_CLI_PROG

def main():
    """ Entry function for jira-cli """
    cli = JiraCLI(prog=JIRA_CLI_PROG)
    cli.parser_arguments()

if __name__ == '__main__':
    main()
