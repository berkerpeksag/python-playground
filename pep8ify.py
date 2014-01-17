from __future__ import print_function

import ast


class Pep8(ast.NodeVisitor):

    def visit_Assign(self, node):
        for target in node.targets:
            self.visit(target)
        print(' = ', end='')
        self.visit(node.value)
        print()

    def visit_BinOp(self, node):
        self.visit(node.left)
        print(' ', end='')
        self.visit(node.op)
        print(' ', end='')
        self.visit(node.right)

    def visit_Name(self, node):
        print(node.id, end='')

    def visit_Num(self, node):
        print(node.n, end='')

    def visit_Add(self, node):
        print('+', end='')

if __name__ == '__main__':
    nodes = ast.parse('x=3+2;y=4')
    Pep8().visit(nodes)
