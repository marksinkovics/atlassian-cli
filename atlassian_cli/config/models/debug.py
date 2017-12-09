""" Debug model """

from jsonobject import (
    JsonObject,
    BooleanProperty,
    IntegerProperty
)

class Debug(JsonObject):
    """ Represent a Debug menu """

    log_level = IntegerProperty(default=0)
    show_elapsed_time = BooleanProperty(default=False)
    show_received_bytes = BooleanProperty(default=False)
    show_arguments = BooleanProperty(default=False)
