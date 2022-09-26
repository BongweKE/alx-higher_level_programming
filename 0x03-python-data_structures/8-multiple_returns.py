#!/usr/bin/python3
def multiple_returns(sentence):
    """A function that returns a tuple with the length of a
    string and its first character.

    Requirements:
        If the sentence is empty, the first character should be equal to None
        You are not allowed to import any module

    Return:
        (length, first char or none)
    """
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
