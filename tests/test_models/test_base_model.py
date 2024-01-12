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

    # to_dict
    def test_to_dict_class_key_exits(self):
        b = BaseModel()
        dic = b.to_dict()

        self.assertIn('__class__', dic.keys())

    def test_to_dict_id_key_exits(self):
        b = BaseModel()
        dic = b.to_dict()
        self.assertIn('id', dic.keys())

    def test_to_dict_createdat_key_exits(self):
        b = BaseModel()
        dic = b.to_dict()
        self.assertIn('created_at', dic.keys())

    def test_to_dict_updatedate_key_exits(self):
        b = BaseModel()
        dic = b.to_dict()
        self.assertIn('updated_at', dic.keys())

    def test_to_dict_dict_exits(self):
        b = BaseModel()
        d = b.__dict__
        dic = b.to_dict()

        for k, v in d.items():
            self.assertIn(k, dic.keys())

    def test_to_dict_date_is_str(self):
        b = BaseModel()
        dic = b.to_dict()
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)

    def test_to_dict_date_correct_iso(self):
        b = BaseModel()
        c_date = b.created_at.isoformat()

        u_date = b.updated_at.isoformat()
        dic = b.to_dict()
        self.assertEqual(dic["created_at"], c_date)
        self.assertEqual(dic["updated_at"], u_date)

    # task 4
    # #kwargs
    def test_no_kwargs(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, 'id'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))

    def test_kwargs(self):
        d = {
            "id": "33",
            'created_at': "2001-03-19T01:28:25.321281",
            'updated_at': "2004-02-12T03:18:22.321281"
            }
        b = BaseModel(**d)

        self.assertTrue(hasattr(b, 'id'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))

        self.assertEqual(b.id, "33")

        cd = datetime(2001, 3, 19, 1, 28, 25, 321281)
        self.assertEqual(b.created_at, cd)

        ud = datetime(2004, 2, 12, 3, 18, 22, 321281)
        self.assertEqual(b.updated_at, ud)

    def test_kwargs_extra_attr(self):
        d = {
            'id': "33",
            'created_at': "2001-03-19T01:28:25.321281",
            'updated_at': "2004-02-12T03:18:22.321281",
            'colour': "blue"
            }
        b = BaseModel(**d)

        self.assertTrue(hasattr(b, 'id'))
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))
        self.assertTrue(hasattr(b, 'colour'))

        self.assertEqual(b.id, "33")

        cd = datetime(2001, 3, 19, 1, 28, 25, 321281)
        self.assertEqual(b.created_at, cd)

        ud = datetime(2004, 2, 12, 3, 18, 22, 321281)
        self.assertEqual(b.updated_at, ud)

        self.assertEqual(b.colour, "blue")

    def test_kwargs_update_date(self):
        d = {
            'updated_at': "2004-02-12T03:18:22.321281",
            }
        b = BaseModel(**d)

        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))

        ud = datetime(2004, 2, 12, 3, 18, 22, 321281)
        self.assertEqual(b.updated_at, ud)

        self.assertNotEqual(b.updated_at, b.created_at)

    def test_kwargs_date_type(self):
        d = {
            "id": "33",
            'created_at': "2001-03-19T01:28:25.321281",
            'updated_at': "2004-02-12T03:18:22.321281"
        }
        b = BaseModel(**d)
        self.assertEqual(type(b.created_at), datetime)
        self.assertEqual(type(b.updated_at), datetime)

    def test_kwargs_dict_class_key_not_attribute(self):
        d = {
            "__class__": "NotBaseModel",
            'created_at': "2001-03-19T01:28:25.321281",
            'updated_at': "2004-02-12T03:18:22.321281"
        }
        b = BaseModel(**d)
        self.assertNotEqual(type(b.__class__), str)
        self.assertEqual(b.__class__, BaseModel)
        # ?
