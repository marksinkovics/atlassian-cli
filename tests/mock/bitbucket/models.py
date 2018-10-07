""" Contains example models for tests """

from atlassian_cli.config.models import User as ConfigUser
from atlassian_cli.atlassian.bitbucket.models import (
    Project,
    PullRequest
)

#
# User
#

USERS = [
    ConfigUser({
        "createdAt": "2018-02-19T20:01:54Z",
        "default": True,
        "url": "https://foobarbaz.com",
        "username": "johndoe"
    })
]

USER = USERS[0]

#
# Project
#

PROJECTS = [
    Project({
        'key': 'KEY1',
        'id:': 1,
        'name': 'Key 1 project',
        'public': False,
        'type': 'type',
        'description': 'This is key 1 project'
    }),
    Project({
        'key': 'KEY2',
        'id:': 2,
        'name': 'Key 2 project',
        'public': True,
        'type': 'type',
        'description': 'This is key 2 project'
    })
]

PROJECT = PROJECTS[1]

#
# Pull Request
#

# class PullRequest(JsonObject):
#     id_ = IntegerProperty(name='id')
#     version = IntegerProperty()
#     title = StringProperty()
#     state = StringProperty()
#     open_ = BooleanProperty(name="open")
#     closed = BooleanProperty()
#     createdDate = EpochProperty()
#     updatedDate = EpochProperty()


PULLREQUESTS = [
    PullRequest({
        'id': 1,
        'version': 1,
        'title': 'Title 1',
        'state': 'state',
        'open': True,
        'closed': False,
        'createdDate': 946782245000,
        'updatedDate': 946782245000
    }),
    PullRequest({
        'id': 2,
        'version': 2,
        'title': 'Title 2',
        'state': 'state',
        'open': False,
        'closed': False,
        'createdDate': 946782245000,
        'updatedDate': 946782245000
    }),
]

PULLREQUEST = PULLREQUESTS[1]
