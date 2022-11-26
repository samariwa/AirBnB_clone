#!/usr/bin/python3
"""
This file contains a class HBNBCommand
This file deals with the entire command
interpretor
The class uses cmd module
The command interpretor should implement
quit and EOF to exit the program
This class deals with providing custom prompt
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """ 
    Class HBNBCommand is a subclass of the Cmd class of the cmd module\
    The class will help in building a console interface for manipulating data\
    and objects
    """
    prompt = '(hbnb) '
    __classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

    def __init__(self):
        """ 
        This is the constructor of the HBNBCommand subclass
	"""
        super().__init__()

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        """Override empty lines function not to do default action.
        That is repeat last command when no command is given\n"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of the called model,\
	saves it (to the JSON file) and prints the id
	"""
        if arg != "":
            if arg in HBNBCommand.__classes:
                cls = globals()[arg]
                my_model = cls()
                storage.new(my_model.to_dict())
                storage.save()
                print(my_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based\
        on the class name and id
        """
        if arg != "":
            try:
                class_name, class_id = arg.split(" ")
            except ValueError:
                if arg in HBNBCommand.__classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
                return
            if class_name in HBNBCommand.__classes and class_id != "":
                my_dict = storage.all()
                my_id = class_name + "." + class_id
                try:
                    d = my_dict[my_id]
                except:
                    print("** no instance found **")
                    return
                my_object = "["+class_name+"] ({:s}) {}"
                f = "%Y-%m-%dT%H:%M:%S.%f"
                d['created_at'] = datetime.strptime(d['created_at'], f)
                d['updated_at'] = datetime.strptime(d['updated_at'], f)
                my_object = my_object.format(class_id, d)
                print(my_object)
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        try:
            class_name, class_id = arg.split(" ")
        except ValueError:
            if arg in HBNBCommand.__classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **") 
            return
        if class_name in HBNBCommand.__classes and class_id != "":
            my_dict = storage.all()
            my_id = class_name + "." + class_id
            try:
                del my_dict[my_id]
            except:
                print("** no instance found **")
                return
            storage.save()


    def do_all(self, arg):
        """
        Prints all string representation of all instances based\
        or not on the class name.
        """
        if arg in HBNBCommand.__classes or arg == "":
            my_dict = storage.all()
            my_list = []
            for keys, v in my_dict.items():
                to_append = False
                class_name, class_id = keys.split(".")
                my_object = "["+class_name+"] ({:s}) {}"
                if arg != "":
                    if class_name == arg:
                        to_append = True
                else:
                    del v['__class__']
                    f = "%Y-%m-%dT%H:%M:%S.%f"
                    v['created_at'] = datetime.strptime(v['created_at'], f)
                    v['updated_at'] = datetime.strptime(v['updated_at'], f)
                    to_append = True
                """
                f = "%Y-%m-%dT%H:%M:%S.%f"
                v['created_at'] = datetime.strptime(v['created_at'], f)
                v['updated_at'] = datetime.strptime(v['updated_at'], f)
                """
                my_object = my_object.format(class_id, v)
                if to_append == True:
                    my_list.append(my_object)
            print(my_list)
        else:
            print("** class doesn't exist **")
	
    def do_update(self, arg):
        """
        Updates an instance based on the class name and\
        id by adding or updating attribute
        """
        args_list = list(arg.split(" "))
        if len(args_list) < 4:
            if len(args_list) == 0:
                print("** class name missing **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            elif len(args_list) == 2:
                print("** attribute name missing **")
            elif len(args_list) == 3:
                print("** value missing **")
        else:
            if args_list[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            cls_model = args_list[0]
            cls_id = args_list[1]
            cls_attr = args_list[2]
            cls_val = args_list[3]
            cls_key = cls_model+'.'+cls_id
            my_dict = storage.all()
            try:
                my_obj = my_dict[cls_key]
                my_obj[cls_attr] = cls_val
                storage.save()
            except:
                print("** no instance found **")
                return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
