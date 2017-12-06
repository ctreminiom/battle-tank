#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request

from app.middlewares.game import init, updateLife, join
from app.middlewares.security import require


class Create(Resource):
    method_decorators = [require]
    def post(self, user):

        game = init(user.public_id)

        return {"message": game['response']}, game['status']



class Join(Resource):
    method_decorators = [require]
    def post(self, user):
        data = request.get_json(silent=True)

        game = join(user.public_id, data['game_uuid'])

        return {"message": game['response']}, game['status']







class Life(Resource):
    def put(self):
        data = request.get_json(silent=True)

        uuid = data["sesion_uuid"]
        x = data["player_uuid"]
        y = data["life"]

        game = updateLife(uuid, x, y)

        return {"life": game}, 201





        


        