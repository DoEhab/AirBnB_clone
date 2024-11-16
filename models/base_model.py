#!/usr/bin/python3
from _datetime import datetime
import models
import uuid

""" Base model class"""


class BaseModel:
    """ the base model initializes the main values """

    def __init__(self, *args, **kwargs):
        """ init method for all instances
        Args:
            *args: values of the args
            **kwargs: keys for the args
        """

        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)


    def __str__(self):
        """ overwrite __str__ method to return class name"""
        return str.format("({}) [{}] <{}>", self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the time for instance change"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """"""
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep


