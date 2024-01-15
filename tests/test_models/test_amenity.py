#!/usr/bin/python3
""" Unittests for User module """


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Testing the Amenity class"""

    def test_user(self):
        """ User inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))
