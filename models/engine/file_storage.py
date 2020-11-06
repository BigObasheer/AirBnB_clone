#!/usr/bin/python3
""" AirBnB Clone """
import json
from os.path import exists


class FileStorage():
    """ Class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return Objects """
        return self.__objects

    def new(self, obj):
        """ Create Objects dict """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ Save to JSON """
        temp = {}

        for keys in self.__objects.keys():
            temp[keys] = self.__objects[keys].to_dict()

        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(temp, jsonfile)

    def reload(self):
        """  Deserializes a JSON file """
        from ..base_model import BaseModel
        from ..user import User
        from ..place import Place
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..review import Review

        if exists(self.__file_path):
            with open(self.__file_path) as jsonfile:
                deserialized = json.load(jsonfile)

            cls = {"BaseModel": BaseModel, "User": User, "Place": Place,
                   "State": State, "City": City, "Amenity": Amenity,
                   "Review": Review}

            for keys in deserialized.keys():
                for cls_key in cls.keys():
                    if deserialized[keys]['__class__'] == cls_key:
                        self.__objects[keys] = cls[cls_key
                                                   ](**deserialized[keys])
                        break
