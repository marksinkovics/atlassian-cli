from jsonobject import JsonObject, StringProperty, IntegerProperty, BooleanProperty

class Repo(JsonObject):
    slug = StringProperty()
    id_ = IntegerProperty(name='id')
    name = StringProperty()
    smcId = StringProperty()
    state = StringProperty()
    statusMessage = StringProperty()
    forkable = BooleanProperty()
    public = BooleanProperty()
