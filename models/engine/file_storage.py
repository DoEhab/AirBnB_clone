#!/usr/bin/python3
import json

from models.base_model import BaseModel
from models.user import User

""" define File storage class"""


class FileStorage:
    """File storage class with private instance file path and object"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """ return saved objects"""
        return FileStorage.__objects

    def new(self, obj):
        """create new objects"""
        cls_name = obj.__class__.__name__
        new_obj_id = "{}.{}".format(cls_name, obj.id)
        FileStorage.__objects[new_obj_id] = obj

    def save(self):
        """serialize object to json file """
        file_objects = FileStorage.__objects
        serialized_objects = {}
        for key, val in file_objects.items():
            serialized_objects[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """deserialize the json object """
        try:
            with open(FileStorage.__file_path) as f:
                stored_obj = json.load(f)
                for obj_key, obj_value in stored_obj.items():
                    obj_class_name = obj_value["__class__"]
                    obj_class = globals().get(obj_class_name)
                    obj_value.pop("__class__")
                    self.__objects[obj_key] = obj_class(**obj_value)

        except FileNotFoundError:
            return
