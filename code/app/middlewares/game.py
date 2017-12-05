from mongoengine import *

from app.models.playerModel import Player
from app.models.gameModel import Game
from app.middlewares.player import create

def init(data):
    player01 = create(data["uuid_player01"], data["type_player01"], data["life_player01"])
    player02 = create(data["uuid_player02"], data["type_player02"], data["life_player02"])

    game = Game(uuid_= data["uuid_game"], players=[player01, player02], winner= "Nothing")
    game.save()

    return game


def updateLife(sesion_uuid, player_uuid, life):
    game = Game.objects(uuid_=sesion_uuid).first()

    player01 = game.players[0].uuid_
    player02 = game.players[1].uuid_

    if player01 == player_uuid:

        if life == "0":
            game.winner = player01

        game.players[0].life_ = life
        game.save()

        return life

    if player02 == player_uuid:

        if life == "0":
            game.winner = player02

        game.players[1].life_ = life
        game.save()

        return life
