from mongoengine import *

class Player(Document):
    uuid_ = StringField(required=True, max_length=4)
    life_ = StringField(required=True, max_length=3)
    type_ = StringField(required=True, max_length=1)
