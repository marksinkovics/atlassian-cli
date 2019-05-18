""" Contains example models for tests """

from atlassian_cli.config.models import User as ConfigUser
from atlassian_cli.atlassian.jira.models import (
    User,
    Issue,
    Sprint,
    Board,
    Epic,
    Version
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
# myself
#

MYSELF = User({
    'active': True,
    'emailAddress': 'johndoe@example.com',
    'name': 'johndoe',
    'displayName': 'John Doe'
})

#
# Board
#

BOARDS = [
    Board({
        'id': 1,
        'active:': False,
        'name': 'Board',
        'type': 'kanban'
    }),
    Board({
        'id': 2,
        'active:': True,
        'name': 'Board',
        'type': 'scrum'
    })
]

BOARD = BOARDS[0]

#
# Issue
#

ISSUES = [
    Issue({
        'id': '1',
        'key:': 'ABC-1'
    }),
    Issue({
        'id': '2',
        'key:': 'ABC-2'
    })
]

ISSUE = ISSUES[0]

#
# Sprint
#

SPRINTS = [
    Sprint({
        'id': 1,
        'state': 'future',
        'name': 'sprint-1'
    }),
    Sprint({
        'id': 2,
        'state': 'active',
        'name': 'sprint-2'
    })
]

SPRINT = SPRINTS[0]

#
# Epic
#

EPICS = [
    Epic({
        'id': 12345,
        'done': False,
        'key': 'ABC-12345',
        'name': 'Epic12345'
    })
]

EPIC = EPICS[0]

#
# Version
#

VERSIONS = [
    Version({
        'id': 1,
        'projectId': 12345,
        'name': 'Version1',
        'description': 'Version1',
        'archived': False,
        'release': False,
        'releaseDate': '2019-09-03T00:00:00.000Z'
    }),
    Version({
        'id': 2,
        'projectId': 12345,
        'name': 'Version2',
        'description': 'Version2',
        'archived': False,
        'release': True,
        'releaseDate': '2019-09-03T00:00:00.000Z'
    })
]

VERSION = VERSIONS[0]
