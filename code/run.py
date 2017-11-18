#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from app.controllers.game import Create, Prueba

from app.controllers.movement import Movement
from app.controllers.game import Life

from db import init_db
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

init_db()

def addPrefix(route):
    return '/api/v1.0/{}'.format(route)

api.add_resource(Create, addPrefix('game/init/'))

api.add_resource(Prueba, addPrefix('game/init/prueba/<string:uuid>'))

api.add_resource(Movement, addPrefix('game/get/movement'))

api.add_resource(Life, addPrefix('game/put/life/'))



if __name__ == '__main__':
    app.run(host='0.0.0.0')