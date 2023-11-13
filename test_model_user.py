#!/usr/bin/python3
from models import storage
from models.user import User

def print_objects(objects):
    print("-- Reloaded objects --")
    for obj_id, obj in objects.items():
        print(obj)

def create_user(first_name, last_name, email, password):
    new_user = User()
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.email = email
    new_user.password = password
    new_user.save()
    return new_user

# Reloaded objects
all_objs = storage.all()
print_objects(all_objs)

# Create a new User
user = create_user("Jon", "ALX", "airbnb_clone@ALX.com", "root")
print(user)

# Create a new User 2
user2 = create_user("Tom", None, "airbnb2_clone@ALX.com", "root")
print(user2)

