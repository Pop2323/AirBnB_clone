#!/usr/bin/python3
from models.base_model import BaseModel

model = BaseModel()
model.name = "ALX"
model.my_number = 89
print(model)
model.save()
print(model)
model_json = model.to_dict()
print(model_json)
print("JSON of my_model:")
for k in model_json.keys():
    print("\t{}: ({}) - {}".format(k, type(model_json[k]), mmodel_json[k]))

print("--")
new_model = BaseModel(**model_json)
print(new_model.id)
print(new_model)
print(type(new_model.created_at))

print("--")
print(model is new_model)
