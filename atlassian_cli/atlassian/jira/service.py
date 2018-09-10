""" Service for Jira API """

from atlassian_cli.atlassian.jira.config import JiraDebugConfig
from atlassian_cli.service import Service, BasicAuthentication
from atlassian_cli.atlassian.jira.models import (
    Board,
    Issue,
    User,
    Sprint,
    Epic
)

class JiraService(Service):
    """ Handle Jira services """

    def __init__(self, model):
        self.model = model
        super().__init__(BasicAuthentication(self.model))
        self.headers.update(self.jira_headers)
        self.debug = JiraDebugConfig()
        self.debug.read()

    @property
    def jira_headers(self):
        """ Basic headers for Jira server requests """
        return {'Content-Type' : 'application/json',
                'Accept' : 'application/json',
                'Accept-Encoding' : 'gzip,deflate'}

    def get(self, url, **kwargs):
        """ Request content from URL """
        if self.debug.config.show_url:
            print('===> URL: {}'.format(url))
        response = super().get(url, **kwargs)
        if self.debug.config.show_elapsed_time:
            print('===> Elapsed time: {}'.format(response.elapsed.total_seconds()))
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
            params.update({'startAt' : start_index})
            response = self.get(url, params=params)
            response_json = response.json()
            start_index += response_json['maxResults']
            values = response.json()[values_key]
            if not values:
                is_last_page = True
                break
            else:
                yield values

    def myself(self):
        """ Get infomation about the current user """
        url = self.model.url + '/rest/api/2/myself'
        value = self.get(url).json()
        return User(value)

    def issue(self, issue_id):
        """ Get information about an specific issue """
        fields = [
            'status',
            'components',
            'labels',
            'summary',
            'assignee',
            'closedSprints',
            'reporter',
            'parent',
            'subtasks'
        ]
        params = {
            'fields' : ','.join(fields)
        }
        url = self.model.url + '/rest/agile/1.0/issue/' + issue_id
        value = self.get(url, params=params).json()
        return Issue(value)

    def jql(self, jql):
        """ Get tickets via Jira Query Languate (JQL) """
        params = {
            'jql' : jql,
            'fields' : 'status,components,labels,summary,assignee,closedSprints,reporter'
        }
        url = self.model.url + '/rest/api/2/search'
        for values in self.iterator_get(url, values_key='issues', params=params):
            yield list(map(Issue, values))

    def boards(self):
        """ Get available board """
        url = self.model.url + '/rest/agile/1.0/board'
        for values in self.iterator_get(url):
            yield list(map(Board, values))

    def board(self, board_id):
        """ Get information about a specific board """
        url = self.model.url + '/rest/agile/1.0/board/' + board_id
        value = self.get(url).json()
        return Board(value)

    def sprints(self, board_id):
        """ Get sprints for a specific boards """
        url = self.model.url + '/rest/agile/1.0/board/' + board_id + '/sprint'
        for values in self.iterator_get(url):
            sprints = list(map(Sprint, values))
            filtered_sprints = list(filter(
                lambda sprint: sprint.origin_board_id == int(board_id),
                sprints))
            yield filtered_sprints

    def sprint(self, sprint_id):
        """ Get information about a specific sprint """
        url = self.model.url + '/rest/agile/1.0/sprint/' + sprint_id
        value = self.get(url).json()
        return Sprint(value)

    def sprint_issues(self, sprint_id):
        """ Get issues of a specific sprint """
        url = self.model.url + '/rest/agile/1.0/sprint/' + sprint_id + '/issue'
        for values in self.iterator_get(url, values_key='issues'):
            yield list(map(Issue, values))

    def epics(self, board_id):
        """ Get epics for a specific boards """
        url = self.model.url + '/rest/agile/1.0/board/' + board_id + '/epic'
        for values in self.iterator_get(url):
            epics = list(map(Epic, values))
            yield epics

    def epic(self, epic_id):
        """ Get information about a specific epic """
        url = self.model.url + '/rest/agile/1.0/epic/' + epic_id
        value = self.get(url).json()
        return Epic(value)

    def epic_issues(self, epic_id):
        """ Get issues of a specific epic """
        url = self.model.url + '/rest/agile/1.0/epic/' + epic_id + '/issue'
        for values in self.iterator_get(url, values_key='issues'):
            yield list(map(Issue, values))
