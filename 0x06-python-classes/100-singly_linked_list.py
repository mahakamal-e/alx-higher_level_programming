#!/usr/bin/python3
""" Class node """


class Node:
    """ Define class Node  """
    def __init__(self, data, next_node=None):
        """
        init

        data: data attribute
        next_node: attribute
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ get data """
        return self.__data

    @data.setter
    def data(self, value):
        """ set data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.data = value

    @property
    def next_node(self):
        """ get next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ implementation of singly linked list """
    def __init__(self):
        """ init """
        self.__head = None

    def sorted_insert(self, value):
        """ method of insert linkedlist

        Args:
        value: data
        """

        if self.__head is None:
            self.__head = Node(value)
        else:
            if value < self.__head.data:
                self.__head = Node(value, self.__head)
            else:
                next_node = self.__head.next_node
                perv_node = self.__head
                while next_node is not None:
                    if value < next_node.data:
                        perv_node.next_node = Node(value, next_node)
                        break
                    next_node = next_node.next_node
                    perv_node = perv_node.next_node
                else:
                    perv_node.next_node = Node(value)

    def __str__(self):
        """ print the list """
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return ('\n'.join(nodes))
