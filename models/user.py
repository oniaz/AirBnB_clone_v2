#!/usr/bin/python3
"""User model module """
# ####
# import sys
# sys.path.insert(1, "/Users/omnia/Desktop/AirBnB_clone")
# ####


from models.base_model import BaseModel


class User(BaseModel):
    """ User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    