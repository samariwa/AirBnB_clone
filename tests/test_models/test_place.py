#!/usr/bin/env python3
"""
MOdule for unittests on place.py
"""
import uuid
import unittest
import datetime
from models.place import Place

class TestPlace(unittest.TestCase):
    """
    Test Individual components for The place Model
    """
    def setUp(self):
        self.my_model = Place()

    # Tests for attributes
    def test_id(self):
        """
        Tests for id attribute of our place model
        """
        idd = self.my_model.id
        self.assertNotEqual(self.my_model.id, None)
        self.assertIs(type(self.my_model.id), str)


        # test id is a uuid4 string
        self.assertIs(type(uuid.UUID(idd)), uuid.UUID)

    def test_created_at(self):
        ''' Test for created_at attribute.'''
        # confirm created_at exists
        self.assertNotEqual(self.my_model.created_at, None)

        # test created_at is a datetime object
        self.assertIs(type(self.my_model.created_at), datetime.datetime)

    def test_updated_at(self):
        ''' Test for updated_at attribute.'''
        # test updated_at is not None object.
        self.assertNotEqual(self.my_model.updated_at, None)

        # test updated_at is a datetime object.
        self.assertIs(type(self.my_model.updated_at), datetime.datetime)

    # ----------------------------------
    # end of tests for attributes
    # ----------------------------------
    # start tests for methods
    def test_save(self):
        prev_updated_at = self.my_model.updated_at
        self.my_model.save()

        # test updated_at was updated on save.
        self.assertNotEqual(self.my_model.updated_at, prev_updated_at)

    def test_to_dict(self):
        my_dict = self.my_model.to_dict()
        expected_dct = self.my_model.__dict__
        expected_dct.update(__class__="Place")

        # test that to_dict produces expected keys
        self.assertEqual(expected_dct.keys(), my_dict.keys())

        # test that to_dict returns type dict
        self.assertIs(type(my_dict), dict)

    def test_str(self):
        ''' Test the __str__ magic method.'''
        # test that __str__() returns a string object
        self.assertIs(type(self.my_model.__str__()), str)
    # _________________________________________
    # end test for methods
    # ________________________________________
