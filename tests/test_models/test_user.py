#!/usr/bin/python3
""" Unittests for User module """


import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Testing the User class"""

    def test_user(self):
        """ User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_id_exist(self):
        """ new isntance, ID attribute exists"""
        u = User()
        self.assertTrue(hasattr(u, 'id'))
