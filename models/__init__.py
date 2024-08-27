#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv



if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
    from models.engine import db_storage
    storage = db_storage.DBStorage()
    """
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    """
    
else:
    """
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    """

    from models.engine import file_storage
    storage = file_storage.FileStorage()
storage.reload()
