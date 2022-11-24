#!/usr/bin/python3
"""
This module contains the FileStorage class that serializes instances to a JSON\
file and deserializes JSON file to instances
Private instance attributes:
__file_path: string - path to the JSON file (ex: file.json)
__objects: dictionary - empty but will store all objects by <class name>.\
id (ex: to store a BaseModel object with id=12121212,\
the key will be BaseModel.12121212)
Public instance methods:
all(self): returns the dictionary __objects
new(self, obj): sets in __objects the obj with key <obj class name>.id
save(self): serializes __objects to the JSON file (path: __file_path)
reload(self): deserializes the JSON file to __objects \
only if the JSON file (__file_path) exists ; otherwise, do nothing.\
If the file doesn't exist, no exception should be raised)
"""
import json
from os import path

class FileStorage:
    __file_path = "Storage.json"
    __objects = {} #<class name>.id

    def __init__(self):
        pass

    def all(self):
        """Returns object"""
        return type(self).__objects

    def new(self, obj):
        """Saves keys to objects"""
        my_classname = type(__class__).__name__
        my_key = my_classname + '.' + "70"
        type(self).__objects[my_key] = obj

    def save(self):
        """Save method"""
        my_file_path = type(self).__file_path
        print("It is I")
        print(type(self).__objects)
        print("It is I")
        my_obj = type(self).__objects
        with open(my_file_path, "w", encoding="UTF-8") as f:
            json.dump(my_obj, f)
        #my_file_path = type(self).__file_path
        #with open(my_file_path, "w", encoding="UTF-8") as f:
         #   json.dump(self.__objects, f)

    def reload(self):
        """Reload method"""
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                type(self).__objects = json.loads(f.read())



