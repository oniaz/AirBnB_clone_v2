#!/usr/bin/python3
"""Base model module """

from datetime import datetime
import uuid


class BaseModel():
    """The base model. Assigns the basic attributes to instance.

    Methods:
        __init__(self)
        __str__(self)
        save(self)
        to_dict(self)
    """
    def __init__(self):
        """Initializes an instance of the BaseModel class with the attributes:
        id, created_at, updated_at.

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

    def to_dict(self):
        """Generates a dictionary object containing all the keys and values of
        the instance __dict__, in addition to the inctance class name.

        Returns:
            dict: dictionary representation of the instance, including its
                attributs and their values.
        """
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()
        return dic
