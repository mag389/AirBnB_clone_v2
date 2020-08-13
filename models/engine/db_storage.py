#!/usr/bin/python3
""" SQL storage engine, vroom """

import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """ CLass handling rds storage stuff """
    __engine = None
    __session = None

    def __init__(self):
        """ init. """

        """ This probably isnt what they meant but it makes it easier. """
        mysql_user = os.environ.get('HBNB_MYSQL_USER')
        mysql_pass = os.environ.get('HBNB_MYSQL_PWD')
        mysql_host = os.environ.get('HBNB_MYSQL_HOST')
        mysql_db = os.environ.get('HBNB_MYSQL_DB')

        """ ik this is ugly but pep8 has forced my hand. 80 char limit. :( """
        login = "{}:{}".format(mysql_user, mysql_pass)
        server = "{}/{}".format(mysql_host, mysql_db)
        eng_str = "mysql+mysqldb://{}@{}".format(login, server)

        self.__engine = create_engine("{}".format(eng_str), pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') is 'test':
            """ drop tables """
            """ will finish this later. """