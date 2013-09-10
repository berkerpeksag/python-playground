#!/usr/bin/env python
# coding: utf-8

from copy import deepcopy


class Node(object):
    __slots__ = 'data', 'next_node'

    def __init__(self, value, next_node=None):
        self.data = value
        self.next_node = next_node

    def __str__(self):
        return 'Node(%r)' % self.data

    __repr__ = __str__


class List(object):
    def __init__(self, *info):
        self.head = None
        if info:
            current = self.head = Node(info[0])
            for n in info[1:]:
                current.next_node = Node(n)
                current = current.next_node

    def __iter__(self):
        current = self.head
        if current is not None:
            yield current
        else:
            return None
        while current.next_node is not None:
            current = current.next_node
            yield current

    def __str__(self):
        return 'List(%s)' % ', '.join(repr(node.data) for node in self)

    __repr__ = __str__

    def __len__(self):
        if not self.head:
            return 0
        return sum(1 for i in self)

    def __add__(self, other):
        copy = deepcopy(self)
        copy.append(other)
        return copy

    def __radd__(self, other):
        copy = deepcopy(self)
        copy.append(other)
        return copy

    def append(self, other):
        end = None
        for end in self:
            pass
        if end is None:
            self.head = other.head
        else:
            end.next_node = other.head

    def insert(self, node, pos=0):
        prev = node
        for count, element in enumerate(self):
            if count == pos:
                node.next_node = element
                if not pos:
                    self.head = node
                else:
                    prev.next_node = node
                return
            prev = element
        self.append(List(*(None for c in range(pos - count - 1))))
        self.append(List(node.data))

    def delete(self, value):
        node_before = Node(None)
        for node in self:
            if node.data == value:
                if node_before.next_node:
                    node_before.next_node = node.next_node
                else:
                    self.head = node.next_node
                return
            else:
                node_before = node
        raise ValueError('Node value %s not in List' % value)

    def __getitem__(self, n):
        for count, node in enumerate(self):
            if count == n:
                return node.data
        raise IndexError('List index out of range')

    def __setitem__(self, n, value):
        for count, node in enumerate(self):
            if count == n:
                node.data = value
                return
        raise IndexError('List index out of range')

    def find(self, value):
        for node in self:
            if node.data == value:
                return node
        raise ValueError('Value %r not in List' % value)

if __name__ == '__main__':
    test_list = List('a', 'b', 'c')
    print test_list
    for node in test_list:
        print node.data

    other_list = List('d')

    print other_list, 'Length', len(other_list)
    test_list.append(other_list)

    print 'Appended', test_list, 'Length', len(test_list)
    test_list.delete('d')
    print "Deleted node with value 'd'", test_list, 'Length', len(test_list)

    try:
        test_list.find('z')
        print('Value %s found' % 'z')
    except ValueError as e:
        print(e)

    for value in test_list:
        test_list.delete(value.data)
        print value, 'deleted: ', test_list, 'Length', len(test_list)

    test_list.append(List(*'abcdefg'))
    print test_list
    test_list.append(List(*range(10)))
    print test_list

    test_list.insert(Node('z'), 23)
    print  test_list
    print len(test_list)

    print test_list[4]
    test_list[4] = 4
    print test_list

    print test_list + List('more test')
    print 'Test list did not change:', test_list
