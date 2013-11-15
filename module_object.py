import sys
import types


def module_object(name, source):
    """
    Make a ModuleType object and add it to ``sys.modules``::

        mod = module_object('setuputils', '/home/berker/setuputils.py')

    """
    with open(source, 'r') as f:
        source = f.read()
    module = types.ModuleType(name, source)
    module.__file__ = name + '.pyc'
    sys.modules[name] = module
    bytecode = compile(source, '<script>', 'exec')
    exec bytecode in module.__dict__
    return module
