""" Simple formatter class """

# https://pypi.python.org/pypi/termcolor
from termcolor import colored

from atlassian_cli.atlassian.jira.formatters import Formatter

class Simple(Formatter):

    def formatUser(self, user):
        return user.name

    def formatUsers(self, users):
        results = list(map(self.formatUser, users))
        return "\n".join(results)

    def formatIssue(self, issue):
        result = "{} - {}".format(colored(issue.key, attrs=['bold']),
                                  issue.fields.summary)
        if self._oneline:
            return result

        if issue.fields.status.name:
            result += '\nStatus: {}'.format(issue.fields.status.name)

        if issue.fields.assignee:
            result += '\nAssignee: {}'.format(issue.fields.assignee.name)

        if issue.fields.reporter:
            result += '\nReporter: {}'.format(issue.fields.reporter.name)

        if issue.fields.parent:
            result += '\nParent: {} - {}'.format(issue.fields.parent.key,
                                                 issue.fields.parent.fields.summary)

        if issue.fields.subtasks:
            result += '\nSubtasks: '
            for subtask in issue.fields.subtasks:
                result += '\n  {} - {}'.format(subtask.key, subtask.fields.summary)

        if issue.fields.components:
            components = map(lambda comp: comp.name, issue.fields.components)
            result += '\nComponents:  {}'.format(','.join(components))

        if issue.fields.labels:
            result += '\nLabels: {}'.format(','.join(issue.fields.labels))

        return result

    def formatIssues(self, issues):
        results = list(map(self.formatIssue, issues))
        return "\n".join(results)

    def formatBoard(self, board):
        result = '{:12} - {}'.format(colored(board.id_, attrs=['bold']), board.name)
        return result

    def formatBoards(self, boards):
        results = list(map(self.formatBoard, boards))
        return "\n".join(results)

    def formatSprint(self, sprint):
        result = '{:12} - {}'.format(colored(sprint.id_, attrs=['bold']), sprint.name)
        return result

    def formatSprints(self, sprints):
        results = list(map(self.formatSprint, sprints))
        return "\n".join(results)
