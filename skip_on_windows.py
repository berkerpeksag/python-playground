import functools
import sys
import unittest


def skip_on_windows(test=None, reason='skipped on Windows'):
    if not callable(test):
        if not isinstance(test, str):
            reason = 'reason must be a string, not {:s}'
            raise TypeError(reason.format(type(test).__name__))
        return functools.partial(skip_on_windows, reason=test)

    @functools.wraps(test)
    def wrapper(*args, **kwargs):
        if sys.platform == 'win32':
            raise unittest.SkipTest(reason)
    return wrapper


class DummyTest(unittest.TestCase):

    def test_foo(self):
        self.assertTrue(True)

    @skip_on_windows
    def test_skip_win(self):
        self.assertTrue(sys.splatform.startswith('linux'))

    @skip_on_windows('needs bar')
    def test_skip_win_too(self):
        self.assetEqual(2, 2)

    def test_raise_type_error(self):
        with self.assertRaises(TypeError):
            1 / 'a'

if __name__ == '__main__':
    unittest.main(verbosity=3)
