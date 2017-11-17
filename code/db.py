#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import config
from mongoengine import *

def init_db():
    connect('documentos',host=config.DB_HOST, port=config.DB_PORT)

    
    
    
    
    

    
    
