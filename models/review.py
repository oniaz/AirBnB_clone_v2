#!/usr/bin/python3
"""Review model module """
# ####
# import sys
# sys.path.insert(1, "/Users/omnia/Desktop/AirBnB_clone")
# ####


from models.base_model import BaseModel


class Review(BaseModel):
    """The review class"""

    place_id = ""
    user_id = ""
    text = ""
