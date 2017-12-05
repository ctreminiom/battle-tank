#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongoengine import *

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app.models.userModel import User
from app.middlewares.security import encode

import uuid



def create(data):

    if  User.objects(username=data['username']).first():
        return "username already exists"
    else:

        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        public_id = str(uuid.uuid4())

        user = User(public_id = public_id,
                    firstName = data['firstName'],
                    lastName = data['lastName'],
                    username = data['username'],
                    password = hashed_password)
        user.save()

        return "New user created"


def validate(auth):
    response = {}

    if not auth or not auth.username or not auth.password:
        response['message'] = "Could not verify"
        response['status']  = 401

        return response

    user = User.objects(username=auth.username).first()

    if not user:
        response['message'] = "Username or password incorrect"
        response['status']  = 401

        return response


    if check_password_hash(user.password, auth.password):

        response['message'] = encode(user)
        response['status'] = 200

        return response

    else:
        response['message'] = "Username or password incorrect"
        response['status']  = 401

        return response
