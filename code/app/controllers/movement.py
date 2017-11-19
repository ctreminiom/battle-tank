#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
from app.middlewares.movement import create, sendMovement


class Movement(Resource):
    def post(self):
        data = request.get_json(silent=True)

        game_uuid = data["game_uuid"]
        player_uuid= data["player_uuid"]
        player_x = data["x"]
        player_y = data["y"]
        

        create(data)

        new_movement = sendMovement()

        json = {"x": new_movement[0], "y": new_movement[1]}

        return json, 200


        ## Tengo el uuid_player, x , y

        ## 1. Guardar datos en la base de datos.
        ## 2. Guardar la coordenada X, Y del movimiento del jugador XX
        ## 3. Validar la coordenada X, Y del otro jugador NN



        ## 4. Regresar la coordenada X del movimiento, la coordenada Y del movimiento
        ## 5. Regresar el tipo de disparo ----> 10, 50, 100
        ## 6. Despues disparar






#Post.objects.count() + 1