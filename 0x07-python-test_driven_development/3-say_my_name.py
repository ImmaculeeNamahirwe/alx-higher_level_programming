#!/usr/bin/python3
"""Defines the name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print the name.
    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If first name or last name are not strings, then.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
