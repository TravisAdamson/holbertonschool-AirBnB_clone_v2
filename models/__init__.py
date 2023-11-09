#!/usr/bin/python3
"""This module instantiates an object of class DBStorage or FileStorage,
This code was updated during this project """
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
