#!/usr/bin/python3
"""
This module contains a class Amenity which inherits from the BaseModel
Public class attributes:
    name: string - empty string
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This is the amenity class that inherits from the BaseModel class
    """
    name = ''
