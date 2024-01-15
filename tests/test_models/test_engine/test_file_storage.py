#!/usr/bin/python3
""" Unittests for file_storage module """


import json

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorageModel(unittest.TestCase):
    """ Testing the FileStorage class"""

    # task 5
    # __file_path:
    def test_file_path(self):
        """ __file_path class attribute exists"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    # __objects:
    def test_objects(self):
        """ __objects class attribute exists"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    # all()
    def test_all(self):
        """ correct output for all()"""
        f = FileStorage()
        dict = f.all()
        self.assertEqual(f.all(), FileStorage._FileStorage__objects)

    # new()
    def test_new(self):
        """ correct output for new()"""
        b = BaseModel()
        self.assertTrue(b in FileStorage._FileStorage__objects.values())

    # save()
    def test_save(self):
        """ correct output for save()"""
        b = BaseModel()
        b.save()
        key = f"BaseModel.{b.id}"
        value = b.to_dict()
        path = FileStorage._FileStorage__file_path
        with open(path, "r", encoding="utf-8") as file:
            dict = json.load(file)
        self.assertTrue(key in dict.keys())
        self.assertEqual(value, dict[key])

    # reload()
    def test_reload(self):
        """ correct output for reload()"""
        path = FileStorage._FileStorage__file_path

        obj_key = "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4"
        obj_dict = {
                "__class__": "BaseModel",
                "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4",
                "updated_at": "2017-09-28T21:11:14.333862",
                "created_at": "2017-09-28T21:11:14.333852"
            }
        obj_id = "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4"

        dict = {obj_key: obj_dict}

        with open(path, "w", encoding="utf-8") as file:
            json.dump(dict, file)

        r = FileStorage()
        r.reload()
        objects = r._FileStorage__objects

        self.assertTrue(obj_key in objects.keys())
        self.assertEqual(objects[obj_key].id, obj_id)
