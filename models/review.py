#!/usr/bin/python3

"""Review Class"""
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class Review(BaseModel):
    """Define Class Review"""
    place_id = ""
    user_id = ""
    text = ""