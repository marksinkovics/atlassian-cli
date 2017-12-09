from jsonobject import JsonObject, BooleanProperty, StringProperty

class User(JsonObject):
    active = BooleanProperty()
    username = StringProperty(name='name')
    email = StringProperty(name='emailAddress')
    name = StringProperty(name='displayName')
