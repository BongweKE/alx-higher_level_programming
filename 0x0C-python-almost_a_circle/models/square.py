#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Module file for square.py"""
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """A method to define how the user sees the square instance"""
        str1 = f"[Square] ({self.id}) {self.__x}/{self.__y}"
        str2 = f"{self.__width}"
        return f"{str1} - {str2}"
