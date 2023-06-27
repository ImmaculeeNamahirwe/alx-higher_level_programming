#!/usr/bin/python3

"""Define the single-linked list's classes."""


class Node:
    """ Express a node in the singly-linked list."""

    def __init__(self, data, next_node=None):
        """Start with the new Node.
        Args:
            data (int): The information of a new Node.
            next_node (Node): A next node of the current Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data of a Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("information must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next_node of Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError(" The next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Express a singly-linked list."""

    def __init__(self):
        """Start with the new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Add the new Node to the Singly-Linked List.
        The node is inserted into the list at a correct
        ordered numerical position.
        Args:
            value (Node): The new Node to be added.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Express the print() representation of the SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
