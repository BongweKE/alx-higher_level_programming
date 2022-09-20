#!/usr/bin/python3
def mult_3(number):
    return number % 3 == 0


def mult_5(number):
    return number % 5 == 0


def mult_3_n_5(number):
    return mult_3(number) and mult_5(number)


def fizzbuzz():
    for i in range(1, 101):
        if mult_3_n_5(i):
            print(f"FizzBuzz", end=" ")
        elif mult_3(i):
            print("Fizz", end=" ")
        elif mult_5(i):
            print("Buzz", end=" ")
        else:
            print(f"{i}", end=" ")
