#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

def create_sesion_uuid():
    return str(uuid.uuid4())[:6]

def create_sesion(player):

    sesion = {
        "uuid" : create_sesion_uuid(),
        "player-01" : player,
        "player-02" : None,
        "full" : False,
        "winner": None
    }

    return sesion


def validate_sesion(sesion):
    print("dddi")