""" Simple formatter class """

# https://pypi.python.org/pypi/termcolor
from termcolor import colored

from atlassian_cli.atlassian.jira.formatters import Formatter

class Simple(Formatter):
    """ Make a simple formatter for Jira """

    def format_user(self, user):
        return user.name

    def format_users(self, users):
        results = list(map(self.format_user, users))
        return "\n".join(results)

    def format_issue(self, issue):
        result = f"{colored(issue.key, attrs=['bold'])} - {issue.fields.summary}"

        if self._oneline:
            return result

        if issue.fields.status.name:
            result += f'\nStatus: {self.format_status(issue.fields.status)}'

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
                result += '\n  {:12} - {}'.format(subtask.key, subtask.fields.summary)
                result += ' ' + self.format_status(subtask.fields.status)

        if issue.fields.components:
            components = map(lambda comp: comp.name, issue.fields.components)
            result += '\nComponents:  {}'.format(','.join(components))

        if issue.fields.labels:
            result += '\nLabels: {}'.format(','.join(issue.fields.labels))

        return result

    def format_issues(self, issues):
        results = list(map(self.format_issue, issues))
        return "\n".join(results)

    def format_board(self, board):
        result = '{:12} - {}'.format(colored(board.id_, attrs=['bold']), board.name)
        return result

    def format_boards(self, boards):
        results = list(map(self.format_board, boards))
        return "\n".join(results)

    def format_sprint(self, sprint):
        if sprint.state == 'closed':
            state_msg = colored('(closed)', 'red')
        elif sprint.state == 'active':
            state_msg = colored('(active)', 'green')
        elif sprint.state == 'future':
            state_msg = colored('(future)', 'blue')


        result = '{:12} - {} {}'.format(colored(sprint.id_, attrs=['bold']),
                                        sprint.name,
                                        state_msg)
        return result

    def format_sprints(self, sprints):
        results = list(map(self.format_sprint, sprints))
        return "\n".join(results)

    def format_epic(self, epic):
        """ Format Epic model """
        result = '{:15} - {}'.format(colored(epic.id_, attrs=['bold']), epic.name)
        return result

    def format_epics(self, epics):
        """ Format a list of Epic model """
        results = list(map(self.format_epic, epics))
        return "\n".join(results)

    def format_version(self, version):
        """ Format an Version model """
        result = '{:15} - {}'.format(colored(version.id_, attrs=['bold']), version.name)
        return result

    def format_versions(self, versions):
        """ Format a list of Version model """
        results = list(map(self.format_version, versions))
        return "\n".join(results)

    def format_status(self, status):
        """ Format an Status model """
        color = status.statusCategory.color()
        on_color = f"on_{color}"
        return colored(f"({status.name})", color)
