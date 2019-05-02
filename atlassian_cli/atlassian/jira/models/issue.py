""" Represent an Issue """

from jsonobject import (
    JsonObject,
    ObjectProperty,
    StringProperty,
    IntegerProperty,
    ListProperty,
    BooleanProperty,
    DefaultProperty
)

from atlassian_cli.atlassian.jira.models.user import User
from atlassian_cli.atlassian.jira.models.board import Sprint

class StatusCategory(JsonObject):
    """ StatusCategory model for Status """
    id_ = IntegerProperty(name='id')
    key = StringProperty()
    colorName = StringProperty()
    name = StringProperty()

    def color(self):
        """ Convert to termcolor """
        if self.colorName == 'blue-gray':
            return 'blue'
        return self.colorName

class Status(JsonObject):
    """ Status model for issue fields """
    description = StringProperty()
    iconUrl = StringProperty()
    name = StringProperty()
    id_ = StringProperty(name='id')
    statusCategory = ObjectProperty(StatusCategory)


class Component(JsonObject):
    """ Component model for issue fields """
    id_ = StringProperty(name='id')
    name = StringProperty()
    description = StringProperty()
    def __str__(self):
        return self.name

class IssueType(JsonObject):
    """ IssueType model for issue fields """
    id_ = StringProperty(name='id')
    name = StringProperty()
    subtask = BooleanProperty()

class Fields(JsonObject):
    """ Fields model for issue"""
    status = ObjectProperty(Status)
    components = ListProperty(Component, default=None)
    labels = ListProperty(StringProperty, default=None)
    summary = StringProperty(default='')
    assignee = ObjectProperty(User)
    closed_sprints = ListProperty(Sprint, default=None, name='closedSprints')
    reporter = ObjectProperty(User)
    issue_type = ObjectProperty(IssueType)
    parent_ = DefaultProperty(default=None, name='parent')
    subtasks_ = DefaultProperty(default=None, name='subtasks')

    @property
    def parent(self):
        """ Getter for parent issue """
        if self.parent_:
            return Issue(self.parent_)
        return None

    @property
    def subtasks(self):
        """ Getter for subtasks """
        if self.subtasks_:
            return list(map(Issue, self.subtasks_))
        return None

class Issue(JsonObject):
    """ Issue model """
    id_ = StringProperty(name='id')
    key = StringProperty()
    fields = ObjectProperty(Fields)
