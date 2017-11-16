#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
from app.middlewares.game import init


class Create(Resource):
    def post(self):
        data = request.get_json(silent=True)
        game = init(data)

        print(game)

        return game, 201






        


        