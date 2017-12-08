from mongoengine import *
from app.models.playerModel import Player

from app.models.gameModel import Game

import uuid


def get_player_uuid(public_id):

    game = Game.objects(enable = True)

    data = [{
        'uuid': sesion.uuid_,
        'players': {
            'user_id_': sesion.players[0].user_id_,
            'life_': sesion.players[0].life_,
            'lifes_': sesion.players[0].lifes_,
            'type_': sesion.players[0].type_
        }
    } for sesion in Game.objects(enable = True)]

    for a in range(len(data)):
        user_uuid = data[a]['players']['user_id_']
        
        if user_uuid == public_id:
            return user_uuid









def format(public_id, player_type):

    data = create_the_default_data()

    player = Player(
        uuid_ = data['uuid'],
        user_id_ = public_id,
        life_ = data['life'],
        lifes_ = data['lifes'],
        type_ = player_type
    )

    return player



def create_the_default_data():
    default = {}

    default['uuid'] = str(uuid.uuid4())[:12]
    default['life'] = 100
    default['lifes'] = 3

    return default







