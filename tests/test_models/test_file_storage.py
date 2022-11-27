#!/usr/bin/env python3
""" Test module for FileStorage class.
"""
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import unittest


class TestFileStorage(unittest.TestCase):
    """ TestCase implementation for FileStorage class
    """
    # -----------------------
    # start tests for methods
    # -----------------------

    def setUp(self):
        ''' Sets up the environment for each test method.'''
        my_model = BaseModel()
        my_user = User()

    def test_objects(self):
        ''' Tests the __objects attribute.'''

        # test that type of __object is dict
        self.assertIs(type(storage.all()), dict)

    def test_all(self):
        ''' Tests the all method.'''
        types = [int, float, str, list, tuple, set, None]

        # test that all() returns an object of type dict
        for cls in types:
            with self.subTest(i=cls):
                self.assertIsNot(type(storage.all()), cls)

    """
    def test_new(self):
        ''' Tests the new method.'''
        classes = [BaseModel, User, Place, State, City, Amenity, Review]

        # test that new() adds new instances of all clss to __object
        for cls in classes:
            prev_objs = storage.all().copy()  # new dict obj; not ref to prev
            cls()  # create new instance of cls; should be added by new()
            curr_objs = storage.all()
            with self.subTest(i=cls):
                self.assertNotEqual(prev_objs, curr_objs)  # if new obj added
    """

    def test_save(self):
        ''' Tests the save() method.'''
        storage.reload()
        old_storage = storage.all().copy()  # collect present __objects
        Place(), State()  # create two new instances added to __objects autom.
        storage.save()  # save __objects with newly added instances
        storage.reload()
        new_storage = storage.all()

        # test that current __objects is actually saved to file.
        self.assertNotEqual(old_storage, new_storage)
    # ------------------------
    # end of tests for methods
    # ------------------------
