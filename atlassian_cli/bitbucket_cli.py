#!/usr/bin/env python3

""" Entry class for bitbucket-cli """

from atlassian_cli.atlassian.bitbucket.cli import BitbucketCLI
from atlassian_cli import BITBUCKET_CLI_PROG

def main():
    """ Entry function for bitbucket-cli """
    cli = BitbucketCLI(prog=BITBUCKET_CLI_PROG)
    cli.parser_arguments()

if __name__ == '__main__':
    main()
