#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from app.controllers.game import Create
from db import aa

app = Flask(__name__)
api = Api(app)

aa()

def addPrefix(route):
    return '/api/v1.0/{}'.format(route)

api.add_resource(Create, addPrefix('game/init/'))


if __name__ == '__main__':
    app.run(debug=True)