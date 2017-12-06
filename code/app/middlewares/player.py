from mongoengine import *
from app.models.playerModel import Player

import uuid

def create(public_id, player_type):

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

    default['uuid'] = str(uuid.uuid4())
    default['life'] = 100
    default['lifes'] = 3

    return default







