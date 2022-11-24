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
from models import storage


class BaseModel:
    """ This is the base class of the models. It contains the core features\
    that will be inherited by all forms of models in the application """
    def __init__(self, *args, **kwargs):
        """ This is the constructor of the base model """
        current_time = datetime.today()
        self.id = str(uuid.uuid4())
        self.created_at = current_time
        self.updated_at = current_time
        if kwargs is not None:
            my_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, my_format)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, my_format)
        else:
            storage.new()
    def __str__(self):
        """Returns String repersentation of class"""
        my_object = "[{:s}] ({:s}) {}"
        my_object = my_object.format(type(self).__name__, self.id, self.__dict__)
        return my_object

    def to_dict(self):
        """Returns dictionary representation of class"""
        d = self.__dict__.copy()
        d['__class__'] = type(self).__name__
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        return d

    def save(self):
        """Updates upadte time to current"""
        self.updated_at = datetime.now()
        storage.save()
