#!/usr/bin/python3
"""Defines the class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with the != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with the == behavior."""
        return self.real == value
