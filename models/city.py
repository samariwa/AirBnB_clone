#!/usr/bin/python3
"""
This module contains a class City which inherits from the BaseModel
Public class attributes:
    state_id: string - empty string. it will be the State.id
    name: string - empty string
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This is the user class that inherits from the BaseModel class
    """
    state_id = ''
    name = ''
