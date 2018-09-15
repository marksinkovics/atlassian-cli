""" Represent a custom datetime for jsonobject module """

from datetime import datetime
from jsonobject import JsonProperty
import six

class CustomDateTimeProperty(JsonProperty):
    """ Specialize JsonProperty to handle a custom datetime """

    def __init__(self, *args, datetime_format="%Y%m%dT%H%M%S%f-%z", **kwargs):
        super(CustomDateTimeProperty, self).__init__(*args, **kwargs)
        self.datetime_format = datetime_format

    _type = datetime
    def wrap(self, obj):
        """ validate object before convert it to datetime object """
        try:
            if not isinstance(obj, six.string_types):
                raise ValueError()
            return self._wrap(obj)
        except ValueError:
            raise ValueError('{0!r} is not a {1}-formatted string'.format(
                obj,
                self._type.__name__,
            ))

    def unwrap(self, obj):
        """ validate object before convert it to string """
        if not isinstance(obj, self._type):
            raise ValueError('{0!r} is not a {1} object'.format(
                obj,
                self._type.__name__,
            ))
        return self._unwrap(obj)

    def _wrap(self, value):
        """ convert value to datetime object """
        try:
            print(value)
            print(self.datetime_format)
            return datetime.strptime(value, self.datetime_format)
        except ValueError as error:
            raise ValueError('Invalid datetime for format {0!r} [{1}]'.format(value, error))

    def _unwrap(self, value): # pylint: disable=R0201
        """ convert value to string """
        return value, value.strftime(self.datetime_format)
