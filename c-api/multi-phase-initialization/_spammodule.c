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
     PyDoc_STR("Return a tuple of '(foo, bar)'.")},
    {NULL, NULL}
};

static int
spam_exec(PyObject *module)
{
    PyModule_AddIntConstant(module, "SPAM", 42);
    return 0;
}

static PyModuleDef_Slot spam_slots[] = {
    {Py_mod_exec, spam_exec},
    {0, NULL},
};

static PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",
    PyDoc_STR("Documentation of spam module"),
    0,
    spam_methods,
    spam_slots,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModuleDef_Init(&spammodule);
}
