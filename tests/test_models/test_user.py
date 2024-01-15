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

    def test_user_email(self):
        """tests the email class attribute"""
        self.assertEqual("", User.email)

    def test_user_password(self):
        """tests the password class attribute"""
        self.assertEqual("", User.password)

    def test_user_first_name(self):
        """tests the first_name class attribute"""
        self.assertEqual("", User.first_name)

    def test_user_last_name(self):
        """tests the last_name class attribute"""
        self.assertEqual("", User.last_name)
