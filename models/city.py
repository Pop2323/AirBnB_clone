#!/usr/bin/python3

"""City Class"""
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class City(BaseModel):
    """Define Class City"""
    state_id = ""
    name = ""
