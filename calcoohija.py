#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):

    def mult(self, op1, op2):
        op1, op2 = self.check(op1, op2)
        return op1 * op2

    def div(self, op1, op2):
        op1, op2 = self.check(op1, op2)
        if op2 != 0:
            return op1 / op2
        else:
            sys.exit('Division by zero is not allowed ')

if __name__ == "__main__":

    try:
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculadora = CalculadoraHija()

    if sys.argv[2] == "suma":
        result = calculadora.plus(op1, op2)
    elif sys.argv[2] == "resta":
        result = calculadora.minus(op1, op2)
    elif sys.argv[2] == "multiplica":
        result = calculadora.mult(op1, op2)
    elif sys.argv[2] == "divide":
        result = calculadora.div(op1, op2)
    print(result)
