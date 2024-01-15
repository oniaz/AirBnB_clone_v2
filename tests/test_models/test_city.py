#!/usr/bin/python3
""" Unittests for City module """


import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Testing the City class"""

    def test_city(self):
        """ User inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))
