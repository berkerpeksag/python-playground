/* Source: http://hg.python.org/cpython/file/default/Python/ceval.c#l4568 */

#include "Python.h"

void main() {
    if (PyTuple_Check(w)) {
        Py_ssize_t i, length;
        length = PyTuple_Size(w);
        for (i = 0; i < length; i += 1) {
            PyObject *exc = PyTuple_GET_ITEM(w, i);
            if (!PyExceptionClass_Check(exc)) {
                PyErr_SetString(PyExc_TypeError, "err msg");
                return NULL;
            }
        }
    }
}
