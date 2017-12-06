#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api


from app.controllers.auth import Register, Login
from app.controllers.game import Create, Join, Report


from db import init_db
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

init_db()




def add_prefix(route):
    return '/api/v1.2.0/{}'.format(route)

api.add_resource(Register, add_prefix('auth/register')) #/api/v1.2.0/auth/register
api.add_resource(Login, add_prefix('auth/login'))       #/api/v1.2.0/auth/login

api.add_resource(Create, add_prefix('game/sesion/create'))  #/api/v1.2.0/game/sesion/create
api.add_resource(Join, add_prefix('game/sesion/join'))      #/api/v1.2.0/game/sesion/join

api.add_resource(Report, add_prefix('game/reports/get/game')) #/api/v1.2.0/game/reports/get/game


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)