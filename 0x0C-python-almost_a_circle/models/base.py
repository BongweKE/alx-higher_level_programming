#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""init file for models. When we call the models package,
this is the starting point
"""
import json
import os


class Base:
    """Base class for most of our classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization for the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A function to return a json representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A method to safe json representation of a class to a file"""
        if list_objs is None or list_objs == []:
            str_content = '[]'
        else:
            str_content = Base.to_json_string(
                [i.to_dictionary() for i in list_objs]
            )
        filename = f"{cls.__name__}.json"
        file_n = open(filename, "w")

        file_n.write(str_content)
        file_n.close()

    def from_json_string(json_string):
        """Convert a string representation of json to json format
        Attrs:
            json_string (str): json string representation
        Return:
            json repersentation of a string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A class method to create a model
        Attrs:
            **dictionary (**kwargs): key value pairs used to create the model
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10, 10, 10)
        elif cls.__name__ == "Square":
            dummy = cls(1, 1, 0)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """A class method used to open a json file and use it's
        content to build instances"""
        f_name = f"{cls.__name__}.json"
        if os.path.isfile(f_name) is False:
            return []
        with open(f_name) as f:
            return [cls.create(**ls) for ls in json.load(f)]
