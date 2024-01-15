#!/usr/bin/python3
""" Unittests for Place module """


import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Testing the Place class"""

    def test_place(self):
        """ Place inherits from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_description(self):
        """tests the description class attribute"""
        self.assertEqual("", Place.description)
