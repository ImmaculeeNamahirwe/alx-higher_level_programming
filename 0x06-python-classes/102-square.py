#!/usr/bin/python3

"""Express a class of the square."""


class Square:
    """Rep the square."""

    def __init__(self, size=0):
        """Starts with the new square.
        Args:
            size (int): Size of a new square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the current size of  square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("The size must be an integer")
        elif value < 0:
            raise ValueError("The size must be >= 0")
        self.__size = value

    def area(self):
        """Back to the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Express the == comparision to the square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Express the != comparison to the square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Express the < comparison to the square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Express the <= comparison to the square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Express the > comparison to the square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Express the >= compmarison to a square."""
        return self.area() >= other.area()
