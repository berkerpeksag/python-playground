from __future__ import print_function

import ast
import collections
import sys

Result = collections.namedtuple('Result', 'module name asname level')


class ImportFinder(ast.NodeVisitor):

    def __init__(self):
        super(ImportFinder, self).__init__()
        self.imports = []

    def visit_Import(self, node):
        self.imports.extend(Result(None, n.name, n.asname, None)
                            for n in node.names)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        self.imports.extend(Result(node.module, n.name, n.asname, node.level)
                            for n in node.names)
        self.generic_visit(node)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ast_importfinder.py <file>', file=sys.stderr)
    with open(sys.argv[1]) as fobj:
        ast_file = ast.parse(fobj.read())
    imports = ImportFinder()
    imports.visit(ast_file)
    for imp in imports.imports:
        print(imp)
