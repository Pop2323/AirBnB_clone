#!/usr/bin/python3
"""FileStorage Class"""
from json import dump, load, dumps
from models import base_model, amenity, city, place, review, state, user
from os.path import exists

BaseModel = base_model.BaseModel
Amenity = amenity.Amenity
City = city.City
Place = place.Place
Review = review.Review
State = state.State
User = user.User
name_class = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """return the dict __object"""
        return FileStorage.__objects
    def new(self, obj):
        """sets object with key in __obj"""
        class_name = obj.__class__.__name__
        id = obj.id
        clas_id = class_name + "." + id
        FileStorage.__objects[clas_id] = obj

    def save(self):
        """Save file storage"""
        dict_json = {}
        for key, value in FileStorage.__objects.items():
            dict_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as fil:
            dump(dict_json, fil)

    def reload(self, name_class):
        """Deserialize JSON file to __objects"""
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fil:
                dic_obj = load(fil)
                for key, value in dic_obj.items():
                    class_nam = key.split(".")[0]
                    if class_nam in name_class:
                        FileStorage.__objects[key] = eval(class_nam)(**value)
                    else:
                        pass
