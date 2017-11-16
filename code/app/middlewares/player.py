from mongoengine import *
from app.models.player import Player

def create(uuid, type, life)
{
    player = Player(uuid_= uuid, type_= type, life_=life)
    player.save()

    return player
}


def findByID(uuid)
{
    return Player.objects(uuid_=uuid).first()
}


def updateLife(uuid, life)
{
    player = Player.objects(uuid_=uuid).first()

    player.life = life
    player.save()
}
