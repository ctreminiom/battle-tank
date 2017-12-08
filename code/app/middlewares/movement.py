from mongoengine import *
from app.models.movementModel import Movement
from datetime import datetime

def built(data):
    player01 = {}
    player02 = {}

    for i in range(len(data)):

        if data['players'][i]['type'] == 1:
            player01['game'] = data['game_uuid']
            player01['uuid'] = data['players'][i]['player_uuid']
            player01['coordenates'] = data['players'][i]['coordenates']
            player01['direction'] = data['players'][i]['direction']
            player01['angle'] = data['players'][i]['angle']
            player01['life'] = data['players'][i]['life']
            player01['lifes'] = data['players'][i]['lifes']
            player01['shoot_type'] = data['players'][i]['shoot_type']
            player01['type'] = data['players'][i]['type']
            
        if data['players'][i]['type'] == 2:
            player02['game'] = data['game_uuid']
            player02['uuid'] = data['players'][i]['player_uuid']
            player02['coordenates'] = data['players'][i]['coordenates']
            player02['direction'] = data['players'][i]['direction']
            player02['angle'] = data['players'][i]['angle']
            player02['life'] = data['players'][i]['life']
            player02['lifes'] = data['players'][i]['lifes']
            player02['shoot_type'] = data['players'][i]['shoot_type']
            player02['type'] = data['players'][i]['type']


    save(player01)
    save(player02)

#    validate(player01, player02)

    return "asdad"
    

def save(player):

    movement = Movement(
        id_ = Movement.objects(player_uuid_= player["uuid"]).count() + 1,
        game_uuid_  = player['game'],
        player_uuid_ = player['uuid'],
        x_ = player['coordenates']['x'],
        y_ = player['coordenates']['y'],
        direction_ = player['direction'],
        angle_ = player['angle'],
        life_ = player['life'],
        lifes_ = player['lifes'],
        shoot_type_ = player['shoot_type'],
        type_ = player['type'],
        log_ = datetime.now()
    )

    movement.save()






def validate_X_coordenates(player01_x, player02_x):
    return True if player01_x == player02_x else False

def validate_Y_coordenates(player01_y, player02_y):
    return True if player01_y == player02_y else False


def validate(player01, player02):

    X = validate_X_coordenates(player01['coordenates']['x'], player02['coordenates']['x'])
    Y = validate_X_coordenates(player01['coordenates']['y'], player02['coordenates']['y'])

#    if player01['coordenates']['x'] < player02['coordenates']['x']:
#        print("X ES MENOR PARA EL PLAYER01")
#    else:
#        print("X ES MAYOR PARA EL PLAYER01")


#    if player01['coordenates']['y'] < player02['coordenates']['y']:
#        print("Y ES MENOR PARA EL PLAYER01")
#    else:
#        print("Y ES MAYOR PARA EL PLAYER01")


        # PLAYER 01 LISTOOOO
    if X is not True and Y is True and player01['angle'] == 'LEFT' and player01['coordenates']['x'] > player02['coordenate']['x']:
        print('player 01 le dio al player 02')


    if X is not True and Y is True and player01['angle'] == 'RIGHT' and player01['coordenates']['x'] < player02['coordenates']['x']:
        print("player 01 le dio al player02") 
    
    if X is True and Y is not True and player01['angle'] == "BOTTON" and player01['coordenates']['y'] < player02['coordenates']['y']:
        print('player 01 le dio al player 02')

    if X is True and Y is True and player01['angle'] == "UP" and player01['coordenates']['y'] > player02['coordenates']['y']:
        print('player 01 le dio al player 02')

        # PLAYER 02 LISTOOOO
    if X is not True and Y is True and player02['angle'] == 'LEFT' and player02['coordenates']['x'] > player01['coordenate']['x']:
        print('player 01 le dio al player 02')

    if X is not True and Y is True and player02['angle'] == 'RIGHT' and player02['coordenates']['x'] < player01['coordenates']['x']:
        print("player 01 le dio al player02") 
    
    if X is True and Y is not True and player02['angle'] == "BOTTON" and player02['coordenates']['y'] < player01['coordenates']['y']:
        print('player 01 le dio al player 02')

    if X is True and Y is True and player02['angle'] == "UP" and player02['coordenates']['y'] > player01['coordenates']['y']:
        print('player 01 le dio al player 02')




    


#    if X is not True and Y is True and player02['angle'] == 'LEFT':
##        print("LE DIO") 
#    else: 
#        print("NO LE DIO")

    
#    if X is True and Y is not True and player01['angle'] == 'BOTTON':
#        print("LE DIO")
#    else:
#        print("NO LE DIO")

#    if X is True and Y is not True and player02['angle'] == 'UP':
#        print("LE DIO")
#    else:
#        print("NO LE DIO")

    



    







        














    

