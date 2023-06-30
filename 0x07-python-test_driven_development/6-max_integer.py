#!/usr/bin/python3
"""Module to find the max integer in the list.
"""


def max_integer(list=[]):
    """Function to find and return a max integer in the list of integers
        The function returns None if the list contains no items.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return 
