#!/usr/bin/python3

def safe_print_division(a, b):
    """a function that divides 2 integers and prints the result.

    Requirements:
    - You can assume that a and b are integers
    - The result of the division should print on the finally: section
    preceded by Inside result:
    You have to use try: / except: / finally:
    You have to use "{}".format() to print the result
    You are not allowed to import any module

    Returns:
    the value of the division, otherwise: None

    """
    try:
        x = a / b
    except ZeroDivisionError:
        x = None
    finally:
        print(f"Inside result: {x}")
        return x
