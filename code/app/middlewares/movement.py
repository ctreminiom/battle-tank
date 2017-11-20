from mongoengine import *
from app.models.movement import Movement
from app.models.game import Game
from datetime import datetime
from random 

def create(data):

    movement = Movement(
        id_ = Movement.objects(player_uuid_= data["player_uuid"]).count() + 1,
        game_uuid_  = data["game_uuid"],
        player_uuid_ = data["player_uuid"],
        x_ = data["x"],
        y_ = data["y"],
        direction_ = data["direction"],
        log_ = datetime.now()
    )

    movement.save()

    return sendMovement(game_uuid, player_uuid)


def sendMovement(game_uuid, player_uuid):

    game = Game.objects(uuid_=game_uuid).first()

    player01 = game.players[0].uuid_
    player02 = game.players[1].uuid_

    if player01 == player_uuid:

        player01_movement = Movement.objects(player_uuid= player01)
        player02_movement = Movement.objects(player_uuid= player02)


        player_01_coordinates = {}
        player_01_coordinates["x"] = player01_movement.x_
        player_01_coordinates["y"] = player01_movement.y_

        player_02_coordinates = {}
        player_02_coordinates["x"] = player02_movement.x_
        player_02_coordinates["y"] = player02_movement.y_

        
        return Format(player_01_coordinates, player_01_coordinates)


    if player02 == player_uuid:
        player01_movement = Movement.objects(player_uuid= player01)
        player02_movement = Movement.objects(player_uuid= player02)


        player_01_coordinates = {}
        player_01_coordinates["x"] = player01_movement.x_
        player_01_coordinates["y"] = player01_movement.y_

        player_02_coordinates = {}
        player_02_coordinates["x"] = player02_movement.x_
        player_02_coordinates["y"] = player02_movement.y_

        
        return Format(player_01_coordinates, player_01_coordinates)



def Format(player_01_coordinates,player_02_coordinates):

    new_coordinates = {}
    
    if int(float(player_01_coordinates["x"])) == int(float(player_02_coordinates["x"])):

        new_coordinates["x"] = int(float(player_01_coordinates["x"])) - random.randrange(100)
        new_coordinates["y"] = random.randrange(400)


    return new_coordinates



        














    

