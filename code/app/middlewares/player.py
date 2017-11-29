from mongoengine import *
from app.models.playerModel import Player

def create(uuid, type, life):
    player = Player(uuid_= uuid, type_= type, life_=life)
    return player