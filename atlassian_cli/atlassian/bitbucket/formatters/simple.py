# https://pypi.python.org/pypi/termcolor
from termcolor import colored

from atlassian_cli.atlassian.bitbucket.formatters import Formatter

class Simple(Formatter):

    def formatProject(self, project):
        if self._oneline:
            return "{0} {1}  {2}".format(colored(project.name, 'yellow', attrs=['bold']),
                                         colored(project.key, attrs=['bold']),
                                         project.description.replace('\r\n', ' > '))
        else:
            result = "{0} ({1}) - {2}\n".format(colored(project.key, attrs=['bold']),
                                                project.id_,
                                                colored(project.name, 'yellow', attrs=['bold']))
            if project.description:
                result += "-- Description: {0}\n".format(project.description)
            result += "-- Type: {0}\n".format(project.type_)
            result += "-- Public: {0}".format(project.public)
            return result

    def formatProjects(self, projects):
        results = list(map(self.formatProject, projects))
        return "\n".join(results)

    def formatPullRequest(self, pullRequest):
        return "{0}".format(pullRequest.title)

    def formatpull_requests(self, pull_requests):
        results = list(map(self.formatPullRequest, pull_requests))
        return "\n".join(results)

    def formatPullRequestCount(self, pullRequestCount):
        return "{}".format(colored(pullRequestCount, attrs=['bold']))

    def formatRepository(self, repository):
        return "{}".format(repository.name)

    def formatRepositories(self, repositories):
        results = list(map(self.formatRepository, repositories))
        return "\n".join(results)
