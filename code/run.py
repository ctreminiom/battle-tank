#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from app.controllers.game import Create

app = Flask(__name__)
api = Api(app)

def addPrefix(route):
    return '/api/v1.0/{}'.format(route)

api.add_resource(Create, addPrefix('game/init'))


if __name__ == '__main__':
    app.run(debug=True)