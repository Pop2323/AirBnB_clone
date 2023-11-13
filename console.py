#!/usr/bin/python3
"""Class HBNBCommand a program called console.py
"""

import cmd
import json
import shlex  # Add this import for shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

Models = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
          "Place": Place, "Review": Review, "State": State, "User": User}


class MyCommand(cmd.Cmd):
    """ hbnb command interpreter """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ End of file"""
        return True

    def do_quit(self, arg):
        """ exit the program"""
        return True

    def emptyline(self):
        """don´t execute nothing """
        pass

    def do_create(self, args):
        """ Creates a new instance """
        if not args:
            print("** class name missing **")
        elif args not in Models:
            print("** class doesn't exist **")
        else:
            instance = Models[args]()
            instance.save()
            print(instance.id)

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
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
        for k, v in storage.all().items():
            if args[1] == v.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")

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
                for k, v in storage.all().items():
                    if args[1] == v.id:
                        print(v)
                        return
                print("** no instance found **")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in Models:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(storage.all()[key], args[2], args[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representations of all instances"""
        split_args = shlex.split(args)
        n_list = []
        dict_json = storage.all()
        if args:
            try:
                for key in storage.all():
                    if split_args[0] == key.split('.')[0]:
                        n_list.append(str(dict_json[key]))
                print(n_list)
            except Exception:
                print("** class doesn't exist **")
        else:
            for key in storage.all():
                n_list.append(str(storage.all()[key]))
            print(n_list)


if __name__ == '__main__':
    MyCommand().cmdloop()
