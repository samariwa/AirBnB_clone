#!/usr/bin/python3
"""
This module contains a class Place which inherits from the BaseModel
Public class attributes:
    city_id: string - empty string. It will be City.id
    user_id: string - empty string. It will be User.id
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list: it will be the list of Amenity.id
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This is the user class that inherits from the BaseModel class
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
