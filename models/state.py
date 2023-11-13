#!/usr/bin/python3

"""This is state class"""
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class State(BaseModel):
    """Define Class State"""
    name = ""
