#!/usr/bin/python3
"""Base model module """
# ####
# import sys
# sys.path.insert(1, "/Users/omnia/Desktop/AirBnB_clone")
# ####


import uuid
from datetime import datetime

import models


class BaseModel():
    """The base model. Assigns the basic attributes to instance.

    Methods:
        __init__(self)
        __str__(self)
        save(self)
        to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """Initializes an instance of the BaseModel class with generated values
        for the basic attributes: "id", "created_at", and "updated_at". If a
        dictionary of attribute-value pairs is passed, it adds/updates these
        attributes with the provided corresponding values.

        Args:
            **kwargs: attribute-value pairs for different instance attributes.

        Attributes:
            id (str): A Unique id for the instance, randomly generated using
                    uuid4.
            created_at (datetime): The instance creation time.
            updated_at (datetime): The time of the modification of the
                    instance, set to creation time upon initalization.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    date = datetime.fromisoformat(kwargs[key])
                    setattr(self, key, date)
                else:
                    setattr(self, key, kwargs[key])
        # else:
        #     self.id = str(uuid.uuid4())
        #     self.created_at = datetime.now()
        #     self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """Return a string representation of the instance.

        This representation contains the instance class name, the instance id,
        and a dictionary of the instance attributes.

        Returns:
            str: string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Generates a dictionary object containing all the keys and values of
        the instance __dict__, in addition to the inctance class name.

        Returns:
            dict: dictionary representation of the instance, including its
                attributs and their values.
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__

        self_dict = self.__dict__
        for key, value in self_dict.items():
            if type(value) is datetime:
                value = value.isoformat()
            dic[key] = value
        return dic
