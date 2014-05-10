# taken from https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/
# tested with Python 3.4

import ctypes


class IntStruct(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_long),
                ("ob_type", ctypes.c_void_p),
                ("ob_size", ctypes.c_ulong),
                ("ob_digit", ctypes.c_long)]

    def __repr__(self):
        return ("IntStruct(ob_digit={self.ob_digit}, "
                "refcount={self.ob_refcnt})").format(self=self)


class ListStruct(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_long),
                ("ob_type", ctypes.c_void_p),
                ("ob_size", ctypes.c_ulong),
                ("ob_item", ctypes.c_long),  # PyObject** pointer cast to long
                ("allocated", ctypes.c_ulong)]

    def __repr__(self):
        return ("ListStruct(len={self.ob_size}, "
                "refcount={self.ob_refcnt})").format(self=self)

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print(ListStruct.from_address(id(l)))
    t = [l, l]  # two more references to L
    print(ListStruct.from_address(id(l)))

    # get a raw pointer to our list
    lstruct = ListStruct.from_address(id(l))

    # create a type which is an array of integer pointers the same length as L
    ptrarray = lstruct.ob_size * ctypes.POINTER(IntStruct)

    # instantiate this type using the ob_item pointer
    lvalues = ptrarray.from_address(lstruct.ob_item)

    print([ptr[0] for ptr in lvalues])  # ptr[0] dereferences the pointer

    # Modifying the Value of an Integer

    i = 113
    print("i", i)
    idi = id(i)
    print("id(i)", idi)
    iptr = IntStruct.from_address(idi)
    iptr.ob_digit = 4  # now Python's 113 contains a 4!
    print("i (after iptr.ob_digit = 4)", 113)
    print("113 == 4", 113 == 4)

    # In-place Modification of List Contents

    l = [42]
    lwrapper = ListStruct.from_address(id(l))
    item_address = ctypes.c_long.from_address(lwrapper.ob_item)
    print("before:", l)

    # change the c-pointer of the list item
    item_address.value = id(6)

    # we need to update reference counts by hand
    IntStruct.from_address(id(42)).ob_refcnt -= 1
    IntStruct.from_address(id(6)).ob_refcnt += 1

    print("after:", l)
