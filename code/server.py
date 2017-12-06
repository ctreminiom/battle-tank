#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api

from app.controllers.game import Create, Life
from app.controllers.movement import Movement
from app.controllers.auth import Register, Login


from app.controllers.player import Prueba

from db import init_db
from flask_cors import CORS


app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

init_db()


def addPrefix(route):
    return '/api/v1.1.0/{}'.format(route)

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')

api.add_resource(Create, addPrefix('game/init/'))
api.add_resource(Life, addPrefix('game/put/life/'))


api.add_resource(Prueba, '/prueba')

api.add_resource(Movement, addPrefix('game/request/movement/'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)