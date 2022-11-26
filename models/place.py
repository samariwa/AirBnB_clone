#!/usr/bin/python3
"""
This module contains a class User which inherits from the BaseModel
Public class attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the user class that inherits from the BaseModel class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
