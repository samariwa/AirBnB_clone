#!/usr/bin/python3
"""
This module contains a class State which inherits from the BaseModel
Public class attributes:
    name: string - empty string
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This is the state class that inherits from the BaseModel class
    """
    name = ''
