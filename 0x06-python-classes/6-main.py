#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square = Square(5, (3,))
my_square.my_print()

print("--")
my_square = Square(0, (10, 3))
my_square.my_print()

print("--")
