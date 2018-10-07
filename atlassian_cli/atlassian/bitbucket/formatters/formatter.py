""" Bitbucket formatter base class """

class Formatter:

    def __init__(self, oneline=False):
        self._oneline = oneline

    def format_project(self, project):
        return project

    def format_projects(self, projects):
        return projects

    def format_pull_request(self, pull_request):
        return pull_request

    def format_pull_requests(self, pull_requests):
        return pull_requests

    def format_pull_request_count(self, pull_request_count):
        return pull_request_count

    def format_repository(self, repository):
        return repository

    def format_repositories(self, repositories):
        return repositories
