#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request

from app.middlewares.game import create, updateLife, join, get_sessions

from app.middlewares.player import get_player_uuid
from app.middlewares.security import require

import json

class Create(Resource):
    method_decorators = [require]
    def post(self, user):

        game = create(user.public_id)

        return {"message": game['message']}, game['status']


class Join(Resource):
    method_decorators = [require]
    def post(self, user):
        data = request.get_json(silent=True)

        game = join(user.public_id, data['game_uuid'])

        return {"message": game['message']}, game['status']


class Report(Resource):
    method_decorators = [require]
    def get(self, user):
        data = get_sessions()

        return data, 200


class Player_UUID(Resource):
    method_decorators = [require]
    def get(self, user):
        data = get_player_uuid(user.public_id)
        
        return {"uuid" : data}, 200


class Life(Resource):
    def put(self):
        data = request.get_json(silent=True)

        uuid = data["sesion_uuid"]
        x = data["player_uuid"]
        y = data["life"]

        game = updateLife(uuid, x, y)

        return {"life": game}, 201

        