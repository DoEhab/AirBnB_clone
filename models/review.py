#!/usr/bin/python3
from models.base_model import BaseModel

"""Define review class"""


class Review(BaseModel):
    """review class with class attribute text, user_id, place_id"""

    place_id = ""
    user_id = ""
    text = ""
