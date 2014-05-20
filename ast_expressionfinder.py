from __future__ import print_function

import ast
import collections
import sys


class ExpressionFinder(ast.NodeVisitor):

    def visit_Str(self, node):
        return repr(node.s)

    def visit_Name(self, node):
        self.add_expr(node, node.id)
        return node.id

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if left and right:
            expr = '({:s} {:s} {:s})'.format(left,
                                             self.op(node.op),
                                             right)
            self.add_expr(node, expr)
            return expr

    def add_expr(self, node, expr):
        """Add expression `expr` found in node `node`."""
        self.exprs[node.lineno].add(expr)

    def expressions(self, node):
        """Return a dict mappling line numbers to expressions."""
        self.exprs = collections.defaultdict(set)
        self.visit(node)
        return self.exprs


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: %s <file>' % __file__, file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1]) as fobj:
        source = fobj.read()
    nodes = ast.parse(source, mode='exec')
    exps = ExpressionFinder().expressions(nodes)
    for lineo, exp in exps.items():
        print(lineno, exp)
