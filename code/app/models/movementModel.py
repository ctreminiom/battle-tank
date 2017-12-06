from mongoengine import *
from datetime import datetime

class Movement(Document):
    id_ = IntField(min_value=1)
    player_uuid_ = StringField(required=True, max_length=100) 
    x_ = StringField(required=True, max_length=10)
    y_ = StringField(required=True, max_length=10)
    direction = StringField(required=True, max_length=100)
    log_ = DateTimeField(required=True)
