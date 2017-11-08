#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
import uuid
from app.middlewares.sesion import create_sesion

def create_player_uuid():
    return str(uuid.uuid4())[:4]

class Create(Resource):

    def get(self):
        player = {
            "uuid" : create_player_uuid(),
            "life" : 100,
            "player_type" : 1
        }

        sesion = create_sesion(player["uuid"])

        return {"player": player, "sesion" : sesion}, 200
        

class Validation(Resource):

    def post(self):
        