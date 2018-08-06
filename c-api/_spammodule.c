#include <Python.h>

static PyObject *
spam_eggs(PyObject *self, PyObject *args)
{
    const char *foo;
    const char *bar;

    if (!PyArg_ParseTuple(args, "ss", &foo, &bar))
        return NULL;

    return Py_BuildValue("ss", foo, bar);
}

static PyMethodDef spam_methods[] = {
    {"eggs", spam_eggs, METH_VARARGS,
     "Return a tuple of '(foo, bar)'."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",
    PyDoc_STR("Documentation of spam module"),
    -1,
    spam_methods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
