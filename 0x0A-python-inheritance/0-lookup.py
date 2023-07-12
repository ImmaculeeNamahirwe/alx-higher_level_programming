#!/usr/bin/python3
"""Defines object attribute lookup function."""


def lookup(obj):
    """Get the list of characteristics that are available for an object."""
    return (dir(obj))
