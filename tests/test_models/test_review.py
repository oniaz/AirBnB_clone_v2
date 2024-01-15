#!/usr/bin/python3
""" Unittests for Review module """


import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Testing the Review class"""

    def test_review(self):
        """ Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))
