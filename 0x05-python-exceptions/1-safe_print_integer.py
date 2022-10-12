#!/usr/bin/python3

def safe_print_integer(value):
    """a function that prints an integer with "{:d}".format().

    Requirements:
    - value can be any type (integer, string, etc.)
    - The integer should be printed followed by a new line
    - You have to use try: / except:
    - You have to use "{:d}".format() to print as integer
    - You are not allowed to import any module
    - You are not allowed to use type()

    Returns:
    True if value has been correctly printed
    (it means the value is an integer)
    Otherwise, returns False
    """
    try:
        print("{:d}".format(value), end='\n')
        return True
    except (ValueError, TypeError):
        return False
