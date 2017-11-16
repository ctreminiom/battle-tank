from mongoengine import *
from app.models.player import Player

class Game(Document):
    uuid_    = StringField(required=True, max_length=20)
    player01 = ReferenceField(Player)
    player02 = ReferenceField(Player)
    winner   = StringField(required=False, max_length=20)