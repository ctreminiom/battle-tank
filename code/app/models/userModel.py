#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *


class User(Document):
    public_id = StringField(required=True, unique=True, max_length=100)
    firstName =  StringField(required=True, unique=True, max_length=100)
    lastName =  StringField(required=True, unique=True, max_length=100)
    username =  StringField(required=True, unique=True, max_length=100)
    password = StringField(required=True, max_length=100)
