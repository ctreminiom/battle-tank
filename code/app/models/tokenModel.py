#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine *
import datetime

class Token(Document):
    user_id = StringField(required=True, unique=False max_length=50)
    token =  StringField(required=True, unique=False max_length=100)
    created_at = DateTimeField(default=datetime.datetime.now)
    expired_at = DateTimeField(required = True)
    