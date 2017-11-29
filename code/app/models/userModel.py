#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *


class User(Document):
    public_id = StringField(required=True, unique=True, max_length=50)
    username =  StringField(required=True, unique=True, max_length=20)
    password = StringField(required=True, max_length=100)
