#!/usr/bin/python3
""" Module that defines the interface for every data model of the project.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Class that defines all common attributes/methods for other Data Model
    classes

    Attributes:
        id (str): Unique id for each BaseModel instance.

        created_at (datetime): The current datetime when an instance is
                               created.
        updated_at (datetime): The current datetime when an instance is
                               created or modified (using the save method).
    """
    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel Instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    date_tmp = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, date_tmp)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Generates a human readable string that represents a BaseModel
         class.

        Returns:
            str: The string representation of the BaseModel with its
                 ID and its Dict of variables.
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates the date of the last modification in the instance using its
        updated_at attribute using the actual datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary a formatted representation of a BaseModel
        instance with its attributes and Classname.

        Returns:
            dict: The representation of the instance.
        """
        representation = {
            key: value.isoformat() if isinstance(value, datetime) else value
            for key, value in self.__dict__.items()
        }
        representation['__class__'] = self.__class__.__name__
        return representation
