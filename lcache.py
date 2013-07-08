import linecache
import sys


class ShowAndTell(object):
    def __init__(self):
        self.nest = 0

    def trace_fn(self, frame, event, arg):
        filename = frame.f_code.co_filename
        lineno = frame.f_lineno
        indent = '  ' * self.nest
        info = '{:s}{:s} @ {:s}: {:s}'.format(indent, filename,
                                              lineno, event)
        src = linecache.getline(filename, lineno)
        print '%-30s | %s' % (info, src[:-1])
        if event == 'call':
            self.nest += 1
        elif event == 'return':
            self.nest -= 1
        return self.trace_fn
