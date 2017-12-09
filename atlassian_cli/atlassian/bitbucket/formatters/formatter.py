""" Bitbucket formatter base class """

class Formatter:

    def __init__(self, oneline=False):
        self._oneline = oneline

    def formatProject(self, project):
        return project

    def formatProjects(self, projects):
        return projects

    def formatPullRequest(self, pullRequest):
        return pullRequest

    def formatpull_requests(self, pull_requests):
        return pull_requests

    def formatPullRequestCount(self, pullRequestCount):
        return pullRequestCount

    def formatRepository(self, repository):
        return repository

    def formatRepositories(self, repositories):
        return repositories
