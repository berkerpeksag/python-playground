#include <Python.h>

static PyObject *
spam_strptime(PyObject *self, PyObject *args)
{
    const char *date_string;
    const char *format;

    if (!PyArg_ParseTuple(args, "ss", &date_string, &format))
        return NULL;

    return Py_BuildValue("ss", date_string, format);
}

static PyMethodDef SpamMethods[] = {
    {"strptime", spam_strptime, METH_VARARGS,
     "Return a parsed date object."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",
    "Documentation of spam module",
    -1,
    SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
