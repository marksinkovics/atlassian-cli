from jsonobject import (
    JsonObject,
    IntegerProperty,
    StringProperty,
    BooleanProperty,
    ObjectProperty,
    ListProperty
)
from atlassian_cli.helpers import EpochProperty
from atlassian_cli.atlassian.bitbucket.models import (
    Project
)

class User(JsonObject):
    name = StringProperty()
    emailAddress = StringProperty()
    id_ = IntegerProperty(name='id')
    displayName = StringProperty()
    active = BooleanProperty()
    slug = StringProperty()
    type_ = StringProperty(name="type")

class PullRequestUser(JsonObject):
    user = ObjectProperty(User)
    role = StringProperty()
    approved = BooleanProperty()
    status = StringProperty()

class Repository(JsonObject):
    id_ = IntegerProperty(name='id')
    slug = StringProperty()
    name = StringProperty()
    scmId = StringProperty()
    project = ObjectProperty(Project)


class Ref(JsonObject):
    id_ = StringProperty(name='id')
    displayId = StringProperty()
    latestCommit = StringProperty()
    repository = ObjectProperty(Repository)

class PullRequestPropertiesMergeResult(JsonObject):
    outcome = StringProperty()
    current = BooleanProperty()

class PullRequestProperties(JsonObject):
    resolvedTaskCount = IntegerProperty()
    commentCount = IntegerProperty()
    openTaskCount = IntegerProperty()
    mergeResult = ObjectProperty(PullRequestPropertiesMergeResult)

class PullRequest(JsonObject):
    id_ = IntegerProperty(name='id')
    version = IntegerProperty()
    title = StringProperty()
    description = StringProperty()
    state = StringProperty()
    open_ = BooleanProperty(name="open")
    closed = BooleanProperty()
    createdDate = EpochProperty()
    updatedDate = EpochProperty()
    fromRef = ObjectProperty(Ref)
    toRef = ObjectProperty(Ref)
    locked = BooleanProperty()
    author = ObjectProperty(PullRequestUser)
    reviewers = ListProperty(PullRequestUser, default=[])
    participants = ListProperty(PullRequestUser, default=[])
    properties = ObjectProperty(PullRequestProperties)
