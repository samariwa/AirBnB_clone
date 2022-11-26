#!/usr/bin/python3
"""
This module contains a class Review which inherits from the BaseModel
Public class attributes:
    place_id: string - empty string. It will be Place.id
    user_id: string - empty string. It will be User.id
    text: string - empty string
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the review class that inherits from the BaseModel class
    """
    place_id = ''
    user_id = ''
    text = ''
