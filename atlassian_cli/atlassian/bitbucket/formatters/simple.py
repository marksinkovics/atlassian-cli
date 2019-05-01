# https://pypi.python.org/pypi/termcolor
from termcolor import colored

from atlassian_cli.atlassian.bitbucket.formatters import Formatter

class Simple(Formatter):

    def format_project(self, project):
        name = colored(project.name, 'yellow', attrs=['bold'])
        key = colored(project.key, attrs=['bold'])
        description = project.description.replace('\r\n', ' > ')
        if self._oneline:
            return f"{name} {key}  {description}"

        result = f"{key} ({project.id_}) - {name}\n"
        if project.description:
            result += f"-- Description: {project.description}\n"
        result += f"-- Type: {project.type_}\n"
        result += f"-- Public: {project.public}"
        return result

    def format_projects(self, projects):
        results = list(map(self.format_project, projects))
        return "\n".join(results)

    def format_pull_request(self, pull_request):
        title = colored(pull_request.title, attrs=['bold'])
        name = (
            f"({pull_request.toRef.repository.project.name}/"
            f"{pull_request.toRef.repository.name})"
        )
        num_of_reviewers = len(pull_request.reviewers)
        num_of_approve = len(list(filter(lambda reviewer: reviewer.approved, pull_request.reviewers)))
        branch = pull_request.toRef.displayId
        return (
            f"#{pull_request.id_} \t"
            f"[{branch}] "
            f"{name} by "
            f"{pull_request.author.user.displayName} - "
            f"({num_of_reviewers}/{num_of_approve}) "
            f"{title}"
        )

    def format_pull_requests(self, pull_requests):
        results = list(map(self.format_pull_request, pull_requests))
        return "\n".join(results)

    def format_pull_request_count(self, pull_request_count):
        return "{}".format(colored(pull_request_count, attrs=['bold']))

    def format_repository(self, repository):
        return f"#{repository.id_} {repository.name}"

    def format_repositories(self, repositories):
        results = list(map(self.format_repository, repositories))
        return "\n".join(results)
