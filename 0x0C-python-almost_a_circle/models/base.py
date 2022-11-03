#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""init file for models. When we call the models package,
this is the starting point
"""
import json
import os
import csv


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
            dummy = cls(10, 10)
        elif cls.__name__ == "Square":
            dummy = cls(1)

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
            return [
                cls.create(**ls)
                for ls in Base.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to csv file"""
        # save in a csv-like format
        if (cls.__name__ == "Rectangle"):
            list_csv = [[r.id, r.width, r.height, r.x, r.y] for r in list_objs]
        else:
            list_csv = [[r.id, r.size, r.x, r.y] for r in list_objs]

        file_name = cls.__name__ + ".csv"
        file_r = open(file_name, "w")
        csv_writer = csv.writer(file_r)
        csv_writer.writerow(list_csv)

        file_r.close()

    @classmethod
    def load_from_file_csv(cls):
        """Read a csv file containing details of a Geometric shape"""
        file_name = cls.__name__ + ".csv"
        nme = cls.__name__
        to_return = []
        with open(file_name, encoding="utf-8") as file_r:
            csv_reader = csv.reader(file_r)
            for i in csv_reader:
                to_return.append(i)
            test = to_return[0]

        # save in dictionary so that create can convert it back to a repr
        if (cls.__name__ == "Rectangle"):
            to_return = [[int(i) for i in j if i not in ',[] '] for j in test]
            to_return = [
                {'id': i[0], 'width': i[1], 'height': i[2], 'x':i[3], 'y':i[4]}
                for i in to_return]
        else:
            to_return = [[int(i) for i in j if i not in ',[] '] for j in test]
            to_return = [
                {'id': i[0], 'size': i[1], 'x':i[2], 'y':i[3]}
                for i in to_return]

        # use cls.create to create the representations for each
        return [
                cls.create(**ls)
                for ls in to_return]
