from mongoengine import *

class Player(EmbeddedDocument):
    uuid_ = StringField(required=True, max_length=20)
    user_id_ = StringField(required=True, max_length=50)
    life_ = IntField(required=True, min_value=1)
    lifes_ = IntField(required=True, min_value=1)
    type_ = StringField(required=True, max_length=20)
