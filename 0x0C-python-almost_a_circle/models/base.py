#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""init file for models. When we call the models package,
this is the starting point
"""
import json
import os
import csv
import turtle


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
            fieldnames = ['id', 'width', 'height', 'x', 'y']
            list_csv = [
                {
                    "id": r.id,
                    "width": r.width,
                    "height": r.height,
                    "x": r.x,
                    "y": r.y
                } for r in list_objs]
        else:
            fieldnames = ['id', 'size', 'x', 'y']
            list_csv = [
                {
                    "id": r.id,
                    "size": r.size,
                    "x": r.x,
                    "y": r.y
                } for r in list_objs]

        file_name = cls.__name__ + ".csv"
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in list_csv:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Read a csv file containing details of a Geometric shape"""
        file_name = cls.__name__ + ".csv"

        to_return = []
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for r in reader:
                if (cls.__name__ == "Square"):
                    list_csv = {
                        "id": int(r['id']),
                        "size": int(r['size']),
                        "x": int(r['x']),
                        "y": int(r['y'])}
                if (cls.__name__ == "Rectangle"):
                    list_csv = {
                        "id": int(r['id']),
                        "width": int(r['width']),
                        "height": int(r['height']),
                        "x": int(r['x']),
                        "y": int(r['y'])
                    }

                to_return.append(cls.create(**list_csv))
            return to_return

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw using turtle"""
        for r in list_rectangles:
            my_screen = turtle.Screen()
            my_screen.setup(500, 500)
            my_screen.bgcolor("red")
            my_drawing = turtle.Turtle()
            my_drawing.goto(r.x, r.y)
            my_drawing.forward(elem.width)
            my_drawing.left(90)
            my_drawing.forward(r.height)
            my_drawing.right(90)
            my_drawing.forward(r.width)
            my_drawing.right(90)
            my_drawing.forward(r.height)
            turtle.done()

        for r in list_squares:
            my_screen = turtle.Screen()
            my_screen.setup(500, 500)
            my_screen.bgcolor("yellow")
            my_square = turtle.Turtle()
            my_square.goto(r.x, r.y)
            my_square.forward(r.size)
            my_square.left(90)
            my_square.forward(r.size)
            my_square.right(90)
            my_square.forward(r.size)
            my_square.right(90)
            my_square.forward(r.size)
            turtle.done()
