#!/usr/bin/python3
""" Unittests for State module """


import unittest
from models.state import State
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Testing the State class"""

    def test_state(self):
        """ State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_name(self):
        """tests the name class attribute"""
        self.assertEqual("", State.name)
