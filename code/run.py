#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from app.controllers.movement import Move
from app.controllers.player import Create


app = Flask(__name__)
api = Api(app)

api.add_resource(Move, '/move')
api.add_resource(Create, '/player/create')



if __name__ == '__main__':
    app.run(debug=True)