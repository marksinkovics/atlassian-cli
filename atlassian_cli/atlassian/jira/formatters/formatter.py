class Formatter:

    def __init__(self, oneline=False):
        self._oneline = oneline

    # pylint: disable=R0201
    def format_user(self, user):
        """ Format User model """
        return user

    def format_users(self, users):
        """ Format a list of User model """
        return users

    def format_issue(self, issue):
        """ Format an Issue model """
        return issue

    def format_issues(self, issues):
        """ Format a list of Issue model """
        return issues

    def format_board(self, board):
        """ Format a Board model """
        return board

    def format_boards(self, boards):
        """ Format a list of Board model """
        return boards

    def format_sprint(self, sprint):
        """ Format a Sprint model """
        return sprint

    def format_sprints(self, sprints):
        """ Format a list of Sprit model """
        return sprints

    def format_epic(self, epic):
        """ Format an Epic model """
        return epic

    def format_epics(self, epics):
        """ Format a list of Epic model """
        return epics
