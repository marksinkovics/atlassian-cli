# https://pypi.python.org/pypi/termcolor
from termcolor import colored

from atlassian_cli.atlassian.bitbucket.formatters import Formatter

class Simple(Formatter):

    def format_project(self, project):
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

    def format_projects(self, projects):
        results = list(map(self.format_project, projects))
        return "\n".join(results)

    def format_pull_request(self, pull_request):
        return "{0}".format(pull_request.title)

    def format_pull_requests(self, pull_requests):
        results = list(map(self.format_pull_request, pull_requests))
        return "\n".join(results)

    def format_pull_request_count(self, pull_request_count):
        return "{}".format(colored(pull_request_count, attrs=['bold']))

    def format_repository(self, repository):
        return "{}".format(repository.name)

    def format_repositories(self, repositories):
        results = list(map(self.format_repository, repositories))
        return "\n".join(results)
