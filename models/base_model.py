#!/usr/bin/python3
""" Module for Base_model """

import uuid
from datetime import datetime
from uuid import uuid4
import models
import json

datetime_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """This BaseModel Class"""

    def __init__(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, datetime_format)
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def to_dict(self):
        """Define to_dict"""
        d = {}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                d[k] = v.isoformat()
        d['__class__'] = self.__class__.__name__
        return d

    def __str__(self):
        """Define str"""
        return("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__))

    def save(self):
        """Save method"""
        self.updated_at = datetime.now()
        models.storage.save()
