#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """a function that divides element by element 2 lists.

    Requirements:
    - my_list_1 and my_list_2 can contain any type
    (integer, string, etc.)
    - list_length can be bigger than the length of both lists
    - If 2 elements can’t be divided, the division result should
    be equal to 0
    - If an element is not an integer or float:
        print: wrong type
    - If the division can’t be done (/0):
        print: division by 0
    - If my_list_1 or my_list_2 is too short
        print: out of range
    - You have to use try: / except: / finally:
    - You are not allowed to import any module

    Returns:
    a new list (length = list_length) with all divisions

    i: keep track of index in each list
    """

    i = 0
    newList = []
    while (i < list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            x = 0
            print("division by 0")
        except TypeError:
            x = 0
            print("wrong type")
        except IndexError:
            x = 0
            print("out of range")
            break
        finally:
            newList.append(x)
            i += 1

    return newList
