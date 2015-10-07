#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
    def check(self, op1, op2):
        try:
            op1 = int(op1)
            op2 = int(op2)
        except ValueError:
            sys.exit("Error:Non numerical parameters")
        return op1, op2

    def plus(self, op1, op2):
        op1, op2 = self.check(op1, op2)
        return op1 + op2

    def minus(self, op1, op2):
        op1, op2 = self.check(op1, op2)
        return op1 - op2

if __name__ == "__main__":

    op1 = sys.argv[1]
    op2 = sys.argv[3]
    calculadora = Calculadora()

    if sys.argv[2] == "suma":
        result = calculadora.plus(op1, op2)
    elif sys.argv[2] == "resta":
        result = calculadora.minus(op1, op2)

    print(result)
