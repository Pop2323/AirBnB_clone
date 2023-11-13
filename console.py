#!/usr/bin/python3

import cmd
import json
import shlex
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

Models = {
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class MyCommand(cmd.Cmd):
    prompt = "(hbnb) > "

    def do_EOF(self, arg):
        """This exits the cmd"""
        return True

    # 'exit' is a built-in function in cmd.Cmd.
    do_exit = do_EOF

    def emptyline(self):
        """Don't do anything"""
        pass

    def do_create(self, args):
        """Creates a new instance"""
        try:
            if not args:
                raise ValueError("** class name missing **")
            elif args not in Models:
                raise ValueError("** class doesn't exist **")
            else:
                instance = Models[args]()
                instance.save()
                print(instance.id)
        except ValueError as e:
            print(e)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in Models:
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(args[0], args[1])
                instances = storage.all()
                if key in instances:
                    print(instances[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in Models:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        instances = storage.all()
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representations of all instances"""
        arg_list = shlex.split(args)
        if not arg_list:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if class_name not in Models:
            print("** class doesn't exist **")
            return
        instances = storage.all()
        filtered_instances = [
                str(instance)
                for key, instance in instances.items()
                if key.split('.')[0] == class_name
                ]
        if not filtered_instances:
            print("[]")
        else:
            print(filtered_instances)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in Models:
            print("** class doesn't exist **")
            return
        if len(args) > 1:
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()
            if key in instances:
                if len(args) > 2:
                    attr_name = args[2]
                    if len(args) > 3:
                        attr_value = args[3]
                        setattr(instances[key], attr_name, attr_value)
                        instances[key].save()
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")


if __name__ == '__main__':
    MyCommand().cmdloop()
