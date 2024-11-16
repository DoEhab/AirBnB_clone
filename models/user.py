#!/usr/bin/python3
from models.base_model import BaseModel

"""Define User class"""


class User(BaseModel):
    """user class with class attribute
        email: user email
        password: user password
        first_name: user first name
        last_name: user last name
    """

    email: ""
    password: ""
    first_name: ""
    last_name: ""
