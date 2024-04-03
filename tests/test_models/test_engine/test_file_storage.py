#!/usr/bin/python3
""" Unittests for file_storage module """


import json
import os

import unittest
from models import storage
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

    # Airbnbv2 shitty code tests
    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

