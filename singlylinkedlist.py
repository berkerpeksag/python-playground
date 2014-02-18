#!/usr/bin/env python

from __future__ import print_function


class Node(object):
    def __init__(self, cargo=None, next_item=None):
        self.cargo = cargo
        self.next = next_item

    def __str__(self):
        return str(self.cargo)


class LinkedList(object):
    """A singly linked list implementation in Python."""

    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)

            self.last.next = current
            self.last = current

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = []

            while current.next is not None:
                current = current.next
                out.append(str(current.cargo))

            return ', '.join(out)
        return '<LinkedList: Empty>'

    def clear(self):
        self.first = None
        self.last = None


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert(3)
    lst.insert(21)
    lst.insert('Lindsey')
    print(lst)
