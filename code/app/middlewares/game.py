from mongoengine import *

from app.models.player import Player
from app.models.game import Game
from app.middlewares.player import create

def init(data):
    player01 = create(data["uuid_player01"], data["type_player01"], data["life_player01"])
    player02 = create(data["uuid_player02"], data["type_player02"], data["life_player02"])

    game = Game(uuid_= data["uuid_game"], player01= player01, player02= player02, winner= "Nothing")

    game.save()
    
    return game

def findByID(uuid):
    return Game.objects(uuid_=uuid).first()

def updateLife(uuid, Life):
    game = Game.objects(uuid_=uuid).first()

    player.winner = player
    player.save()

    return player



