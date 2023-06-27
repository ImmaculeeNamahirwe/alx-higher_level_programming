#!/usr/bin/python3

"""Express a class of the square."""


class Square:
    """Represent the square."""

    def __init__(self, size=0, position=(0, 0)):
        """Start the new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position/location of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError(" The size must be an integer")
        elif value < 0:
            raise ValueError(" The size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("The position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Back to a current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print a square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Express the print() representation of the Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
