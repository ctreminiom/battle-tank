from mongoengine import *
from app.models.playerModel import Player
from app.models.gameModel import Game
from app.middlewares.player import format

import uuid


def create(public_id):
    player = format(public_id, '1')

    game = Game(
        uuid_ = str(uuid.uuid4())[:12],
        players = [player],
        finished = False,
        enable = True,
        winner = "Nothing"
    )
    game.save()

    response = {}
    response['message'] = "Game sesion created"
    response['status'] = 201

    return response


def join(public_id, game_uuid):
    player = format(public_id, '2')

    game = Game.objects(uuid_ = game_uuid).first()
    game.players.append(player)
    game.save()

    response = {}
    response['message'] = "Game sesion completed"
    response['status'] = 201

    return response


def get_sessions():
    game = Game.objects(enable = True)

    data = [{
        'uuid': sesion.uuid_,
        'players': {
            'user_id_': sesion.players[0].user_id_,
            'life_': sesion.players[0].life_,
            'lifes_': sesion.players[0].lifes_,
            'type_': sesion.players[0].type_
        },
        'finished': sesion.finished,
        'enable': sesion.enable,
        'winner': sesion.winner
    } for sesion in Game.objects(enable = True)]

    return data


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
