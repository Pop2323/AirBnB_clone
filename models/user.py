#!/usr/bin/python3

"""User Class"""
import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """Define Class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
