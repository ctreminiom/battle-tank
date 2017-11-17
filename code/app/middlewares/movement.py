from mongoengine import *
from app.models.movement import Movement
from datetime import datetime

def create(data):

    movement = Movement(
        id_ = Movement.objects(player_uuid_= data["player_uuid"]).count() + 1,
        player_uuid_ = data["player_uuid"],
        x_ = data["x"],
        y_ = data["y"],
        log_ = datetime.now()
    )

    movement.save()



def sendMovement():
    data = []

    data.append("234")
    data.append("120")

    return data
    
    

