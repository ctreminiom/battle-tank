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

        new_movement = sendMovement(game_uuid = data["game_uuid"], player_uuid= data["player_uuid"])

        json = {"x": new_movement["x"], "y": new_movement["y"]}

        return json, 200