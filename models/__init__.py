#!/usr/bin/python3
"""create instance of file storage class"""
from models.engine.file_storage import FileStorage
from models.user import User

storage = FileStorage()
storage.reload()