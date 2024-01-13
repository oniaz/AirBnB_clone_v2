#!/usr/bin/python3
"""File storage module """
####
import sys
sys.path.insert(1, "/Users/omnia/Desktop/AirBnB_clone")
####


import json


class FileStorage():
    """Handles the serialization of instances to JSON files and the
    deserialization of JSON files into instances.

    Attributes:
        __file_path (str): the path to the JSON file
        __objects (dict): stores all objects in the form "<class name>.id"
    """

    __file_path = "file.json"
    __objects = {}

    # def __init__(self):
    #     """ initializing an instance."""

    def all(self):
        """Returns the __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to __objects, saved in the form <class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        value = obj.to_dict()
        FileStorage.__objects[key] = value

    def save(self):
        """Serializes and saves the __objects dictionary into the JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """If it exits, deserializes the JSON file to the dictionary
        __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
        except (FileNotFoundError):
            pass
        pass
