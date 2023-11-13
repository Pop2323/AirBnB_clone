#!/usr/bin/python3

"""User Class"""
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class User(BaseModel):
    """Define Class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    pass