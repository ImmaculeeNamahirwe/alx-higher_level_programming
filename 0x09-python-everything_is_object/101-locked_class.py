#!/usr/bin/python3
# 101-locked_class.py

"""Defines the locked class."""


class LockedClass:
    """
    Restrict the user from creating new LockedClass attributes
    for anything other than 'first name' attributes.
    """

    __slots__ = ["first_name"]
