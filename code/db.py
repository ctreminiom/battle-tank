#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import config
from mongoengine import *

connect(
    config.DB_NAME, 
    host=config.DB_HOST, 
    port=config.DB_PORT
)

class Player(Document):
    uuid_ = StringField(required=True, max_length=4)
    life_ = StringField(required=True, max_length=3)
    type_ = StringField(required=True, max_length=1)


class Sesion(Document):
    uuid_    = StringField(required=True, max_length=6)
    player01 = StringField(required=True, max_length=4)
    player02 = StringField(required=False, max_length=4)
    full     = BooleanField(required=False)
    winner   = StringField(required=False, max_length=4)
    
    
    
    
    

    
    
