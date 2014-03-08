"""
Usage::

    @profile
    def your_function():
        for i in range(1000):
            x = i ^ i

"""

import cProfile


def profile(func):
    def profiled_func(*args, **kwargs):
        prof = cProfile.Profile()
        try:
            prof.enable()
            result = func(*args, **kwargs)
            prof.disable()
            return result
        finally:
            prof.print_stats()
    return profiled_func
