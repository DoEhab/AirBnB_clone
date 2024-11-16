#!/usr/bin/python3
import json

from models.base_model import BaseModel

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
        for key in file_objects.keys():
            with open(FileStorage.__file_path, "w") as f:
                json.dump(file_objects[key].to_dict(), f)


    def reload(self):
        """deserialize the json object """
        try:
            with open(FileStorage.__file_path) as f:
                stored_obj = json.load(f)
                for value in stored_obj.values:
                    pass
        except FileNotFoundError:
            return


