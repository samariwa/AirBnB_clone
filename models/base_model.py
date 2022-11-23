#!/usr/bin/python3
"""
This file contains class BaseModel. This class is a base model
that other classes will inherit from. It defines all common
attributes/methods for other classes

Public instance attributes:

    id: string assign with an uuid when an instance is created,
    created_at: assign with the current datetime when an
        instance is created
    updated_at: updated every time you change your object


Public instance methods:

    save(self): updates the public instance attribute updated_at
        with the current datetime
    to_dict(self):returns a dictionary containing all keys/values of
        __dict__ of the instance


NOTE: created_at and updated_at must be converted to string
object in ISO format:
    Format: format: %Y-%m-%dT%H:%M:%S.%f
NOTE: __str__: should print: [<class name>] (<self.id>) <self.__dict__>
"""
import uuid
from datetime import datetime
import json


class BaseModel:
    """ This is the base class of the models. It contains the core features\
    that will be inherited by all forms of models in the application """
    def __init__(self):
        """ This is the constructor of the base model """
        current_time = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Returns String repersentation of class"""
        my_object = "[{:s}] ({:s}) {:s}"
        my_dict = json.dumps(self.__dict__)
        my_object = my_object.format(type(self).__name__, self.id, my_dict)
        return my_object

    def save(self):
        """Updates upadte time to current"""
        updated_time = datetime.now()
        self.updated_at = updated_time.strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        """Returns dictionary representation of class"""
        return self.__dict__
