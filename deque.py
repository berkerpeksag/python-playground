"""
A deque (pronounced "deck") implementation in Python

A deque, also known as a double-ended queue, is an ordered
collection of items similar to the queue. It has two ends,
a front and a rear, and the items remain positioned in the
collection. What makes a deque different is the unrestrictive
nature of adding and removing items. New items can be added
at either the front or the rear. Likewise, existing items can
be removed from either end. In a sense, this hybrid linear
structure provides all the capabilities of stacks and queues
in a single data structure.

It is important to note that even though the deque can assume
many of the characteristics of stacks and queues, it does not
require the LIFO and FIFO orderings that are enforced by those
data structures. It is up to you to make consistent use of the
addition and removal operations.

The deque operations are given below.

- Deque() creates a new deque that is empty. It needs no
  parameters and returns an empty deque.

- add_front(item) adds a new item to the front of the deque.
  It needs the item and returns nothing.

- add_rear(item) adds a new item to the rear of the deque.
  It needs the item and returns nothing.

- remove_front() removes the front item from the deque.
  It needs no parameters and returns the item. The deque is
  modified.

- remove_rear() removes the rear item from the deque.
  It needs no parameters and returns the item. The deque is
  modified.

- is_empty() tests to see whether the deque is empty.
  It needs no parameters and returns a boolean value.

- size() returns the number of items in the deque.
  It needs no parameters and returns an integer.


Lists vs. Deques

Deques support thread-safe, memory efficient appends and pops
from either side of the deque with approximately the same O(1)
performance in either direction.

Though list objects support similar operations, they are
optimized for fast fixed-length operations and incur O(n) memory
movement costs for pop(0) and insert(0, v) operations which
change both the size and position of the underlying data
representation.

You can't use slice/index operations on a deque, but you can use
popleft/appendleft, which are operations deque is optimized for.

Indexed access is O(1) at both ends but slows to O(n) in the
middle. For fast random access, use lists instead.

Python lists are much better for random-access and fixed-length
operations, including slicing, While deques are much more useful
for pushing and popping things off the ends, with indexing (but
not slicing, interestingly) being possible but slower than with
lists.

"""


class Deque(object):

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    @property
    def is_empty(self):
        return self.size == 0

    @property
    def size(self):
        return len(self.items)
