#!/usr/bin/python3
"""
Unittest for Basemodel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for base model class"""
    def test_attributes(self):
        """Test id and undefined attributes"""
        my_model = BaseModel()
        my_second_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertNotEqual(my_model.id, my_second_model)
        self.assertIsInstance(my_model.id, str)
        self.assertTrue(my_model.name, "My First Model")
        self.assertIsInstance(my_model.name, str)
        self.assertTrue(my_model.my_number, 89)
        self.assertIsInstance(my_model.my_number, int)
