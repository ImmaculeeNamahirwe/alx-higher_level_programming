#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """the built-in list class's sorted printing is implemented."""

    def print_sorted(self):
        """Lists should be printed in ascending order."""
        print(sorted(self))
