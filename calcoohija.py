#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
    def plus(self, op1, op2):
        return op1 + op2
    def minus(self, op1, op2):
        return op1 - op2

class CalculadoraHija(Calculadora):
    def mult(self, op1, op2):
        return op1 * op2
    def div(self, op1, op2):
        return op1 / op2

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
    elif sys.argv[2] == "multiplicacion":
        result = calculadora.mult(op1, op2)
    elif sys.argv[2] == "division":
        if op2 != 0:
            result = calculadora.div(op1, op2)
        else:
            sys.exit('Division by zero is not allowed')
    print(result)
