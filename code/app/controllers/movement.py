#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request

from app.middlewares.security import require
from app.middlewares.movement import built



class Movement(Resource):
    method_decorators = [require]
    def post(self, user):
        data = request.get_json(silent=True)

        test = built(data)


        return test, 200

