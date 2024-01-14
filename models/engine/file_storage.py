#!/usr/bin/python3
"""File storage module """
####
# import sys
# sys.path.insert(1, "/Users/omnia/Desktop/AirBnB_clone")
####


import json

from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """Handles the serialization of instances to JSON files and the
    deserialization of JSON files into instances.

    Attributes:
        __file_path (str): the path to the JSON file
        __objects (dict): stores all objects in the form "<class name>.id"
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to __objects, saved in the form <class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        value = obj
        FileStorage.__objects[key] = value

    def save(self):
        """Generates a dictionary based on __objects where instead of the value
        being the object itself, the value is obj.to_dict(). This dictionary
        then gets serialized and saved the into the JSON file.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dic = {}
            for key, value in FileStorage.__objects.items():
                dic[key] = value.to_dict()
            json.dump(dic, file)

    def reload(self):
        """If it exits, deserializes the JSON file into a dictionary, then
        creates new instances based on the object attribute/values in the
        dictionary."""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                all_objs_dict = json.load(file)
                for class_id, obj_dict in all_objs_dict.items():
                    new_instance = eval(
                        f"{obj_dict['__class__']}(**{obj_dict})")
                    self.new(new_instance)
        except (FileNotFoundError):
            pass
        pass
