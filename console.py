#!/usr/bin/python3
"""
This file contains a class HBNBCommand
This file deals with the entire command
interpretor
The class uses cmd module
The command interpretor should implement
quit and EOF to exit the program
This class deals with providing custom prompt

create:
    Creates a new instance of BaseModel
    saves it (to the JSON file)
    prints the id
    If the class name is missing, print ** class name missing **

"""
import cmd
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    prompt = '(hbnb) '

    def __init__(self):
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
        if arg != "":
            if arg == "BaseModel":
                my_model = BaseModel()
                storage.new(my_model.to_dict())
                storage.save()
                print(my_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        if arg != "":
            try:
                class_name, class_id = arg.split(" ")
            except ValueError:
                if arg == "BaseModel":
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
                return
            if class_name == "BaseModel" and class_id != "":
                my_dict = storage.all()
                my_id = "BaseModel" + "." + class_id
                try:
                    d = my_dict[my_id]
                except:
                    print("** no instance found **")
                    return
                my_object = "[BaseModel] ({:s}) {}"
                f = "%Y-%m-%dT%H:%M:%S.%f"
                d['created_at'] = datetime.strptime(d['created_at'], f)
                d['updated_at'] = datetime.strptime(d['updated_at'], f)
                my_object = my_object.format(class_id, d)
                print(my_object)
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        try:
            class_name, class_id = arg.split(" ")
        except ValueError:
            if arg == "BaseModel":
                print("** instance id missing **")
            else:
                print("** class doesn't exist **") 
            return
        if class_name == "BaseModel" and class_id != "":
            my_dict = storage.all()
            my_id = "BaseModel" + "." + class_id
            try:
                del my_dict[my_id]
            except:
                print("** no instance found **")
                return
            storage.save()


    def do_all(self, arg):
        pass

    def do_update(self, arg):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
