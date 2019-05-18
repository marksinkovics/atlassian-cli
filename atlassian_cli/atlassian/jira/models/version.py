""" Represent Jira Version and its descendants """
from jsonobject import (
    JsonObject,
    BooleanProperty,
    StringProperty,
    IntegerProperty,
    ObjectProperty
)

from atlassian_cli.helpers import CustomDateTimeProperty

# pylint: disable=R0903

class Version(JsonObject):
    """ Version model """
    id_ = IntegerProperty(name='id')
    projectId = IntegerProperty()
    name = StringProperty()
    description = StringProperty()
    archived = BooleanProperty()
    released = BooleanProperty()
    releaseDate = CustomDateTimeProperty(datetime_format="%Y-%m-%d %H:%M:%S.%z")
    startDate = CustomDateTimeProperty(datetime_format="%Y-%m-%d %H:%M:%S.%z")
