""" Represent Jira Board and its descendants """

from jsonobject import (
    JsonObject,
    BooleanProperty,
    StringProperty,
    IntegerProperty,
    DateTimeProperty
)

class Board(JsonObject):
    """ Board model"""
    id_ = IntegerProperty(name='id')
    active = BooleanProperty()
    name = StringProperty(name='name')
    type_ = StringProperty(name='type')

class Sprint(JsonObject):
    """ Spring model """
    id_ = IntegerProperty(name='id')
    state = StringProperty(name='state')
    name = StringProperty(name='name')
    start_date = DateTimeProperty(name='startDate')
    end_date = DateTimeProperty(name='endDate')
    complete_date = DateTimeProperty(name='completeDate')
    origin_board_id = IntegerProperty(name='originBoardId')

class Epic(JsonObject):
    """ Epic model """
    id_ = IntegerProperty(name='id')
    name = StringProperty()
    summary = StringProperty()
    done = BooleanProperty()

class Version(JsonObject):
    """ Version model """
    id_ = IntegerProperty(name='id')
    project_id = IntegerProperty(name='projectId')
    name = StringProperty()
    description = StringProperty()
    archived = BooleanProperty()
    released = BooleanProperty()
    release_date = DateTimeProperty(name='releaseDate')
