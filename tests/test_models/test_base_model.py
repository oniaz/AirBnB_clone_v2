#!/usr/bin/python3
""" Unittests for base_model module """


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing the BaseModel class"""

    # id
    def test_id(self):
        b = BaseModel()
        self.assertEqual(type(b.id), str)

    def test_id_unique(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_id_exist(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, 'id'))

    # dates
    def test_creation_type(self):
        b = BaseModel()
        self.assertEqual(type(b.created_at), datetime)

    def test_update_type(self):
        b = BaseModel()
        self.assertEqual(type(b.updated_at), datetime)

    def test_creation_update_init(self):
        b = BaseModel()
        self.assertEqual(b.updated_at, b.created_at)

    def test_createion_in_past(self):
        b = BaseModel()
        self.assertLessEqual(b.created_at, datetime.now())

    def test_created_at_exists(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, 'created_at'))

    def test_updated_at_exists(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, 'updated_at'))

    # save()
    def test_save_updates(self):
        b = BaseModel()
        oldtime = b.updated_at
        b.save()
        self.assertNotEqual(oldtime, b.updated_at)

    # __str__
    def test_str(self):
        b = BaseModel()
        s1 = b.__str__()
        s2 = f"[{b.__class__.__name__}] ({b.id}) {b.__dict__}"
