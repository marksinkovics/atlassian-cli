from jsonobject import JsonObject, IntegerProperty, StringProperty, BooleanProperty
from atlassian_cli.helpers import EpochProperty

class PullRequest(JsonObject):
    id_ = IntegerProperty(name='id')
    version = IntegerProperty()
    title = StringProperty()
    state = StringProperty()
    open_ = BooleanProperty(name="open")
    closed = BooleanProperty()
    createdDate = EpochProperty()
    updatedDate = EpochProperty()
