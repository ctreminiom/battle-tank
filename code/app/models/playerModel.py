from mongoengine import *

class Player(EmbeddedDocument):
    uuid_ = StringField(required=True, max_length=20)
    life_ = StringField(required=True, max_length=20)
    type_ = StringField(required=True, max_length=20)