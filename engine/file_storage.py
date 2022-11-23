#!/usr/bin/python3
"""
    This file seralizes/deseralizes
    Instance <-> Dictionary <-> JSON string <-> file

    create the variable storage, an instance of FileStorage
    call reload() method on this variable

"""
import json

class FileStorage
    __file_path = "" #example file.json
    __objects = {} #<class name>.id 
    def __init__(self):
        pass
    def all(self):
        return __objects
    def new(self, obj):
        my_classname = type(__class__).__name__
        my_key = my_classname + '.' + self.id
        __object[my_key] = obj
    def save(self):
        my_list = []
        file_path = type(__class__).__name__ + ".json"
        if file_name:
            open with(file_path, "r", encoding="UTF-8") as read_from:
                my_list = json.loads(read_from.read())
            my_list.append(__objects)
            my_json_string = json.dumps(my_list)

        open with (file_name, "w+", encoding="UTF-8") as write_to:
            write_to.write(my_json_string)

    def reload(self):
        if file_name:
            open with(file_path, "r", encoding="UTF-8") as read_from:
                my_json_object= json.loads(read_from.read())




