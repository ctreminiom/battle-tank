from mongoengine import *
from app.models.playerModel import Player

class Game(Document):
    uuid_ = StringField(required=True, max_length=100)
    players = ListField(EmbeddedDocumentField(Player))
    finished = BooleanField(required=True)
    enable = BooleanField(required=True)
    winner = StringField(required=False, max_length=100)
