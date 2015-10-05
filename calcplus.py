#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fich = open(sys.argv[1], "r")
lineas = fich.readlines()

calc = calcoohija.CalculadoraHija()

try:
    for linea in lineas:
        datos = linea.split(',')
        operacion = datos[0]
        if operacion == "suma":
            suma = 0
            for operandos in datos[1:]:
                suma = calc.plus(suma, int(operandos))
        if operacion == "resta":
            rest = int(datos[1])
            for operandos in datos[2:]:
                rest = calc.minus(rest, int(operandos))
        if operacion == "multiplica":
            mult = int(datos[1])
            for operandos in datos[2:]:
                mult = calc.mult(mult, int(operandos))
        if operacion == "divide":
            div = int(datos[1])
            for operandos in datos[2:]:
                div = calc.div(div, int(operandos))

    print(suma)
    print(rest)
    print(mult)
    print(div)
except ValueError:
    sys.exit("Error: Non numerical parameters")

