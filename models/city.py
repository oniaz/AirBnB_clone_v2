#!/usr/bin/python3
"""City model module """
# ####
# import sys
# sys.path.insert(1, "/Users/omnia/Desktop/AirBnB_clone")
# ####


from models.base_model import BaseModel


class City(BaseModel):
    """The city class"""

    state_id = ""
    name = ""
