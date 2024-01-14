#!/usr/bin/python3
""" init for models package """
####
# import sys
# sys.path.insert(1, "/Users/omnia/Desktop/AirBnB_clone")
####


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
