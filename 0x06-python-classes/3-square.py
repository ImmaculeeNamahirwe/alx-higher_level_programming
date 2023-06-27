#!/usr/bin/python3

"""Represent a class of square."""


class Square:
    """Define the square."""

    def __init__(self, size=0):
        """Start with the new square.
        Args:
            size (int): The size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of a square."""
        return (self.__size * self.__size)
