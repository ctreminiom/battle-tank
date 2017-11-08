#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from random import randrange

class Move(Resource):
    def get(self):

        allowed_movements = ["up", "down", "left", "right"]
        allowed_time = [1, 2, 3, 4, 5]

        movement = allowed_movements[randrange(4)]
        time = allowed_time[randrange(4)]

        return {"movement" : movement, "time" : time}, 200