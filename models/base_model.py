from _datetime import datetime
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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ overwrite __str__ method to return class name"""
        print(str.format("({}) [{}] <{}>", self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ updates the time for instance change"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """"""
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep


