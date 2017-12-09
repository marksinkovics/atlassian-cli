""" Represent a epoch time for jsonobject module """

from datetime import datetime, timezone
from jsonobject import JsonProperty

class EpochProperty(JsonProperty):
    """ Specialize JsonProperty to handle epoch time """
    _type = datetime
    def wrap(self, obj):
        try:
            if not isinstance(obj, int):
                raise ValueError()
            return self._wrap(obj)
        except ValueError:
            raise ValueError('{0!r} is not a {1}-formatted string'.format(
                obj,
                self._type.__name__,
            ))

    def unwrap(self, obj):
        if not isinstance(obj, self._type):
            raise ValueError('{0!r} is not a {1} object'.format(
                obj,
                self._type.__name__,
            ))
        return self._unwrap(obj)

    def _wrap(self, obj): # pylint: disable=R0201
        try:
            return datetime.utcfromtimestamp(obj / 1000.0)
        except ValueError as exp:
            raise ValueError('Invalid ISO date {0!r} [{1}]'.format(obj, exp))

    def _unwrap(self, obj): # pylint: disable=R0201
        return obj, obj.replace(tzinfo=timezone.utc).timestamp() * 1000.0
