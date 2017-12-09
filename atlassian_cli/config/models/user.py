""" User model """
import keyring

from jsonobject import (
    JsonObject,
    DateTimeProperty,
    StringProperty,
    BooleanProperty
)

from ...metadata import SERVICE_IDENTIFIER

class User(JsonObject):
    """ Represent a user account """
    username = StringProperty()
    url = StringProperty()
    createdAt = DateTimeProperty()
    updatedAt = DateTimeProperty()
    default = BooleanProperty(default=False)

    @property
    def model_id(self):
        """ Use as a unique identifier """
        return "{}@{}".format(self.username, self.url)

    @property
    def password(self):
        """ Read password directly in a OS based secured area """
        return keyring.get_password(SERVICE_IDENTIFIER, self.model_id)

    @password.setter
    def password(self, value):
        """ Store password directly in a OS based secured area """
        if value:
            keyring.set_password(SERVICE_IDENTIFIER, self.model_id, value)
        else:
            if keyring.get_password(SERVICE_IDENTIFIER, self.model_id):
                keyring.delete_password(SERVICE_IDENTIFIER, self.model_id)

    def __eq__(self, other):
        return (self.url == other.url and
                self.username == other.username)

    def __str__(self):
        return '{}@{}'.format(self.username, self.url)
