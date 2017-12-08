from mongoengine import *
from datetime import datetime

class Movement(Document):
    id_ = IntField(min_value=1)
    game_uuid_ = StringField(required=True, max_length=100) 
    player_uuid_ = StringField(required=True, max_length=100) 
    x_ = IntField(min_value=1)
    y_ = IntField(min_value=1)
    direction_ = StringField(required=True, max_length=100)
    angle_ = StringField(required=True, max_length=100)
    life_ = IntField(min_value=1)
    lifes_ = IntField(min_value=1)
    shoot_type_ = IntField(min_value=1)
    type_ =IntField(min_value=1)
    log_ = DateTimeField(required=True)
