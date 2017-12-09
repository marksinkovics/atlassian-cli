""" Service for Bitbucket API """

from atlassian_cli.atlassian.bitbucket.config import BitbucketDebugConfig
from atlassian_cli.service import Service, BasicAuthentication
from atlassian_cli.atlassian.bitbucket.models import (
    Project,
    PullRequest,
    Repo
)

class BitbucketService(Service):
    """ Handle Bitbucket services """
    def __init__(self, model):
        self.model = model
        super().__init__(BasicAuthentication(self.model))
        self.headers.update(self.bitbucket_headers)
        self.debug = BitbucketDebugConfig()
        self.debug.read()

    @property
    def bitbucket_headers(self):
        """ Basic headers for Bitbucket server requests """
        return {'Content-Type' : 'application/json',
                'Accept' : 'application/json',
                'Accept-Encoding' : 'gzip,deflate'}

    def get(self, url, **kwargs):
        response = super().get(url, **kwargs)
        if self.debug.config.show_elapsed_time:
            print('Elapsed time: {}'.format(response.elapsed.total_seconds()))
        return response

    def pager_get(self, url, values_key="values"):
        """ Get value page by page (synchronously)"""
        result = []
        for values in self.iterator_get(url, values_key=values_key):
            result += values
        return result

    def iterator_get(self, url, values_key="values", params=None):
        """ Get value page by page via iterator """
        is_last_page = False
        start_index = 0
        while not is_last_page:
            params = {} if not params else params
            params.update({'start' : start_index})
            response = self.get(url, params=params)
            response_json = response.json()
            start_index += response_json['size']
            values = response.json()[values_key]
            is_last_page = response_json['isLastPage']
            yield values
            if not values:
                is_last_page = True


    def projects(self):
        """ Get projects """
        url = self.model.url + '/rest/api/1.0/projects'
        for values in self.iterator_get(url):
            yield list(map(Project, values))

    def project(self, project_id):
        """ Get a specific project """
        url = self.model.url + '/rest/api/1.0/projects/' + project_id
        value = self.get(url).json()
        return Project(value)

    def project_repos(self, project_id):
        """ Get repos of a specific project """
        url = self.model.url + '/rest/api/1.0/projects/' + project_id + '/repos'
        for values in self.iterator_get(url):
            yield list(map(Repo, values))

    def project_repo(self, project_id, repo_slug):
        """ Get specific repo for a specific project """
        url = self.model.url + '/rest/api/1.0/projects/' + project_id + '/repos/' + repo_slug
        value = self.get(url).json()
        return Repo(value)

    def pull_requests(self):
        """ Get My pull requests """
        url = self.model.url + '/rest/api/1.0/inbox/pull-requests'
        for values in self.iterator_get(url):
            yield list(map(PullRequest, values))

    def pull_requests_count(self):
        """ Get count of my pull requests """
        url = self.model.url + '/rest/api/1.0/inbox/pull-requests/count'
        response = self.get(url)
        return response.json()["count"]
