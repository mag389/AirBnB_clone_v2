#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os


store_type = os.environ.get('HBNB_TYPE_STORAGE')
print("in the init")
print(store_type)
if store_type == "db":
    """ use the mysql database storage version """
    print("db type storage")
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    """ use the default json storage """
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
