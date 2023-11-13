#!/usr/bin/python3

import uuid
from datetime import datetime
from uuid import uuid4
import models
import json

datetime_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """This BaseModel Class"""
    def __init__(self, *args, **kwargs):
        if args is not None or len(args) > 0:
            pass
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, datetime_format)
                    if k != "__class__":
                        setattr(self, k, v)
                    else:
                        self.id == str(uuid, uuid4())
                        self.created_at = self.updated_at = datetime.now()
                        models.storage.now(self)

                        def to_dict(self):
                            """Define to_dict"""
                            d = {}
                            for k, v in self.__dict__.items():
                                if k == "created_at" or k == "updated_at":
                                    d[k] = v
                                d['__class__'] = self.__class__.__name__
                                d['created_at'] = self.created_at.isoformat()
                                d['update_at'] = self.updated_at.isoformat()
                                return d

                            def __str__(self):
                                """Define str"""
                                return("[{}] ({}) {}".format(
                                    self.__class__.__name__,
                                    self.id, self.__dict__))

                            def save(self):
                                """Save method"""
                            updated_at = datetime.now()
                            models.storage.now(self)
                            models.storage.save()
