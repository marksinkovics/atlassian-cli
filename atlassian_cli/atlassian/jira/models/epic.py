""" Represent Jira Epic and its descendants """

from jsonobject import (
    JsonObject,
    BooleanProperty,
    StringProperty,
    IntegerProperty,
    ObjectProperty
)

# pylint: disable=R0903

class EpicColor(JsonObject):
    """ Epic color model """
    key = IntegerProperty(name='key')

class Epic(JsonObject):
    """ Epic model """
    id_ = IntegerProperty(name='id')
    done = BooleanProperty()
    key = IntegerProperty(name='key')
    name = StringProperty(name='name')
    color = ObjectProperty(EpicColor)
