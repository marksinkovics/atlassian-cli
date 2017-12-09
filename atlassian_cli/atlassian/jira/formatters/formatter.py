class Formatter:

    def __init__(self, oneline=False):
        self._oneline = oneline

    # pylint: disable=R0201
    def formatUser(self, user):
        return user

    def formatUsers(self, users):
        return users

    def formatIssue(self, issue):
        return issue

    def formatIssues(self, issues):
        return issues

    def formatBoard(self, board):
        return board

    def formatBoards(self, boards):
        return boards

    def formatSprint(self, sprint):
        return sprint

    def formatSprints(self, sprints):
        return sprints
