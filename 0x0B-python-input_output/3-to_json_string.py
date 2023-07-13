#!/usr/bin/python3
"""Defines the string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of string object."""
    return json.dumps(my_obj)
