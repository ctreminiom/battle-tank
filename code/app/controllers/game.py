#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
from app.middlewares.game import init, updateLife

class Create(Resource):
    def post(self):
        data = request.get_json(silent=True)
        game = init(data)
        return data, 200


class Life(Resource):
    def put(self):
        data = request.get_json(silent=True)

        uuid = data["sesion_uuid"]
        x = data["player_uuid"]
        y = data["life"]

        game = updateLife(uuid, x, y)

        return {"life": game}, 201





        


        