#!/usr4/bin/python3
""" AirBnb Clone """
from uuid import uuid4 
from datetime.datetime import now


class BaseModel
    """ Class BaseModel """

    def __init__(self):
        """ Initialize """
        self.id = uuid4()
        self.created_at = now()
        self.updated_at = now()

    def __str__(self):
        """ Return string """
        class_name = self.__name__
        id = self.id
        return "[{}] ({}) {}".format(class_name, id, self.__dict__)

    def save(self):
        """ Update datetime """
        self.updated_at = now()

    def to_dict(self):
        """ Returns dict of the instance """
