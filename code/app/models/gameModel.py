from mongoengine import *
from app.models.playerModel import Player

class Game(Document):
    uuid_    = StringField(required=True, max_length=20)
    players = ListField(EmbeddedDocumentField(Player))
    winner   = StringField(required=False, max_length=20)