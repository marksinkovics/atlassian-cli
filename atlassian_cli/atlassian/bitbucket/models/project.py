from jsonobject import JsonObject, StringProperty, IntegerProperty, BooleanProperty

class Project(JsonObject):
    key = StringProperty()
    id_ = IntegerProperty(name='id')
    name = StringProperty()
    public = BooleanProperty()
    type_ = StringProperty(name='type')
    description = StringProperty(default="")
