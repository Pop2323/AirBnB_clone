#!/usr/bin/python3
""" Place_model class """

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place_model class """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
