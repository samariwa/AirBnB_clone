#!/usr/bin/python3
"""
This file contains class BaseModel. This class is a base model
that other classes will inherit from. It defines all common attributes/methods
for other classes

Public instance attributes:

    id: string assign with an uuid when an instance is created,
    created_at: assign with the current datetime when an instance is created
    updated_at: updated every time you change your object


Public instance methods:

    save(self): updates the public instance attribute updated_at with the current datetime
    to_dict(self):returns a dictionary containing all keys/values of __dict__ of the instance


NOTE: created_at and updated_at must be converted to string object in ISO format:
    Format: format: %Y-%m-%dT%H:%M:%S.%f
NOTE: __str__: should print: [<class name>] (<self.id>) <self.__dict__>
"""
class BaseModel:
    """class BaseModel"""
    def __init___(self):
        self.id = 
