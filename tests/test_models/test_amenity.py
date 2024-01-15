#!/usr/bin/python3
""" Unittests for User module """


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Testing the Amenity class"""

    def test_amenity(self):
        """ User inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_name(self):
        """tests the name class attribute"""
        self.assertEqual("", Amenity.name)
