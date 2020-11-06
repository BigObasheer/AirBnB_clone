#!/usr4/bin/python3
""" AirBnb Clone """
from uuid import uuid4 
from datetime import datetime


class BaseModel:
    """ Class BaseModel """

    def __init__(self):
        """ Initialize """
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Return string """
        class_name = self.__class__.__name__
        id = self.id
        return "[{}] ({}) {}".format(class_name, id, self.__dict__)

    def save(self):
        """ Update datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns dict of the instance """
        # attrs = {}
        # attrs['id'], attrs['created_at'], attrs['updated_at'] = self.id, self.created_at, self.updated_at
        attrs = dict(self.__dict__)
        attrs['__class__'] = self.__class__.__name__
        attrs['created_at'] = self.created_at.isoformat('T')
        attrs['updated_at'] = self.updated_at.isoformat('T')
        return attrs
