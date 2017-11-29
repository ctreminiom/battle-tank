#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
from app.middlewares.user import create, validate

class Register(Resource):
    def post(self):
        data = request.get_json(silent=True)
        return {"message": create(data)}

class Login(Resource):
    def post(self):
        auth = request.authorization
        message = validate(auth)

        return {"message": message['message']}, message['status']
