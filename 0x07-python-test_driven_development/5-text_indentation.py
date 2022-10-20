#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" A module with a function that modifies input text """


def text_indentation(text):
    """This function receives text as input, and adds two line
    separators after each line ending with ., ? or :

    Checks:
        text input must be a string
        There should be no space at the beginning or end of each
        printed line
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    temp = ''.join([''.join([i, '\n', '\n'])
                    if i in ['.', '?', ':'] else i
                    for i in text])
    temp = list(temp)


    for k, v in enumerate(temp):
        if v == '\n' and (k+1) < len(temp) and temp[k+1] == ' ':
            del(temp[k+1])

    print(''.join(temp), end='')
